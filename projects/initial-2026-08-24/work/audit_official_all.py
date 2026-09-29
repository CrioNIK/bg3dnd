from __future__ import annotations

import collections
import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve()
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
EN_PATH = REPO / "Mods" / MOD / "Localization" / "English" / "english.xml"
UK_PATH = REPO / "Mods" / MOD / "Localization" / "Ukrainian" / "ukrainian.xml"
BG_EN_PATH = ROOT / "bg3-en.xml"
BG_UK_PATH = ROOT / "bg3-uk.xml"
OUT_PATH = ROOT / "official_exact_mismatches.tsv"


def load(path: Path) -> tuple[list[ET.Element], dict[str, str]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {n.attrib["contentuid"]: n.text or "" for n in nodes}


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def main() -> None:
    en_nodes, en = load(EN_PATH)
    _, uk = load(UK_PATH)
    _, bg_en = load(BG_EN_PATH)
    _, bg_uk = load(BG_UK_PATH)

    official: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for uid, source in bg_en.items():
        target = bg_uk.get(uid, "")
        if source and target:
            official[norm(source)][target] += 1

    rows: list[tuple[str, str, str, str, int]] = []
    comparable = 0
    ambiguous = 0
    exact = 0
    for node in en_nodes:
        uid = node.attrib["contentuid"]
        source = en[uid]
        candidates = official.get(norm(source))
        if not candidates:
            continue
        comparable += 1
        top = candidates.most_common()
        expected = top[0][0]
        if len(top) > 1 and top[0][1] == top[1][1]:
            ambiguous += 1
            continue
        actual = uk.get(uid, "")
        if norm(actual) == norm(expected):
            exact += 1
            continue
        rows.append((uid, source, expected, actual, top[0][1]))

    with OUT_PATH.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["uid", "english", "official_ukrainian", "current_ukrainian", "official_count"])
        writer.writerows(rows)

    print(f"mod_entries={len(en_nodes)}")
    print(f"comparable={comparable}")
    print(f"exact={exact}")
    print(f"ambiguous={ambiguous}")
    print(f"mismatches={len(rows)}")
    print(f"report={OUT_PATH}")


if __name__ == "__main__":
    main()
