from __future__ import annotations

import bisect
import concurrent.futures
import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
TARGET = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "ukrainian_current.xml"
OUTPUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "languagetool_findings.tsv"
API = "http://127.0.0.1:8087/v2/check"

TAG_RE = re.compile(r"</?[^>]+>")


def visible(text: str) -> str:
    return " ".join(TAG_RE.sub(" ", text).split())


def check_batch(
    items: list[tuple[str, str, str]],
) -> list[tuple[str, str, str, dict[str, object]]]:
    starts: list[int] = []
    parts: list[str] = []
    cursor = 0
    for _, _, text in items:
        starts.append(cursor)
        parts.append(text)
        cursor += len(text) + 2
    text = "\n\n".join(parts)
    payload = urlencode({"language": "uk-UA", "text": text}).encode("utf-8")
    request = Request(API, data=payload, method="POST")
    with urlopen(request, timeout=120) as response:
        result = json.loads(response.read().decode("utf-8"))
    mapped: list[tuple[str, str, str, dict[str, object]]] = []
    for match in result.get("matches", []):
        offset = int(match["offset"])
        index = bisect.bisect_right(starts, offset) - 1
        if index < 0:
            continue
        uid, original, item_text = items[index]
        local = offset - starts[index]
        mapped.append((uid, original, item_text, {**match, "offset": local}))
    return mapped


def main() -> None:
    nodes = list(ET.parse(TARGET).getroot().findall("content"))
    items: list[tuple[str, str, str]] = []
    for node in nodes:
        original = node.text or ""
        items.append((node.attrib["contentuid"], original, visible(original)))
    batches = [items[index : index + 50] for index in range(0, len(items), 50)]

    rows: list[tuple[str, ...]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for mapped in pool.map(check_batch, batches):
            for uid, original, text, match in mapped:
                offset = int(match["offset"])
                length = int(match.get("length", 0))
                offending = text[offset : offset + length]
                replacements = ", ".join(
                    item.get("value", "") for item in match.get("replacements", [])[:8]
                )
                rule = match.get("rule", {})
                category = rule.get("category", {}).get("name", "")
                rows.append(
                    (
                        uid,
                        rule.get("id", ""),
                        category,
                        offending,
                        match.get("message", ""),
                        replacements,
                        original.replace("\n", "\\n"),
                    )
                )

    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(
            (
                "contentuid",
                "rule_id",
                "category",
                "offending",
                "message",
                "suggestions",
                "translation",
            )
        )
        writer.writerows(rows)

    print(f"entries={len(nodes)} findings={len(rows)} wrote={OUTPUT}")


if __name__ == "__main__":
    main()
