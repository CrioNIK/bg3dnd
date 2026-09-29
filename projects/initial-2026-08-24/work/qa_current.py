from __future__ import annotations

import collections
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "audit_installed_20260824_2257" / "base" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "English" / "english.xml"
TARGET = ROOT / "ukrainian_current.xml"

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
language_rows: list[tuple[str, str, str, str]] = []
unchanged_rows: list[tuple[str, str]] = []

term_patterns = {
    "spell": re.compile(r"заклин", re.IGNORECASE),
    "saving_throw": re.compile(r"рятувальн\w*\s+кид", re.IGNORECASE),
    "bonus_action": re.compile(r"бонусн\w*\s+ді", re.IGNORECASE),
    "spell_slot": re.compile(r"\b(?:слот|комірк)\w*\s+(?:заклят|заклин)", re.IGNORECASE),
    "cantrip": re.compile(r"кантр|кантрип", re.IGNORECASE),
    "armor_class": re.compile(r"клас\w*\s+(?:броні|обладунк)", re.IGNORECASE),
}

# Heuristics for common machine-translation artefacts. These are review flags,
# not automatic failures: some words (for example, "сутність") are valid in
# lore prose but suspicious in rules text where the source says "creature".
language_patterns = {
    "ability_calque": re.compile(
        r"(?:модифікатор|перевірк\w*)\s+(?:здібност|здатност)", re.IGNORECASE
    ),
    "entity_calque": re.compile(r"(?:уражен|постраждал)\w*\s+сутніст", re.IGNORECASE),
    "darkvision_calque": re.compile(
        r"темн\w*\s+зір|отримуєте\s+темряву\s+на\s+відстан", re.IGNORECASE
    ),
    "pact_calque": re.compile(r"\bпактн\w*", re.IGNORECASE),
    "ui_word_order": re.compile(
        r"атака\s+(?:кид|кида)|перевірк\w*\s+(?:здібност|здатност)", re.IGNORECASE
    ),
    "wrong_condition": re.compile(
        r"стан(?:і|у|ом)?\s+(?:схильност|обмежен)|\bскритніст\b", re.IGNORECASE
    ),
    "difficult_terrain": re.compile(r"важкопрохідн\w*\s+місцевіст", re.IGNORECASE),
    "imperative_title": re.compile(r"^\s*(?:викликайте|отримайте|зробіть)\b", re.IGNORECASE),
    "damage_take_calque": re.compile(r"(?:візьме|приймає)\s+\[[^\]]+\]", re.IGNORECASE),
    "die_agreement": re.compile(r"\b(?:один|цей|його|кістки?)\s+кістка\b", re.IGNORECASE),
    "die_verb_agreement": re.compile(
        r"\b(?:кинути|киньте|кидайте)\s+(?:свій|свою|один|одну)?\s*кістка\b|\bодин\s+із\s+кісток\b",
        re.IGNORECASE,
    ),
    "hit_points_calque": re.compile(
        r"\b(?:очк(?:и|ів)\s+життя|життєв(?:і|их)\s+(?:бал(?:и|ів)|очк(?:и|ів))|тимчасов\w*\s+окуляр\w*|окуляр(?:и|ів)\s+життя|хіт-очк\w*)\b",
        re.IGNORECASE,
    ),
    "saving_throw_calque": re.compile(
        r"\b(?:кидок\s+захисту|врятувати\s+кидок|МС\s+збереження)\b",
        re.IGNORECASE,
    ),
    "damage_type_calque": re.compile(
        r"\b(?:кололь\w*|дубин\w*\s+шкод\w*|кидков\w*\s+шкод\w*)\b",
        re.IGNORECASE,
    ),
    "condition_calque": re.compile(
        r"\b(?:стан\w*\s+лежач\w*|стриман\w*\s+стан\w*|умов\w*\s+зачар\w*)\b",
        re.IGNORECASE,
    ),
    "literal_as_action": re.compile(r"\bу\s+якості\s+(?:дії|реагування)\b", re.IGNORECASE),
    "cantrip_calque": re.compile(r"\bтрип\b", re.IGNORECASE),
    "known_typos": re.compile(r"\b(?:кільості|до\s+свої\s+швидкості)\b", re.IGNORECASE),
    "reaction_calque": re.compile(
        r"\b(?:прийняти|взяти|робити)\s+реагування\b", re.IGNORECASE
    ),
    "cantrip_machine": re.compile(
        r"\b(?:чаркнижник\w*|іллриггер\w*)\b|"
        r"(?:виберіть|вивчили|вивчаєте)\s+(?:три\s+)?(?:підказк\w*|інтриг\w*)|"
        r"знаєте,\s+що\s+таке\s+світло",
        re.IGNORECASE,
    ),
    "raw_spell_terms": re.compile(
        r"\b(?:Туманн(?:ий|ого|ому)\s+крок|Шилелаг\w*|Дик(?:а|ої|ій|у)\s+форм(?:а|и|і|у))\b",
        re.IGNORECASE,
    ),
    "condition_capitalization": re.compile(
        r"\bстан\s+(?:Невидимість|Переляк|Повалення|Причарування|Непрацездатність|Стримування)\b"
    ),
    "dice_grammar_extended": re.compile(
        r"\b(?:кількість\s+d\d+|вашого\s+кістки|кожен\s+витрачений\s+кістка|Кістки\s+ризику\s+починається)\b",
        re.IGNORECASE,
    ),
    "action_name_calque": re.compile(
        r"\b(?:від’єднання|дію\s+Відхід)\b", re.IGNORECASE
    ),
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
        errors.append(
            f"tag mismatch for {uid}: source={TAG_RE.findall(src)!r} target={TAG_RE.findall(dst)!r}"
        )
    if BRACKET_RE.findall(src) != BRACKET_RE.findall(dst):
        errors.append(f"placeholder mismatch for {uid}: {BRACKET_RE.findall(src)} != {BRACKET_RE.findall(dst)}")
    source_dice = [value.lower() for value in DICE_RE.findall(src)]
    target_dice = [value.lower() for value in DICE_RE.findall(dst)]
    if source_dice != target_dice:
        errors.append(f"dice mismatch for {uid}: {source_dice} != {target_dice}")
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
    for label, pattern in language_patterns.items():
        if pattern.search(dst):
            language_rows.append((label, uid, src.replace("\n", "\\n"), dst.replace("\n", "\\n")))


def write_tsv(name: str, header: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    path = ROOT / name
    with path.open("w", encoding="utf-8", newline="") as stream:
        stream.write("\t".join(header) + "\n")
        for row in rows:
            stream.write("\t".join(value.replace("\t", " ") for value in row) + "\n")


write_tsv("qa_current_residual_english.tsv", ("contentuid", "english_words", "source", "translation"), residual_rows)
write_tsv(
    "qa_current_residual_spans.tsv",
    ("count", "span"),
    [(str(count), span) for span, count in residual_spans.most_common()],
)
write_tsv("qa_current_titles.tsv", ("contentuid", "source", "translation"), title_rows)
write_tsv("qa_current_terms.tsv", ("term", "contentuid", "source", "translation"), term_rows)
write_tsv(
    "qa_current_language.tsv",
    ("flag", "contentuid", "source", "translation"),
    language_rows,
)
write_tsv("qa_current_unchanged.tsv", ("contentuid", "source"), unchanged_rows)

print(
    f"entries={len(target)} errors={len(errors)} residual={len(residual_rows)} "
    f"titles={len(title_rows)} term_flags={len(term_rows)} "
    f"language_flags={len(language_rows)} unchanged={len(unchanged_rows)}"
)
for error in errors[:100]:
    print("ERROR", error)
if errors:
    raise SystemExit(1)
