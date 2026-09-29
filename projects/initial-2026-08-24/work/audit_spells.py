from __future__ import annotations

import collections
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from editorial_overrides import UID_OVERRIDES as EDITORIAL_UID_OVERRIDES
from proofreading_overrides import UID_OVERRIDES as PROOFREADING_UID_OVERRIDES


ROOT = Path(__file__).resolve().parent
BASE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "audit_installed_20260824_2257" / "base"
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
STATS = BASE / "Public" / MOD / "Stats" / "Generated" / "Data"
SOURCE = BASE / "Mods" / MOD / "Localization" / "English" / "english.xml"
TARGET = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "ukrainian_current.xml"
BG_EN = ROOT / "bg3-en.xml"
BG_UK = ROOT / "bg3-uk.xml"

ENTRY_RE = re.compile(r'^new entry "([^"]+)"$', re.MULTILINE)
TYPE_RE = re.compile(r'^type "([^"]+)"$', re.MULTILINE)
USING_RE = re.compile(r'^using "([^"]+)"$', re.MULTILINE)
DATA_RE = re.compile(r'^data "([^"]+)" "(.*)"$', re.MULTILINE)
HANDLE_RE = re.compile(r"^(h[0-9a-z]+);\d+$", re.IGNORECASE)
TAG_RE = re.compile(r"</?[^>]+>")
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"\b(\d*d\d+)(?:s)?\b", re.IGNORECASE)
ASCII_RE = re.compile(r"\b[A-Za-z][A-Za-z'’-]{2,}\b")
CYRILLIC_RE = re.compile(r"[А-Яа-яІіЇїЄєҐґ]")


def localization(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def visible(text: str) -> str:
    return DICE_RE.sub(" ", PLACEHOLDER_RE.sub(" ", TAG_RE.sub(" ", text)))


def parse_stats() -> dict[str, dict[str, object]]:
    entries: dict[str, dict[str, object]] = {}
    for path in sorted(STATS.glob("Spell_*.txt")):
        text = path.read_text(encoding="utf-8-sig")
        matches = list(ENTRY_RE.finditer(text))
        for index, match in enumerate(matches):
            chunk = text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
            entry_type = TYPE_RE.search(chunk)
            using = USING_RE.search(chunk)
            fields = {key: value for key, value in DATA_RE.findall(chunk)}
            entries[match.group(1)] = {
                "type": entry_type.group(1) if entry_type else "",
                "using": using.group(1) if using else "",
                "fields": fields,
                "file": path.name,
            }
    return entries


def parse_scroll_stats() -> dict[str, str]:
    path = STATS / "Object.txt"
    text = path.read_text(encoding="utf-8-sig")
    matches = list(ENTRY_RE.finditer(text))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        chunk = text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        fields = {key: value for key, value in DATA_RE.findall(chunk)}
        name = match.group(1)
        if name.startswith("OBJ_Scroll_") or fields.get("ObjectCategory", "").startswith("MagicScroll"):
            root_template = fields.get("RootTemplate", "")
            if root_template:
                result[root_template.lower()] = name
    return result


def parse_scroll_templates(scroll_stats: dict[str, str]) -> tuple[set[str], set[str], set[str]]:
    template_dir = BASE / "Public" / MOD / "RootTemplates"
    templates: set[str] = set()
    titles: set[str] = set()
    descriptions: set[str] = set()
    for path in sorted(template_dir.glob("*.lsx")):
        root_id = path.stem.lower()
        if root_id not in scroll_stats:
            continue
        templates.add(root_id)
        root = ET.parse(path).getroot()
        for attribute in root.iter("attribute"):
            uid = attribute.attrib.get("handle", "")
            if not uid:
                continue
            if attribute.attrib.get("id") == "DisplayName":
                titles.add(uid)
            elif "Description" in attribute.attrib.get("id", ""):
                descriptions.add(uid)
    return templates, titles, descriptions


def parse_spell_lists() -> tuple[int, set[str]]:
    path = BASE / "Public" / MOD / "Lists" / "SpellLists.lsx"
    root = ET.parse(path).getroot()
    list_nodes = list(root.findall(".//node[@id='SpellList']"))
    spell_ids: set[str] = set()
    for attribute in root.findall(".//attribute[@id='Spells']"):
        spell_ids.update(value for value in attribute.attrib.get("value", "").split(";") if value)
    return len(list_nodes), spell_ids


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


def official_exact() -> dict[str, str]:
    en_nodes, en = localization(BG_EN)
    _, uk = localization(BG_UK)
    candidates: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for node in en_nodes:
        uid = node.attrib["contentuid"]
        source = node.text or ""
        target_node = uk.get(uid)
        target = target_node.text or "" if target_node is not None else ""
        if source and target and CYRILLIC_RE.search(target) and not ASCII_RE.search(visible(target)):
            candidates[source][target] += 1
    return {source: targets.most_common(1)[0][0] for source, targets in candidates.items()}


def main() -> None:
    source_nodes, source = localization(SOURCE)
    target_nodes, target = localization(TARGET)
    entries = parse_stats()
    exact = official_exact()
    scroll_stats = parse_scroll_stats()
    scroll_templates, scroll_title_handles, scroll_description_handles = parse_scroll_templates(scroll_stats)
    scroll_template_files_missing = set(scroll_stats) - scroll_templates
    spell_list_count, listed_spell_ids = parse_spell_lists()

    spell_entries = {name: value for name, value in entries.items() if value["type"] == "SpellData"}
    all_title_handles: set[str] = set()
    all_description_handles: set[str] = set()
    actual_title_handles: set[str] = set()
    actual_entry_names: set[str] = set()

    for name, entry in spell_entries.items():
        fields = resolved_fields(name, entries)
        own_fields: dict[str, str] = entry["fields"]  # type: ignore[assignment]
        title = handle(fields.get("DisplayName", ""))
        if title and title in source:
            all_title_handles.add(title)
        for key, value in fields.items():
            if "Description" in key:
                uid = handle(value)
                if uid and uid in source:
                    all_description_handles.add(uid)

        flags = fields.get("SpellFlags", "")
        costs = fields.get("UseCosts", "")
        is_actual_spell = (
            "IsSpell" in flags
            or "SpellSlot" in costs
            or bool(fields.get("MemoryCost"))
            or (bool(fields.get("Level")) and bool(fields.get("SpellSchool")))
        )
        is_root = not own_fields.get("RootSpellID") and not re.search(r"_[2-9]$", name)
        if is_actual_spell and is_root and title and title in source:
            actual_title_handles.add(title)
            actual_entry_names.add(name)

    handles = all_title_handles | all_description_handles
    missing = handles - set(target)
    residual = {
        uid for uid in handles & set(target) if ASCII_RE.search(visible(target[uid].text or ""))
    }
    unchanged = {
        uid
        for uid in handles & set(target)
        if (source[uid].text or "") == (target[uid].text or "") and ASCII_RE.search(source[uid].text or "")
    }
    tag_mismatches = {
        uid
        for uid in handles & set(target)
        if collections.Counter(TAG_RE.findall(source[uid].text or ""))
        != collections.Counter(TAG_RE.findall(target[uid].text or ""))
    }
    placeholder_mismatches = {
        uid
        for uid in handles & set(target)
        if PLACEHOLDER_RE.findall(source[uid].text or "") != PLACEHOLDER_RE.findall(target[uid].text or "")
    }
    dice_mismatches = {
        uid
        for uid in handles & set(target)
        if [value.lower() for value in DICE_RE.findall(source[uid].text or "")]
        != [value.lower() for value in DICE_RE.findall(target[uid].text or "")]
    }

    official_matches = 0
    official_mismatches: list[tuple[str, str, str, str]] = []
    for uid in sorted(actual_title_handles):
        english = source[uid].text or ""
        expected = exact.get(english)
        if not expected:
            continue
        official_matches += 1
        actual = target[uid].text or ""
        if actual != expected:
            official_mismatches.append((uid, english, expected, actual))

    official_description_comparisons = 0
    official_description_editorial_exceptions = 0
    official_description_mismatches: list[tuple[str, str, str]] = []
    for uid in sorted(all_description_handles):
        english = source[uid].text or ""
        expected = exact.get(english)
        if not expected:
            continue
        official_description_comparisons += 1
        actual = target[uid].text or ""
        if actual != expected:
            if (
                (uid in EDITORIAL_UID_OVERRIDES and actual == EDITORIAL_UID_OVERRIDES[uid])
                or (uid in PROOFREADING_UID_OVERRIDES and actual == PROOFREADING_UID_OVERRIDES[uid])
            ):
                official_description_editorial_exceptions += 1
            else:
                official_description_mismatches.append((uid, expected, actual))

    scroll_handles = scroll_title_handles | scroll_description_handles
    scroll_missing_source = scroll_handles - set(source)
    scroll_missing_target = scroll_handles - set(target)
    scroll_visible_english = {
        uid for uid in scroll_handles & set(target) if ASCII_RE.search(visible(target[uid].text or ""))
    }
    scroll_unchanged_english = {
        uid
        for uid in scroll_handles & set(source) & set(target)
        if (source[uid].text or "") == (target[uid].text or "") and ASCII_RE.search(source[uid].text or "")
    }
    scroll_tag_mismatches = {
        uid
        for uid in scroll_handles & set(source) & set(target)
        if collections.Counter(TAG_RE.findall(source[uid].text or ""))
        != collections.Counter(TAG_RE.findall(target[uid].text or ""))
    }
    scroll_placeholder_mismatches = {
        uid
        for uid in scroll_handles & set(source) & set(target)
        if PLACEHOLDER_RE.findall(source[uid].text or "") != PLACEHOLDER_RE.findall(target[uid].text or "")
    }
    scroll_dice_mismatches = {
        uid
        for uid in scroll_handles & set(source) & set(target)
        if [value.lower() for value in DICE_RE.findall(source[uid].text or "")]
        != [value.lower() for value in DICE_RE.findall(target[uid].text or "")]
    }
    listed_custom_ids = listed_spell_ids & set(spell_entries)
    listed_custom_resolved_titles = {
        name: handle(resolved_fields(name, entries).get("DisplayName", "")) for name in listed_custom_ids
    }
    listed_custom_missing_localized_title = {
        name
        for name, uid in listed_custom_resolved_titles.items()
        if uid and uid in source and uid not in target
    }

    print(f"SpellData entries parsed: {len(spell_entries)}")
    print(f"Localized spell/action title handles: {len(all_title_handles)}")
    print(f"Localized spell/action description handles: {len(all_description_handles)}")
    print(f"Root spell entries detected: {len(actual_entry_names)}")
    print(f"Distinct root spell title handles: {len(actual_title_handles)}")
    print(f"Official BG3 title comparisons: {official_matches}")
    print(f"Missing Ukrainian handles: {len(missing)}")
    print(f"Visible English handles: {len(residual)}")
    print(f"Unchanged English handles: {len(unchanged)}")
    print(f"Tag mismatches: {len(tag_mismatches)}")
    print(f"Placeholder mismatches: {len(placeholder_mismatches)}")
    print(f"Dice mismatches: {len(dice_mismatches)}")
    print(f"Official title mismatches: {len(official_mismatches)}")
    print(f"Official description comparisons: {official_description_comparisons}")
    print(f"Intentional editorial description corrections: {official_description_editorial_exceptions}")
    print(f"Official description mismatches: {len(official_description_mismatches)}")
    print(f"Spell-list nodes: {spell_list_count}")
    print(f"Distinct spell IDs in lists: {len(listed_spell_ids)}")
    print(f"Listed spell IDs defined by mod: {len(listed_custom_ids)}")
    print(f"Listed custom spells missing localized titles: {len(listed_custom_missing_localized_title)}")
    print(f"Scroll stats entries: {len(scroll_stats)}")
    print(f"Scroll root templates found: {len(scroll_templates)}")
    print(f"Scroll root-template files missing: {len(scroll_template_files_missing)}")
    print(f"Scroll title handles: {len(scroll_title_handles)}")
    print(f"Scroll description handles: {len(scroll_description_handles)}")
    print(f"Scroll handles missing from source: {len(scroll_missing_source)}")
    print(f"Scroll handles missing from Ukrainian: {len(scroll_missing_target)}")
    print(f"Scroll handles with visible English: {len(scroll_visible_english)}")
    print(f"Scroll handles unchanged in English: {len(scroll_unchanged_english)}")
    print(f"Scroll tag mismatches: {len(scroll_tag_mismatches)}")
    print(f"Scroll placeholder mismatches: {len(scroll_placeholder_mismatches)}")
    print(f"Scroll dice mismatches: {len(scroll_dice_mismatches)}")
    for uid, english, expected, actual in official_mismatches[:100]:
        print(f"MISMATCH\t{uid}\t{english}\t{expected}\t{actual}")
    for uid, expected, actual in official_description_mismatches[:30]:
        print(f"DESCRIPTION_MISMATCH\t{uid}\t{expected}\t{actual}")
    for uid in sorted(tag_mismatches):
        print(f"TAG_MISMATCH\t{uid}\t{source[uid].text or ''}\t{target[uid].text or ''}")
    for uid in sorted(placeholder_mismatches):
        print(f"PLACEHOLDER_MISMATCH\t{uid}\t{source[uid].text or ''}\t{target[uid].text or ''}")
    for uid in sorted(dice_mismatches):
        print(f"DICE_MISMATCH\t{uid}\t{source[uid].text or ''}\t{target[uid].text or ''}")
    for root_id in sorted(scroll_template_files_missing):
        print(f"SCROLL_TEMPLATE_MISSING\t{root_id}\t{scroll_stats[root_id]}")
    for uid in sorted(actual_title_handles, key=lambda value: (source[value].text or "").lower()):
        print(f"SPELL_TITLE\t{uid}\t{source[uid].text or ''}\t{target[uid].text or ''}")


if __name__ == "__main__":
    main()
