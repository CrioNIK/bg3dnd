from __future__ import annotations

import collections
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "ukrainian_current.xml"
TAG_RE = re.compile(r"<[^>]+>")

PATTERNS = {
    "damage": re.compile(r"\b(?:по|у)шкоджен\w*\b", re.IGNORECASE),
    "radiant": re.compile(r"\b(?:радіаційн\w*|радіант\w*|радіації)\b", re.IGNORECASE),
    "saving_throw": re.compile(
        r"\b(?:рятівн\w*|рятувальн\w*|захисн\w*|економн\w*|"
        r"збереженн\w*|порятунк\w*|порятунку)\b",
        re.IGNORECASE,
    ),
    "spell_slot": re.compile(r"\b(?:слот\w*|гнізд\w*|комірк\w*)\b", re.IGNORECASE),
    "opportunity_attack": re.compile(r"\b(?:атак\w* можливост\w*|можливісн\w* атак\w*)\b", re.IGNORECASE),
    "check": re.compile(r"\bчек\w*\b", re.IGNORECASE),
}


def main() -> None:
    nodes = ET.parse(TARGET).getroot().findall("content")
    for name, pattern in PATTERNS.items():
        found: collections.Counter[str] = collections.Counter()
        rows: list[tuple[str, str]] = []
        for node in nodes:
            visible = TAG_RE.sub("", node.text or "")
            matches = pattern.findall(visible)
            if matches:
                found.update(value.casefold() for value in matches)
                rows.append((node.attrib["contentuid"], visible.replace("\n", " ")))
        print(f"\n[{name}] rows={len(rows)} forms={sum(found.values())}")
        print("forms:", ", ".join(f"{key}={count}" for key, count in found.most_common()))
        for uid, value in rows[:20]:
            print(f"{uid}\t{value}")


if __name__ == "__main__":
    main()
