from __future__ import annotations

import collections
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "dnd55e-spilluminati" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "English" / "english.xml"
TARGET = ROOT / "ukrainian.xml"

TAG_RE = re.compile(r"</?[^>]+>")
BRACKET_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"\b(\d*d\d+)(?:s)?(?:\s*[+\-]\s*\d+)?\b", re.IGNORECASE)
ASCII_WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z'’-]{2,}\b")


def load(path: Path) -> list[ET.Element]:
    return list(ET.parse(path).getroot().findall("content"))


source = load(SOURCE)
target = load(TARGET)
errors: list[str] = []

if len(source) != len(target):
    errors.append(f"entry count differs: {len(source)} != {len(target)}")

residual_rows: list[tuple[str, str, str, str]] = []
residual_spans: collections.Counter[str] = collections.Counter()
title_rows: list[tuple[str, str, str]] = []
term_rows: list[tuple[str, str, str, str]] = []
unchanged_rows: list[tuple[str, str]] = []

term_patterns = {
    "spell": re.compile(r"заклин", re.IGNORECASE),
    "saving_throw": re.compile(r"рятувальн\w*\s+кид", re.IGNORECASE),
    "bonus_action": re.compile(r"бонусн\w*\s+ді", re.IGNORECASE),
    "spell_slot": re.compile(r"\b(?:слот|комірк)\w*\s+(?:заклят|заклин)", re.IGNORECASE),
    "cantrip": re.compile(r"кантр|кантрип", re.IGNORECASE),
    "armor_class": re.compile(r"клас\w*\s+(?:броні|обладунк)", re.IGNORECASE),
}

for index, (src_node, dst_node) in enumerate(zip(source, target)):
    uid = src_node.attrib.get("contentuid", "")
    if uid != dst_node.attrib.get("contentuid", ""):
        errors.append(f"uid mismatch at {index}: {uid} != {dst_node.attrib.get('contentuid')}")
    if src_node.attrib.get("version") != dst_node.attrib.get("version"):
        errors.append(f"version mismatch for {uid}")

    src = src_node.text or ""
    dst = dst_node.text or ""
    if collections.Counter(TAG_RE.findall(src)) != collections.Counter(TAG_RE.findall(dst)):
        errors.append(f"tag mismatch for {uid}")
    if BRACKET_RE.findall(src) != BRACKET_RE.findall(dst):
        errors.append(f"placeholder mismatch for {uid}: {BRACKET_RE.findall(src)} != {BRACKET_RE.findall(dst)}")
    if DICE_RE.findall(src) != DICE_RE.findall(dst):
        errors.append(f"dice mismatch for {uid}: {DICE_RE.findall(src)} != {DICE_RE.findall(dst)}")
    if "ZXQ" in dst:
        errors.append(f"temporary token remains for {uid}")

    visible = TAG_RE.sub(" ", dst)
    visible = BRACKET_RE.sub(" ", visible)
    visible = DICE_RE.sub(" ", visible)
    words = ASCII_WORD_RE.findall(visible)
    if words:
        residual_rows.append((uid, ", ".join(words), src.replace("\n", "\\n"), dst.replace("\n", "\\n")))
        residual_spans.update(
            re.findall(r"[A-Za-z][A-Za-z'’-]*(?: +[A-Za-z][A-Za-z'’-]*)*", visible)
        )
    if src == dst and ASCII_WORD_RE.search(src):
        unchanged_rows.append((uid, src.replace("\n", "\\n")))

    if (
        len(src) <= 100
        and "\n" not in src
        and not re.search(r"[.!?;:]$", src.strip())
        and len(ASCII_WORD_RE.findall(TAG_RE.sub(" ", src))) <= 12
    ):
        title_rows.append((uid, src, dst))

    for label, pattern in term_patterns.items():
        if pattern.search(dst):
            term_rows.append((label, uid, src.replace("\n", "\\n"), dst.replace("\n", "\\n")))


def write_tsv(name: str, header: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    path = ROOT / name
    with path.open("w", encoding="utf-8", newline="") as stream:
        stream.write("\t".join(header) + "\n")
        for row in rows:
            stream.write("\t".join(value.replace("\t", " ") for value in row) + "\n")


write_tsv("qa_residual_english.tsv", ("contentuid", "english_words", "source", "translation"), residual_rows)
write_tsv(
    "qa_residual_spans.tsv",
    ("count", "span"),
    [(str(count), span) for span, count in residual_spans.most_common()],
)
write_tsv("qa_titles.tsv", ("contentuid", "source", "translation"), title_rows)
write_tsv("qa_terms.tsv", ("term", "contentuid", "source", "translation"), term_rows)
write_tsv("qa_unchanged.tsv", ("contentuid", "source"), unchanged_rows)

print(
    f"entries={len(target)} errors={len(errors)} residual={len(residual_rows)} "
    f"titles={len(title_rows)} term_flags={len(term_rows)} unchanged={len(unchanged_rows)}"
)
for error in errors[:100]:
    print("ERROR", error)
if errors:
    raise SystemExit(1)
