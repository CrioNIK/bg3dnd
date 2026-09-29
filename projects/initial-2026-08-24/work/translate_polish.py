from __future__ import annotations

import collections
import html
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "bg3dnd"
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
EN_PATH = REPO / "Mods" / MOD / "Localization" / "English" / "english.xml"
PL_PATH = REPO / "Mods" / MOD / "Localization" / "Polish" / "polish.xml"
BG_EN_PATH = ROOT / "official_bg3_english_20260828" / "english.loca.xml"
BG_PL_PATH = ROOT / "official_bg3_polish_20260828" / "polish.loca.xml"
CACHE_PATH = ROOT / "polish_translation_cache.json"

API_URL = "https://clients5.google.com/translate_a/t"
MAX_BATCH_CHARS = 2600


# Terms without an official BG3 equivalent. The Polish BG3 corpus remains the
# authority whenever it contains the source text.
COMMUNITY_EXACT = {
    "Artificer": "Wynalazca",
    "Gunslinger": "Rewolwerowiec",
    "Illrigger": "Illrigger",
    "Monster Hunter": "Łowca potworów",
    "Battle Smith": "Kowal bitewny",
    "Armorer": "Płatnerz",
    "Artillerist": "Artylerzysta",
    "Alchemist": "Alchemik",
    "Weapon Mastery": "Mistrzostwo broni",
    "Weapon Masteries": "Mistrzostwa broni",
    "Cleave": "Rozcięcie",
    "Graze": "Draśnięcie",
    "Nick": "Dublet",
    "Push": "Pchnięcie",
    "Sap": "Osłabienie",
    "Slow": "Spowolnienie",
    "Topple": "Przewrócenie",
    "Vex": "Finta",
}


# Exact core terminology taken from the shipped Polish BG3 localization.
OFFICIAL_TERMS = {
    "Action": "Akcja",
    "Bonus Action": "Akcja dodatkowa",
    "Reaction": "Reakcja",
    "Spell": "Czar",
    "Spells": "Czary",
    "Cantrip": "Sztuczka",
    "Cantrips": "Sztuczki",
    "Spell Slot": "Komórka czaru",
    "Spell Slots": "Komórki czarów",
    "Saving Throw": "Rzut obronny",
    "Saving Throws": "Rzuty obronne",
    "Attack Roll": "Test ataku",
    "Armour Class": "Klasa Pancerza",
    "Armor Class": "Klasa Pancerza",
    "Difficulty Class": "Stopień Trudności",
    "Proficiency Bonus": "Premia z biegłości",
    "Temporary Hit Points": "Tymczasowe punkty wytrzymałości",
    "Hit Points": "Punkty wytrzymałości",
    "Short Rest": "Krótki odpoczynek",
    "Long Rest": "Długi odpoczynek",
    "Advantage": "Ułatwienie",
    "Disadvantage": "Utrudnienie",
    "Opportunity Attack": "Atak okazyjny",
    "Concentration": "Koncentracja",
    "Radiant Damage": "Obrażenia od światłości",
    "Necrotic Damage": "Obrażenia nekrotyczne",
    "Force Damage": "Obrażenia od mocy",
    "Psychic Damage": "Obrażenia psychiczne",
    "Thunder Damage": "Obrażenia od dźwięku",
    "Lightning Damage": "Obrażenia od elektryczności",
    "Fire Damage": "Obrażenia od ognia",
    "Cold Damage": "Obrażenia od zimna",
    "Acid Damage": "Obrażenia od kwasu",
    "Poison Damage": "Obrażenia od trucizny",
    "Piercing Damage": "Obrażenia kłute",
    "Slashing Damage": "Obrażenia cięte",
    "Bludgeoning Damage": "Obrażenia obuchowe",
    "Strength": "Siła",
    "Dexterity": "Zręczność",
    "Constitution": "Kondycja",
    "Intelligence": "Inteligencja",
    "Wisdom": "Mądrość",
    "Charisma": "Charyzma",
    "Fighter": "Wojownik",
    "Barbarian": "Barbarzyńca",
    "Bard": "Bard",
    "Cleric": "Kleryk",
    "Druid": "Druid",
    "Monk": "Mnich",
    "Paladin": "Paladyn",
    "Ranger": "Łowca",
    "Rogue": "Łotrzyk",
    "Sorcerer": "Zaklinacz",
    "Warlock": "Czarownik",
    "Wizard": "Mag",
}


TOKEN_RE = re.compile(
    r"</?[^>]+>|\[[^\]\n]+\]|\b\d*d\d+(?:\s*[+\-]\s*\d+)?\b|\bDC\s*\d+\b|\b[A-Fa-f0-9]{8}(?:-[A-Fa-f0-9]{4}){3}-[A-Fa-f0-9]{12}\b",
    re.IGNORECASE,
)


def load_nodes(path: Path) -> tuple[ET.ElementTree, list[ET.Element]]:
    tree = ET.parse(path)
    return tree, list(tree.getroot().findall("content"))


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def protect(text: str, serial: int) -> tuple[str, dict[str, str]]:
    replacements: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        token = f"ZXQPH{serial:05d}{len(replacements):03d}ZXQ"
        replacements[token] = match.group(0)
        return token

    return TOKEN_RE.sub(replace, text), replacements


def restore(text: str, replacements: dict[str, str]) -> str:
    for token, value in replacements.items():
        text = text.replace(token, value)
    missing = [token for token in replacements if token in text]
    if missing:
        raise ValueError(f"Unrestored placeholders: {missing}")
    return text


def translate_request(session: requests.Session, text: str) -> str:
    params = {"client": "dict-chrome-ex", "sl": "en", "tl": "pl", "q": text}
    delay = 1.0
    for _ in range(9):
        response = session.get(API_URL, params=params, timeout=90)
        if response.status_code == 200:
            payload = response.json()
            if isinstance(payload, list) and payload:
                return str(payload[0])
            if isinstance(payload, str):
                return payload
            raise RuntimeError(f"Unexpected translation response: {payload!r}")
        if response.status_code not in {429, 500, 502, 503, 504}:
            response.raise_for_status()
        time.sleep(delay)
        delay = min(delay * 2, 30)
    raise RuntimeError(f"Translation request failed after retries: HTTP {response.status_code}")


def translate_batch(session: requests.Session, items: list[tuple[str, str]]) -> dict[str, str]:
    protected: list[tuple[str, str, dict[str, str]]] = []
    for serial, (key, source) in enumerate(items):
        safe, replacements = protect(source, serial)
        protected.append((key, safe, replacements))

    markers = [f"ZXQSEP{i:04d}ZXQ" for i in range(len(protected) - 1)]
    chunks: list[str] = []
    for index, (_, safe, _) in enumerate(protected):
        chunks.append(safe)
        if index < len(markers):
            chunks.append(markers[index])
    translated = translate_request(session, "\n".join(chunks))

    parts = [translated]
    for marker in markers:
        next_parts: list[str] = []
        for part in parts:
            if marker in part:
                left, right = part.split(marker, 1)
                next_parts.extend([left, right])
            else:
                next_parts.append(part)
        parts = next_parts
    if len(parts) != len(items):
        if len(items) == 1:
            raise RuntimeError(f"Translation marker failure: {items[0][0]}")
        result: dict[str, str] = {}
        midpoint = len(items) // 2
        result.update(translate_batch(session, items[:midpoint]))
        result.update(translate_batch(session, items[midpoint:]))
        return result

    result: dict[str, str] = {}
    for (key, _, replacements), part in zip(protected, parts):
        result[key] = html.unescape(restore(part.strip(), replacements))
    return result


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    mod_tree, mod_nodes = load_nodes(EN_PATH)
    _, bg_en_nodes = load_nodes(BG_EN_PATH)
    _, bg_pl_nodes = load_nodes(BG_PL_PATH)

    bg_en = {node.attrib["contentuid"]: node.text or "" for node in bg_en_nodes}
    bg_pl = {node.attrib["contentuid"]: node.text or "" for node in bg_pl_nodes}

    official_candidates: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for uid, source in bg_en.items():
        target = bg_pl.get(uid, "")
        if source and target:
            official_candidates[normalise(source)][target] += 1

    official_by_text: dict[str, str] = {}
    for source, candidates in official_candidates.items():
        ranked = candidates.most_common()
        if len(ranked) == 1 or ranked[0][1] > ranked[1][1]:
            official_by_text[source] = ranked[0][0]

    # Pin the independently verified core terms even when the game corpus has
    # several context-dependent translations for an English word.
    official_by_text.update({normalise(k): v for k, v in OFFICIAL_TERMS.items()})

    cache: dict[str, str] = {}
    if CACHE_PATH.exists():
        cache = json.loads(CACHE_PATH.read_text(encoding="utf-8"))

    unique_sources: dict[str, str] = {}
    for node in mod_nodes:
        source = node.text or ""
        unique_sources.setdefault(normalise(source), source)

    translated_by_source: dict[str, str] = {}
    pending: list[tuple[str, str]] = []
    stats = collections.Counter()
    for index, (key, source) in enumerate(unique_sources.items()):
        if source in COMMUNITY_EXACT:
            translated_by_source[key] = COMMUNITY_EXACT[source]
            stats["community_exact"] += 1
        elif key in official_by_text:
            translated_by_source[key] = official_by_text[key]
            stats["official_text"] += 1
        elif source in cache:
            translated_by_source[key] = cache[source]
            stats["cache"] += 1
        elif not re.search(r"[A-Za-z]", source):
            translated_by_source[key] = source
            stats["non_english"] += 1
        else:
            pending.append((f"S{index:05d}", source))

    source_by_id = {key: source for key, source in pending}
    norm_by_id = {key: normalise(source) for key, source in pending}

    batches: list[list[tuple[str, str]]] = []
    batch: list[tuple[str, str]] = []
    size = 0
    for item in pending:
        item_size = len(item[1]) + 24
        if batch and size + item_size > MAX_BATCH_CHARS:
            batches.append(batch)
            batch = []
            size = 0
        batch.append(item)
        size += item_size
    if batch:
        batches.append(batch)

    session = requests.Session()
    session.headers.update(
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"}
    )
    for batch_index, batch_items in enumerate(batches, start=1):
        new_values = translate_batch(session, batch_items)
        for key, translation in new_values.items():
            source = source_by_id[key]
            translated_by_source[norm_by_id[key]] = translation
            cache[source] = translation
        save_cache(cache)
        print(
            f"batch {batch_index}/{len(batches)} strings={len(batch_items)} "
            f"completed={len(translated_by_source)}/{len(unique_sources)}",
            flush=True,
        )
        time.sleep(0.08)

    for node in mod_nodes:
        source = node.text or ""
        node.text = translated_by_source[normalise(source)]

    ET.indent(mod_tree, space="  ")
    mod_tree.write(PL_PATH, encoding="utf-8", xml_declaration=True, short_empty_elements=False)
    print(
        f"wrote={PL_PATH} entries={len(mod_nodes)} unique={len(unique_sources)} "
        f"online={len(pending)} stats={dict(stats)}"
    )


if __name__ == "__main__":
    main()
