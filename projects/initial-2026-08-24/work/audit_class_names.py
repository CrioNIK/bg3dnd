from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE = ROOT / "audit_installed_20260824_2257" / "base"
MOD = BASE / "Public" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
CLASSES = MOD / "ClassDescriptions" / "ClassDescriptions.lsx"
ENGLISH = (
    BASE
    / "Mods"
    / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
    / "Localization"
    / "English"
    / "english.xml"
)
UKRAINIAN = ROOT / "ukrainian_current.xml"
BG_ENGLISH = ROOT / "bg3-en.xml"
BG_UKRAINIAN = ROOT / "bg3-uk.xml"


def localization(path: Path) -> dict[str, str]:
    return {
        node.attrib["contentuid"]: node.text or ""
        for node in ET.parse(path).getroot().findall("content")
    }


def main() -> None:
    english = localization(ENGLISH)
    ukrainian = localization(UKRAINIAN)
    official_english = localization(BG_ENGLISH)
    official_ukrainian = localization(BG_UKRAINIAN)
    count = 0
    for node in ET.parse(CLASSES).iter("node"):
        if node.attrib.get("id") != "ClassDescription":
            continue
        attributes = {item.attrib.get("id"): item for item in node.findall("attribute")}
        name = attributes.get("Name")
        display = attributes.get("DisplayName")
        if name is None or display is None:
            continue
        handle = display.attrib["handle"]
        source = english.get(handle, official_english.get(handle, "<missing>"))
        target = ukrainian.get(handle, official_ukrainian.get(handle, "<missing>"))
        print(f"{name.attrib['value']}\t{handle}\t{source}\t{target}")
        count += 1
    print(f"TOTAL\t{count}")


if __name__ == "__main__":
    main()
