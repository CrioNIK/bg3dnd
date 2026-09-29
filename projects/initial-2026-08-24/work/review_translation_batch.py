from __future__ import annotations

import argparse
import csv
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def load_xml(path: Path):
    return [(n.attrib["contentuid"], n.text or "") for n in ET.parse(path).getroot().findall("content")]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", type=Path)
    ap.add_argument("--field", default="")
    ap.add_argument("--file", default="")
    ap.add_argument("--unreferenced", action="store_true")
    ap.add_argument("--unique-source", action="store_true")
    ap.add_argument("--skip-official-exact", action="store_true")
    ap.add_argument("--min-words", type=int, default=0)
    ap.add_argument("--max-words", type=int, default=100000)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--after-uid", default="")
    ap.add_argument("--limit", type=int, default=40)
    args = ap.parse_args()

    root = Path(__file__).resolve().parent
    mod = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
    en_path = args.repo / "Mods" / mod / "Localization" / "English" / "english.xml"
    uk_path = args.repo / "Mods" / mod / "Localization" / "Ukrainian" / "ukrainian.xml"
    en = load_xml(en_path)
    uk = dict(load_xml(uk_path))
    official_targets_by_source: dict[str, set[str]] = {}
    if args.skip_official_exact:
        official_en_path = root / "bg3-en.xml"
        official_uk_path = root / "bg3-uk.xml"
        official_en = dict(load_xml(official_en_path))
        official_uk = dict(load_xml(official_uk_path))
        for official_uid, official_source in official_en.items():
            official_target = official_uk.get(official_uid)
            if official_target is not None:
                official_targets_by_source.setdefault(official_source, set()).add(official_target)
    context_path = root / "repo_context.tsv"
    context = {}
    if context_path.exists():
        with context_path.open(encoding="utf-8-sig", newline="") as f:
            context = {r["uid"]: r for r in csv.DictReader(f, delimiter="\t")}

    rows = []
    seen = set()
    for uid, source in en:
        target = uk.get(uid, "")
        if args.skip_official_exact and target in official_targets_by_source.get(source, set()):
            continue
        meta = context.get(uid.lower())
        if args.unreferenced != (meta is None):
            if args.unreferenced or args.field or args.file:
                continue
        if args.field and (not meta or args.field.casefold() not in meta["fields"].casefold()):
            continue
        if args.file and (not meta or args.file.casefold() not in meta["files"].casefold()):
            continue
        words = len(re.findall(r"\b[\w’'-]+\b", re.sub(r"<[^>]+>", " ", source)))
        if not args.min_words <= words <= args.max_words:
            continue
        if args.unique_source:
            if source in seen:
                continue
            seen.add(source)
        rows.append((uid, source, target, meta or {}))

    offset = args.offset
    if args.after_uid:
        offset = next((i + 1 for i, row in enumerate(rows) if row[0].casefold() == args.after_uid.casefold()), offset)
    selected = rows[offset : offset + args.limit]
    print(f"TOTAL={len(rows)} OFFSET={offset} SHOWN={len(selected)}")
    for index, (uid, source, target, meta) in enumerate(selected, offset):
        fields = meta.get("fields", "unreferenced")
        files = meta.get("files", "")
        contexts = meta.get("contexts", "")
        print(f"\n### {index} {uid} [{fields}] {files} {contexts}")
        print("EN:", source.replace("\n", "\\n"))
        print("UK:", target.replace("\n", "\\n"))


if __name__ == "__main__":
    main()
