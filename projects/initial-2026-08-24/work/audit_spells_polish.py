from __future__ import annotations

import collections
import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "bg3dnd"
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
STATS = BASE / "Public" / MOD / "Stats" / "Generated" / "Data"
SOURCE = BASE / "Mods" / MOD / "Localization" / "English" / "english.xml"
TARGET = BASE / "Mods" / MOD / "Localization" / "Polish" / "polish.xml"
BG_EN = ROOT / "official_bg3_english_20260828" / "english.loca.xml"
BG_PL = ROOT / "official_bg3_polish_20260828" / "polish.loca.xml"
ROOT_TEMPLATE_DIRS = (
    [Path(value).resolve() for value in sys.argv[2:]]
    if len(sys.argv) > 2
    else [BASE / "Public" / MOD / "RootTemplates"]
)

ENTRY_RE = re.compile(r'^new entry "([^"]+)"$', re.MULTILINE)
TYPE_RE = re.compile(r'^type "([^"]+)"$', re.MULTILINE)
USING_RE = re.compile(r'^using "([^"]+)"$', re.MULTILINE)
DATA_RE = re.compile(r'^data "([^"]+)" "(.*)"$', re.MULTILINE)
HANDLE_RE = re.compile(r"^(h[0-9a-z]+);\d+$", re.IGNORECASE)
TAG_RE = re.compile(r"</?[^>]+>")
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"(?<![A-Za-z0-9])(\d*)[dk](\d+)(?:s)?(?![A-Za-z0-9])", re.IGNORECASE)
ENGLISH_RE = re.compile(
    r"\b(?:the|this|that|you|your|when|while|with|without|and|can|cannot|may|must|"
    r"target|creature|spell|attack|damage|level|turn|action|bonus|saving|throw|roll|"
    r"rest|range|within|feet|gain|deal|take|use|using|until|once|each|another|choice|"
    r"equal|number|finish|proficiency|modifier|weapon|feature|condition|points|"
    r"temporary|strength|dexterity|constitution|intelligence|wisdom|charisma|speed)\b",
    re.IGNORECASE,
)

UNCHANGED_WHITELIST = {
    "Bernard",
    "Infiltrator",
    "Shillelagh",
}


def localization(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def visible(text: str) -> str:
    return TAG_RE.sub(" ", PLACEHOLDER_RE.sub(" ", text))


def dice_signature(text: str) -> collections.Counter[tuple[str, str]]:
    return collections.Counter((count or "1", sides) for count, sides in DICE_RE.findall(text))


def parse_stats() -> dict[str, dict[str, object]]:
    entries: dict[str, dict[str, object]] = {}
    for path in sorted(STATS.glob("Spell_*.txt")):
        text = path.read_text(encoding="utf-8-sig")
        matches = list(ENTRY_RE.finditer(text))
        for index, match in enumerate(matches):
            chunk = text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
            entry_type = TYPE_RE.search(chunk)
            using = USING_RE.search(chunk)
            entries[match.group(1)] = {
                "type": entry_type.group(1) if entry_type else "",
                "using": using.group(1) if using else "",
                "fields": {key: value for key, value in DATA_RE.findall(chunk)},
            }
    return entries


def resolved_fields(name: str, entries: dict[str, dict[str, object]], seen: set[str] | None = None) -> dict[str, str]:
    seen = set() if seen is None else seen
    if name in seen or name not in entries:
        return {}
    seen.add(name)
    entry = entries[name]
    parent = str(entry["using"])
    result = resolved_fields(parent, entries, seen) if parent else {}
    result.update(entry["fields"])  # type: ignore[arg-type]
    return result


def handle(value: str) -> str | None:
    match = HANDLE_RE.fullmatch(value)
    return match.group(1) if match else None


def stable_official_map(source: dict[str, ET.Element], target: dict[str, ET.Element]) -> dict[str, str]:
    candidates: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for uid, source_node in source.items():
        target_node = target.get(uid)
        source_text = source_node.text or ""
        target_text = target_node.text if target_node is not None else ""
        if source_text and target_text:
            candidates[normalise(source_text)][target_text] += 1
    result: dict[str, str] = {}
    for source_text, options in candidates.items():
        ranked = options.most_common()
        if len(ranked) == 1 or ranked[0][1] > ranked[1][1]:
            result[source_text] = ranked[0][0]
    return result


def parse_scroll_handles(entries: dict[str, dict[str, object]]) -> tuple[int, set[str], set[str], int]:
    object_path = STATS / "Object.txt"
    if not object_path.exists():
        return 0, set(), set(), 0
    text = object_path.read_text(encoding="utf-8-sig")
    matches = list(ENTRY_RE.finditer(text))
    scroll_roots: set[str] = set()
    for index, match in enumerate(matches):
        chunk = text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        fields = {key: value for key, value in DATA_RE.findall(chunk)}
        if match.group(1).startswith("OBJ_Scroll_") or fields.get("ObjectCategory", "").startswith("MagicScroll"):
            root = fields.get("RootTemplate", "")
            if root:
                scroll_roots.add(root.lower())

    title_handles: set[str] = set()
    description_handles: set[str] = set()
    found_templates = 0
    processed_roots: set[str] = set()
    for template_dir in ROOT_TEMPLATE_DIRS:
        for path in sorted(template_dir.glob("*.lsx")):
            root_id = path.stem.lower()
            if root_id not in scroll_roots or root_id in processed_roots:
                continue
            processed_roots.add(root_id)
            found_templates += 1
            root = ET.parse(path).getroot()
            for attribute in root.iter("attribute"):
                uid = attribute.attrib.get("handle", "")
                if not uid:
                    continue
                if attribute.attrib.get("id") == "DisplayName":
                    title_handles.add(uid)
                elif "Description" in attribute.attrib.get("id", ""):
                    description_handles.add(uid)
    return len(scroll_roots), title_handles, description_handles, found_templates


def main() -> None:
    source_nodes, source = localization(SOURCE)
    target_nodes, target = localization(TARGET)
    _, bg_en = localization(BG_EN)
    _, bg_pl = localization(BG_PL)
    official = stable_official_map(bg_en, bg_pl)
    entries = parse_stats()

    spell_entries = {name: value for name, value in entries.items() if value["type"] == "SpellData"}
    title_handles: set[str] = set()
    description_handles: set[str] = set()
    root_spell_names: set[str] = set()
    root_title_handles: set[str] = set()
    for name, entry in spell_entries.items():
        fields = resolved_fields(name, entries)
        own_fields: dict[str, str] = entry["fields"]  # type: ignore[assignment]
        title = handle(fields.get("DisplayName", ""))
        if title and title in source:
            title_handles.add(title)
        for key, value in fields.items():
            if "Description" in key:
                uid = handle(value)
                if uid and uid in source:
                    description_handles.add(uid)

        flags = fields.get("SpellFlags", "")
        costs = fields.get("UseCosts", "")
        is_actual = (
            "IsSpell" in flags
            or "SpellSlot" in costs
            or bool(fields.get("MemoryCost"))
            or (bool(fields.get("Level")) and bool(fields.get("SpellSchool")))
        )
        is_root = not own_fields.get("RootSpellID") and not re.search(r"_[2-9]$", name)
        if is_actual and is_root and title and title in source:
            root_spell_names.add(name)
            root_title_handles.add(title)

    all_handles = title_handles | description_handles
    structure_errors: list[tuple[str, str]] = []
    language_errors: list[tuple[str, str]] = []
    official_title_mismatches: list[tuple[str, str, str, str]] = []
    official_description_mismatches: list[tuple[str, str, str]] = []

    for uid in sorted(all_handles):
        if uid not in target:
            structure_errors.append((uid, "missing target handle"))
            continue
        source_text = source[uid].text or ""
        target_text = target[uid].text or ""
        if collections.Counter(TAG_RE.findall(source_text)) != collections.Counter(TAG_RE.findall(target_text)):
            structure_errors.append((uid, "tag mismatch"))
        if PLACEHOLDER_RE.findall(source_text) != PLACEHOLDER_RE.findall(target_text):
            structure_errors.append((uid, "placeholder mismatch"))
        if dice_signature(source_text) != dice_signature(target_text):
            structure_errors.append((uid, "dice mismatch"))
        if ENGLISH_RE.search(visible(target_text)):
            language_errors.append((uid, "residual English"))
        if source_text == target_text and normalise(source_text) not in UNCHANGED_WHITELIST and re.search(r"[A-Za-z]", source_text):
            language_errors.append((uid, "unchanged English"))

    approved_official_title_corrections = {
        # The stable exact BG3 match is the status adjective; the spell name in
        # the Polish D&D 2024 corpus is the noun "Przebudzenie".
        "hfefb5384gcdb9g70a3g4fd3g5796fed23526": "Przebudzenie",
    }
    approved_official_description_corrections = {
        # The shipped Polish rows contain a noun-agreement error and an
        # Attack-Roll/Saving-Throw semantic swap, respectively.
        "h409cb932g8ed1gc110g3616g0fa1bc73cc21": (
            "Nakaż istocie, by natychmiast <LSTag Type=\"Status\" Tooltip=\"PRONE\">padła</LSTag> na ziemię."
        ),
        "hc0faf0e3g6b1bgefbbge13cg61d3cdca920b": (
            "Nałóż klątwę dotykiem. Istota pod jej wpływem ma <LSTag Tooltip=\"Disadvantage\">"
            "utrudnienie</LSTag> w <LSTag Tooltip=\"AttackRoll\">testach ataku</LSTag> przeciwko tobie."
        ),
    }
    approved_title_corrections = 0
    for uid in sorted(root_title_handles):
        english = source[uid].text or ""
        expected = official.get(normalise(english))
        actual = target[uid].text or ""
        if expected is not None and actual == approved_official_title_corrections.get(uid) and actual != expected:
            approved_title_corrections += 1
        elif expected is not None and actual != expected:
            official_title_mismatches.append((uid, english, expected, target[uid].text or ""))
    for uid in sorted(description_handles):
        english = source[uid].text or ""
        expected = official.get(normalise(english))
        actual = target[uid].text or ""
        if expected is not None and actual not in {expected, approved_official_description_corrections.get(uid)}:
            official_description_mismatches.append((uid, expected, target[uid].text or ""))

    scroll_roots, scroll_titles, scroll_descriptions, scroll_templates = parse_scroll_handles(entries)
    scroll_handles = scroll_titles | scroll_descriptions
    scroll_missing_source = scroll_handles - set(source)
    scroll_missing_target = scroll_handles - set(target)

    list_path = BASE / "Public" / MOD / "Lists" / "SpellLists.lsx"
    list_root = ET.parse(list_path).getroot()
    list_nodes = list(list_root.findall(".//node[@id='SpellList']"))
    listed_ids: set[str] = set()
    for attribute in list_root.findall(".//attribute[@id='Spells']"):
        listed_ids.update(value for value in attribute.attrib.get("value", "").split(";") if value)
    listed_custom = listed_ids & set(spell_entries)
    listed_missing_titles = {
        name
        for name in listed_custom
        if (uid := handle(resolved_fields(name, entries).get("DisplayName", ""))) and uid in source and uid not in target
    }

    print(f"SpellData entries parsed: {len(spell_entries)}")
    print(f"Localized spell/action title handles: {len(title_handles)}")
    print(f"Localized spell/action description handles: {len(description_handles)}")
    print(f"Root spell entries detected: {len(root_spell_names)}")
    print(f"Distinct root spell title handles: {len(root_title_handles)}")
    print(f"Spell structure errors: {len(structure_errors)}")
    print(f"Spell language errors: {len(language_errors)}")
    print(f"Official root-title mismatches: {len(official_title_mismatches)}")
    print(f"Approved official root-title corrections: {approved_title_corrections}")
    print(f"Official description mismatches: {len(official_description_mismatches)}")
    print(f"Spell-list nodes: {len(list_nodes)}")
    print(f"Distinct spell IDs in lists: {len(listed_ids)}")
    print(f"Listed IDs defined by mod: {len(listed_custom)}")
    print(f"Listed custom spells missing Polish titles: {len(listed_missing_titles)}")
    print(f"Scroll stats entries: {scroll_roots}")
    print(f"Scroll root templates found: {scroll_templates}")
    print(f"Scroll title handles: {len(scroll_titles)}")
    print(f"Scroll description handles: {len(scroll_descriptions)}")
    print(f"Scroll handles missing from source: {len(scroll_missing_source)}")
    print(f"Scroll handles missing from Polish: {len(scroll_missing_target)}")

    title_report = ROOT / "polish_spell_titles.tsv"
    with title_report.open("w", encoding="utf-8", newline="") as handle_out:
        writer = csv.writer(handle_out, delimiter="\t", lineterminator="\n")
        writer.writerow(("contentuid", "english", "polish", "official_exact"))
        for uid in sorted(root_title_handles, key=lambda value: (source[value].text or "").casefold()):
            english = source[uid].text or ""
            writer.writerow((uid, english, target[uid].text or "", "yes" if normalise(english) in official else "no"))
    print(f"Root spell title report: {title_report}")

    for uid, issue in structure_errors[:100]:
        print(f"STRUCTURE\t{uid}\t{issue}")
    for uid, issue in language_errors[:100]:
        print(f"LANGUAGE\t{uid}\t{issue}\t{target[uid].text or ''}")
    for uid, english, expected, actual in official_title_mismatches[:100]:
        print(f"OFFICIAL_TITLE\t{uid}\t{english}\t{expected}\t{actual}")
    for uid, expected, actual in official_description_mismatches[:100]:
        print(f"OFFICIAL_DESCRIPTION\t{uid}\t{expected}\t{actual}")

    if structure_errors or language_errors or official_title_mismatches or official_description_mismatches or listed_missing_titles:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
