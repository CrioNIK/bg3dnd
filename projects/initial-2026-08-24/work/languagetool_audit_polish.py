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
TARGET = Path(sys.argv[1]).resolve()
OUTPUT = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else ROOT / "languagetool_polish_findings.tsv"
API = "http://127.0.0.1:8087/v2/check"

TAG_RE = re.compile(r"</?[^>]+>")
BREAK_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)


def visible(text: str) -> str:
    # LSTag markup wraps visible words. Replacing each opening/closing tag
    # with a space produced artificial strings such as "szał ," and hundreds
    # of false punctuation findings. Removing markup preserves the exact
    # punctuation users see in game.
    text = BREAK_RE.sub("\n", text)
    return " ".join(TAG_RE.sub("", text).split())


def check_batch(items: list[tuple[str, str, str]]) -> list[tuple[str, str, str, dict[str, object]]]:
    starts: list[int] = []
    parts: list[str] = []
    cursor = 0
    for _, _, text in items:
        starts.append(cursor)
        parts.append(text)
        cursor += len(text) + 2
    text = "\n\n".join(parts)
    payload = urlencode({"language": "pl-PL", "text": text}).encode("utf-8")
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
        mapped.append((uid, original, item_text, {**match, "offset": offset - starts[index]}))
    return mapped


def main() -> None:
    nodes = list(ET.parse(TARGET).getroot().findall("content"))
    items = [
        (node.attrib["contentuid"], node.text or "", visible(node.text or ""))
        for node in nodes
    ]
    batches = [items[index : index + 40] for index in range(0, len(items), 40)]

    rows: list[tuple[str, ...]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for mapped in pool.map(check_batch, batches):
            for uid, original, text, match in mapped:
                offset = int(match["offset"])
                length = int(match.get("length", 0))
                rule = match.get("rule", {})
                rows.append(
                    (
                        uid,
                        str(rule.get("id", "")),
                        str(rule.get("category", {}).get("name", "")),
                        text[offset : offset + length],
                        str(match.get("message", "")),
                        ", ".join(item.get("value", "") for item in match.get("replacements", [])[:8]),
                        original.replace("\n", "\\n"),
                    )
                )

    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(("contentuid", "rule_id", "category", "offending", "message", "suggestions", "translation"))
        writer.writerows(rows)
    print(f"entries={len(nodes)} findings={len(rows)} wrote={OUTPUT}")


if __name__ == "__main__":
    main()
