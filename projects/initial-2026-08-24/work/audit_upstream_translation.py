from __future__ import annotations

import argparse
import collections
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def load(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def duplicates(nodes: list[ET.Element]) -> dict[str, int]:
    counts = collections.Counter(node.attrib["contentuid"] for node in nodes)
    return {uid: count for uid, count in counts.items() if count > 1}


def preview(value: str) -> str:
    return value.replace("\n", "\\n")[:500]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("current_english", type=Path)
    parser.add_argument("ukrainian", type=Path)
    parser.add_argument("--previous-english", type=Path)
    parser.add_argument("--details-out", type=Path)
    args = parser.parse_args()

    current_nodes, current = load(args.current_english)
    uk_nodes, uk = load(args.ukrainian)
    print(f"current_entries={len(current_nodes)} unique={len(current)} duplicates={len(duplicates(current_nodes))}")
    print(f"uk_entries={len(uk_nodes)} unique={len(uk)} duplicates={len(duplicates(uk_nodes))}")

    missing = [uid for uid in current if uid not in uk]
    extra = [uid for uid in uk if uid not in current]
    version_mismatch = [
        uid
        for uid in current
        if uid in uk and current[uid].attrib.get("version") != uk[uid].attrib.get("version")
    ]
    order_mismatch = sum(
        1
        for left, right in zip(current_nodes, uk_nodes)
        if left.attrib.get("contentuid") != right.attrib.get("contentuid")
    ) + abs(len(current_nodes) - len(uk_nodes))
    print(f"missing={len(missing)} extra={len(extra)} version_mismatch={len(version_mismatch)} order_mismatch={order_mismatch}")

    if args.previous_english:
        _, previous = load(args.previous_english)
        new = [uid for uid in current if uid not in previous]
        removed = [uid for uid in previous if uid not in current]
        changed_text = [
            uid
            for uid in current
            if uid in previous and (current[uid].text or "") != (previous[uid].text or "")
        ]
        changed_version = [
            uid
            for uid in current
            if uid in previous
            and current[uid].attrib.get("version") != previous[uid].attrib.get("version")
        ]
        print(
            f"new_since_previous={len(new)} removed_since_previous={len(removed)} "
            f"changed_text={len(changed_text)} changed_version={len(changed_version)}"
        )
        if args.details_out:
            details = {
                "new": [
                    {
                        "contentuid": uid,
                        "version": current[uid].attrib.get("version", ""),
                        "english": current[uid].text or "",
                    }
                    for uid in new
                ],
                "changed": [
                    {
                        "contentuid": uid,
                        "version": current[uid].attrib.get("version", ""),
                        "previous_english": previous[uid].text or "",
                        "english": current[uid].text or "",
                        "ukrainian": (uk[uid].text or "") if uid in uk else "",
                    }
                    for uid in changed_text
                ],
            }
            args.details_out.write_text(
                json.dumps(details, ensure_ascii=False, indent=2), encoding="utf-8"
            )
        for label, uids in (("NEW", new), ("CHANGED", changed_text)):
            for uid in uids:
                print(f"{label}\t{uid}\t{preview(current[uid].text or '')}")

    for label, uids in (("MISSING", missing), ("EXTRA", extra), ("VERSION", version_mismatch)):
        for uid in uids:
            node = current.get(uid)
            if node is None:
                node = uk.get(uid)
            print(f"{label}\t{uid}\t{preview((node.text if node is not None else '') or '')}")


if __name__ == "__main__":
    main()
