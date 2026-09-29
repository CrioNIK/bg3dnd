from __future__ import annotations

import csv
import pathlib
import xml.etree.ElementTree as ET
from collections import defaultdict

import audit_spells as audit


ROOT = pathlib.Path(__file__).resolve().parent
DATA = (
    ROOT
    / "dnd55e-spilluminati"
    / "Public"
    / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
)
FILES = (
    ("classes", "ClassDescriptions/ClassDescriptions.lsx"),
    ("races", "Races/Races.lsx"),
    ("backgrounds", "Backgrounds/Backgrounds.lsx"),
    ("feats", "Feats/FeatDescriptions.lsx"),
    ("progressions", "Progressions/ProgressionDescriptions.lsx"),
)


def node_context(node: ET.Element) -> str:
    values: dict[str, str] = {}
    for attr in node.findall("./attribute"):
        key = attr.get("id", "")
        value = attr.get("value", "")
        if key in {"Name", "ExactMatch", "UUID", "FeatId", "ProgressionId"} and value:
            values[key] = value
    return ";".join(f"{key}={value}" for key, value in values.items())


def write_tsv(path: pathlib.Path, rows: list[tuple[str, ...]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow((
            "uid",
            "category",
            "field",
            "context",
            "english",
            "current_ukrainian",
            "official_bg3_ukrainian",
        ))
        writer.writerows(rows)


def main() -> None:
    _, source = audit.localization(audit.SOURCE)
    _, target = audit.localization(audit.TARGET)
    exact = audit.official_exact()
    found: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))

    for category, relative in FILES:
        tree = ET.parse(DATA / relative)
        for node in tree.iter("node"):
            context = node_context(node)
            for attr in node.findall("./attribute"):
                uid = attr.get("handle", "")
                if not uid or uid not in source:
                    continue
                found[uid]["category"].add(category)
                found[uid]["field"].add(attr.get("id", ""))
                if context:
                    found[uid]["context"].add(context)

    rows: list[tuple[str, ...]] = []
    for uid, metadata in found.items():
        english = source[uid].text or ""
        rows.append((
            uid,
            ";".join(sorted(metadata["category"])),
            ";".join(sorted(metadata["field"])),
            " | ".join(sorted(metadata["context"])),
            english,
            target[uid].text or "",
            exact.get(english, ""),
        ))
    rows.sort(key=lambda row: (row[1], row[2], row[3], row[4].casefold()))
    write_tsv(ROOT / "core_editorial.tsv", rows)
    print(f"core_rows={len(rows)}")


if __name__ == "__main__":
    main()
