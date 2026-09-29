from __future__ import annotations

import collections
import csv
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "audit_installed_20260824_2257" / "base" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "English" / "english.xml"
TARGET = ROOT / "ukrainian_current.xml"
BG_EN = ROOT / "bg3-en.xml"
BG_UK = ROOT / "bg3-uk.xml"
OUT = ROOT / "editorial_inventory.tsv"

TAG_RE = re.compile(r"</?[^>]+>")
TOKEN_RE = re.compile(r"</?[^>]+>|\[[^\]\n]+\]|\b\d*d\d+(?:s)?\b", re.I)


def load(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def visible(value: str) -> str:
    return " ".join(TOKEN_RE.sub(" ", value).split())


def main() -> None:
    source_nodes, source = load(SOURCE)
    _, target = load(TARGET)
    bg_en_nodes, bg_en = load(BG_EN)
    _, bg_uk = load(BG_UK)

    official: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for node in bg_en_nodes:
        uid = node.attrib["contentuid"]
        en = node.text or ""
        uk_node = bg_uk.get(uid)
        uk = uk_node.text or "" if uk_node is not None else ""
        if en and uk:
            official[en][uk] += 1

    official_exact = {en: choices.most_common(1)[0][0] for en, choices in official.items()}
    uids_by_source: dict[str, list[str]] = collections.defaultdict(list)
    for node in source_nodes:
        uids_by_source[node.text or ""].append(node.attrib["contentuid"])

    rows: list[tuple[str, int, str, str, str, str]] = []
    for en, uids in uids_by_source.items():
        variants = collections.Counter((target[uid].text or "") for uid in uids)
        current = variants.most_common(1)[0][0]
        source_kind = "official-exact" if en in official_exact else "mod-only"
        official_uk = official_exact.get(en, "")
        rows.append((source_kind, len(uids), uids[0], en, current, official_uk))

    rows.sort(key=lambda row: (row[0], -row[1], visible(row[3]).casefold()))
    with OUT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(("kind", "occurrences", "sample_uid", "english", "current_ukrainian", "official_bg3_ukrainian"))
        writer.writerows(rows)

    counts = collections.Counter(row[0] for row in rows)
    print(f"entries={len(source_nodes)} unique_source_texts={len(rows)}")
    print(f"official_exact_unique={counts['official-exact']} mod_only_unique={counts['mod-only']}")
    print(f"official_exact_rows={sum(row[1] for row in rows if row[0] == 'official-exact')}")
    print(f"mod_only_rows={sum(row[1] for row in rows if row[0] == 'mod-only')}")
    print(f"wrote={OUT}")


if __name__ == "__main__":
    main()
