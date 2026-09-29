from __future__ import annotations

import collections
import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "bg3dnd"
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
EN_PATH = REPO / "Mods" / MOD / "Localization" / "English" / "english.xml"
PL_PATH = REPO / "Mods" / MOD / "Localization" / "Polish" / "polish.xml"
BG_EN_PATH = ROOT / "official_bg3_english_20260828" / "english.loca.xml"
BG_PL_PATH = ROOT / "official_bg3_polish_20260828" / "polish.loca.xml"
REPORT_PATH = ROOT / "polish_audit_findings.tsv"

TAG_RE = re.compile(r"</?[^>]+>")
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"(?<![A-Za-z0-9])(\d*)[dk](\d+)(?:s)?(?![A-Za-z0-9])", re.IGNORECASE)
SPACE_RE = re.compile(r"\s+")
EN_DISTANCE_RE = re.compile(
    r"(?<![\w.,])(\d+(?:\.\d+)?)\s*(?:[-‑–—]\s*)?(?:feet|foot)\b",
    re.IGNORECASE,
)
PL_DISTANCE_RE = re.compile(
    r"(?<![\w.,])(\d+(?:[,.]\d+)?)\s*(?:[-‑–—]\s*)?(?:m\b|metr\w*)",
    re.IGNORECASE,
)

# This deliberately looks only for words that are very unlikely to be valid
# Polish prose. A generic ASCII detector is unusable for Polish.
ENGLISH_WORD_RE = re.compile(
    r"\b(?:the|this|that|these|those|you|your|yours|when|while|with|without|and|or|"
    r"can|cannot|may|must|target|creature|spell|attack|damage|level|turn|action|bonus|"
    r"saving|throw|roll|rest|range|within|feet|foot|gain|deal|take|use|using|until|"
    r"once|each|another|choice|equal|number|becomes|finish|long|short|proficiency|"
    r"modifier|weapon|feature|condition|points|temporary|raging|rage|strength|"
    r"cantrip|performance|persuasion|stealth|hide|wizard|sorcerer|warlock|ranger|"
    r"artificer|bardic|inspiration|spirits|beyond|radiant|grave|web|casting|ignite|"
    r"lash|nick|divine|spark|dexterity|constitution|intelligence|wisdom|charisma|speed|resistance|move|"
    r"half|same|hit|extra|type|legend|inspired|flying|strong|breath|wrath|sea|wild)\b",
    re.IGNORECASE,
)

SUSPICIOUS_PATTERNS = {
    "English D&D term": ENGLISH_WORD_RE,
    "literal spell slot": re.compile(r"\bmiejsc(?:e|a|u|em|ach|ami) na zaklęci", re.IGNORECASE),
    "Rune Knight mistranslation": re.compile(r"\b(?:Ruhn|Noże run)\w*\b", re.IGNORECASE),
    "giant calque": re.compile(r"\bgigant\w*\b", re.IGNORECASE),
    "bonus action calque": re.compile(r"\bAkcj\w* Bonusow\w*\b|\bakcj\w* bonusow\w*\b"),
    "hit points mistranslation": re.compile(r"\bPunkt(?:y|ów|u|em|ami|ach)? Życia\b"),
    "zero-width/nonbreaking anomaly": re.compile(r"[\u200b\u200c\u200d\ufeff]|\u00a0"),
    "imperial distance": re.compile(r"\b\d+(?:[,.]\d+)?\s+(?:stóp|stopy|stopę|stopa)\b", re.IGNORECASE),
    "attack roll calque": re.compile(r"\brzut(?:y|ów|u|em|ami|ach)? ataku\b", re.IGNORECASE),
    "channel divinity calque": re.compile(r"\bBosko(?:ść|ści) Kanału\b"),
    "wild shape calque": re.compile(r"\bDziki(?:ego|m)? kształt(?:u|em)?\b", re.IGNORECASE),
    "feature calque": re.compile(r"\bfunkcj(?:a|i|ę|ą)\b", re.IGNORECASE),
    "ward/totem calque": re.compile(r"\btotem(?:u|em|y|ów|ami|ach)?\b", re.IGNORECASE),
    "guiding bolt calque": re.compile(r"\bśrub(?:a|y|ę|ą|ie) prowadząc\w*\b", re.IGNORECASE),
    "magic initiate legacy": re.compile(r"\b(?:magiczny wtajemniczony|wtajemniczony w magię)\b", re.IGNORECASE),
    "usable classes legacy": re.compile(r"\b(?:użyteczne klasy|klasy użytkowe)\b", re.IGNORECASE),
    "cunning strike legacy": re.compile(r"\bprzebiegł\w+ uderzeni\w*\b", re.IGNORECASE),
    "spirit channeling legacy": re.compile(
        r"\bkontrolowane (?:przekazy|przesyłanie|przekazywanie(?: informacji| kanałów)?)\b",
        re.IGNORECASE,
    ),
    "dream legacy": re.compile(r"\b(?:oderwan\w+ od marzeń|oderwan\w+ od snów)\b", re.IGNORECASE),
    "giant ancestry legacy": re.compile(r"\b(?:olbrzymy przodkowie|przodkowie olbrzymów|pochodzenie olbrzyma)\b", re.IGNORECASE),
    "unbroken circle legacy": re.compile(r"\b(?:Nieprzerwany Krąg|Nieprzerwanego Kręgu|Krąg Nieprzerwanych Czarów)\b", re.IGNORECASE),
    "eldritch smite legacy": re.compile(r"\bniesamowite uderzenie\b", re.IGNORECASE),
    "protect target grammar": re.compile(r"\bchroń istota\b", re.IGNORECASE),
    "creature relative-pronoun grammar": re.compile(r"\bistotę, którą (?:jest|cię)\b", re.IGNORECASE),
    "cursed-creature grammar": re.compile(r"\bBędąc przeklętym, istota\b", re.IGNORECASE),
    "Words of Creation mistranslation": re.compile(r"\bSłow(?:a|ów) Istoty\b", re.IGNORECASE),
    "Eldritch legacy": re.compile(
        r"\b(?:Inwokacj\w+ Niesamowitości|Niesamowit\w+ (?:Uderzenie|Włócznia|Działo))\b",
        re.IGNORECASE,
    ),
    "condition mistranslation": re.compile(
        r"\b(?:stan(?:y|ów|om|ami|ach)? (?:Skłonny|Czarodziejka|Przestraszony|Niezdolność)|"
        r"zaczarowanemu istocie|Uderzenie Tarczą: Podatny|Pchnięcie telekinetyczne \(na brzuchu\))\b",
        re.IGNORECASE,
    ),
    "creature accusative grammar": re.compile(r"\btrafisz istota\b", re.IGNORECASE),
    "mismatched Polish quote": re.compile(r"„[^”\n]*\""),
    "companion grammar": re.compile(r"\bbestii towarzyszowi\b", re.IGNORECASE),
    "cone grammar": re.compile(r"\bStożku pochodzące\b", re.IGNORECASE),
    "blinded-condition grammar": re.compile(r"\bstan Oślepienie\b", re.IGNORECASE),
    "grave-keeper punctuation": re.compile(r"\bżywych osoby dbające\b", re.IGNORECASE),
    "prone-condition legacy": re.compile(r"\bstan Leżenie\b", re.IGNORECASE),
    "Channel Divinity mistranslation": re.compile(r"\bBoskość kanału\b", re.IGNORECASE),
    "Wild Shape title mistranslation": re.compile(r"\bDzika witalność kształtu\b", re.IGNORECASE),
    "Heroic Inspiration mistranslation": re.compile(
        r"\bBohatersk(?:a|ą|iej|ą)\s+[Ii]nspiracj(?:a|ę|i|ą)\b",
        re.IGNORECASE,
    ),
    "saving-throw mixed construction": re.compile(
        r"\bmusi wykonać udany rzut obronny [^.\n]+? albo (?:otrzymuje|zostaje|nie może)\b",
        re.IGNORECASE,
    ),
    "critical-hit object grammar": re.compile(
        r"\b(?:zadasz|zadajesz)(?: istocie)? trafienie krytyczne\b",
        re.IGNORECASE,
    ),
    "critical-hit noun grammar": re.compile(r"\bpo zadaniu trafienia krytycznego\b", re.IGNORECASE),
    "creature accusative grammar": re.compile(r"\bZmuś istota\b", re.IGNORECASE),
    "attack-roll double noun": re.compile(r"\brzutu testu ataku\b", re.IGNORECASE),
    "hit adjective grammar": re.compile(r"\btrafiony atak\b", re.IGNORECASE),
    "illusion-radius grammar": re.compile(r"\bW \[\d+\] iluzji testów ataku\b", re.IGNORECASE),
    "cunning-strike paralyze legacy": re.compile(r"\bSparaliżować\.\s+Kiedy\b", re.IGNORECASE),
    "shield-bash prone legacy": re.compile(r"\bUderzenie Tarczą \(Na Leżaku\)\b", re.IGNORECASE),
    "sneak-attack legacy": re.compile(r"\bAtak(?:u|iem)? z ukrycia\b", re.IGNORECASE),
    "second-person passive gender": re.compile(
        r"\b(?:jesteś|zostajesz|nie możesz być)\s+(?:poddany|Zakrwawiony|Przerażony|oślepiona)\b",
        re.IGNORECASE,
    ),
    "size-change gender": re.compile(r"\bstajesz się (?:Duży|Średnim)\b", re.IGNORECASE),
    "damage-type legacy": re.compile(
        r"\b(?:obrażenia (?:tłuczone|sieczne|tnące|promieniujące)|obrażenia od (?:blasku|siły)|"
        r"obrażenia (?:Kwasu|Zimna|Ognia|Błyskawicy|Pioruna))\b",
        re.IGNORECASE,
    ),
    "modifier word order": re.compile(r"\bZręczność\s+(?:<[^>]+>)?modyfikator\b", re.IGNORECASE),
    "proficiency-bonus missing preposition": re.compile(r"\bpremi(?:a|i|ę|ą) biegłości\b", re.IGNORECASE),
    "law title casing": re.compile(r"\bBastion Prawa\b"),
    "gendered second-person past": re.compile(r"\b\w+(?:łeś|łaś)\b", re.IGNORECASE),
    "gendered second-person adjective": re.compile(
        r"\b(?:jesteś|zostajesz|stajesz się|stać się|pozostajesz)\s+"
        r"(?:nieuzbrojony|narażony|obezwładniony|odporny|niewidzialnym|biegły|przyzwyczajony|przeniesiony|powalony)\b",
        re.IGNORECASE,
    ),
}

# Proper names and loanwords intentionally left unchanged in Polish.
UNCHANGED_WHITELIST = {
    "Aasimar",
    "Bernard",
    "Eladrin",
    "Gale",
    "Gnoll",
    "Goblin",
    "Hobgoblin",
    "Illrigger",
    "Infiltrator",
    "Kalashtar",
    "Kobold",
    "Minsc",
    "Sahuagin",
    "Shadar-kai",
    "Shillelagh",
    "Wyll",
}

# Deliberate corrections where a stable exact match in the shipped BG3 corpus
# is not the right string for this mod context.  Keep these explicit so an
# unrelated deviation from official terminology still fails the audit.
APPROVED_OFFICIAL_CORRECTIONS = {
    # These isolated mastery words collide with unrelated BG3 UI commands;
    # use the established Polish D&D 2024 mastery-property names instead.
    "hb60d9b3bg491bg7056g1bd9gc752b67bfd56": "Szerokie cięcie",
    "h64e7021cg8b69g3f60gde38gd59f3cdc5846": "Popchnięcie",
    "ha395ebeag3995g70fage1d7g718229b74f9b": "Obalenie",
    # The exact official match drops the Forgotten Realms faction name.
    "hdca03596gcde4g4b29g8a36g81f8496c69a4": "Najemnik Płonącej Pięści",
    # Preserve the official Warding Flare term while normalising title case.
    "hb220d543g0de9ga76cg8f82gc0f939ce0a89": "Ulepszony ochronny rozbłysk",
    # BG3's exact "Awaken" match is the status adjective, not the D&D spell.
    "hfefb5384gcdb9g70a3g4fd3g5796fed23526": "Przebudzenie",
    # The official exact match is an adjective; this mod handle is a feature
    # name and needs a noun phrase.
    "h2eddaae5gd399g869eg1cdag9e9a178e24d8": "Nasycenie",
    # The shipped Polish biography closes its Polish opening quote with an
    # ASCII quotation mark; fix only that unambiguous punctuation typo.
    "h1034780age61eg388fg49d2g23bd1ca7ca75": (
        "Wyll, nazywany „Klingą Pogranicza”, używa swojej magii do walki z potworami i diabłami nękającymi "
        "Wybrzeże Mieczy. W chwili rozpaczy przyjął zaoferowaną mu moc, stając się tym samym pionkiem w "
        "piekielnej grze, w której nie radzi sobie zbyt dobrze."
    ),
    # The shipped Polish string mistranslates Attack Rolls as Saving Throws.
    # Preserve the official terms, but correct the mechanic in these exact rows.
    "h03f4e692g56c6g5001g17adg72f182951516": (
        "Nałóż klątwę dotykiem. Istota pod jej wpływem ma <LSTag Tooltip=\"Disadvantage\">"
        "utrudnienie</LSTag> w <LSTag Tooltip=\"AttackRoll\">testach ataku</LSTag> przeciwko tobie."
    ),
    "hc0faf0e3g6b1bgefbbge13cg61d3cdca920b": (
        "Nałóż klątwę dotykiem. Istota pod jej wpływem ma <LSTag Tooltip=\"Disadvantage\">"
        "utrudnienie</LSTag> w <LSTag Tooltip=\"AttackRoll\">testach ataku</LSTag> przeciwko tobie."
    ),
    # The exact official rows contain clear Polish grammar/terminology errors;
    # retain the official concepts while correcting only those errors.
    "h33a83d2bg7e97g9bebg4b1ag640c88459c92": (
        "Zadajesz dodatkowe obrażenia od kwasu w liczbie równej twojej <LSTag "
        "Tooltip=\"ProficiencyBonus\">premii z biegłości</LSTag>. Przy trafieniu tworzysz wokół celu "
        "kałużę kwasu, która zmniejsza jego <LSTag Tooltip=\"ArmourClass\">Klasę Pancerza</LSTag> o [1]."
    ),
    "h409cb932g8ed1gc110g3616g0fa1bc73cc21": (
        "Nakaż istocie, by natychmiast <LSTag Type=\"Status\" Tooltip=\"PRONE\">padła</LSTag> na ziemię."
    ),
}


def normalise(text: str) -> str:
    return SPACE_RE.sub(" ", text).strip()


def load(path: Path) -> tuple[list[ET.Element], dict[str, ET.Element]]:
    nodes = list(ET.parse(path).getroot().findall("content"))
    return nodes, {node.attrib["contentuid"]: node for node in nodes}


def visible(text: str) -> str:
    return TAG_RE.sub(" ", PLACEHOLDER_RE.sub(" ", text))


def dice_signature(text: str) -> collections.Counter[tuple[str, str]]:
    return collections.Counter((count or "1", sides) for count, sides in DICE_RE.findall(text))


def stable_official_map(source: dict[str, ET.Element], target: dict[str, ET.Element]) -> dict[str, str]:
    candidates: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for uid, source_node in source.items():
        target_node = target.get(uid)
        source_text = source_node.text or ""
        target_text = target_node.text if target_node is not None else ""
        if source_text and target_text:
            candidates[normalise(source_text)][target_text] += 1
    result: dict[str, str] = {}
    for source_text, options in candidates.items():
        ranked = options.most_common()
        if len(ranked) == 1 or ranked[0][1] > ranked[1][1]:
            result[source_text] = ranked[0][0]
    return result


def short(text: str, limit: int = 280) -> str:
    value = normalise(text).replace("\t", " ")
    return value if len(value) <= limit else value[: limit - 1] + "…"


def main() -> None:
    source_nodes, source = load(EN_PATH)
    target_nodes, target = load(PL_PATH)
    _, bg_en = load(BG_EN_PATH)
    _, bg_pl = load(BG_PL_PATH)
    official = stable_official_map(bg_en, bg_pl)

    findings: list[tuple[str, str, str, str]] = []
    counts = collections.Counter()

    source_counts = collections.Counter(node.attrib["contentuid"] for node in source_nodes)
    target_counts = collections.Counter(node.attrib["contentuid"] for node in target_nodes)
    for uid, amount in target_counts.items():
        if amount > 1:
            findings.append(("STRUCTURE", uid, "duplicate UID", str(amount)))
    for uid in sorted(set(source) - set(target)):
        findings.append(("STRUCTURE", uid, "missing UID", ""))
    for uid in sorted(set(target) - set(source)):
        findings.append(("STRUCTURE", uid, "extra UID", ""))

    official_hits = 0
    official_mismatches = 0
    official_corrections = 0
    unchanged = 0
    for uid, source_node in source.items():
        target_node = target.get(uid)
        if target_node is None:
            continue
        source_text = source_node.text or ""
        target_text = target_node.text or ""
        source_visible = visible(source_text)
        target_visible = visible(target_text)

        if source_node.attrib.get("version") != target_node.attrib.get("version"):
            findings.append(("STRUCTURE", uid, "version mismatch", target_node.attrib.get("version", "")))
        if not target_text.strip():
            findings.append(("STRUCTURE", uid, "empty translation", ""))
        if collections.Counter(TAG_RE.findall(source_text)) != collections.Counter(TAG_RE.findall(target_text)):
            findings.append(("STRUCTURE", uid, "tag mismatch", short(target_text)))
        if PLACEHOLDER_RE.findall(source_text) != PLACEHOLDER_RE.findall(target_text):
            findings.append(("STRUCTURE", uid, "placeholder mismatch", short(target_text)))
        if dice_signature(source_text) != dice_signature(target_text):
            findings.append(
                ("STRUCTURE", uid, "dice mismatch", f"{dict(dice_signature(source_text))} != {dict(dice_signature(target_text))}")
            )

        source_distances = [float(value) for value in EN_DISTANCE_RE.findall(source_visible)]
        target_distances = [float(value.replace(",", ".")) for value in PL_DISTANCE_RE.findall(target_visible)]
        if source_distances and len(source_distances) == len(target_distances):
            expected = [round(value * 0.3, 4) for value in source_distances]
            actual = [round(value, 4) for value in target_distances]
            if expected != actual:
                findings.append(
                    (
                        "LANGUAGE",
                        uid,
                        "distance mismatch",
                        f"feet={source_distances}; expected_m={expected}; actual_m={actual}; {short(target_text)}",
                    )
                )

        official_text = official.get(normalise(source_text))
        approved_correction = APPROVED_OFFICIAL_CORRECTIONS.get(uid)
        official_canonical = official_text is not None and (
            target_text == official_text or target_text == approved_correction
        )
        if official_text is not None:
            official_hits += 1
            if target_text == approved_correction and target_text != official_text:
                official_corrections += 1
            elif target_text != official_text:
                official_mismatches += 1
                findings.append(("OFFICIAL", uid, "does not match official BG3 Polish", short(target_text)))

        if (
            not official_canonical
            and
            source_text == target_text
            and re.search(r"[A-Za-z]", source_visible)
            and normalise(source_visible) not in UNCHANGED_WHITELIST
        ):
            unchanged += 1
            findings.append(("LANGUAGE", uid, "unchanged English", short(target_text)))

        if not official_canonical:
            for label, pattern in SUSPICIOUS_PATTERNS.items():
                matches = sorted({match.group(0) for match in pattern.finditer(target_visible)})
                if matches:
                    findings.append(("LANGUAGE", uid, label + ": " + ", ".join(matches), short(target_text)))

    # Identical source strings should not drift between handles.  This is
    # especially important for duplicated action labels and concise rules text.
    exact_groups: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
    for uid, source_node in source.items():
        target_node = target.get(uid)
        if target_node is not None:
            exact_groups[source_node.text or ""].append((uid, target_node.text or ""))
    for source_text, rows in exact_groups.items():
        variants = sorted({text for _, text in rows})
        if len(rows) > 1 and len(variants) > 1:
            uid = rows[0][0]
            findings.append(
                (
                    "CONSISTENCY",
                    uid,
                    f"identical English has {len(variants)} Polish variants",
                    short(source_text),
                )
            )

    for category, _, _, _ in findings:
        counts[category] += 1

    with REPORT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(("category", "contentuid", "finding", "text"))
        writer.writerows(findings)

    print(f"source_entries={len(source_nodes)}")
    print(f"target_entries={len(target_nodes)}")
    print(f"source_duplicate_uids={sum(count > 1 for count in source_counts.values())}")
    print(f"target_duplicate_uids={sum(count > 1 for count in target_counts.values())}")
    print(f"official_exact_hits={official_hits}")
    print(f"approved_official_corrections={official_corrections}")
    print(f"official_mismatches={official_mismatches}")
    print(f"unchanged_nonwhitelisted={unchanged}")
    print(f"findings={len(findings)} categories={dict(counts)}")
    print(f"report={REPORT_PATH}")


if __name__ == "__main__":
    main()
