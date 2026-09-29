from __future__ import annotations

import csv
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict


ROOT = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(sys.argv[1]).resolve()
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
DATA = REPO / "Public" / MOD
SOURCE_XML = REPO / "Mods" / MOD / "Localization" / "English" / "english.xml"
TARGET_XML = REPO / "Mods" / MOD / "Localization" / "Ukrainian" / "ukrainian.xml"
OUT = pathlib.Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else ROOT / "repo_context.tsv"
HANDLE_RE = re.compile(r"\b(h[0-9a-fg]{36})\b(?:;\d+)?", re.IGNORECASE)
ENTRY_RE = re.compile(r'^new entry "([^"]+)"')
DATA_RE = re.compile(r'^data "([^"]+)" "([^"]*)"')


def localization(path: pathlib.Path) -> dict[str, str]:
    return {
        n.attrib["contentuid"].lower(): n.text or ""
        for n in ET.parse(path).getroot().findall("content")
    }


def add(found, uid: str, path: pathlib.Path, field: str, context: str) -> None:
    item = found[uid.lower()]
    item["file"].add(path.relative_to(DATA).as_posix())
    if field:
        item["field"].add(field)
    if context:
        item["context"].add(context)


def scan_lsx(found, path: pathlib.Path, source: set[str]) -> None:
    try:
        tree = ET.parse(path)
    except ET.ParseError:
        return
    for node in tree.iter("node"):
        bits = []
        for attr in node.findall("./attribute"):
            if attr.get("id") in {"Name", "UUID", "MapKey", "FeatId", "ProgressionId", "SpellId"} and attr.get("value"):
                bits.append(f'{attr.get("id")}={attr.get("value")}')
        context = ";".join(bits)
        for attr in node.findall("./attribute"):
            uid = attr.get("handle", "").lower()
            if uid in source:
                add(found, uid, path, attr.get("id", ""), context)


def scan_txt(found, path: pathlib.Path, source: set[str]) -> None:
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
            if uid.lower() in source:
                add(found, uid, path, field, entry)


def main() -> None:
    source = localization(SOURCE_XML)
    target = localization(TARGET_XML)
    found = defaultdict(lambda: defaultdict(set))
    source_ids = set(source)
    for path in DATA.rglob("*.lsx"):
        scan_lsx(found, path, source_ids)
    for path in DATA.rglob("*.txt"):
        scan_txt(found, path, source_ids)

    with OUT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(("uid", "files", "fields", "contexts", "english", "current_ukrainian"))
        for uid, metadata in sorted(found.items(), key=lambda item: (
            ";".join(sorted(item[1]["file"])),
            ";".join(sorted(item[1]["field"])),
            source[item[0]].casefold(),
        )):
            writer.writerow((
                uid,
                ";".join(sorted(metadata["file"])),
                ";".join(sorted(metadata["field"])),
                ";".join(sorted(metadata["context"])),
                source[uid],
                target.get(uid, ""),
            ))
    print(f"referenced_uids={len(found)} source_uids={len(source)} unreferenced={len(source)-len(found)} out={OUT}")


if __name__ == "__main__":
    main()
