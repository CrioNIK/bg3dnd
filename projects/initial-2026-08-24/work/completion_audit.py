from __future__ import annotations

import collections
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent
BASE_ROOT = ROOT / "audit_installed_20260824_2257" / "base"
MOD_FOLDER = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
CURRENT_EN = BASE_ROOT / "Mods" / MOD_FOLDER / "Localization" / "English" / "english.xml"
OLD_EN = ROOT / "dnd55e-spilluminati" / "Mods" / MOD_FOLDER / "Localization" / "English" / "english.xml"
TARGET = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "ukrainian_current.xml"
PUBLIC = BASE_ROOT / "Public" / MOD_FOLDER
BG_EN = ROOT / "bg3-en.xml"
BG_UK = ROOT / "bg3-uk.xml"

TAG_RE = re.compile(r"</?[^>]+>")
BRACKET_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"\b((?:\d*)d\d+)(?:s)?\b", re.IGNORECASE)
ASCII_WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z'’-]{2,}\b")
CYRILLIC_RE = re.compile(r"[А-Яа-яІіЇїЄєҐґ]")


def load(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def visible(text: str) -> str:
    return DICE_RE.sub(" ", BRACKET_RE.sub(" ", TAG_RE.sub(" ", text)))


def duplicate_uids(nodes: list[ET.Element]) -> list[str]:
    counts = collections.Counter(node.attrib["contentuid"] for node in nodes)
    return [uid for uid, count in counts.items() if count > 1]


def referenced_handles(path: Path) -> set[str]:
    handles: set[str] = set()
    for attribute in ET.parse(path).iter("attribute"):
        handle = attribute.attrib.get("handle")
        if handle:
            handles.add(handle)
    return handles


def main() -> None:
    errors: list[str] = []
    current_nodes, current = load(CURRENT_EN)
    old_nodes, old = load(OLD_EN)
    target_nodes, target = load(TARGET)
    _, bg_en = load(BG_EN)
    _, bg_uk = load(BG_UK)

    if duplicate_uids(current_nodes):
        errors.append("current English has duplicate UIDs")
    if duplicate_uids(target_nodes):
        errors.append("Ukrainian has duplicate UIDs")
    if set(current) != set(target):
        errors.append(
            f"UID set mismatch: missing={len(set(current) - set(target))}, stale={len(set(target) - set(current))}"
        )

    version_mismatches = 0
    empty_rows = 0
    tag_mismatches = 0
    placeholder_mismatches = 0
    dice_mismatches = 0
    dice_mismatch_examples: list[str] = []
    visible_english_rows = 0
    unchanged_english_rows = 0
    for uid, source_node in current.items():
        target_node = target.get(uid)
        if target_node is None:
            continue
        source = source_node.text or ""
        translation = target_node.text or ""
        version_mismatches += source_node.attrib.get("version") != target_node.attrib.get("version")
        empty_rows += not translation.strip()
        tag_mismatches += collections.Counter(TAG_RE.findall(source)) != collections.Counter(
            TAG_RE.findall(translation)
        )
        placeholder_mismatches += BRACKET_RE.findall(source) != BRACKET_RE.findall(translation)
        source_dice = collections.Counter(value.lower() for value in DICE_RE.findall(source))
        target_dice = collections.Counter(value.lower() for value in DICE_RE.findall(translation))
        dice_differs = source_dice != target_dice
        dice_mismatches += dice_differs
        if dice_differs and len(dice_mismatch_examples) < 20:
            dice_mismatch_examples.append(f"{uid}: {dict(source_dice)} != {dict(target_dice)}")
        visible_english_rows += bool(ASCII_WORD_RE.search(visible(translation)))
        unchanged_english_rows += source == translation and bool(ASCII_WORD_RE.search(source))

    integrity = {
        "version mismatches": version_mismatches,
        "empty rows": empty_rows,
        "tag mismatches": tag_mismatches,
        "placeholder mismatches": placeholder_mismatches,
        "dice mismatches": dice_mismatches,
        "visible English rows": visible_english_rows,
        "unchanged English rows": unchanged_english_rows,
    }
    for label, count in integrity.items():
        if count:
            errors.append(f"{label}: {count}")

    new_uids = set(current) - set(old)
    removed_uids = set(old) - set(current)
    changed_uids = {
        uid for uid in set(current) & set(old) if (current[uid].text or "") != (old[uid].text or "")
    }
    changed_versions = {
        uid
        for uid in set(current) & set(old)
        if current[uid].attrib.get("version") != old[uid].attrib.get("version")
    }
    for label, uids in (("new", new_uids), ("changed", changed_uids)):
        missing = uids - set(target)
        english = [uid for uid in uids & set(target) if ASCII_WORD_RE.search(visible(target[uid].text or ""))]
        if missing or english:
            errors.append(f"{label} subset: missing={len(missing)}, English={len(english)}")

    banned_patterns = {
        "тіфлінг": r"\bтіфлінг\w*\b",
        "рейнджер": r"\bрейнджер\w*\b",
        "страйк": r"\bстрайк\w*\b",
        "сейв": r"\bсейв\w*\b",
        "тест": r"\bтест\w*\b",
        "кастинг": r"\bкастинг\w*\b",
        "spell slot calque": r"\b(?:слот|комірк|гнізд)\w*\s+(?:заклят|заклин)",
        "opportunity attack calque": r"\bатак\w* можливост",
        "radiant calque": r"\b(?:радіант|радіаційн)\w*\b",
        "disadvantage calque": r"\bневигідн\w*\b",
        "cleric calque": r"\b(?:клерик|клирик)\w*\b",
        "skill calque": r"\bнавик\w*\b",
        "hit calque": r"\bпопадан\w*\b",
        "Magic Initiate calque": r"\b(?:магічний ініціатор|магія ініціатива)\b",
        "Eldritch transliteration": r"\bелдріч\w*\b",
        "pool calque": r"\b(?:пул(?:у|ом|і|а)?|басейн\w*)\b",
        "check calque": r"\bчек(?:ами|ах|ів|и|ом|у|а)?\b",
        "die calque": r"\bкубик\w*\b",
        "English dice plural": r"\bd\d+s\b",
        "deal calque": r"\bнанес\w*\s+шкод\w*\b",
        "web mistranslation": r"\bінтернет\b",
    }
    all_target_text = "\n".join(node.text or "" for node in target_nodes)
    banned_counts = {
        label: len(re.findall(pattern, all_target_text, flags=re.IGNORECASE))
        for label, pattern in banned_patterns.items()
    }
    for label, count in banned_counts.items():
        if count:
            errors.append(f"banned term {label}: {count}")

    resource_paths = {
        "class/subclass": [PUBLIC / "ClassDescriptions" / "ClassDescriptions.lsx"],
        "race/subrace": [PUBLIC / "Races" / "Races.lsx"],
        "background": [PUBLIC / "Backgrounds" / "Backgrounds.lsx"],
        "feat": [PUBLIC / "Feats" / "FeatDescriptions.lsx"],
        "progression": [
            PUBLIC / "Progressions" / "Progressions.lsx",
            PUBLIC / "Progressions" / "ProgressionDescriptions.lsx",
        ],
    }
    resource_results: dict[str, tuple[int, int, int]] = {}
    for label, paths in resource_paths.items():
        handles: set[str] = set()
        for path in paths:
            handles.update(referenced_handles(path))
        mod_handles = handles & set(current)
        official_handles = (handles - mod_handles) & set(bg_en)
        missing_mod = mod_handles - set(target)
        missing_official = official_handles - set(bg_uk)
        untranslated = [
            uid
            for uid in mod_handles & set(target)
            if not CYRILLIC_RE.search(target[uid].text or "")
            or ASCII_WORD_RE.search(visible(target[uid].text or ""))
        ]
        resource_results[label] = (len(mod_handles), len(official_handles), len(untranslated))
        if missing_mod or missing_official or untranslated:
            errors.append(
                f"{label}: missing custom={len(missing_mod)}, missing official={len(missing_official)}, untranslated={len(untranslated)}"
            )

    screenshot_expectations = {
        "h52005c15gb62ag4e2egb087ge08e4918fcdc": "Дампір",
        "hfe00d696gc13ega9a7g3f41g5fe01cf6c73e": "Абісальний бісин",
        "hc7b4d637g873egedaega2b5g55638c2965cd": "Хтонічний бісин",
        "h502c43ffg8aceg5a29gb438g81efeef8bc10": "Пекельний бісин",
        "h287cfbfeg028cgfb00g3888gc26915b76c24": "Еладрін",
    }
    for uid, expected in screenshot_expectations.items():
        actual = target.get(uid)
        if actual is None or (actual.text or "") != expected:
            errors.append(f"screenshot title {uid}: expected {expected!r}")
    for uid in (
        "hbf2d2837g837cgd6c3g5fdegad558013ec2f",
        "he5309e85gddddg797fg0081g19accd6ede60",
    ):
        actual = target.get(uid)
        if actual is None or not CYRILLIC_RE.search(actual.text or "") or ASCII_WORD_RE.search(visible(actual.text or "")):
            errors.append(f"screenshot description {uid} is not fully Ukrainian")

    lines = [
        "D&D 5.5e Beyond — Ukrainian localization audit",
        f"Target: {TARGET}",
        "",
        f"Current source entries: {len(current_nodes)}",
        f"Ukrainian entries: {len(target_nodes)}",
        f"New since previous mod build: {len(new_uids)}",
        f"Changed since previous mod build: {len(changed_uids)}",
        f"Version-only changes: {len(changed_versions)}",
        f"Removed from current source: {len(removed_uids)}",
        "",
        "Integrity checks:",
    ]
    lines.extend(f"- {label}: {count}" for label, count in integrity.items())
    lines.extend(("", "Referenced localization handles:"))
    for label, (custom, official, untranslated) in resource_results.items():
        lines.append(
            f"- {label}: custom={custom}, official fallback={official}, untranslated custom={untranslated}"
        )
    lines.extend(("", "Prohibited terminology:"))
    lines.extend(f"- {label}: {count}" for label, count in banned_counts.items())
    lines.extend(("", f"RESULT: {'PASS' if not errors else 'FAIL'}"))
    if errors:
        lines.extend(f"ERROR: {error}" for error in errors)
        lines.extend(f"DICE: {example}" for example in dice_mismatch_examples)
    report = "\n".join(lines) + "\n"
    print(report, end="")
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(report, encoding="utf-8")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
