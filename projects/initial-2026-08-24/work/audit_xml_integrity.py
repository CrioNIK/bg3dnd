from __future__ import annotations

import collections
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


TAG_RE = re.compile(r"</?[^>]+>")
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"\b(?:\d*)d\d+", re.IGNORECASE)
ASCII_WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z'’-]{2,}\b")


def load(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def visible(text: str) -> str:
    return DICE_RE.sub(" ", PLACEHOLDER_RE.sub(" ", TAG_RE.sub(" ", text)))


def main() -> None:
    source_path = Path(sys.argv[1])
    target_path = Path(sys.argv[2])
    source_nodes, source = load(source_path)
    target_nodes, target = load(target_path)

    counts = collections.Counter(node.attrib["contentuid"] for node in target_nodes)
    duplicates = [uid for uid, count in counts.items() if count > 1]
    missing = set(source) - set(target)
    extra = set(target) - set(source)
    version: list[str] = []
    empty: list[str] = []
    tags: list[str] = []
    placeholders: list[str] = []
    dice: list[str] = []
    unchanged_english: list[str] = []
    visible_english: list[str] = []

    for uid, source_node in source.items():
        target_node = target.get(uid)
        if target_node is None:
            continue
        source_text = source_node.text or ""
        target_text = target_node.text or ""
        if source_node.attrib.get("version") != target_node.attrib.get("version"):
            version.append(uid)
        if not target_text.strip():
            empty.append(uid)
        if collections.Counter(TAG_RE.findall(source_text)) != collections.Counter(TAG_RE.findall(target_text)):
            tags.append(uid)
        if PLACEHOLDER_RE.findall(source_text) != PLACEHOLDER_RE.findall(target_text):
            placeholders.append(uid)
        if collections.Counter(x.lower() for x in DICE_RE.findall(source_text)) != collections.Counter(
            x.lower() for x in DICE_RE.findall(target_text)
        ):
            dice.append(uid)
        if source_text == target_text and ASCII_WORD_RE.search(visible(source_text)):
            unchanged_english.append(uid)
        if ASCII_WORD_RE.search(visible(target_text)):
            visible_english.append(uid)

    results = {
        "source_entries": len(source_nodes),
        "target_entries": len(target_nodes),
        "duplicates": len(duplicates),
        "missing": len(missing),
        "extra": len(extra),
        "version_mismatches": len(version),
        "empty": len(empty),
        "tag_mismatches": len(tags),
        "placeholder_mismatches": len(placeholders),
        "dice_mismatches": len(dice),
        "unchanged_english": len(unchanged_english),
        "visible_english": len(visible_english),
    }
    for key, value in results.items():
        print(f"{key}={value}")
    for label, values in (
        ("DUPLICATE", duplicates),
        ("MISSING", sorted(missing)),
        ("EXTRA", sorted(extra)),
        ("VERSION", version),
        ("EMPTY", empty),
        ("TAG", tags),
        ("PLACEHOLDER", placeholders),
        ("DICE", dice),
        ("UNCHANGED_ENGLISH", unchanged_english),
        ("VISIBLE_ENGLISH", visible_english),
    ):
        for uid in values[:30]:
            print(f"{label}\t{uid}\t{(target.get(uid) or source.get(uid)).text or ''}")


if __name__ == "__main__":
    main()
