from __future__ import annotations

import csv
import pathlib
import re
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
HANDLE_RE = re.compile(r'\b(h[0-9a-fg]{36})\b(?:;\d+)?', re.IGNORECASE)
ENTRY_RE = re.compile(r'^new entry "([^"]+)"')
DATA_RE = re.compile(r'^data "([^"]+)" "([^"]*)"')


def add(
    found: dict[str, dict[str, set[str]]],
    uid: str,
    path: pathlib.Path,
    field: str,
    context: str,
) -> None:
    item = found[uid.lower()]
    item["file"].add(path.relative_to(DATA).as_posix())
    if field:
        item["field"].add(field)
    if context:
        item["context"].add(context)


def scan_lsx(
    found: dict[str, dict[str, set[str]]], path: pathlib.Path, source: set[str]
) -> None:
    try:
        tree = ET.parse(path)
    except ET.ParseError:
        return
    for node in tree.iter("node"):
        context_bits: list[str] = []
        for attr in node.findall("./attribute"):
            if attr.get("id") in {
                "Name",
                "UUID",
                "MapKey",
                "FeatId",
                "ProgressionId",
                "SpellId",
            } and attr.get("value"):
                context_bits.append(f'{attr.get("id")}={attr.get("value")}')
        context = ";".join(context_bits)
        for attr in node.findall("./attribute"):
            uid = attr.get("handle", "").lower()
            if uid in source:
                add(found, uid, path, attr.get("id", ""), context)


def scan_txt(
    found: dict[str, dict[str, set[str]]], path: pathlib.Path, source: set[str]
) -> None:
    entry = ""
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        if match := ENTRY_RE.match(line):
            entry = match.group(1)
            continue
        match = DATA_RE.match(line)
        if not match:
            continue
        field, value = match.groups()
        for uid in HANDLE_RE.findall(value):
            uid = uid.lower()
            if uid in source:
                add(found, uid, path, field, entry)


def main() -> None:
    _, source_records = audit.localization(audit.SOURCE)
    _, target_records = audit.localization(audit.TARGET)
    exact = audit.official_exact()
    source = {uid.lower(): record for uid, record in source_records.items()}
    target = {uid.lower(): record for uid, record in target_records.items()}
    found: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))

    for path in DATA.rglob("*.lsx"):
        scan_lsx(found, path, set(source))
    for path in DATA.rglob("*.txt"):
        scan_txt(found, path, set(source))

    out = ROOT / "all_context.tsv"
    with out.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow((
            "uid",
            "files",
            "fields",
            "contexts",
            "english",
            "current_ukrainian",
            "official_bg3_ukrainian",
        ))
        for uid, metadata in sorted(
            found.items(),
            key=lambda item: (
                ";".join(sorted(item[1]["file"])),
                ";".join(sorted(item[1]["field"])),
                (source[item[0]].text or "").casefold(),
            ),
        ):
            english = source[uid].text or ""
            writer.writerow((
                uid,
                ";".join(sorted(metadata["file"])),
                ";".join(sorted(metadata["field"])),
                ";".join(sorted(metadata["context"])),
                english,
                target.get(uid).text if uid in target else "",
                exact.get(english, ""),
            ))

    print(f"referenced_uids={len(found)} source_uids={len(source)} unreferenced={len(source)-len(found)}")


if __name__ == "__main__":
    main()
