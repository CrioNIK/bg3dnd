from __future__ import annotations

import collections
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MOD_XML = ROOT / "dnd55e-spilluminati" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "English" / "english.xml"
BG_EN_XML = ROOT / "bg3-en.xml"
BG_UK_XML = ROOT / "bg3-uk.xml"
REPORT = ROOT / "glossary_candidates.tsv"


def load(path: Path) -> list[tuple[str, str]]:
    root = ET.parse(path).getroot()
    return [(node.attrib["contentuid"], node.text or "") for node in root.findall("content")]


mod = load(MOD_XML)
bg_en = load(BG_EN_XML)
bg_uk = dict(load(BG_UK_XML))
mod_ids = {uid for uid, _ in mod}

english_by_text: dict[str, list[str]] = collections.defaultdict(list)
for uid, text in bg_en:
    if uid in bg_uk:
        english_by_text[text].append(uid)

unmatched: list[str] = []
for uid, text in mod:
    if uid in bg_uk:
        continue
    if text in english_by_text:
        continue
    unmatched.append(text)

translations: dict[str, set[str]] = collections.defaultdict(set)
for uid, en in bg_en:
    uk = bg_uk.get(uid)
    if uk:
        translations[en].add(uk)

ngram_counts: collections.Counter[str] = collections.Counter()
word_re = re.compile(r"[A-Za-z]+(?:['’\-][A-Za-z]+)*")
for text in unmatched:
    for segment in re.split(r"[\n.!?;:<>\[\]()]", text):
        words = word_re.findall(segment)
        for size in range(1, min(8, len(words)) + 1):
            for start in range(0, len(words) - size + 1):
                ngram_counts[" ".join(words[start:start + size]).lower()] += 1

rows: list[tuple[int, int, str, str]] = []
for en, uk_set in translations.items():
    if len(uk_set) != 1:
        continue
    if not (3 <= len(en) <= 70):
        continue
    if "\n" in en or "<" in en or "[" in en:
        continue
    if len(en.split()) > 8:
        continue
    if not re.search(r"[A-Za-z]", en):
        continue
    if re.fullmatch(r"[A-Za-z]'?[A-Za-z]*", en) and en.lower() in {
        "a", "an", "the", "to", "of", "and", "or", "you", "your", "is", "are",
        "on", "in", "at", "as", "it", "this", "that", "with", "for", "from", "by",
    }:
        continue
    normalized = " ".join(word_re.findall(en)).lower()
    if normalized != en.lower():
        continue
    hits = ngram_counts[normalized]
    if hits:
        rows.append((hits, len(en), en, next(iter(uk_set))))

rows.sort(key=lambda row: (-row[0], -row[1], row[2].lower()))
with REPORT.open("w", encoding="utf-8", newline="") as stream:
    stream.write("hits\tlength\tenglish\tukrainian\n")
    for hits, length, en, uk in rows:
        stream.write(f"{hits}\t{length}\t{en.replace(chr(9), ' ')}\t{uk.replace(chr(9), ' ')}\n")

print(f"mod={len(mod)} unmatched={len(unmatched)} candidates={len(rows)} report={REPORT}")
