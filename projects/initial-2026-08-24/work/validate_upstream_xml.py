from __future__ import annotations

import argparse
import collections
import re
import xml.etree.ElementTree as ET
from pathlib import Path


TAG_RE = re.compile(r"</?[^>]+>")
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"\b\d*d\d+(?:s)?(?:\s*[+\-]\s*\d+)?\b", re.IGNORECASE)
LATIN_WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z'’-]{2,}\b")


def nodes(path: Path) -> list[ET.Element]:
    return list(ET.parse(path).getroot().findall("content"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("english", type=Path)
    parser.add_argument("ukrainian", type=Path)
    args = parser.parse_args()

    source = nodes(args.english)
    target = nodes(args.ukrainian)
    errors: list[str] = []
    warnings: list[str] = []

    if len(source) != len(target):
        errors.append(f"entry count: {len(source)} != {len(target)}")

    source_ids = [node.attrib.get("contentuid", "") for node in source]
    target_ids = [node.attrib.get("contentuid", "") for node in target]
    source_counts = collections.Counter(source_ids)
    target_counts = collections.Counter(target_ids)
    if source_counts != target_counts:
        errors.append("handle sets/counts differ")
    duplicate_source = [uid for uid, count in source_counts.items() if count != 1]
    duplicate_target = [uid for uid, count in target_counts.items() if count != 1]
    if duplicate_source:
        errors.append(f"duplicate English handles: {duplicate_source}")
    if duplicate_target:
        errors.append(f"duplicate Ukrainian handles: {duplicate_target}")

    unchanged_english: list[tuple[str, str]] = []
    residual_english: list[tuple[str, list[str]]] = []
    empty: list[str] = []
    for index, (src, dst) in enumerate(zip(source, target)):
        uid = src.attrib.get("contentuid", "")
        if uid != dst.attrib.get("contentuid", ""):
            errors.append(f"order/handle mismatch at {index}: {uid} != {dst.attrib.get('contentuid')}")
            continue
        if src.attrib != dst.attrib:
            errors.append(f"attribute mismatch for {uid}: {src.attrib} != {dst.attrib}")
        src_text = src.text or ""
        dst_text = dst.text or ""
        if not dst_text.strip():
            empty.append(uid)
        if collections.Counter(TAG_RE.findall(src_text)) != collections.Counter(TAG_RE.findall(dst_text)):
            errors.append(f"embedded tag mismatch for {uid}")
        if PLACEHOLDER_RE.findall(src_text) != PLACEHOLDER_RE.findall(dst_text):
            errors.append(f"placeholder mismatch for {uid}")
        src_dice = [match.lower().replace(" ", "").removesuffix("s") for match in DICE_RE.findall(src_text)]
        dst_dice = [match.lower().replace(" ", "").removesuffix("s") for match in DICE_RE.findall(dst_text)]
        if src_dice != dst_dice:
            errors.append(f"dice mismatch for {uid}: {src_dice} != {dst_dice}")
        if "\ufffd" in dst_text:
            errors.append(f"replacement character for {uid}")
        if src_text == dst_text and LATIN_WORD_RE.search(src_text):
            unchanged_english.append((uid, src_text))
        visible = TAG_RE.sub(" ", dst_text)
        visible = PLACEHOLDER_RE.sub(" ", visible)
        visible = DICE_RE.sub(" ", visible)
        latin_words = LATIN_WORD_RE.findall(visible)
        if latin_words:
            residual_english.append((uid, latin_words))

    if empty:
        errors.append(f"empty translations: {empty}")
    if unchanged_english:
        warnings.append(f"unchanged English entries: {len(unchanged_english)}")
        for uid, value in unchanged_english[:50]:
            warnings.append(f"  {uid}: {value[:180]!r}")
    if residual_english:
        for uid, words in residual_english[:50]:
            errors.append(f"visible English for {uid}: {words}")

    print(
        f"entries={len(target)} unique={len(target_counts)} empty={len(empty)} "
        f"unchanged_english={len(unchanged_english)} residual_english={len(residual_english)} "
        f"errors={len(errors)}"
    )
    for warning in warnings:
        print(f"WARNING {warning}")
    for error in errors[:200]:
        print(f"ERROR {error}")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
