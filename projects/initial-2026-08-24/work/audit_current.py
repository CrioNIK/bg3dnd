from __future__ import annotations

import collections
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OLD_EN = ROOT / "dnd55e-spilluminati" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "English" / "english.xml"
CURRENT_EN = ROOT / "audit_installed_20260824_2257" / "base" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "English" / "english.xml"
CURRENT_RU = ROOT / "audit_installed_20260824_2257" / "base" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "Russian" / "russian.xml"
ADDON_RU = ROOT / "audit_installed_20260824_2257" / "ru" / "Mods" / "DnD 5.5e AIO Russian" / "Localization" / "Russian" / "russian.xml"
CURRENT_UK = ROOT / "ukrainian.xml"

TAG_RE = re.compile(r"</?[^>]+>")
BRACKET_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"\b\d*d\d+(?:s)?(?:\s*[+\-]\s*\d+)?\b", re.I)
LATIN_WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z'’-]{2,}\b")


def load(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def duplicates(nodes: list[ET.Element]) -> dict[str, int]:
    counts = collections.Counter(node.attrib["contentuid"] for node in nodes)
    return {uid: count for uid, count in counts.items() if count > 1}


def visible_english(text: str) -> list[str]:
    text = TAG_RE.sub(" ", text)
    text = BRACKET_RE.sub(" ", text)
    text = DICE_RE.sub(" ", text)
    return LATIN_WORD_RE.findall(text)


def main() -> None:
    old_nodes, old = load(OLD_EN)
    current_nodes, current = load(CURRENT_EN)
    ru_nodes, ru = load(CURRENT_RU)
    addon_ru_nodes, addon_ru = load(ADDON_RU)
    uk_nodes, uk = load(CURRENT_UK)

    print(f"old_en_entries={len(old_nodes)} unique={len(old)} duplicates={len(duplicates(old_nodes))}")
    print(f"current_en_entries={len(current_nodes)} unique={len(current)} duplicates={len(duplicates(current_nodes))}")
    print(f"current_ru_entries={len(ru_nodes)} unique={len(ru)} duplicates={len(duplicates(ru_nodes))}")
    print(f"addon_ru_entries={len(addon_ru_nodes)} unique={len(addon_ru)} duplicates={len(duplicates(addon_ru_nodes))}")
    print(f"uk_entries={len(uk_nodes)} unique={len(uk)} duplicates={len(duplicates(uk_nodes))}")

    new_uids = [uid for uid in current if uid not in old]
    removed_uids = [uid for uid in old if uid not in current]
    changed_text = [
        uid for uid in current if uid in old and (current[uid].text or "") != (old[uid].text or "")
    ]
    changed_version = [
        uid
        for uid in current
        if uid in old and current[uid].attrib.get("version") != old[uid].attrib.get("version")
    ]
    missing_uk = [uid for uid in current if uid not in uk]
    stale_uk = [uid for uid in uk if uid not in current]
    source_changed_but_same_uk = [
        uid
        for uid in changed_text
        if uid in uk and (uk[uid].text or "") == (old[uid].text or "")
    ]
    current_english_in_uk = [
        (uid, visible_english(uk[uid].text or ""))
        for uid in current
        if uid in uk and visible_english(uk[uid].text or "")
    ]

    print(f"new_uids={len(new_uids)} removed_uids={len(removed_uids)}")
    print(f"changed_text={len(changed_text)} changed_version={len(changed_version)}")
    print(f"missing_uk={len(missing_uk)} stale_uk={len(stale_uk)}")
    print(f"source_changed_but_same_uk={len(source_changed_but_same_uk)}")
    print(f"visible_english_rows_in_uk={len(current_english_in_uk)}")
    print(f"current_en_missing_in_current_ru={len(set(current) - set(ru))}")
    print(f"current_en_missing_in_addon_ru={len(set(current) - set(addon_ru))}")

    print("NEW_UID_SAMPLES")
    for uid in new_uids[:100]:
        print(uid, repr((current[uid].text or "")[:240]))
    print("CHANGED_TEXT_SAMPLES")
    for uid in changed_text[:100]:
        print(uid, "OLD=", repr((old[uid].text or "")[:180]), "NEW=", repr((current[uid].text or "")[:180]))
    print("MISSING_UK_SAMPLES")
    for uid in missing_uk[:100]:
        print(uid, repr((current[uid].text or "")[:240]))


if __name__ == "__main__":
    main()
