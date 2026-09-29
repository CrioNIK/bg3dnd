from __future__ import annotations

import collections
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


work = Path(__file__).resolve().parent
repo = Path(sys.argv[1]).resolve()
base = repo / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization"


def norm(text: str | None) -> str:
    visible = re.sub(r"<[^>]+>", "", text or "")
    return " ".join(visible.split()).casefold().replace("’", "'")


english = {
    node.attrib["contentuid"]: node.text or ""
    for node in ET.parse(base / "English" / "english.xml").getroot()
}
polish = {
    node.attrib["contentuid"]: node.text or ""
    for node in ET.parse(base / "Polish" / "polish.xml").getroot()
}
official_polish = {
    node.attrib["contentuid"]: node.text or ""
    for node in ET.parse(work / "official_bg3_polish_20260828" / "polish.loca.xml").getroot()
}
official_map: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
for node in ET.parse(work / "official_bg3_english_20260828" / "english.loca.xml").getroot():
    uid = node.attrib["contentuid"]
    if uid in official_polish:
        official_map[norm(node.text)].append((uid, official_polish[uid]))

for uid in sys.argv[2:]:
    matches = official_map[norm(english[uid])]
    print(f"\n{uid}\nEN: {english[uid]}\nPL: {polish[uid]}\nOFFICIAL_MATCHES={len(matches)}")
    for official_uid, text in matches:
        print(f"{official_uid} => {text}")
