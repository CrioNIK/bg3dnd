from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

from upstream_translation_overrides import UID_OVERRIDES


def load(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("english", type=Path)
    parser.add_argument("existing_ukrainian", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source_nodes, source = load(args.english)
    existing_nodes, existing = load(args.existing_ukrainian)

    if len(source_nodes) != len(source):
        raise SystemExit("Duplicate contentuid values in English source")
    if len(existing_nodes) != len(existing):
        raise SystemExit("Duplicate contentuid values in existing Ukrainian source")

    unknown_overrides = sorted(set(UID_OVERRIDES) - set(source))
    if unknown_overrides:
        raise SystemExit(f"Overrides for unknown handles: {unknown_overrides}")

    missing_without_override = [
        uid for uid in source if uid not in existing and uid not in UID_OVERRIDES
    ]
    if missing_without_override:
        raise SystemExit(f"Missing translations: {missing_without_override}")

    lines = [
        '<?xml version="1.0"?>',
        '<contentList xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',
    ]
    for node in source_nodes:
        if set(node.attrib) != {"contentuid", "version"}:
            raise SystemExit(f"Unexpected attributes for {node.attrib.get('contentuid')}: {node.attrib}")
        uid = node.attrib["contentuid"]
        version = node.attrib["version"]
        text = UID_OVERRIDES.get(uid)
        if text is None:
            text = existing[uid].text or ""
        text = "\n".join(line.rstrip() for line in text.split("\n"))
        lines.append(
            f'  <content contentuid="{uid}" version="{version}">{escape(text)}</content>'
        )
    lines.append("</contentList>")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"Wrote {len(source_nodes)} entries; reused {len(source_nodes) - len(UID_OVERRIDES)}; "
        f"overrode {len(UID_OVERRIDES)}"
    )


if __name__ == "__main__":
    main()
