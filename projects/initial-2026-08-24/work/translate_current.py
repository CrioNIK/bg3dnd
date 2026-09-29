from __future__ import annotations

import collections
import html
import json
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parent
MOD_XML = ROOT / "audit_installed_20260824_2257" / "base" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "English" / "english.xml"
OLD_MOD_XML = ROOT / "dnd55e-spilluminati" / "Mods" / "DnD2024_897914ef-5c96-053c-44af-0be823f895fe" / "Localization" / "English" / "english.xml"
OLD_UK_XML = ROOT / "ukrainian.xml"
BG_EN_XML = ROOT / "bg3-en.xml"
BG_UK_XML = ROOT / "bg3-uk.xml"
OUT_XML = ROOT / "ukrainian_current.xml"
CACHE_FILE = ROOT / "translation_cache_current.json"

API_URL = "https://clients5.google.com/translate_a/t"
MAX_BATCH_CHARS = 2800


# Community-preferred names used only where BG3 has no official equivalent.
CUSTOM_EXACT = {
    "Artificer": "Винахідник",
    "Gunslinger": "Стрілець",
    "Illrigger": "Ілріґер",
    "Monster Hunter": "Мисливець на чудовиськ",
    "Battle Smith": "Бойовий коваль",
    "Armorer": "Броняр",
    "Artillerist": "Артилерист",
    "Alchemist": "Алхімік",
    "Cleave": "Прорубування",
    "Graze": "Ковзний удар",
    "Nick": "Надріз",
    "Push": "Поштовх",
    "Sap": "Знесилення",
    "Slow": "Сповільнення",
    "Topple": "Підсічка",
    "Weapon Mastery": "Майстерність зброї",
    "Weapon Masteries": "Майстерності зброї",
    "Spell Slot": "Чарунка заклять",
    "Spell Slots": "Чарунки заклять",
    "Cantrip": "Замовляння",
    "Cantrips": "Замовляння",
    "Saving Throw": "Кидок протидії",
    "Saving Throws": "Кидки протидії",
    "Bonus Action": "Вторинна дія",
    "Attack Roll": "Кидок атаки",
    "Armour Class": "Рівень захисту",
    "Armor Class": "Рівень захисту",
    "Difficulty Class": "Межа складності",
    "Proficiency Bonus": "Бонус спеціалізації",
    "Temporary Hit Points": "Тимчасові очки здоров’я",
    "Hit Points": "Очки здоров’я",
    "Hit Point": "Очко здоров’я",
    "Short Rest": "Короткий відпочинок",
    "Long Rest": "Довгий відпочинок",
    "Advantage": "Перевага",
    "Disadvantage": "Завада",
    "Opportunity Attack": "Принагідна атака",
    "Wild Magic Surge": "Сплеск дикої магії",
    "Channel Divinity": "Боже наснаження",
}


TOKEN_RE = re.compile(
    r"</?[^>]+>|\[[^\]\n]+\]|\b\d*d\d+(?:\s*[+\-]\s*\d+)?\b|\bDC\s*\d+\b",
    re.IGNORECASE,
)


def load_nodes(path: Path) -> tuple[ET.ElementTree, list[ET.Element]]:
    tree = ET.parse(path)
    return tree, list(tree.getroot().findall("content"))


def preserve_case(source: str, replacement: str) -> str:
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def sub_ci(text: str, pattern: str, replacement: str) -> str:
    return re.sub(pattern, lambda m: preserve_case(m.group(0), replacement), text, flags=re.IGNORECASE)


def terminology(text: str) -> str:
    # Core BG3 vocabulary, including common inflected machine-translation forms.
    word_forms = {
        "заклинаннями": "закляттями",
        "заклинанням": "закляттям",
        "заклинанню": "закляттю",
        "заклинанні": "заклятті",
        "заклинань": "заклять",
        "заклинання": "закляття",
        "кантріпами": "замовляннями",
        "кантріпів": "замовлянь",
        "кантріпи": "замовляння",
        "кантріп": "замовляння",
        "кантрипами": "замовляннями",
        "кантрипів": "замовлянь",
        "кантрипи": "замовляння",
        "кантрип": "замовляння",
        "точками здоров'я": "очками здоров’я",
        "точками здоров’я": "очками здоров’я",
        "точок здоров'я": "очок здоров’я",
        "точок здоров’я": "очок здоров’я",
        "точки здоров'я": "очки здоров’я",
        "точки здоров’я": "очки здоров’я",
        "точку здоров'я": "очко здоров’я",
        "точку здоров’я": "очко здоров’я",
        "пунктами здоров'я": "очками здоров’я",
        "пунктами здоров’я": "очками здоров’я",
        "пунктів здоров'я": "очок здоров’я",
        "пунктів здоров’я": "очок здоров’я",
        "пункти здоров'я": "очки здоров’я",
        "пункти здоров’я": "очки здоров’я",
        "пункт здоров'я": "очко здоров’я",
        "пункт здоров’я": "очко здоров’я",
    }
    for source in sorted(word_forms, key=len, reverse=True):
        text = sub_ci(text, rf"(?<![А-Яа-яІіЇїЄєҐґ]){re.escape(source)}(?![А-Яа-яІіЇїЄєҐґ])", word_forms[source])

    phrase_forms = [
        (r"рятувальними кидками", "кидками протидії"),
        (r"рятувальним кидкам", "кидкам протидії"),
        (r"рятувальних кидках", "кидках протидії"),
        (r"рятувальних кидків", "кидків протидії"),
        (r"рятувальні кидки", "кидки протидії"),
        (r"рятувальним кидком", "кидком протидії"),
        (r"рятувальному кидку", "кидку протидії"),
        (r"рятувального кидка", "кидка протидії"),
        (r"рятувальний кидок", "кидок протидії"),
        (r"бонусними діями", "вторинними діями"),
        (r"бонусних дій", "вторинних дій"),
        (r"бонусні дії", "вторинні дії"),
        (r"бонусною дією", "вторинною дією"),
        (r"бонусній дії", "вторинній дії"),
        (r"бонусної дії", "вторинної дії"),
        (r"бонусну дію", "вторинну дію"),
        (r"бонусна дія", "вторинна дія"),
        (r"класу броні", "рівня захисту"),
        (r"класом броні", "рівнем захисту"),
        (r"клас броні", "рівень захисту"),
        (r"бонусом майстерності", "бонусом спеціалізації"),
        (r"бонусу майстерності", "бонусу спеціалізації"),
        (r"бонус майстерності", "бонус спеціалізації"),
        (r"бонусом володіння", "бонусом спеціалізації"),
        (r"бонусу володіння", "бонусу спеціалізації"),
        (r"бонус володіння", "бонус спеціалізації"),
        (r"слотами закляття", "чарунками заклять"),
        (r"слотів закляття", "чарунок заклять"),
        (r"слоти закляття", "чарунки заклять"),
        (r"слотом закляття", "чарункою заклять"),
        (r"слоту закляття", "чарунки заклять"),
        (r"слот закляття", "чарунка заклять"),
        (r"комірками закляття", "чарунками заклять"),
        (r"комірок закляття", "чарунок заклять"),
        (r"комірки закляття", "чарунки заклять"),
        (r"комірку закляття", "чарунку заклять"),
        (r"комірка закляття", "чарунка заклять"),
        (r"атака можливості", "принагідна атака"),
        (r"атаки можливості", "принагідної атаки"),
        (r"дикої магії сплеск", "сплеск дикої магії"),
    ]
    for pattern, replacement in phrase_forms:
        text = sub_ci(text, rf"(?<![А-Яа-яІіЇїЄєҐґ]){pattern}(?![А-Яа-яІіЇїЄєҐґ])", replacement)

    damage_adjectives = {
        "сяюча": "променева",
        "сяючої": "променевої",
        "сяючу": "променеву",
        "сяючою": "променевою",
        "промениста": "променева",
        "променистої": "променевої",
        "променисту": "променеву",
        "променистою": "променевою",
        "радіантна": "променева",
        "радіантної": "променевої",
        "радіантну": "променеву",
        "радіантною": "променевою",
        "дробильна": "забійна",
        "дробильної": "забійної",
        "дробильну": "забійну",
        "дробильною": "забійною",
        "ріжуча": "рубальна",
        "ріжучої": "рубальної",
        "ріжучу": "рубальну",
        "ріжучою": "рубальною",
        "пронизлива": "колольна",
        "пронизливої": "колольної",
        "пронизливу": "колольну",
        "пронизливою": "колольною",
    }
    for source in sorted(damage_adjectives, key=len, reverse=True):
        text = sub_ci(text, rf"(?<![А-Яа-яІіЇїЄєҐґ]){source}(?=\s+шкод)", damage_adjectives[source])
    return text


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
    params = {"client": "dict-chrome-ex", "sl": "en", "tl": "uk", "q": text}
    delay = 1.0
    for attempt in range(8):
        response = session.get(API_URL, params=params, timeout=60)
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
    for serial, (uid, source) in enumerate(items):
        safe, replacements = protect(source, serial)
        protected.append((uid, safe, replacements))

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
            raise RuntimeError("Translation marker failure for a single item")
        result: dict[str, str] = {}
        for item in items:
            result.update(translate_batch(session, [item]))
        return result

    result = {}
    for (uid, _, replacements), part in zip(protected, parts):
        value = restore(part.strip(), replacements)
        result[uid] = terminology(html.unescape(value))
    return result


def save_cache(cache: dict[str, dict[str, str]]) -> None:
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    mod_tree, mod_nodes = load_nodes(MOD_XML)
    _, old_mod_nodes = load_nodes(OLD_MOD_XML)
    _, old_uk_nodes = load_nodes(OLD_UK_XML)
    _, en_nodes = load_nodes(BG_EN_XML)
    _, uk_nodes = load_nodes(BG_UK_XML)
    old_en_by_uid = {node.attrib["contentuid"]: node.text or "" for node in old_mod_nodes}
    old_uk_by_uid = {node.attrib["contentuid"]: node.text or "" for node in old_uk_nodes}
    en_by_uid = {node.attrib["contentuid"]: node.text or "" for node in en_nodes}
    uk_by_uid = {node.attrib["contentuid"]: node.text or "" for node in uk_nodes}

    official_candidates: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for uid, en_text in en_by_uid.items():
        uk_text = uk_by_uid.get(uid)
        if uk_text:
            official_candidates[en_text][uk_text] += 1

    official_by_text: dict[str, str] = {}
    for en_text, candidates in official_candidates.items():
        if len(candidates) == 1 or len(en_text) >= 20:
            official_by_text[en_text] = candidates.most_common(1)[0][0]

    cache: dict[str, dict[str, str]] = {}
    if CACHE_FILE.exists():
        cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))

    translations: dict[str, str] = {}
    pending: list[tuple[str, str]] = []
    stats = collections.Counter()

    special_uid = {
        "h01dfd531g605ag4c72gb4edg3846ab351eae": "Мисливський довгий лук",
        "h16a91f2cg659dg4a91gbb02g7dd759e681be": uk_by_uid["h16a91f2cg659dg4a91gbb02g7dd759e681be"].replace("короткий лук", "довгий лук"),
    }

    for node in mod_nodes:
        uid = node.attrib["contentuid"]
        source = node.text or ""
        cached = cache.get(uid, {})
        if uid in old_uk_by_uid and source == old_en_by_uid.get(uid):
            translations[uid] = old_uk_by_uid[uid]
            stats["reused_unchanged"] += 1
        elif uid in special_uid:
            translations[uid] = special_uid[uid]
            stats["adapted_official"] += 1
        elif uid in uk_by_uid and source == en_by_uid.get(uid):
            translations[uid] = uk_by_uid[uid]
            stats["official_uid"] += 1
        elif source in CUSTOM_EXACT:
            translations[uid] = CUSTOM_EXACT[source]
            stats["community_exact"] += 1
        elif source in official_by_text:
            translations[uid] = official_by_text[source]
            stats["official_text"] += 1
        elif cached.get("source") == source and cached.get("translation"):
            translations[uid] = cached["translation"]
            stats["cache"] += 1
        elif not re.search(r"[A-Za-z]", source):
            translations[uid] = source
            stats["non_english"] += 1
        else:
            pending.append((uid, source))

    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"})

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

    for index, batch_items in enumerate(batches, start=1):
        new_values = translate_batch(session, batch_items)
        translations.update(new_values)
        for uid, translation in new_values.items():
            source = next(source for item_uid, source in batch_items if item_uid == uid)
            cache[uid] = {"source": source, "translation": translation}
        save_cache(cache)
        print(f"batch {index}/{len(batches)} entries={len(batch_items)} translated={len(translations)}/{len(mod_nodes)}", flush=True)
        time.sleep(0.08)

    for node in mod_nodes:
        node.text = terminology(translations[node.attrib["contentuid"]])

    ET.indent(mod_tree, space="  ")
    mod_tree.write(OUT_XML, encoding="utf-8", xml_declaration=True, short_empty_elements=False)
    print(f"wrote={OUT_XML} entries={len(mod_nodes)} stats={dict(stats)} online={len(pending)}")


if __name__ == "__main__":
    main()
