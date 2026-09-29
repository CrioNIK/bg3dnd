from __future__ import annotations

import collections
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "bg3dnd"
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
EN_PATH = REPO / "Mods" / MOD / "Localization" / "English" / "english.xml"
PL_PATH = REPO / "Mods" / MOD / "Localization" / "Polish" / "polish.xml"
BG_EN_PATH = ROOT / "official_bg3_english_20260828" / "english.loca.xml"
BG_PL_PATH = ROOT / "official_bg3_polish_20260828" / "polish.loca.xml"
COMMUNITY_ROOTS = [
    # More complete community data, including the 2024 PHB and Forge of the
    # Artificer. It takes priority when both community sources have a match.
    ROOT / "community_polish_dnd_premium" / "lang",
    ROOT / "community_polish_dnd5_foundry" / "lang",
]

TAG_RE = re.compile(r"</?[^>]+>")
TAG_BLOCK_RE = re.compile(r"(<LSTag\b[^>]*>)(.*?)(</LSTag>)", re.DOTALL)
BRACKET_RE = re.compile(r"\[[^\]\n]+\]")
DICE_RE = re.compile(r"(?<![A-Za-z0-9])(\d*)d(\d+)(?![A-Za-z0-9])", re.IGNORECASE)
EN_FEET_RE = re.compile(
    r"(?<![\w.,])(\d+(?:\.\d+)?)\s*(?:[-‑–—]\s*)?(?:feet|foot)\b",
    re.IGNORECASE,
)
PL_FEET_RE = re.compile(r"(?<![\w.,])\d+(?:[,.]\d+)?\s+(?:stóp|stopy|stopę|stopa)\b", re.IGNORECASE)
PL_METRE_RE = re.compile(
    r"(?<![\w.,])(\d+(?:[,.]\d+)?)\s*(?:[-‑–—]\s*)?(?:m\b|metr\w*)",
    re.IGNORECASE,
)
LEVEL_FEATURE_RE = re.compile(r"Level (\d+): (.+)")

# A short source string can match unrelated UI text in the official corpus.
# Keep known homonyms out of the derived level-feature title pass.
OFFICIAL_LEVEL_FEATURE_BLOCKLIST = {
    "Submit",
}


EXACT_OVERRIDES = {
    # The Polish D&D 2024 Forge of the Artificer community localization uses
    # Wynalazca consistently for the class; BG3 has no official class name.
    "Artificer": "Wynalazca",
    "Spell Resistance": "Odporność na czary",
    "Level 10: Spell Resistance": "Poziom 10: Odporność na czary",
    "Seeking Spell": "Naprowadzany czar",
    "Metamagic: Seeking Spell": "Metamagia: Naprowadzany czar",
    "Level 1: Bardic Inspiration": "Poziom 1: Bardowska inspiracja",
    "War Caster": "Mag bitewny",
    "Feat: War Caster": "Atut: Mag bitewny",
    "War Caster: Booming Blade": "Mag bitewny: Grzmiące ostrze",
    "War Caster: Green-Flame Blade": "Mag bitewny: Ostrze zielonego płomienia",
    "War Caster: True Strike": "Mag bitewny: Prawdziwe uderzenie",
    "War Caster: Vengeful Blade": "Mag bitewny: Mściwe ostrze",
    "War Caster: Shocking Grasp": "Mag bitewny: Porażający uścisk",
    "Gunslinger": "Rewolwerowiec",
    "Illrigger": "Illrigger",
    "Monster Hunter": "Łowca potworów",
    "Battle Smith": "Kowal bitewny",
    "Level 3: Battle Smith Spells": "Poziom 3: Czary kowala bitewnego",
    "Painkiller": "Uśmierzacz",
    "Architect of Ruin": "Architekt ruiny",
    "Feat: Grave Keeper": "Atut: Strażnik grobu",
    "Grave Keeper": "Strażnik grobu",
    "Level 3: Channel Oath": "Poziom 3: Moc przysięgi",
    "Channel Oath": "Moc przysięgi",
    "Dao’s Crush": "Miażdżący uścisk dao",
    "Dao's Crush": "Miażdżący uścisk dao",
    "Djinni’s Escape": "Ucieczka dżinna",
    "Djinni's Escape": "Ucieczka dżinna",
    "Efreeti’s Fury": "Furia efreetiego",
    "Efreeti's Fury": "Furia efreetiego",
    "Marid’s Surge": "Fala marida",
    "Marid's Surge": "Fala marida",
    "Level 3: Form of Dread": "Poziom 3: Postać grozy",
    "Form of Dread": "Postać grozy",
    "Necrotic Resilience": "Nekrotyczna odporność",
    "Unholy Resuscitation": "Bezbożne wskrzeszenie",
    "Hollow Warden": "Strażnik pustki",
    "Level 3: Hollow Warden Spells": "Poziom 3: Czary Strażnika pustki",
    "Armorer": "Płatnerz",
    "Artillerist": "Artylerzysta",
    "Alchemist": "Alchemik",
    # D&D 2024 names from the active Polish Foundry community localization.
    "Cleave": "Szerokie cięcie",
    "Graze": "Draśnięcie",
    "Nick": "Nacięcie",
    "Push": "Popchnięcie",
    "Sap": "Osłabienie",
    "Slow": "Spowolnienie",
    "Topple": "Obalenie",
    "Vex": "Nękanie",
    "Weapon Mastery": "Mistrzostwo broni",
    "Weapon Masteries": "Mistrzostwa broni",
    # Clear typo in the community data.
    "Steady Aim": "Stabilne celowanie",
    "Forgotten Realms: Heroes of Faerûn: Origin Feats": "Zapomniane Krainy: Bohaterowie Faerûnu — atuty pochodzenia",
    "Dodge Roll": "Przewrót unikowy",
    "Jackpot": "Główna wygrana",
    "Giant’s Might": "Potęga olbrzyma",
    "Runic Shield": "Runiczna tarcza",
    "Great Stature": "Wielka postura",
    "Rune": "Runa",
    "Bedevil": "Dręczenie",
    # Spell/action title editorial pass. Official BG3 exact matches still take
    # priority over these; the remaining names follow the active Polish D&D
    # community corpus and the shipped BG3 naming style.
    "Aganazzar's Scorcher": "Spopielacz Aganazzara",
    "Arcane Alchemy": "Tajemna alchemia",
    "Arcane Vigor": "Magiczna krzepa",
    "Arcane Vigor: D6": "Magiczna krzepa: k6",
    "Arcane Vigor: D8": "Magiczna krzepa: k8",
    "Arcane Vigor: D10": "Magiczna krzepa: k10",
    "Arcane Vigor: D12": "Magiczna krzepa: k12",
    "Astral Flood": "Astralna powódź",
    "Ballistic Smite": "Balistyczne ugodzenie",
    "Ballistic Smite: Acid": "Balistyczne ugodzenie: Kwas",
    "Ballistic Smite: Cold": "Balistyczne ugodzenie: Zimno",
    "Ballistic Smite: Fire": "Balistyczne ugodzenie: Ogień",
    "Ballistic Smite: Lightning": "Balistyczne ugodzenie: Elektryczność",
    "Ballistic Smite: Poison": "Balistyczne ugodzenie: Trucizna",
    "Ballistic Smite: Thunder": "Balistyczne ugodzenie: Dźwięk",
    "Cloak of Shadow": "Płaszcz cienia",
    "Cloud’s Jaunt": "Wędrówka chmur",
    "Cloud's Jaunt": "Wędrówka chmur",
    "Conflagrant Channel": "Płomienny kanał",
    "Dazing Blast": "Oszałamiający wybuch",
    "Djinni’s Escape": "Ucieczka dżinna",
    "Djinni's Escape": "Ucieczka dżinna",
    "Dummy Spell": "Czar testowy",
    "Duplicitous Casting": "Czarowanie przez sobowtóra",
    "Elemental Exhalation": "Zionięcie żywiołu",
    "Fey Step": "Krok fey",
    "Fire Dance": "Taniec ognia",
    "Fire Rune": "Runa ognia",
    "Frightful Start": "Przerażający początek",
    "Green-Flame Blade": "Ostrze zielonego płomienia",
    "Hell’s Lash": "Piekielny bicz",
    "Hell's Lash": "Piekielny bicz",
    "Holy Weapon": "Święta broń",
    "Hungering Blade": "Głodne ostrze",
    "Move Dawn": "Przesuń świt",
    "Murder of Crows ": "Stado kruków",
    "Murder of Crows": "Stado kruków",
    "Murmurs of Doom": "Pomruki zagłady",
    "Prestidigitation: Clean": "Kuglarstwo: oczyść",
    "Prestidigitation: Ignite": "Kuglarstwo: zapal",
    "Prestidigitation: Snuff": "Kuglarstwo: zgaś",
    "Rangers Companion": "Towarzysz łowcy",
    "Recharge Arcane Ward": "Naładuj magiczną powłokę",
    "Searing Orb": "Płonąca kula",
    "Spectral Slash": "Widmowe cięcie",
    "Summon Beast: Giant Eagle": "Przyzwij bestię: olbrzymi orzeł",
    "Summon Beast: Giant Eagle (Illusion)": "Przyzwij bestię: olbrzymi orzeł (iluzja)",
    "Summon Fey: Red Cap": "Przyzwij fey: krasnal",
    "Summon Fey: Red Cap (Illusion)": "Przyzwij fey: krasnal (iluzja)",
    "Sword Burst": "Wybuch miecza",
    "Tasha's Mind Whip": "Bicz umysłu Tashy",
    "Thorn Armor": "Cierniowa zbroja",
    "Tide of Darkness": "Przypływ ciemności",
    "Trollblood Infusion": "Nasycenie krwią trolla",
    "True Strike (Melee)": "Prawdziwe uderzenie (wręcz)",
    "True Strike (Ranged)": "Prawdziwe uderzenie (dystansowe)",
    "Umbral Tendril": "Cienista macka",
    "Vengeful Blade": "Mściwe ostrze",
    "Void Strike": "Uderzenie pustki",
    "High Roller": "Hazardzista",
    "Hill Strike": "Uderzenie wzgórza",
    "Level 3: Circle of the Land Spells": "Poziom 3: czary Kręgu Ziemi",
    "Circle of the Land Spells": "Czary Kręgu Ziemi",
    "Circle of the Land Spells: Arid Land": "Czary Kręgu Ziemi: jałowa kraina",
    "Circle of the Land Spells: Polar Land": "Czary Kręgu Ziemi: polarna kraina",
    "Circle of the Land Spells: Temperate Land": "Czary Kręgu Ziemi: umiarkowana kraina",
    "Circle of the Land Spells: Tropical Land": "Czary Kręgu Ziemi: tropikalna kraina",
    "Level 5: One with Shadows": "Poziom 5: Jedność z cieniem",
    "Sanctified Blade": "Uświęcone ostrze",
    "Sanctified blade": "Uświęcone ostrze",
    "Level 3: Divine Blessings": "Poziom 3: Boskie błogosławieństwa",
    "Level 3: Armor of the Faithful": "Poziom 3: Zbroja wiernych",
    "Armor of the Faithful": "Zbroja wiernych",
    "Level 3: Divine Inspiration": "Poziom 3: Boskie natchnienie",
    "Level 3: Rend the Blasphemous": "Poziom 3: Rozdarcie bluźniercy",
    "Rend the Blasphemous": "Rozdarcie bluźniercy",
    "Divine Point": "Punkt boskości",
    "Level 9: Chains of Judgement": "Poziom 9: Łańcuchy wyroku",
    "Chains of Judgement": "Łańcuchy wyroku",
    "Level 9: Divine Retaliation": "Poziom 9: Boski odwet",
    "Divine Retaliation": "Boski odwet",
    "Level 9: Erupting Blades": "Poziom 9: Wybuchające ostrza",
    "Erupting Blades": "Wybuchające ostrza",
    "Path of the Fractured": "Ścieżka rozszczepienia",
    "Level 3: Face of Rage": "Poziom 3: Oblicze szału",
    "Level 3: Mask of Civility": "Poziom 3: Maska ogłady",
    "Level 6: Brains and Brawn": "Poziom 6: Rozum i krzepa",
    "Level 10: Cunning and Brutal": "Poziom 10: Spryt i brutalność",
    "Face of Rage: Push": "Oblicze szału: Odepchnięcie",
    "Face of Rage: Prone": "Oblicze szału: Powalenie",
    '<LSTag Type="Status" Tooltip="POISONED">Poisons</LSTag> the target.': (
        '<LSTag Type="Status" Tooltip="POISONED">Zatruwa</LSTag> cel.'
    ),
    'Entreat. You gain proficiency in <LSTag Type="Skills" Tooltip="Persuasion">Persuasion</LSTag>.': (
        'Błagaj. Zyskujesz biegłość w '
        '<LSTag Type="Skills" Tooltip="Persuasion">Perswazji</LSTag>.'
    ),
    "You replace the Hunter’s Prey option with the other one.": (
        "Zastępujesz wybraną opcję Ofiary łowcy drugą z dostępnych."
    ),
    'Curse a creature with your touch. It has <LSTag Tooltip="Disadvantage">Disadvantage</LSTag> on '
    '<LSTag Tooltip="AttackRoll">Attack Rolls</LSTag> against you.': (
        'Dotknięciem przeklinasz istotę. Ma <LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AttackRoll">testach ataku</LSTag> przeciwko tobie.'
    ),
    'Deal an additional [1] when you attack the target and impart <LSTag Tooltip="Disadvantage">Disadvantage</LSTag> '
    'on Strength <LSTag Tooltip="AbilityCheck">Checks</LSTag>.': (
        'Gdy atakujesz cel, zadajesz mu dodatkowo [1], a cel ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> Siły.'
    ),
    'Deal an additional [1] when you attack the target and impart <LSTag Tooltip="Disadvantage">Disadvantage</LSTag> '
    'on Dexterity <LSTag Tooltip="AbilityCheck">Checks</LSTag>.': (
        'Gdy atakujesz cel, zadajesz mu dodatkowo [1], a cel ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> Zręczności.'
    ),
    'Deal an additional [1] when you attack the target and impart <LSTag Tooltip="Disadvantage">Disadvantage</LSTag> '
    'on Constitution <LSTag Tooltip="AbilityCheck">Checks</LSTag>.': (
        'Gdy atakujesz cel, zadajesz mu dodatkowo [1], a cel ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> Kondycji.'
    ),
    'Deal an additional [1] when you attack the target and impart <LSTag Tooltip="Disadvantage">Disadvantage</LSTag> '
    'on Intelligence <LSTag Tooltip="AbilityCheck">Checks</LSTag>.': (
        'Gdy atakujesz cel, zadajesz mu dodatkowo [1], a cel ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> Inteligencji.'
    ),
    'Deal an additional [1] when you attack the target and impart <LSTag Tooltip="Disadvantage">Disadvantage</LSTag> '
    'on Wisdom <LSTag Tooltip="AbilityCheck">Checks</LSTag>.': (
        'Gdy atakujesz cel, zadajesz mu dodatkowo [1], a cel ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> Mądrości.'
    ),
    'Deal an additional [1] when you attack the target and impart <LSTag Tooltip="Disadvantage">Disadvantage</LSTag> '
    'on Charisma <LSTag Tooltip="AbilityCheck">Checks</LSTag>.': (
        'Gdy atakujesz cel, zadajesz mu dodatkowo [1], a cel ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> Charyzmy.'
    ),
    'Make your attacks deal an additional [1] damage to the target and give it '
    '<LSTag Tooltip="Disadvantage">Disadvantage</LSTag> on an '
    '<LSTag Tooltip="Abilities">Ability</LSTag> of your choosing.': (
        'Twoje ataki zadają celowi dodatkowo [1], a cel ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w testach wybranej przez ciebie '
        '<LSTag Tooltip="Abilities">cechy</LSTag>.'
    ),
    "As a Reaction when a creature targets you with an attack, you can expend 1 Divine Point to force it "
    "to make a Wisdom saving throw. On a failed save, the attacker must choose a new target or the attack "
    "has no effect, and it can’t target you again until the start of your next turn. This feature does not "
    "protect you from areas of effect.": (
        "Gdy istota wybierze cię jako cel ataku, możesz w ramach reakcji wydać 1 punkt boskości i zmusić ją "
        "do wykonania rzutu obronnego na Mądrość. Przy niepowodzeniu atakujący musi wybrać nowy cel; jeśli "
        "tego nie zrobi, atak nie wywołuje żadnego efektu. Do początku twojej następnej tury nie może ponownie "
        "wybrać cię jako celu. Ta cecha nie chroni przed efektami obszarowymi."
    ),
    "When you hit a creature with your sanctified blade, you can expend 1 Divine Point to bind it in holy "
    "chains. The target must succeed on a Strength saving throw or take Radiant damage equal to your Wisdom "
    "modifier and gain the Restrained condition until the end of your next turn.": (
        "Gdy trafisz istotę swoim uświęconym ostrzem, możesz wydać 1 punkt boskości, aby spętać ją świętymi "
        "łańcuchami. Cel musi wykonać udany rzut obronny na Siłę, w przeciwnym razie otrzymuje obrażenia od "
        "światłości równe twojemu modyfikatorowi Mądrości i ma stan Unieruchomienia do końca twojej następnej "
        "tury."
    ),
    "You can expend 2 Divine Points to call down radiant blades in a 45-foot-long, 5-foot-wide Line. Each "
    "creature in the Line must make a Dexterity saving throw, taking Radiant damage equal to your Sneak "
    "Attack damage on a failed save, or half as much damage on a successful one.": (
        "Możesz wydać 2 punkty boskości, aby przywołać ostrza światłości w linii o długości 13,5 m i "
        "szerokości 1,5 m. Każda istota w tej linii wykonuje rzut obronny na Zręczność. Przy niepowodzeniu "
        "otrzymuje obrażenia od światłości równe obrażeniom twojego Ataku z ukrycia, a przy powodzeniu — "
        "połowę tej wartości."
    ),
}

# D&D 2024 level-up headings absent from the shipped BG3 corpus. These use
# the established Polish community names, with obvious corpus typos corrected.
EXACT_OVERRIDES.update({
    "Level 3: Primal Knowledge": "Poziom 3: Pierwotna wiedza",
    "Level 7: Instinctive Pounce": "Poziom 7: Instynktowny zryw",
    "Level 9: Brutal Strike": "Poziom 9: Brutalne uderzenie",
    "Level 7: Blessed Strikes: Potent Spellcasting": (
        "Poziom 7: Błogosławione uderzenia: Potężne czarowanie"
    ),
    "Level 5: Sear Undead": "Poziom 5: Spopielenie Nieumarłych",
    "Level 3: Mind Magic": "Poziom 3: Magia umysłu",
    "Level 1: Druidic": "Poziom 1: Język druidyczny",
    "Level 3: Circle Forms": "Poziom 3: Zwierzęce formy kręgu",
    "Level 7: Elemental Fury: Potent Spellcasting": (
        "Poziom 7: Furia żywiołów: Potężne czarowanie"
    ),
    "Level 6: Improved Circle Forms": "Poziom 6: Ulepszone Zwierzęce formy kręgu",
    "Level 2: Tactical Mind": "Poziom 2: Taktyczny umysł",
    "Level 5: Tactical Shift": "Poziom 5: Taktyczne przemieszczenie",
    "Level 3: Remarkable Athlete": "Poziom 3: Niezwykły atleta",
    "Level 10: Heroic Warrior": "Poziom 10: Heroiczny wojownik",
    "Level 1: Unarmored Defense": "Poziom 1: Obrona bez pancerza",
    "Level 2: Unarmored Movement": "Poziom 2: Szybkość mnicha",
    "Level 3: Deflect Attacks": "Poziom 3: Odbijanie ataków",
    "Level 6: Empowered Strikes": "Poziom 6: Wzmocnione uderzenia",
    "Level 9: Acrobatic Movement": "Poziom 9: Akrobatyczny ruch",
    "Level 10: Heightened Focus": "Poziom 10: Zwiększone skupienie",
    "Level 10: Self-Restoration": "Poziom 10: Samouzdrowienie",
    "Level 3: Shadow Arts": "Poziom 3: Sztuki cienia",
    "Level 11: Stride of the Elements": "Poziom 11: Pęd żywiołów",
    "Level 11: Fleet Step": "Poziom 11: Szybki krok",
    "Level 5: Faithful Steed": "Poziom 5: Wierny wierzchowiec",
    "Level 9: Abjure Foes": "Poziom 9: Odpędzenie wrogów",
    "Level 11: Radiant Strikes": "Poziom 11: Uderzenia światłości",
    "Level 3: Steady Aim": "Poziom 3: Stabilne celowanie",
    "Level 7: Sorcery Incarnate": "Poziom 7: Ucieleśnienie magii",
})


LAND_ARID_PL = (
    "Jeśli wybierzesz jałową krainę, przygotowujesz następujące czary: na 3. poziomie — Rozmycie, "
    "Płonące dłonie i Ognisty pocisk; na 5. poziomie — Kula ognia; na 7. poziomie — Skaza; "
    "a na 9. poziomie — Ściana kamienia."
)
LAND_POLAR_PL = (
    "Jeśli wybierzesz polarną krainę, przygotowujesz następujące czary: na 3. poziomie — Chmura "
    "mgły, Unieruchomienie osoby i Promień mrozu; na 5. poziomie — Śnieżyca; na 7. poziomie — "
    "Burza lodu; a na 9. poziomie — Stożek zimna."
)
LAND_TEMPERATE_TREE_PL = (
    'Jeśli wybierzesz umiarkowaną krainę, przygotowujesz następujące czary: na 3. poziomie — Krok '
    'przez mgłę, <LSTag Type="Spell" Tooltip="Target_ShockingGrasp">Porażający uścisk</LSTag> i '
    "Uśpienie; na 5. poziomie — Błyskawica; na 7. poziomie — Swoboda ruchu; a na 9. poziomie — "
    "Spacer między drzewami."
)
LAND_TEMPERATE_RESTORATION_PL = (
    'Jeśli wybierzesz umiarkowaną krainę, przygotowujesz następujące czary: na 3. poziomie — Krok '
    'przez mgłę, <LSTag Type="Spell" Tooltip="Target_ShockingGrasp">Porażający uścisk</LSTag> i '
    "Uśpienie; na 5. poziomie — Błyskawica; na 7. poziomie — Swoboda ruchu; a na 9. poziomie — "
    "Większe przywrócenie."
)
LAND_TROPICAL_PL = (
    "Jeśli wybierzesz tropikalną krainę, przygotowujesz następujące czary: na 3. poziomie — Kwasowy "
    "rozprysk, Promień zatrucia i Pajęczyna; na 5. poziomie — Śmierdząca chmura; na 7. poziomie — "
    "Polimorfia; a na 9. poziomie — Plaga owadów."
)
LAND_INTRO_PL = (
    "Za każdym razem, gdy kończysz długi odpoczynek, wybierasz jeden rodzaj krainy: jałową, polarną, "
    "umiarkowaną albo tropikalną. Na podstawie wyboru korzystasz z odpowiedniej tabeli i masz "
    "przygotowane wszystkie wymienione w niej czary dostępne na twoim poziomie druida lub niższym."
)

# Embedded feat labels often contain a full background or feature description,
# so they do not qualify for exact-title matching.  Keep their first line in
# sync with the shipped Polish BG3 feat name, falling back to the current Polish
# D&D 2024 corpus for feats absent from the game.  Parenthesised variants are
# internal BG3 labels derived from the same canonical feat title.
FEAT_PREFIX_OVERRIDES = {
    "Alert": "Czujność",
    "Athlete": "Atleta",
    "Charger": "Szarża",
    "Crossbow Expert (Point-Blank)": "Specjalista kusznik (strzelanie w zwarciu)",
    "Crossbow Expert (Wounding)": "Specjalista kusznik (raniący bełt)",
    "Crusher": "Zgniatacz",
    "Defensive Duellist": "Mistrz zasłony",
    "Dual Wielder": "Oburęczny",
    "Dual Wielder (Bonus Attack)": "Oburęczny (dodatkowy atak)",
    "Durable": "Twardziel",
    "Dragonscarred": "Smocze znamię",
    "Dragonscarred (Acid Resistance)": "Smocze znamię (odporność na kwas)",
    "Dragonscarred (Cold Resistance)": "Smocze znamię (odporność na zimno)",
    "Dragonscarred (Fire Resistance)": "Smocze znamię (odporność na ogień)",
    "Dragonscarred (Lightning Resistance)": "Smocze znamię (odporność na elektryczność)",
    "Dragonscarred (Poison Resistance)": "Smocze znamię (odporność na truciznę)",
    "Genie Magic": "Magia dżina",
    "Great Weapon Master": "Mistrz broni dwuręcznej",
    "Harper Teamwork": "Zgranie Harfiarzy",
    "Heavy Armour Master": "Mistrz ciężkiego pancerza",
    "Inspiring Leader": "Przywódca",
    "Lucky": "Szczęściarz",
    "Lordly Resolve": "Lordowska determinacja",
    "Mage Slayer": "Zabójca magów",
    "Medium Armour Master": "Mistrz średniego pancerza",
    "Mounted Combatant": "Kawalerzysta",
    "Mythal Touched": "Dotknięty przez mythal",
    "Savage Attacker": "Brutalny napastnik",
    "Sentinel (Opportunity Advantage)": "Wartownik (ułatwienie w atakach okazyjnych)",
    "Sentinel (Snare)": "Wartownik (unieruchomienie)",
    "Sentinel (Vengeance)": "Wartownik (odwet)",
    "Shadow Touched": "Dotknięty przez Cień",
    "Spell Sniper (Melee)": "Mistyczny strzelec (wręcz)",
    "Spell Sniper (Ranged)": "Mistyczny strzelec (dystansowy)",
    "Weapon Master": "Mistrz oręża",
    "Zhentarim Tactics": "Taktyka Zhentarimów",
}

EXACT_OVERRIDES.update({
    # Correct two misleading community/baseline title matches in the Heroes of
    # Faerûn feat block and keep its action label consistent with the reviewed
    # prose used by the same feature.
    "Genie Magic": "Magia dżina",
    "Orders Resilience": "Odporność Zakonu",
    "Flustering Strike": "Peszące uderzenie",
    "Encourage Ally": "Pokrzep sojusznika",
    "Standard Bearer": "Chorąży",
    "If you choose Arid Land, you have Blur, Burning Hands, and Fire Bolt prepared at 3rd level; "
    "Fireball at 5th level; Blight at 7th level; and Wall of Stone at 9th level.": LAND_ARID_PL,
    "If you choose Polar Land, you have Fog Cloud, Hold Person, and Ray of Frost prepared at 3rd level; "
    "Sleet Storm at 5th level; Ice Storm at 7th level; and Cone of Cold at 9th level.": LAND_POLAR_PL,
    'If you choose Temperate Land, you have Misty Step, <LSTag Type="Spell" '
    'Tooltip="Target_ShockingGrasp">Shocking Grasp</LSTag>, and Sleep prepared at 3rd level; '
    "Lightning Bolt at 5th level; Freedom of Movement at 7th level; and Tree Stride at 9th level.": (
        LAND_TEMPERATE_TREE_PL
    ),
    'If you choose Temperate Land, you have Misty Step, <LSTag Type="Spell" '
    'Tooltip="Target_ShockingGrasp">Shocking Grasp</LSTag>, and Sleep prepared at 3rd level; '
    "Lightning Bolt at 5th level; Freedom of Movement at 7th level; and Greater Restoration at 9th level.": (
        LAND_TEMPERATE_RESTORATION_PL
    ),
    "If you choose Tropical Land, you have Acid Splash, Ray of Sickness, and Web prepared at 3rd level; "
    "Stinking Cloud at 5th level; Polymorph at 7th level; and Insect Plague at 9th level.": LAND_TROPICAL_PL,
    "You can manifest shimmering blades of psychic energy.\n\nWhile wielding a dagger, shortsword, or "
    'scimitar, you can change the weapon’s damage type to Psychic and give it the <LSTag Tooltip="Thrown">'
    "Thrown</LSTag> property.": (
        "Możesz materializować połyskujące ostrza energii psychicznej.\n\nGdy dzierżysz sztylet, krótki miecz "
        'lub sejmitar, możesz zmienić typ obrażeń tej broni na psychiczne i nadać jej właściwość '
        '<LSTag Tooltip="Thrown">Rzucana</LSTag>.'
    ),
    "Cantrip. You learn the Ray of Frost cantrip.\n\nFrostbite. Once per turn when you hit a creature "
    "with an attack roll and deal Cold damage, you can temporarily negate the creature’s defenses. "
    "The creature subtracts 1d4 from the next saving throw it makes before the end of your next turn.": (
        "Sztuczka. Poznajesz sztuczkę Promień mrozu.\n\nOdmrożenie. Raz na turę, gdy trafisz istotę "
        "testem ataku i zadasz obrażenia od zimna, możesz tymczasowo osłabić jej obronę. Istota "
        "odejmuje 1k4 od następnego rzutu obronnego wykonanego przed końcem twojej następnej tury."
    ),
    "The effect improves when you reach 10th level in this class.": (
        "Efekt zostaje wzmocniony po osiągnięciu 10. poziomu tej klasy."
    ),
    "Your Speed increases by 10 feet. It increases by another 5 feet when you reach Bard levels 6 "
    "(total increase of 15 feet).": (
        "Twoja szybkość wzrasta o 3 m. Po osiągnięciu 6. poziomu barda wzrasta o kolejne 1,5 m "
        "(łącznie o 4,5 m)."
    ),
    # Remaining interface labels and spell names found by the English-residue
    # audit. Official BG3 wording is used where it exists; otherwise these use
    # the active Polish D&D community corpus or a conservative editorial name.
    "Glaive, Greatsword": "Glewia, Wielki miecz",
    "Level 11: Stalker's Flurry": "Poziom 11: Gwałtowność tropiciela",
    "Level 11: Stalker’s Flurry": "Poziom 11: Gwałtowność tropiciela",
    "Level 3: Mage Hand Legerdemain": "Poziom 3: Kuglarstwo magicznej dłoni",
    "Feat: Martial Adept": "Atut: Adept sztuk walki",
    "Feat: Sentinel (Snare)": "Atut: Wartownik (Sidła)",
    "Feat: Ritual Caster": "Atut: Znawca rytuałów",
    "Feat: Dungeon Delver": "Atut: Badacz podziemi",
    "Feat: Skulker": "Atut: Czatownik",
    "Feat: Cold Caster": "Atut: Władający zimnem",
    "Controlled Channeling: Wayfarer": "Kontrolowane przewodzenie: Wędrowiec",
    "Crusher: Enhanced Critical": "Zgniatacz: wzmocnione trafienie krytyczne",
    "Scroll of Darkbolt": "Zwój mrocznego pocisku",
    "Scroll of Synaptic Static": "Zwój szumu synaptycznego",
    "Scroll of Barkskin": "Zwój korowej skóry",
    "Scroll of Vitriolic Sphere": "Zwój żrącej kuli",
    "Scroll of Elminster's Elusion": "Zwój nieuchwytności Elminstera",
    "Scroll of Finger Guns": "Zwój pistoletów z palców",
    "Level 2: Bedevil": "Poziom 2: Dręczenie",
    "Level 2: Lissome": "Poziom 2: Zwinność",
    "Level 3: Dread Ambusher": "Poziom 3: Straszliwa zasadzka",
    "Level 6: Magic Item Tinker": "Poziom 6: Majsterkowicz magicznych przedmiotów",
    "Level 6: Mind Sharpener": "Poziom 6: Wyostrzacz umysłu",
    "Level 6: Infernal Conduit": "Poziom 6: Piekielne przewodzenie",
    "Level 5: Alchemical Savant": "Poziom 5: Alchemiczny erudyta",
    "Contagion: Seizure": "Zaraza: drgawki",
    "Grazing Shot": "Draśnięcie strzałem",
    "Shadow Gnawer": "Pożeracz cieni",
    "Cold-Hearted": "Zimne serce",
    "Maddala Deadeye": "Maddala Sokole Oko",
    "Giant Ancestry: Cloud Giant": "Pochodzenie olbrzyma: olbrzym chmurowy",
    "Mind Sharpener": "Wyostrzacz umysłu",
    "Savant": "Erudyta",
    "Stymying Mark": "Hamujące piętno",
    "Eldritch Hexed: Strength": "Nadnaturalna klątwa: Siła",
    "Eldritch Hexed: Dexterity": "Nadnaturalna klątwa: Zręczność",
    "Eldritch Hexed: Constitution": "Nadnaturalna klątwa: Kondycja",
    "Eldritch Hexed: Intelligence": "Nadnaturalna klątwa: Inteligencja",
    "Eldritch Hexed: Wisdom": "Nadnaturalna klątwa: Mądrość",
    "Eldritch Hexed: Charisma": "Nadnaturalna klątwa: Charyzma",
    "Elemental Attunement": "Harmonia żywiołów",
    "Finger Guns": "Pistolety z palców",
    "Magic Initiate: Finger Guns": "Wtajemniczony: Pistolety z palców",
    "Darkbolt": "Mroczny pocisk",
    "Synaptic Static": "Szum synaptyczny",
    "Vitriolic Sphere": "Żrąca kula",
    "Elminster's Elusion": "Nieuchwytność Elminstera",
    "Mace, Spear, Flail, Longsword, Morningstar, War Pick": (
        "Buława, Włócznia, Kiścień, Miecz długi, Morgensztern, Nadziak"
    ),
    "Quarterstaff, Battleaxe, Maul, Trident": "Drąg, Topór bojowy, Młot dwuręczny, Trójząb",
    "Level 1: Primal Order: Poison Spray": "Poziom 1: Pierwotny porządek: Trujący rozprysk",
    "Magic Initiate: Chill Touch": "Wtajemniczony: Przeszywający dotyk",
    "Magic Initiate: Poison Spray": "Wtajemniczony: Trujący rozprysk",
    "Magic Initiate: Colour Spray": "Wtajemniczony: Kolorowy rozprysk",
    "Feat: Piercer": "Atut: Przebijacz",
    "Feat: Slasher": "Atut: Siepacz",
    "Fey Touched: Charm Person": "Dotknięty przez Fey: Zauroczenie osoby",
    "Fey Touched: Heroism": "Dotknięty przez Fey: Heroizm",
    "Fey Touched: Hunter's Mark": "Dotknięty przez Fey: Znak łowcy",
    "Shadow Touched: Colour Spray": "Dotknięty przez cień: Kolorowy rozprysk",
    "Shadow Magic: Colour Spray": "Magia cienia: Kolorowy rozprysk",
    "Dragon's Terror": "Smocza groza",
    "Origin Feat: Tyro of the Gauntlet": "Atut pochodzenia: Nowicjusz Rękawicy",
    "Feat: Tyro of the Gauntlet": "Atut: Nowicjusz Rękawicy",
    "Level 3: Genie's Splendor": "Poziom 3: Wspaniałość dżina",
    "Feat: Charm Twister": "Atut: Tkacz amuletów",
    "Charm Twister": "Tkacz amuletów",
    "Level 3: Hexblade Manifest": "Poziom 3: Manifestacja Hexblade’a",
    "Hexblade Manifest": "Manifestacja Hexblade’a",
    "Slasher: Enhanced Critical": "Siepacz: wzmocnione trafienie krytyczne",
    "Slasher: Hamstring": "Siepacz: podcięcie ścięgna",
    "Controlled Channeling: Arsonist": "Kontrolowane przewodzenie: Podpalacz",
    "Scroll of Heat Metal": "Zwój rozgrzania metalu",
    "Scroll of Danse Macabre": "Zwój makabrycznego tańca",
    "Level 3: Bang, You’re Dead!": "Poziom 3: Bum, nie żyjesz!",
    "Level 3: Bang, You're Dead!": "Poziom 3: Bum, nie żyjesz!",
    "Cunning Strike: Trip": "Przebiegły atak: Podcięcie",
    "Danse Macabre": "Makabryczny taniec",
    "Doom Song": "Pieśń zagłady",
    "Steel Defender": "Stalowy obrońca",
})


UID_OVERRIDES = {
    # The online baseline dropped the final tagged clause; this restores the
    # complete meaning and every source tag.
    "h0e2f0dfaga02cg9ad3g9586ga7ad2ece81cf": (
        'Zyskujesz biegłość w umiejętnościach <LSTag Type="Skills" Tooltip="Insight">Intuicja</LSTag> '
        'i <LSTag Type="Skills" Tooltip="Medicine">Medycyna</LSTag>. Łącząc ekstrakty, możesz przygotować '
        'dwa roztwory alchemiczne zamiast jednego, jeśli pomyślnie wykonasz '
        '<LSTag Tooltip="AbilityCheck">test</LSTag> Medycyny o '
        '<LSTag Tooltip="DifficultyClass">ST</LSTag> 15.'
    ),
    # Community source markup introduced Foundry-only &Reference placeholders
    # that do not exist in the mod. Keep the complete Polish wording but no
    # unsupported placeholders.
    "h1dedae79g3922gbd27g0925g98aec4318fa7": (
        "Możesz użyć nut muzycznych lub słów mocy, aby zakłócić efekty wpływające na umysł. "
        "Gdy tobie lub istocie w promieniu 30 stóp od ciebie nie powiedzie się rzut obronny "
        "przeciwko efektowi nakładającemu stan Zauroczenia lub Przerażenia, możesz użyć reakcji, "
        "by wymusić ponowienie rzutu obronnego. Nowy rzut jest wykonywany z ułatwieniem."
    ),
    "h0f358bf7g4a10gc77fg43cfg0c187137ef7a": (
        "Możesz użyć nut muzycznych lub słów mocy, aby zakłócić efekty wpływające na umysł. "
        "Gdy tobie lub istocie w promieniu 30 stóp od ciebie nie powiedzie się rzut obronny "
        "przeciwko efektowi nakładającemu stan Zauroczenia lub Przerażenia, możesz użyć reakcji, "
        "by wymusić ponowienie rzutu obronnego. Nowy rzut jest wykonywany z ułatwieniem."
    ),
    "h97dd1bbcg1ca7g6953g67d7g155182b6526b": (
        "Potrafisz zręcznie unikać niektórych niebezpieczeństw. Gdy jesteś narażony na efekt, "
        "który pozwala wykonać rzut obronny na Zręczność, aby otrzymać tylko połowę obrażeń, "
        "zamiast tego nie otrzymujesz żadnych obrażeń przy udanym rzucie i tylko połowę obrażeń "
        "przy nieudanym. Nie możesz użyć tej zdolności, jeśli jesteś Obezwładniony."
    ),
    "h0e929a83g6124gede3gd6d6g810f31fc91bf": (
        "Rycerze runiczni rozwijają swoje umiejętności bojowe, korzystając z nadprzyrodzonej mocy "
        "run — pradawnej praktyki zapoczątkowanej przez olbrzymy. Rytowników run można spotkać "
        "wśród wszystkich rodów olbrzymów, a swojej sztuki najpewniej nauczyłeś się bezpośrednio "
        "lub pośrednio od takiego mistycznego rzemieślnika. Być może odnalazłeś dzieło olbrzyma "
        "wyryte na wzgórzu lub w jaskini, poznałeś runy dzięki mędrcowi albo spotkałeś olbrzyma "
        "osobiście. Tak czy inaczej, zgłębiłeś rzemiosło olbrzymów i nauczyłeś się nakładać "
        "magiczne runy, by wzmacniać swój ekwipunek."
    ),
    "ha77cb967ga90dgf3bagbb92g9b2af176e030": (
        "Legenda Barda Łucznika zainspirowała wielu młodych ludzi z Dale, którzy pragną dowieść "
        "swej wartości, zabijając potężnego potwora. Jak wielu przed tobą, od dawna rozmyślasz "
        "nad sposobami walki z ogromnymi stworzeniami, licząc, że pewnego dnia zdobędziesz sławę, "
        "pokonując jedno z nich.\n\n"
        "Masz ułatwienie w testach ataku przeciwko Dużym lub większym stworzeniom. Ponadto, gdy "
        "trafiasz takie stworzenie, zadajesz dodatkowe obrażenia równe modyfikatorowi Siły."
    ),
    "ha574dfdfgf055g69c1g9889gce2fffa674e6": (
        "Czarna Strzała, która powaliła smoka Smauga, mogła być do tego przeznaczona, lecz ręka, "
        "która posłała ją z taką siłą, była niezwykle mocna. Gdy rzucasz włócznią lub napinasz "
        "łuk, dbasz o pewny chwyt i celny strzał.\n\n"
        "Podczas wykonywania ataku dystansowego bronią używasz modyfikatora Siły do testu ataku "
        "i obrażeń; do obu rzutów musisz użyć tego samego modyfikatora. Jeśli w tej samej turze "
        "przemieścisz się nie dalej niż o połowę swojej szybkości i trafisz stworzenie atakiem "
        "dystansowym bronią, możesz w ramach akcji dodatkowej zadać tym atakiem dodatkowe 1k4 "
        "obrażeń tego samego typu co broń."
    ),
    "h214e9d1dg45fcg6388gdc9cg6130d7c87cf2": (
        'Podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag> raz na turę możesz wypuścić '
        'smugi cienistego dymu. Dym rozciąga się na 3 metry od ciebie w każdym kierunku. Każde '
        'inne stworzenie znajdujące się w dymie jest <LSTag Type="Status" Tooltip="BLINDED">oślepione</LSTag>.'
    ),
    "hc17eba4eg936fg2851g0508gb73011778121": (
        'Podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag> raz na turę możesz wypuścić '
        'smugi cienistego dymu. Dym rozciąga się na 3 metry od ciebie w każdym kierunku. Każde '
        'inne stworzenie znajdujące się w dymie jest <LSTag Type="Status" Tooltip="BLINDED">oślepione</LSTag>.'
    ),
    "h1a71759egf1c8g9a25g2327g7210d3bcea88": (
        'Podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag> możesz czerpać siłę z '
        'otaczających cię cieni, by odzyskać witalność. W półmroku lub ciemności możesz w ramach '
        'akcji dodatkowej odzyskać punkty wytrzymałości równe sumie 1k12 i twojego modyfikatora Kondycji.'
    ),
    "h4d7a4652g2bf4gcf0dg7e2bg038ddc3b14d4": (
        'Podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag> możesz czerpać siłę z '
        'otaczających cię cieni, by odzyskać witalność. W półmroku lub ciemności możesz w ramach '
        'akcji dodatkowej odzyskać punkty wytrzymałości równe sumie 1k12 i twojego modyfikatora Kondycji.'
    ),
    "haa843db4g20ebg9021gacedg3f8ada559a41": (
        'Barbarzyńcy kroczący Ścieżką olbrzyma czerpią siłę z tych samych pierwotnych mocy co '
        'olbrzymy. Gdy wpadają w <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, przepełnia ich '
        'moc żywiołów, a ich ciała rosną, przybierając postacie przywodzące na myśl potęgę olbrzymów. '
        'Niektórzy wyglądają jak powiększone wersje samych siebie, czasem z błyskiem energii żywiołów '
        'w oczach i wokół broni. Inni przeobrażają się znacznie bardziej, przybierając wygląd '
        'prawdziwego olbrzyma albo istoty podobnej do żywiołaka, spowitej ogniem, mrozem lub błyskawicami.'
    ),
    "hfcbd3784g4436g3a40g1260g63eb8006c7fa": (
        'Twoje oddanie dzikim, nadnaturalnym istotom zmienia cię jeszcze bardziej. Po przemianie za '
        'pomocą <LSTag Type="Passive" Tooltip="HollowWarden_3_WrathOfTheWild">Gniewu dziczy</LSTag> '
        'zyskujesz następujące dodatkowe korzyści.\n\n'
        'Groźna aura. Gdy stworzeniu nie powiedzie się rzut obronny przeciwko twojej '
        '<LSTag Type="Status" Tooltip="UNNERVING_AURA">Niepokojącej aurze</LSTag>, nie może ono '
        'odzyskiwać punktów wytrzymałości ani wykonywać reakcji aż do początku twojej następnej tury.\n\n'
        'Złowieszcze ciosy. Gdy trafisz testem ataku stworzenie, które jest Przerażone, atak zadaje '
        'dodatkowe obrażenia równe twojemu modyfikatorowi Mądrości.'
    ),
    "h3a320da8g90b9g9714ge237g45c9782afbd0": (
        "Jeśli użyjesz Szaleńczego ataku, cel otrzymuje dodatkowe 1k10 obrażeń tego samego typu co "
        "obrażenia zadane przez broń lub atak bez broni, a ty możesz wywołać jeden wybrany efekt "
        "Brutalnego uderzenia.\n\n"
        "Potężny cios. Cel zostaje odepchnięty o [1] prosto od ciebie. Następnie możesz przemieścić "
        "się prosto w stronę celu na odległość równą maksymalnie połowie swojej szybkości, nie "
        "prowokując ataków okazyjnych.\n"
        "Podcięcie ścięgna. Szybkość celu zostaje zmniejszona o [1] do początku twojej następnej "
        "tury. Cel może być objęty tylko jednym Podcięciem ścięgna naraz — działa najnowsze."
    ),
    "hfd45d1c1g9dd3g206agfb7eg456c6af02ac0": (
        'Raz na <LSTag Tooltip="ShortRest">krótki odpoczynek</LSTag>, gdy podczas '
        '<LSTag Type="Status" Tooltip="RAGE">szału</LSTag> liczba twoich '
        '<LSTag Tooltip="HitPoints">punktów wytrzymałości</LSTag> miałaby spaść do [1], zamiast '
        '<LSTag Type="Status" Tooltip="DOWNED">stracić przytomność</LSTag> odzyskujesz punkty '
        'wytrzymałości w liczbie równej dwukrotności twojego poziomu barbarzyńcy.'
    ),
    "h035b29c1g51d0ge9f8gb63fgc75cd5045b0c": (
        "Zawsze masz przygotowane czary Zauroczenie osoby i Lustrzane odbicia.\n\n"
        "Ponadto bezpośrednio po rzuceniu czaru ze szkoły uroków lub iluzji przy użyciu komórki "
        "czaru możesz zmusić istotę, którą widzisz w odległości do [1] od siebie, do wykonania rzutu "
        "obronnego na Mądrość przeciwko twojemu ST rzutu obronnego przeciwko czarowi. W razie "
        "niepowodzenia cel jest Zauroczony lub Przerażony (wedle twojego wyboru) przez 1 minutę."
    ),
    "h619804afg28a4g6f48g9db2gb39ec7c1d073": (
        'Możesz ukierunkować boską energię, aby wywoływać specjalne efekty, takie jak '
        '<LSTag Type="Spell" Tooltip="Target_DivineSpark">Boska iskra</LSTag> i Odpędzanie '
        'nieumarłych. Za każdym razem, gdy używasz Aktu wiary, wybierasz jeden z nich. Na wyższych '
        'poziomach kleryka zyskujesz dodatkowe efekty i użycia. Jedno użycie odzyskujesz po krótkim '
        'odpoczynku, a wszystkie po długim odpoczynku. ST rzutów obronnych oblicza się na podstawie '
        'twojego ST rzutu obronnego przeciwko czarowi.'
    ),
    "hcac62cb2g678dgbdc4g4a80g875b53ed7a48": (
        "Po zakończeniu krótkiego lub długiego odpoczynku odzyskujesz wszystkie zużyte użycia "
        "Ochronnego rozbłysku.\n\nPonadto za każdym razem, gdy używasz Ochronnego rozbłysku, możesz "
        "przyznać celowi ataku, który go wywołał, tymczasowe punkty wytrzymałości w liczbie równej "
        "sumie 2k6 i twojego modyfikatora Mądrości."
    ),
    "hdd98d6aage020gf00bgcd6fg4be2ad2fd956": (
        'Zyskujesz biegłość w rzutach obronnych na Inteligencję.\n\nDodaj połowę swojego '
        'modyfikatora Mądrości do <LSTag Tooltip="AbilityCheck">testów cechy</LSTag>, w których '
        'nie masz <LSTag Tooltip="Proficiency">biegłości</LSTag>.'
    ),
    "h5c0401b6g3fc4gaadagf4bbg097715066c52": (
        'Skupienie na unikaniu ataków.\n\n<LSTag Tooltip="AttackRoll">Testy ataku</LSTag> przeciwko '
        'tej istocie są wykonywane z <LSTag Tooltip="Disadvantage">utrudnieniem</LSTag>, a ona '
        'sama ma <LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="SavingThrow">rzutach obronnych</LSTag> na Zręczność.'
    ),
    "h9e315a90g0705gb2c6g1a8eg13de362924de": (
        'Zyskujesz ekspertyzę (patrz słownik zasad) w dwóch wybranych umiejętnościach, w których '
        'masz biegłość. <LSTag Type="Skills" Tooltip="Performance">Występy</LSTag> i '
        '<LSTag Type="Skills" Tooltip="Persuasion">Perswazja</LSTag> są zalecane, jeśli masz w '
        'nich biegłość.\n\nNa 9. poziomie barda zyskujesz ekspertyzę w dwóch kolejnych wybranych '
        'umiejętnościach, w których masz biegłość.'
    ),
    "h3c269efagf9cbgfc7dga3bag5ea715ef1024": (
        "Potrafisz wpływać na równowagę między życiem a śmiercią, co zapewnia ci następujące korzyści.\n\n"
        "Zew śmierci. Raz na turę, gdy zadajesz obrażenia czarem albo trafieniem w teście ataku "
        "stworzeniu, które nie ma wszystkich punktów wytrzymałości, otrzymuje ono dodatkowe 1k4 "
        "obrażeń nekrotycznych. Dodatkowe obrażenia wzrastają do 1k6 po osiągnięciu 11. poziomu kleryka.\n\n"
        "Powrót do życia. Możesz rzucić Powstrzymanie śmierci w ramach akcji dodatkowej.\n\n"
        "Ponadto, gdy czarem lub Aktem wiary przywracasz punkty wytrzymałości stworzeniu mającemu "
        "0 punktów wytrzymałości i normalnie musiałbyś wykonać w tym celu co najmniej jeden rzut "
        "kością, nie wykonujesz tych rzutów. Stworzenie odzyskuje zamiast tego punkty wytrzymałości "
        "w liczbie równej twojemu poziomowi kleryka."
    ),
    "h8fe28200g46b7g051cga5b0ga6bd5b6a5b73": (
        "Zawarłeś pakt z istotą, która przeciwstawia się cyklowi życia i śmierci: potężnym liczem, "
        "wampirem lub inną nieumarłą istotą. Ci pradawni patroni sami byli kiedyś śmiertelnikami, "
        "dlatego dobrze znają ścieżki ambicji i drogi prowadzące przez wrota śmierci. Chętnie dzielą "
        "się tą bluźnierczą wiedzą i innymi tajemnicami z tymi, którzy wypełniają ich wolę wśród żywych."
    ),
    "h91a9a031gbb78g3004g2f6cg6dcdb8f2cea3": (
        'Możesz korzystać z walki dwiema broniami, nawet jeśli twoja broń nie jest '
        '<LSTag Tooltip="Light">lekka</LSTag>. Nie możesz walczyć dwiema broniami, jeśli są one '
        '<LSTag Tooltip="TwoHanded">dwuręczne</LSTag>.<br><br>Gdy w swojej turze wykonasz akcję '
        'Ataku i zaatakujesz bronią do walki wręcz, możesz później w tej samej turze wykonać jeden '
        'atak drugą ręką w ramach akcji dodatkowej. Jeśli opanowałeś właściwość Nacięcie i trzymasz '
        'w drugiej ręce broń z tą właściwością, możesz wykonać do dwóch ataków drugą ręką na turę.'
    ),
    "h2a38021bge7c4g0eedgdbf5g331c3221892d": (
        "Na przykład zwój Ściany ognia (czaru 4. poziomu) wymaga dostępu do komórek czarów 3. "
        "poziomu. Postać może spełnić ten warunek, mając 5 poziomów maga albo na przykład 4 poziomy "
        "maga i 3 poziomy mistycznego oszusta. Postać mająca 4 poziomy kleryka i 3 poziomy "
        "mistycznego oszusta nie spełnia jednak tego warunku, ponieważ Ściana ognia nie znajduje "
        "się na liście czarów kleryka."
    ),
    "h1558545egaf7dg1079g8177g9f6871b6f525": (
        'Cel jest objęty stanem <LSTag Type="Status" Tooltip="INVISIBLE">niewidzialności</LSTag> '
        'do końca swojej następnej tury albo do chwili, gdy wykona test ataku, zada obrażenia lub '
        'rzuci czar. Gdy niewidzialność się kończy, każda istota w emanacji o promieniu 1,5 m, której '
        'źródłem jest cel, musi wykonać udany rzut obronny na Kondycję. W razie niepowodzenia '
        'otrzymuje obrażenia nekrotyczne równe wynikowi dwóch rzutów kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>.'
    ),
    "hf545430ag2493gc858g08d3g0bef38197077": (
        'Jest objęty stanem <LSTag Type="Status" Tooltip="INVISIBLE">niewidzialności</LSTag>. Gdy '
        'niewidzialność się kończy, każda istota w emanacji o promieniu 1,5 m, której źródłem jest '
        'ta postać, musi wykonać udany rzut obronny na Kondycję. W razie niepowodzenia otrzymuje '
        'obrażenia nekrotyczne równe wynikowi dwóch rzutów kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>.'
    ),
    "ha5f5579fg9ce6ge4abg474ag9e80c16acfae": (
        'Przywołujesz i wypuszczasz stado śmiercionośnych kruków. Każde wybrane przez ciebie '
        'stworzenie w stożku o długości 9 m, którego źródłem jesteś, wykonuje rzut obronny na '
        'Zręczność. W razie niepowodzenia cel otrzymuje 5k6 obrażeń od mocy i zyskuje stan '
        '<LSTag Type="Status" Tooltip="BLINDED">Oślepienia</LSTag>. W razie powodzenia otrzymuje '
        'połowę obrażeń. Oślepiona istota ponawia rzut obronny na koniec każdej swojej tury i w '
        'razie powodzenia kończy działanie efektu na sobie.'
    ),
    "hdf6371dcga18fg87bcgbe0dgf6e2f7928012": (
        'Tworzysz pulsującą kulę energii i ciskasz nią w jedną istotę w zasięgu. Wykonaj przeciwko '
        'celowi dystansowy test ataku czarem. Przy trafieniu cel otrzymuje obrażenia od światłości. '
        'Niezależnie od trafienia kula wybucha następnie rozbłyskiem światła. Cel i każda istota w '
        'promieniu 3 m od niego wykonują rzut obronny na Kondycję. W razie niepowodzenia istota '
        'zyskuje do końca swojej następnej tury stan '
        '<LSTag Type="Status" Tooltip="BLINDED">Oślepienia</LSTag>.'
    ),
    "hd0b1b087g7e7fg7cf3gdc0fg4b7196bb961f": (
        'W ramach akcji dodatkowej możesz zużyć jedno użycie '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> '
        'i przywołać określonego ducha. Gdy to robisz, wybierz ducha z tabeli '
        '<LSTag Type="Passive" Tooltip="Spirits_3_SpiritsFromBeyond">Duchy z zaświatów</LSTag> '
        'zamiast wykonywać rzut. Numer przypisany wybranemu duchowi musi być mniejszy lub równy '
        'najwyższej wartości na twojej kości bardowskiej inspiracji. Na przykład, jeśli używasz '
        'kości k8, możesz wybrać dowolnego ducha aż do Cienia włącznie.'
    ),
    "hc63ea14cgb031g53b1ge9c5gd05f610e629c": (
        LAND_INTRO_PL + "\n\n" + LAND_ARID_PL + "\n\n" + LAND_POLAR_PL + "\n\n" +
        LAND_TEMPERATE_TREE_PL + "\n\n" + LAND_TROPICAL_PL
    ),
    "hd95cf570g7ab5ga240gfd2eg759fa404ffde": (
        LAND_INTRO_PL + "\n\n" + LAND_ARID_PL + "\n\n" + LAND_POLAR_PL + "\n\n" +
        LAND_TEMPERATE_RESTORATION_PL + "\n\n" + LAND_TROPICAL_PL
    ),
    "hd365173fgd836g93a3gdf92g64f01d869f29": (
        LAND_INTRO_PL + "\n\n" + LAND_ARID_PL + "\n\n" + LAND_POLAR_PL + "\n\n" +
        LAND_TEMPERATE_RESTORATION_PL + "\n\n" + LAND_TROPICAL_PL
    ),
    "h8708a627g8357g1f81g5bfdgc87a5b00b9fe": (
        'Otrzymujesz liczbę <LSTag Type="ActionResource" Tooltip="LuckPoint">punktów szczęścia</LSTag> '
        'równą twojej premii z biegłości. Możesz wydawać te punkty, aby zyskać '
        '<LSTag Tooltip="Advantage">ułatwienie</LSTag> w <LSTag Tooltip="AttackRoll">testach ataku</LSTag>, '
        '<LSTag Tooltip="AbilityCheck">testach cechy</LSTag> lub <LSTag Tooltip="SavingThrow">rzutach '
        'obronnych</LSTag>, albo zmusić przeciwnika do powtórzenia <LSTag Tooltip="AttackRoll">testu '
        'ataku</LSTag>.'
    ),
    "h531047f9gd6d4g5415g3f87gada7b4be2fa4": (
        'Gdy przeciwnik w zasięgu walki wręcz atakuje sojusznika, możesz użyć '
        '<LSTag Type="ActionResource" Tooltip="ReactionActionPoint">reakcji</LSTag>, aby zaatakować '
        'go bronią. Wybrany sojusznik nie może mieć atutu Strażnik.\n\nMasz '
        '<LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="OpportunityAttack">atakach okazyjnych</LSTag>, a gdy trafisz istotę atakiem '
        'okazyjnym, nie może się ona przemieszczać do końca swojej tury.'
    ),
    "h47c75c00gad45gcc7agd1fbg3816f09eaa53": (
        'Zadaje obrażenia psychiczne i ma właściwość <LSTag Tooltip="Thrown">Rzucana</LSTag>.\n\n'
        'Broni nie można wytrącić z ręki osoby, która ją dzierży, a gdy zostanie '
        '<LSTag Type="Spell" Tooltip="Throw_Throw">rzucona</LSTag>, automatycznie do niej powraca.'
    ),
    "h0eb341bcgb4f9g7430gafc5g64f46cf69004": (
        'W ramach reakcji możesz nałożyć <LSTag Tooltip="Disadvantage">utrudnienie</LSTag> na '
        '<LSTag Tooltip="AttackRoll">test ataku</LSTag> przeciwko tobie.\n\nJeśli atak chybi, przez 1 turę '
        'masz <LSTag Tooltip="Advantage">ułatwienie</LSTag> w następnym teście ataku przeciwko '
        'napastnikowi.\n\nPo użyciu tej zdolności nie możesz użyć jej ponownie do zakończenia krótkiego '
        'lub długiego odpoczynku, chyba że zużyjesz komórkę czaru Magii paktu (bez użycia akcji), '
        'aby odzyskać jej użycie.'
    ),
    "ha1b537d6gb014g4e76gdd96g37cbe829c37c": (
        'Istota otrzymuje od czarującego dodatkowe [1]. Ma też <LSTag Tooltip="Disadvantage">utrudnienie</LSTag> '
        'w <LSTag Tooltip="AbilityCheck">testach</LSTag> Kondycji i <LSTag Tooltip="SavingThrow">rzutach '
        'obronnych</LSTag> na Kondycję.'
    ),
    "h9ca6d01dge19ag99cbg8e93gf6de98c14607": (
        "Twoja biegłość w walce wręcz pozwala zadawać miażdżące ciosy, nie pozwalając przeciwnikowi "
        "odzyskać równowagi. Gdy trafisz istotę testem ataku bronią do walki wręcz, możesz wykorzystać "
        "reakcję, aby zadać dodatkowe 2k6 obrażeń tego samego typu co broń. Istota ma utrudnienie w "
        "następnym teście ataku wykonanym przed początkiem twojej następnej tury.\n\nPo osiągnięciu 11. "
        "poziomu łowcy potworów dodatkowe obrażenia wzrastają do 4k6."
    ),
    "h97af1d74g3b7ega7c6g7dceg969a03ccef68": (
        "Drugi główny ród elfów Północnych Krain wędruje niewielkimi grupami przez tundrę i lodowe "
        "wzgórza Ponurej Przestrzeni, polując na karibu i mamuty z grzbietów reniferów oraz białofutrych "
        "tygrysów szablozębnych. Lodowe elfy żyją zwykle w odosobnieniu i są zaciekle samowystarczalne. "
        "Zyskały przez to opinię skrytych, choć w rzeczywistości po prostu niewiele obchodzi je szerszy "
        "świat. Nie oczekują pomocy od obcych ani nie są też skłonne jej udzielać. Czasami są jednak "
        "gotowe handlować z ludźmi, krasnoludami i trollkinami. Wbrew przekonaniom niedoinformowanych "
        "przybyszów tylko nieliczne społeczności lodowych elfów czczą Boreasa i wypełniają jego wolę; "
        "większość nie chce mieć nic wspólnego z tym złowrogim bóstwem."
    ),
    "h5844527eg5bc7g6d08gb8bdg836fe861ad65": (
        "Odmieńcy, o nieustannie zmieniającym się wyglądzie, żyją nierozpoznani w wielu społecznościach. "
        "Każdy odmieniec może w nadnaturalny sposób przybrać dowolną twarz, jaką zechce. Dla niektórych "
        "odmieńców nowa twarz może ujawniać aspekt ich duszy."
    ),
    "h00779e8dg1144g5eecg3f98g33292e8dea42": (
        "Odmieńcy, o nieustannie zmieniającym się wyglądzie, żyją nierozpoznani w wielu społecznościach. "
        "Każdy odmieniec może w nadnaturalny sposób przybrać dowolną twarz, jaką zechce. Dla niektórych "
        "odmieńców nowa twarz może ujawniać aspekt ich duszy."
    ),
    "h2d809685g28ffge26ag3e6ag5fa20f63c9e3": (
        'Możesz korzystać z walki dwiema broniami, nawet jeśli twoja broń nie jest '
        '<LSTag Tooltip="Light">lekka</LSTag>. Nie możesz walczyć dwiema broniami, jeśli są one '
        '<LSTag Tooltip="TwoHanded">dwuręczne</LSTag>.<br><br>Gdy w swojej turze wykonasz akcję '
        'Ataku i zaatakujesz bronią do walki wręcz, możesz później w tej samej turze wykonać jeden '
        'atak drugą ręką w ramach akcji dodatkowej. Jeśli opanowałeś właściwość Nacięcie i trzymasz '
        'w drugiej ręce broń z tą właściwością, możesz wykonać do dwóch ataków drugą ręką na turę.'
    ),
    "h05ec7064ga697gdc69g5003g66e24f5cb04b": (
        "Cel otrzymuje dodatkowe 1k6 obrażeń od mocy. Jeśli cel jest stworzeniem, musi wykonać udany "
        "rzut obronny na Siłę; w przeciwnym razie zyskuje stan Powalenia."
    ),
    "h0e59eedfg13a0g2433g31c1g969915edce8d": (
        "Cel otrzymuje dodatkowe 1k6 obrażeń od zimna. Jeśli cel jest stworzeniem, musi wykonać udany "
        "rzut obronny na Kondycję; w przeciwnym razie jego szybkość spada do 0 do początku twojej następnej tury."
    ),
    "hc3df7c24g824ag06f4ge664geda5e80d2018": (
        "Cel otrzymuje dodatkowe 1k6 obrażeń od mocy. Jeśli cel jest stworzeniem, musi wykonać udany "
        "rzut obronny na Siłę; w przeciwnym razie zostaje odepchnięty od ciebie o 3 m w linii prostej."
    ),
    "hf81d0d50g810egc762gf156g017583f5ab0c": (
        "Cel otrzymuje dodatkowe 1k6 obrażeń od elektryczności. Jeśli cel jest stworzeniem, musi wykonać "
        "udany rzut obronny na Kondycję; w przeciwnym razie ma utrudnienie w testach ataku do początku "
        "twojej następnej tury."
    ),
    "h897e40eeg7135g851fg8143gc3ccb162516c": (
        "Cel otrzymuje dodatkowe 1k4 obrażeń od dźwięku. Stajesz się dla niego niewidzialny do początku "
        "twojej następnej tury albo do chwili bezpośrednio po wykonaniu testu ataku lub rzuceniu czaru."
    ),
    "h2c45092ag40cag1de6gb0cag6f5b529f8501": (
        "Możesz materializować połyskujące ostrza energii psychicznej.\n\nGdy dzierżysz sztylet, krótki miecz "
        'lub sejmitar, możesz zmienić typ obrażeń tej broni na psychiczne i nadać jej właściwość '
        '<LSTag Tooltip="Thrown">Rzucana</LSTag>.'
    ),
    "h35a0000fg8dc5g3af7ge6b5g3ad5700dd6e6": (
        "Możesz materializować połyskujące ostrza energii psychicznej.\n\nGdy dzierżysz sztylet, krótki miecz "
        'lub sejmitar, możesz zmienić typ obrażeń tej broni na psychiczne i nadać jej właściwość '
        '<LSTag Tooltip="Thrown">Rzucana</LSTag>.'
    ),
    "h07cec1a0g7220ge9ebg9676gffd755fa50d0": (
        "Wyczyn: Wieża Purpurowego Smoka\n\nPoświęciłeś życie bezpieczeństwu Cormyru i starałeś "
        "się o przyjęcie do elitarnego zakonu wojowników tego królestwa — Rycerzy Purpurowego Smoka. "
        "Zanim jednak oficjalnie do nich dołączysz, musisz najpierw służyć jako giermek. Znalazłeś "
        "seniora gotowego przyjąć cię na służbę i nauczyć zwyczajów zakonu. Czy dochowasz ideałów "
        "Rycerzy Purpurowego Smoka — chwały, honoru i siły — oraz dowiedziesz, że zasługujesz na "
        'pasowanie?\n\nProśba. Zyskujesz biegłość w <LSTag Type="Skills" Tooltip="Persuasion">Perswazji'
        '</LSTag>.\n\nOkrzyk zagrzewający. Możesz wybrać widoczne stworzenia w promieniu 9 m od siebie, '
        "w liczbie równej twojej premii z biegłości. Wybrane stworzenia zyskują Bohaterską inspirację. "
        "Po użyciu tej korzyści możesz użyć jej ponownie dopiero po długim odpoczynku."
    ),
    "hf2f81938g5ca0gb0eega680g3ec73dd11dd8": (
        'Prośba. Zyskujesz biegłość w <LSTag Type="Skills" Tooltip="Persuasion">Perswazji</LSTag>.\n\n'
        "Okrzyk zagrzewający. Możesz wybrać widoczne stworzenia w promieniu 9 m od siebie, w liczbie "
        "równej twojej premii z biegłości. Wybrane stworzenia zyskują Bohaterską inspirację. Po użyciu "
        "tej korzyści możesz użyć jej ponownie dopiero po długim odpoczynku."
    ),
    "h76a090b6gcb17g375dg822fgdf79bae4b00a": (
        'Prośba. Zyskujesz biegłość w <LSTag Type="Skills" Tooltip="Persuasion">Perswazji</LSTag>.\n\n'
        "Okrzyk zagrzewający. Możesz wybrać widoczne stworzenia w promieniu 9 m od siebie, w liczbie "
        "równej twojej premii z biegłości. Wybrane stworzenia zyskują "
        '<LSTag Type="Status" Tooltip="HEROIC_INSPIRATION_TEMP">Bohaterską inspirację</LSTag>. Po '
        "użyciu tej korzyści możesz użyć jej ponownie dopiero po długim odpoczynku."
    ),
    "h17794a45gbffdg8b0dg0332g414e8cee0aa7": (
        "Aasimar (wymawiane AH-sih-mar) to śmiertelnicy, którzy noszą w swoich duszach iskrę Wyższych "
        "Planów. Niezależnie od tego, czy pochodzą od anielskiej istoty, czy są nasyceni mocą "
        "Niebianina, potrafią rozniecić tę iskrę, aby nieść światło, uzdrawiać i wyzwalać niebiański "
        "gniew.\n\nAasimar mogą pojawić się wśród każdej populacji śmiertelników. Przypominają swoich "
        "rodziców, jednak żyją nawet do 160 lat i posiadają cechy zdradzające ich niebiańskie dziedzictwo, "
        "takie jak metaliczne piegi, świetliste oczy, aureolę lub kolor skóry anioła (srebrny, opalizujący "
        "zielony bądź miedzianoczerwony). Cechy te początkowo są subtelne, a stają się bardziej oczywiste, "
        "gdy aasimar nauczy się w pełni ukazywać swoją anielską naturę."
    ),
    "hce976d1agab7cg7729g705eged5dfe8fa201": (
        "Aasimar (wymawiane AH-sih-mar) to śmiertelnicy, którzy noszą w swoich duszach iskrę Wyższych "
        "Planów. Niezależnie od tego, czy pochodzą od anielskiej istoty, czy są nasyceni mocą "
        "Niebianina, potrafią rozniecić tę iskrę, aby nieść światło, uzdrawiać i wyzwalać niebiański "
        "gniew.\n\nAasimar mogą pojawić się wśród każdej populacji śmiertelników. Przypominają swoich "
        "rodziców, jednak żyją nawet do 160 lat i posiadają cechy zdradzające ich niebiańskie dziedzictwo, "
        "takie jak metaliczne piegi, świetliste oczy, aureolę lub kolor skóry anioła (srebrny, opalizujący "
        "zielony bądź miedzianoczerwony). Cechy te początkowo są subtelne, a stają się bardziej oczywiste, "
        "gdy aasimar nauczy się w pełni ukazywać swoją anielską naturę."
    ),
    "h2d86c838g5e8cg8763gdf9bgaeb1290ded87": (
        'Masz <LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="SavingThrow">rzutach obronnych</LSTag> wykonywanych, by utrzymać '
        '<LSTag Tooltip="Concentration">koncentrację</LSTag> na czarze.\n\nW ramach '
        '<LSTag Type="ActionResource" Tooltip="ReactionActionPoint">reakcji</LSTag> możesz rzucić '
        '<LSTag Type="Spell" Tooltip="Target_ShockingGrasp">Porażający uścisk</LSTag> na cel '
        "opuszczający twój zasięg walki wręcz."
    ),
    "haea51e98gfb73g894eg965bg2978e243f5e4": (
        'Masz <LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="SavingThrow">rzutach obronnych</LSTag> wykonywanych, by utrzymać '
        '<LSTag Tooltip="Concentration">koncentrację</LSTag> na czarze.\n\nMożesz również w ramach '
        '<LSTag Type="ActionResource" Tooltip="ReactionActionPoint">reakcji</LSTag> rzucić '
        '<LSTag Type="Spell" Tooltip="Target_ShockingGrasp">Porażający uścisk</LSTag> na cel '
        "opuszczający twój zasięg walki wręcz."
    ),
    "h2f5f424bg14ceg447ag33b9g312025e7738d": (
        'Zadaje dodatkowe [1] obrażeń bronią do walki wręcz, bronią improwizowaną i rzucanymi '
        'przedmiotami. <br><br>Sojusznicy mają <LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="AttackRoll">testach ataku</LSTag> przeciwko przeciwnikom w obrębie [2].'
        '<br><br>Ma również odporność na obrażenia fizyczne oraz ułatwienie w testach Siły '
        '<LSTag Tooltip="AbilityCheck">cechy</LSTag> i <LSTag Tooltip="SavingThrow">rzutach obronnych'
        '</LSTag> na Siłę.<br><br>Nie może rzucać czarów ani utrzymywać koncentracji.'
    ),
    "h708146b3g1fd7g7ca1g06e9g815f4a5e342b": (
        'Zadaje dodatkowe [1] obrażeń bronią do walki wręcz, bronią improwizowaną i rzucanymi '
        'przedmiotami. <br><br>Sojusznicy mają <LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="AttackRoll">testach ataku</LSTag> przeciwko przeciwnikom w obrębie [2].'
        '<br><br>Ma również odporność na obrażenia fizyczne oraz ułatwienie w testach Siły '
        '<LSTag Tooltip="AbilityCheck">cechy</LSTag> i <LSTag Tooltip="SavingThrow">rzutach obronnych'
        '</LSTag> na Siłę.<br><br>Nie może rzucać czarów ani utrzymywać koncentracji.'
    ),
    "h3f4c0be2gf28cg9925g8be8g0c8a747faf6e": (
        'Możesz używać <LSTag Type="Spell" Tooltip="Shout_PackHowl_Barbarian">Pobudzającego wycia'
        '</LSTag>, a twoi sojusznicy mają <LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="AttackRoll">testach ataku</LSTag> przeciwko przeciwnikom w obrębie [1] od ciebie.'
    ),
    "h4b29ebdegfa87g42bege4a2g3b10f7973640": (
        'Gdy Moloch przyjmie cię jako swojego illriggera, zyskujesz <LSTag Tooltip="Expertise">'
        'ekspertyzę</LSTag> w <LSTag Tooltip="AbilityCheck">testach</LSTag> '
        '<LSTag Type="Skills" Tooltip="Persuasion">Perswazji</LSTag> i '
        '<LSTag Type="Skills" Tooltip="Deception">Oszustwa</LSTag>.'
    ),
    "hb052fe34g86bfg992cg2672g146c445e9dc4": (
        'Gdy Moloch przyjmie cię jako swojego illriggera, zyskujesz <LSTag Tooltip="Expertise">'
        'ekspertyzę</LSTag> w <LSTag Tooltip="AbilityCheck">testach</LSTag> '
        '<LSTag Type="Skills" Tooltip="Persuasion">Perswazji</LSTag> i '
        '<LSTag Type="Skills" Tooltip="Deception">Oszustwa</LSTag>.'
    ),
    "h5cc8709eg0974gcec1g323cg0a299d48a147": (
        'Masz <LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> <LSTag Type="Skills" Tooltip="Perception">'
        'Percepcji</LSTag> wykonywanych, aby wykrywać ukryte przedmioty.\n\nMasz '
        '<LSTag Tooltip="Advantage">ułatwienie</LSTag> w <LSTag Tooltip="SavingThrow">rzutach '
        'obronnych</LSTag> wykonywanych, by unikać pułapek, oraz <LSTag Tooltip="Resistant">odporność'
        '</LSTag> na obrażenia od pułapek.\n\nWidzisz w ciemności na odległość do [1].'
    ),
    "h9dd8a551g9f01g98dbg64f1ga485e59f0e9d": (
        'Zyskujesz <LSTag Tooltip="Advantage">ułatwienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> <LSTag Type="Skills" Tooltip="Perception">'
        'Percepcji</LSTag> wykonywanych, aby wykrywać ukryte przedmioty, oraz w '
        '<LSTag Tooltip="SavingThrow">rzutach obronnych</LSTag> wykonywanych, aby unikać pułapek lub '
        'opierać się ich efektom.\n\nZyskujesz <LSTag Tooltip="Resistant">odporność</LSTag> na '
        'obrażenia zadawane przez pułapki.\n\nWidzisz w ciemności.'
    ),
    "hfc88b2cagdfdcg7342gecebg306e2918ed9e": (
        'Znajduje się w pobliżu barbarzyńcy w szale z Wilczym Sercem. <br><br>Sojusznicy barbarzyńcy '
        'mają <LSTag Tooltip="Advantage">ułatwienie</LSTag> w <LSTag Tooltip="AttackRoll">testach '
        'ataku</LSTag> przeciwko tej istocie.'
    ),
    "h9cbc738dgd21bg77f4g2687gd1ac412ca2b4": (
        "Ciskasz drobiną światła w wybraną istotę lub obiekt w zasięgu. Wykonaj przeciwko celowi "
        "dystansowy test ataku czarem. Przy trafieniu cel otrzymuje obrażenia od światłości, a do końca "
        "twojej następnej tury emituje słabe światło w promieniu [1] i nie może korzystać ze stanu "
        '<LSTag Type="Status" Tooltip="INVISIBLE">niewidzialności</LSTag>.'
    ),
    "h3bb523e2gc26eg22c2g87e9g4e1e0da5e1af": (
        'Twój Grad ciosów, <LSTag Type="Spell" Tooltip="Shout_PatientDefense">Cierpliwa obrona</LSTag> '
        "i Krok w powietrzu zyskują następujące korzyści:\n\nGrad ciosów. Możesz wydać 1 punkt "
        "skupienia, aby użyć Gradu ciosów i wykonać trzy ataki bez broni zamiast dwóch.\n\nCierpliwa "
        "obrona i Krok w powietrzu. Gdy wydajesz punkt skupienia, aby użyć którejkolwiek z tych "
        "zdolności, zyskujesz tymczasowe punkty wytrzymałości w liczbie równej wynikowi dwóch rzutów "
        "kością sztuk walki."
    ),
    "hc41356d2g2208g0d0fg0023g8a9c6958aaac": (
        "Magia twojej przysięgi sprawia, że zawsze masz pod ręką określone czary. Po osiągnięciu poziomów "
        "paladyna wskazanych w tabeli Czarów Przysięgi Chwały masz odtąd zawsze przygotowane następujące "
        "czary: na 3. poziomie — Pocisk wiodący i Heroizm; na 5. poziomie — Wzmocnienie cechy i Magiczna "
        'broń; a na 9. poziomie — <LSTag Type="Spell" Tooltip="Target_Haste">Przyspieszenie</LSTag> i '
        "Ochrona przed energią."
    ),
    "h4aa07c08gb93egab88g61e1g0ced3d3207e0": (
        "Gdy rzucasz dowolny czar 1. lub wyższego poziomu pochodzący ze zdolności Psioniczne czary, "
        "możesz jak zwykle zużyć komórkę czaru albo wydać liczbę punktów zaklinania równą poziomowi "
        "czaru. Czar rzucony za punkty zaklinania nie wymaga komponentów werbalnych ani somatycznych. "
        "Nie wymaga też komponentów materialnych, chyba że czar je zużywa lub określa ich koszt."
    ),
    "hc00e6ea9gfd5egcff2g4900g073fd4c5bd3f": (
        "Spalasz wszystkie pieczęcie nałożone przez ciebie na istotę. Za każdą spaloną pieczęć zadajesz "
        "jej 1k6 obrażeń od ognia albo obrażeń nekrotycznych (wedle twojego wyboru). Spalona pieczęć "
        "natychmiast znika.\n\nPo osiągnięciu 5. poziomu tej klasy twoja więź z arcydiabłem się wzmacnia. "
        "Każda spalona pieczęć zadaje dodatkowe 1k6 obrażeń, łącznie 2k6 za pieczęć. Po osiągnięciu "
        "10. poziomu obrażenia każdej pieczęci wzrastają o kolejne 1k6, łącznie do 3k6 za pieczęć."
    ),
    "h3210721bg910cg6d5egf7e0gace10faa1161": (
        'Zyskano 12 <LSTag Tooltip="TemporaryHitPoints">tymczasowych punktów wytrzymałości</LSTag>.'
    ),
    "h6d9021a0gb82bgbcb8ge41bgbb23b222a400": (
        'Szarżuj do przodu, mogąc <LSTag Type="Status" Tooltip="PRONE">powalić</LSTag> cel.'
    ),
    "hae58b170g1a86g562dg9c15gc5a91fb03fe1": (
        '<LSTag Tooltip="Resistant">Odporność</LSTag> na obrażenia od czarów rzucanych w promieniu '
        '[1] od paladyna.'
    ),
    "hc78792c5gf4b3g8f75gc78fge4e46626954f": (
        "Rozumiesz potęgę ciosu wyprowadzanego z cienia. Raz na turę, gdy trafisz istotę naznaczoną "
        "pieczęcią atakiem bronią do walki wręcz i masz ułatwienie w teście ataku, możesz rzucić tyloma "
        "kośćmi k4, ile wynosi twoja premia z biegłości, i zadać dodatkowe obrażenia równe sumie wyników."
    ),
    "h2a979e60g8047g338bg7d21g17a10ae143c0": (
        "Rozumiesz potęgę ciosu wyprowadzanego z cienia. Raz na turę, gdy trafisz istotę naznaczoną "
        "pieczęcią atakiem bronią do walki wręcz i masz ułatwienie w teście ataku, możesz rzucić tyloma "
        "kośćmi k4, ile wynosi twoja premia z biegłości, i zadać dodatkowe obrażenia równe sumie wyników."
    ),
    "he41177dagaf29g13c8gc756g66414bcb409d": (
        "Studiowanie obrzędów pogrzebowych i troska o spoczynek zmarłych uczyniły z ciebie pośrednika "
        "między światem żywych i umarłych. Zyskujesz następujące korzyści.\n\nBoski kanał. Zyskujesz "
        "jedno użycie zdolności Akt wiary klasy kleryka i możesz dzięki niemu wywołać efekt Odpędzanie "
        "nieumarłych. Jeśli masz już Akt wiary, dodajesz to użycie do zdolności jednej wybranej klasy."
    ),
    "h894a8c5dg5c28g7d23gb198gb51499628687": (
        "Studiowanie obrzędów pogrzebowych i troska o spoczynek zmarłych uczyniły z ciebie pośrednika "
        "między światem żywych i umarłych. Zyskujesz następujące korzyści.\n\nBoski kanał. Zyskujesz "
        "jedno użycie zdolności Akt wiary klasy kleryka i możesz dzięki niemu wywołać efekt Odpędzanie "
        "nieumarłych. Jeśli masz już Akt wiary, dodajesz to użycie do zdolności jednej wybranej klasy."
    ),
    "h7d405f4ag1770gee29gfd7egc0479b1be286": (
        "Atut: Strażnik grobu\n\nW miejscu bliższym krainie umarłych niż żywych osoby dbające o "
        "wieczny spoczynek i pochówek zmarłych budzą zarówno głęboki szacunek, jak i lęk. Parałeś się "
        "pracą grabarza, pracownika zakładu pogrzebowego i balsamisty. Niekiedy tylko ty znalazłeś dobre "
        "słowo dla uczczenia pamięci tych, którzy odeszli. Dobrze znasz spustoszenia dokonywane przez "
        "nieumarłych i nie pozwalasz im zakłócać spoczynku powierzonych ci zmarłych.\n\nStrażnik grobu. "
        "Zyskujesz jedno użycie zdolności Akt wiary klasy kleryka i możesz dzięki niemu wywołać efekt "
        "Odpędzanie nieumarłych. Jeśli masz już Akt wiary, dodajesz to użycie do zdolności jednej "
        "wybranej klasy."
    ),
    "h11ed03f2g16a9g0ee9g4b45g6c8ca4ac593d": (
        "Zimowi wędrowcy doskonalą swój kunszt w ponurej, skutej lodem dziczy miejsc takich jak Dolina "
        "Lodowego Wichru. Ci bezwzględni, oszronieni łowcy polują na potwory nawiedzające arktyczne "
        "pustkowia, aż w końcu sami stają się lodowatymi postrachami. Doskonale znają zjawiska "
        "charakterystyczne dla Doliny Lodowego Wichru, w tym utajoną magię upadłych miast Netheru, "
        "endemiczne potwory, takie jak yeti i koty skalne, oraz rosnące zagrożenie ze strony najeźdźców "
        "z Podmroku. Z powodu chłodnego pragmatyzmu, przerażającej magii i opanowania regionu budzą w "
        "równym stopniu szacunek i strach. Mieszkańcy Dziesięciu Miast mówią, że częste zetknięcie ze "
        "złowrogimi bytami daje zimowym wędrowcom ich budzące grozę moce. Wielu nomadów Reghed z kolei "
        "wierzy, że duchy natury obdarzają zimowych wędrowców wyjątkową klątwą."
    ),
    "h61b97fdcga929gadd6gfe5cgaff22e08890c": (
        "Drugi główny ród elfów Północnych Krain wędruje niewielkimi grupami przez tundrę i lodowe "
        "wzgórza Ponurej Przestrzeni, polując na karibu i mamuty z grzbietów reniferów oraz białofutrych "
        "tygrysów szablozębnych. Lodowe elfy żyją zwykle w odosobnieniu i są zaciekle samowystarczalne. "
        "Zyskały przez to opinię skrytych, choć w rzeczywistości po prostu niewiele obchodzi je szerszy "
        "świat. Nie oczekują pomocy od obcych ani nie są też skłonne jej udzielać. Czasami są jednak "
        "gotowe handlować z ludźmi, krasnoludami i trollkinami. Wbrew przekonaniom niedoinformowanych "
        "przybyszów tylko nieliczne społeczności lodowych elfów czczą Boreasa i wypełniają jego wolę; "
        "większość nie chce mieć nic wspólnego z tym złowrogim bóstwem."
    ),
    "h200d6e32g6f1cge25cg2d27g8bab65f46465": (
        "W każdej swojej turze możesz użyć akcji, aby automatycznie zadać celowi [1] obrażeń nekrotycznych."
    ),
    "h0680f65eg2944g3595ga9d1gc7b9d923668f": (
        "Wyciągasz ku widocznej istocie w zasięgu mackę atramentowej ciemności, która wysysa z niej "
        "życie. Cel musi wykonać rzut obronny na Zręczność. W razie powodzenia otrzymuje [1] obrażeń "
        "nekrotycznych, a czar się kończy. W razie niepowodzenia otrzymuje [2] obrażeń nekrotycznych, "
        "a do zakończenia czaru w każdej swojej turze możesz użyć akcji, aby automatycznie zadać mu "
        "4k8 obrażeń nekrotycznych. Czar kończy się, jeśli użyjesz akcji do zrobienia czegokolwiek "
        "innego, cel znajdzie się poza zasięgiem czaru albo uzyska względem ciebie całkowitą osłonę.\n\n"
        "Za każdym razem, gdy czar zadaje celowi obrażenia, odzyskujesz punkty wytrzymałości w liczbie "
        "równej połowie otrzymanych przez niego obrażeń nekrotycznych."
    ),
    "hc6f8b2cdg61f9g10e0g8f71g1e3b9ec13c29": (
        "Gdy zadajesz istocie obrażenia z Ataku z ukrycia, możesz zdecydować, że użyte w nim kości k6 "
        "zostaną zastąpione kośćmi k8, a atak zada obrażenia od trucizny zamiast obrażeń typu "
        "zadawanego przez broń."
    ),
    "hf1e041c0ga156g608cg02dfg22c1dad1bf3a": (
        "Uśmierzacze, ciężkozbrojni żołnierze śmierci z Piekła, służą Dispaterowi i prowadzą natarcia "
        "we wszystkich większych piekielnych bitwach.\n\nDispater włada Dis, Miastem Wojny. Gdy Piekło "
        "najeżdża inny świat, to armia Dispatera walczy i ginie. Jego Uśmierzacze są mistrzami strategii, "
        "którzy dowodzą z pierwszej linii, wzbudzając w żołnierzach grozę i podziw. Są władczy, pełni "
        "dumy i pychy, a często wręcz obsesyjnie dbają o wygląd.\n\nChoć należą do najbardziej rycerskich "
        "illriggerów, ich waleczność jest wypaczona. Przyjmują i honorują wyzwania do pojedynku oraz "
        "szybko karzą każdego, kto próbuje się wtrącić. Kiedy jednak przegrywają, nie wahają się oszukiwać; "
        "kiedy zaś wygrywają, arogancko igrają z przeciwnikiem, zanim go wykończą.\n\nW chwili słabości "
        "lub desperacji władca innego świata może ujrzeć nieuchronną klęskę swej armii i wezwać Dispatera. "
        "Zawsze skory do siania konfliktu i niezgody, Dispater często odpowiada na takie prośby, wysyłając "
        "Uśmierzacza, by poprowadził wojska zdesperowanego władcy."
    ),
    "h1594d7ffge703g7b01g1f9bg2776670f8c1f": (
        "Fortuna bywa kapryśna — chyba że jesteś Hazardzistą. Ci rewolwerowcy są mistrzami kart i "
        "kości, którzy łączą zamiłowanie do ryzyka z talentem strzeleckim. Wykorzystują szczęście do "
        "ostatniej kropli, a gdy go zabraknie, podbijają stawkę jeszcze wyżej. Po co zadowalać się "
        "zwycięstwem, skoro można postawić wszystko i zgarnąć główną wygraną?"
    ),
    "h6ea1c6eag9b3dg7479ge12cgb52dd829b0da": (
        "Chorążowie są wzorami męstwa i przywództwa, którzy chronią niewinnych i mobilizują innych "
        "poszukiwaczy przygód do walki w imię sprawiedliwości i wolności. Wielu z nich to rycerze "
        "służący w Cormyrze, Srebrnych Marchiach, Damarze, Chessencie lub innych krainach Faerûnu. "
        "Przemierzają krainy jako błędni rycerze, przenosząc walkę ze złem poza granice swojego "
        "królestwa.\n\nChorąży polega na rozsądku, odwadze i wierności kodeksowi rycerskiemu, które "
        "kierują nim w walce ze złoczyńcami. Samotny chorąży jest wykwalifikowanym wojownikiem, ale "
        "dowodząc grupą sojuszników, potrafi przekształcić nawet słabo wyposażoną milicję w zaciekły "
        "oddział bojowy."
    ),
    "hc52cd33bg7738g4b5eg085dgfcbe54464a64": (
        "Atut: Szczęście\n\nMythale są źródłami potężnej magii, zdolnej zmieniać Splot, a nawet samą "
        "naturę rzeczywistości. Większość z nich została stworzona w zamierzchłych czasach, a wiele od "
        "tamtej pory uległo uszkodzeniu lub zapadło w uśpienie. Jako kustosz mythalu z Dalelands twoje "
        "pierwsze zetknięcie z mythalem prawdopodobnie miało miejsce w ruinach Myth Drannoru. Wędrujesz "
        "po Faerûnie w poszukiwaniu innych zrujnowanych miejsc mocy, pragnąc zgłębić historię i potęgę "
        "mythali — a może nawet przywrócić do działania jeden z uszkodzonych."
    ),
    "h7e916fa3g95c4g0367g8918g7dd56be199a8": (
        "Wędrowiec feyskich ścieżek. Gdy w swojej turze wykonujesz akcję Odstąpienia, trudny teren do "
        "końca tej tury nie kosztuje cię dodatkowego ruchu.\n\nPeszące uderzenie. Gdy trafisz istotę "
        "testem ataku, możesz spróbować ją speszyć. Cel musi wykonać udany rzut obronny na Mądrość "
        "(ST 8 + modyfikator cechy zwiększonej przez ten atut + twoja premia z biegłości); w razie "
        "niepowodzenia ma utrudnienie w rzutach obronnych do końca twojej następnej tury.\n\nMożesz "
        "skorzystać z tej korzyści tyle razy, ile wynosi twoja premia z biegłości, a wszystkie zużyte "
        "użycia odzyskujesz po długim odpoczynku."
    ),
    "h978a3ea0g73c2gc59cgc52eg4aecbaa53dae": (
        "Wędrowiec feyskich ścieżek. Gdy w swojej turze wykonujesz akcję Odstąpienia, trudny teren do "
        "końca tej tury nie kosztuje cię dodatkowego ruchu.\n\nPeszące uderzenie. Gdy trafisz istotę "
        "testem ataku, możesz spróbować ją speszyć. Cel musi wykonać udany rzut obronny na Mądrość "
        "(ST 8 + modyfikator cechy zwiększonej przez ten atut + twoja premia z biegłości); w razie "
        "niepowodzenia ma utrudnienie w rzutach obronnych do końca twojej następnej tury.\n\nMożesz "
        "skorzystać z tej korzyści tyle razy, ile wynosi twoja premia z biegłości, a wszystkie zużyte "
        "użycia odzyskujesz po długim odpoczynku."
    ),
    "h9200202eg02d1g77b7gd08cgcdd8fe5b794f": (
        "Twoje testy ataku bronią dystansową kończą się trafieniem krytycznym przy wyniku 19 albo 20 "
        "na k20.\n\nNa 9. poziomie rewolwerowca ataki bronią dystansową kończą się trafieniem krytycznym "
        "przy wyniku 18–20."
    ),
    "hf88019fag13a2g173ege79egebe738b8ee20": (
        "Twoje testy ataku bronią dystansową kończą się trafieniem krytycznym przy wyniku 19 albo 20 "
        "na k20.\n\nNa 9. poziomie rewolwerowca ataki bronią dystansową kończą się trafieniem krytycznym "
        "przy wyniku 18–20."
    ),
    "hdeab958dge913gf95bg123dg27338a365d6d": (
        "Atut: Oprych Zhentarimów\n\nMoże potrzebowałeś pieniędzy. Może tęskniłeś za rodziną, choćby "
        "najbardziej podejrzaną. A może po prostu umiesz doprowadzić robotę do końca wszelkimi "
        "niezbędnymi środkami. Bez względu na powód wstąpiłeś do Zhentarimów, najsłynniejszej gildii "
        "najemników w Krainach. Choć jej przywódcy twierdzą, że organizacja bardziej przypomina rodzinę "
        "niż tajny syndykat, niewiele rodzin dorównuje jej pod względem nieuczciwości, nepotyzmu i "
        "korupcji. Doskonaliłeś spryt, refleks i władanie ostrzem, aby piąć się w szeregach gildii.\n\n"
        "Wykorzystanie luki. Gdy wykonujesz rzut obrażeń ataku okazyjnego, możesz rzucić kośćmi obrażeń "
        "dwukrotnie i wybrać jeden z wyników.\n\nRodzina przede wszystkim. Raz na długi odpoczynek "
        "zapewniasz sobie i sojusznikom w promieniu 9 m ułatwienie w testach inicjatywy."
    ),
}

UID_OVERRIDES.update({
    "h761a2d1bgfaa4g6c2fgbda3g198675b6a886": (
        "Opanowałeś sztukę zastawiania przerażających zasadzek, co zapewnia ci następujące korzyści.\n\n"
        "Zryw z zasadzki. Na początku pierwszej tury każdej walki twoja szybkość zwiększa się o [1] "
        "do końca tej tury.\n\n"
        "Przerażające uderzenie. Gdy trafisz istotę atakiem bronią, możesz zadać jej dodatkowe [2]. "
        "Z tej korzyści możesz skorzystać tylko raz na turę i tyle razy, ile wynosi twój modyfikator "
        "Mądrości (minimum raz). Wszystkie zużyte użycia odzyskujesz po długim odpoczynku.\n\n"
        "Premia do inicjatywy. Gdy wykonujesz test inicjatywy, możesz dodać do niego swój modyfikator Mądrości."
    ),
    "h3757893egada1gdcfdgf81egfaecbf54b4e4": (
        "Możesz dostosować swoją magiczną zbroję. Wybierz jeden z następujących modeli: Drednot, "
        "Strażnik albo Infiltrator. Wybrany model zapewnia ci szczególne korzyści, gdy nosisz tę zbroję.\n\n"
        "Każdy model obejmuje specjalną broń. Gdy nią atakujesz, możesz używać modyfikatora Inteligencji "
        "zamiast modyfikatora Siły lub Zręczności w testach ataku i rzutach obrażeń."
    ),
    "hcc906553g972bg8298gd9cfga6a42e0fdb7c": (
        "Możesz dostosować swoją magiczną zbroję. Wybierz jeden z następujących modeli: Drednot, "
        "Strażnik albo Infiltrator. Wybrany model zapewnia ci szczególne korzyści, gdy nosisz tę zbroję.\n\n"
        "Każdy model obejmuje specjalną broń. Gdy nią atakujesz, możesz używać modyfikatora Inteligencji "
        "zamiast modyfikatora Siły lub Zręczności w testach ataku i rzutach obrażeń."
    ),
    "h4d24d172g9754g69f8g404agfcebc39ded6a": (
        "Na 3. poziomie zyskujesz zdolność Czary zimowego wędrowca. Magia twojej ścieżki sprawia, "
        "że zawsze masz przygotowane określone czary. Na 3. poziomie jest to Lodowy nóż, "
        "na 5. poziomie — Unieruchomienie osoby, a na 9. poziomie — Zdjęcie klątwy."
    ),
    "h434df1f3gdadag1149g4c36g6bfc2c7a1bec": (
        "Po osiągnięciu określonych poziomów kleryka zawsze masz przygotowane następujące czary: "
        "na 3. poziomie — Blask faerie, Uśpienie, Księżycowy promień i Widzenie niewidzialnego; "
        "na 5. poziomie — Aura witalności i Uderzenie pustki; na 7. poziomie — Swoboda poruszania się i "
        '<LSTag Type="Spell" Tooltip="Target_Invisibility_Greater">Większa niewidzialność</LSTag>; '
        "a na 9. poziomie — Krąg mocy i Świt. Czary te nie wliczają się do liczby czarów, które możesz przygotować."
    ),
    "h1944ab59g9198g6ac4gba4ag5a0efe856cbb": (
        'Przywołaj czarnego niedźwiedzia, który rozszarpuje wrogów '
        '<LSTag Type="Spell" Tooltip="Target_Claws_Bear_Black_Summon">Pazurami</LSTag> i powala ich '
        '<LSTag Type="Spell" Tooltip="Rush_Rush_Boar_Summon">Szarżą</LSTag>.'
    ),
    "h6827c922gd910gca98gee99gdbd9b0f178b1": (
        'Przybierz postać głębokiego rothé, które rzuca '
        '<LSTag Type="Spell" Tooltip="Target_DancingLights">Tańczące światła</LSTag> i atakuje wrogów '
        '<LSTag Type="Spell" Tooltip="Rush_Rush_DeepRothe">Szarżą</LSTag>.'
    ),
    "hbd1c29f3g9d49g7f6bgd0f5g7628a41aeced": (
        'Przywołaj groźnego kruka, który potrafi latać i atakować wrogów '
        '<LSTag Type="Spell" Tooltip="Target_Beak_Raven_Summon_BeastMaster">Dziobem</LSTag>. '
        'Gdy wylatuje poza zasięg wroga, nie prowokuje '
        '<LSTag Tooltip="OpportunityAttack">ataków okazyjnych</LSTag>.'
    ),
    "hf051b82fgb193ga37bg540ege6200dcbd93e": (
        "Zamiast broni możesz używać magii.\n\n"
        "Pistolety z palców. Poznajesz sztuczkę Pistolety z palców.\n\n"
        "Magiczny strzał. Gdy trafisz cel atakiem Pistoletów z palców, możesz zużyć jedną kość ryzyka "
        "i dodać jej wynik do rzutu obrażeń."
    ),
    "ha92a78f3ge96agd47egb8ddg6ad716d3cc56": (
        "Klątwa Hexblade’a. Możesz rzucić Urok bez zużywania komórki czaru tyle razy, ile wynosi twój "
        "modyfikator Charyzmy (minimum raz), a wszystkie zużyte użycia odzyskujesz po długim odpoczynku. "
        "Gdy rzucasz Urok, widmowa broń przypominająca twojego patrona zaczyna krążyć wokół przeklętego celu.\n\n"
        "Manewry Hexblade’a. Raz na turę, gdy trafisz atakiem cel objęty twoim Urokiem, możesz wywołać jeden "
        "z następujących dodatkowych efektów:\n\nWysysające cięcie, Dręczące ostrze, Hamujące piętno"
    ),
    "hb2925e5dgb422g689cgfe37g45413ec054f1": (
        "Upadek wzgórza (olbrzym wzgórzowy). Gdy trafisz atakiem istotę rozmiaru dużego lub mniejszego "
        "i zadasz jej obrażenia, możesz nadać jej stan Powalenia."
    ),
    "h69a470cbg07f2g82ddg9603g8091c23a6a5a": (
        "Gdy używasz Złowrogiego zakazu, aby nałożyć lub spalić pieczęć, jego zasięg wynosi 18 m zamiast 9 m. "
        "Gdy na 6. poziomie zyskasz zdolność Piekielne przewodzenie, jej zasięg wynosi 9 m zamiast dotyku.\n\n"
        "Ponadto wykonywanie ataku dystansowego w promieniu 1,5 m od wrogiej istoty nie nakłada utrudnienia "
        "na twój test ataku."
    ),
    "h2fdc2689g1529ge2b4gd969g4df570df4ae6": (
        "Wynalazcy są mistrzami wynalazczości. Za pomocą pomysłowości i magii wydobywają z przedmiotów "
        "niezwykłe możliwości. Postrzegają magię jako złożony system, który można rozszyfrować, a następnie "
        "wykorzystać w czarach i wynalazkach."
    ),
    "h64879c2eg307fgbb40gef3egfe67041bc0cf": (
        "Po każdym długim odpoczynku, jeśli masz przy sobie przybory alchemika, możesz za ich pomocą "
        "magicznie stworzyć dwa eliksiry.\n\n"
        "Tworzenie dodatkowych eliksirów. Możesz zużyć jedną komórkę czaru, aby stworzyć kolejny eliksir.\n\n"
        "Po osiągnięciu określonych poziomów wynalazcy tworzysz po każdym długim odpoczynku dodatkowy "
        "eliksir: łącznie trzy na 5. poziomie i cztery na 9. poziomie."
    ),
    "h7ac02ad8g0798gdcabg9abag78fd5b57ba92": (
        "Kawalerzysta doskonale radzi sobie w walce konnej. Zwykle pochodzi ze szlachty i wychowuje się na "
        "dworze, dlatego równie swobodnie prowadzi szarżę kawalerii, jak wymienia cięte riposty podczas "
        "oficjalnej kolacji. Kawalerzyści uczą się również chronić powierzonych im ludzi i często służą jako "
        "obrońcy przełożonych oraz słabszych. Wielu z nich porzuca wygodne życie i wyrusza na chwalebną "
        "przygodę, aby naprawiać krzywdy albo zdobyć sławę."
    ),
    "h974a5e6ag1e52gc326gd4b2g92e4681ec152": (
        "Ten czar jest technicznym wpisem bez żadnego działania. Podczas wybierania czaru dodawanego do księgi "
        "za pomocą zdolności Erudyta maga awans nie może zostać ukończony, jeśli wszystkie dostępne czary zostały "
        "już poznane w inny sposób, na przykład przez przepisywanie zwojów, i nie pozostał żaden możliwy wybór. "
        "Ten wpis dodano jako obejście takiej sytuacji."
    ),
    "h99239365g1e0eg35cfgc2edg0a2bbfb668ae": (
        'Istota otrzymuje od rzucającego dodatkowe [1]. Ma również '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach</LSTag> Charyzmy i '
        '<LSTag Tooltip="SavingThrow">rzutach obronnych</LSTag> na Charyzmę.'
    ),
    "h6fbb1933ge0e0gc26ag9144gcde944d43651": (
        "W ramach akcji magicznej unosisz święty symbol i zużywasz jedno użycie Aktu wiary, wywołując błysk "
        "światła w emanacji o promieniu 9 m. Każda magiczna Ciemność na tym obszarze, na przykład stworzona "
        "czarem Ciemność, zostaje rozproszona. Ponadto każda wybrana przez ciebie istota na tym obszarze wykonuje "
        "rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje 2k10 plus twój poziom kleryka obrażeń od światłości, "
        "a przy powodzeniu połowę tej wartości."
    ),
    "h6a7e8dbfg5edcgcfebgef9bgb58dbe804543": (
        "Możesz zużyć 2 punkty boskości, aby przywołać promienne ostrza w linii o długości 13,5 m i szerokości "
        "1,5 m. Każda istota w tej linii wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia "
        "od światłości równe obrażeniom twojego Ataku z ukrycia, a przy powodzeniu połowę tej wartości."
    ),
    "hda73ee14g5c7dg9f17g063dg92a87621426e": (
        "Możesz zużyć 2 punkty boskości, aby przywołać promienne ostrza w linii o długości 13,5 m i szerokości "
        "1,5 m. Każda istota w tej linii wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia "
        "od światłości równe obrażeniom twojego Ataku z ukrycia, a przy powodzeniu połowę tej wartości."
    ),
    "hed352d94g7b9dg3b87g2d2bgb0b679111113": (
        "Przy trafieniu istnieje szansa na nałożenie stanu Płonięcia. Płonącym celom zadaje dodatkowe [1]."
    ),
    "hd61761e0gbebfg6542gac8bgd70ab3faa548": (
        "Raz na turę, gdy trafisz istotę atakiem bronią, możesz zadać jej dodatkowe 1k8 obrażeń nekrotycznych."
    ),
    "h974a5e6ag1e52gc326gd4b2g92e4681ec152": (
        "Ten czar jest technicznym wpisem bez żadnego działania. Gdy za pomocą zdolności Erudyta wybierasz "
        "czar dodawany do księgi, nie można ukończyć awansu, jeśli wszystkie dostępne czary zostały już "
        "poznane w inny sposób, na przykład przez przepisywanie zwojów, i nie pozostał żaden możliwy wybór. "
        "Ten wpis dodano jako obejście takiej sytuacji."
    ),
    "h5b4e785ag06afgf727gca99g7e0aa28facda": (
        'Omijanie osłony. Twoje <LSTag Tooltip="RangedWeaponAttack">ataki dystansowe bronią</LSTag> '
        'nie otrzymują kar wynikających z <LSTag Tooltip="HighGroundRules">zasad przewagi wysokości</LSTag>.\n\n'
        "Strzelanie w zwarciu. Obecność w promieniu 1,5 m od wroga nie nakłada utrudnienia na twoje "
        "testy ataku bronią dystansową.\n\n"
        "Dalekie strzały. Atakowanie dwuręczną bronią dystansową zwiększa jej normalny zasięg do 27 m."
    ),
    "hc4c144a0g2e9bg6166g297cg8829f3a2bd83": (
        "Boska istota pomaga ci pozostać w walce. Dysponujesz pulą czterech kości k12, które możesz zużywać, "
        "aby się leczyć. W ramach akcji dodatkowej możesz zużyć dowolną liczbę kości z puli, rzucić nimi i "
        "odzyskać punkty wytrzymałości w liczbie równej sumie wyników.\n\n"
        "Wszystkie zużyte kości odzyskujesz po długim odpoczynku.\n\n"
        "Maksymalna liczba kości w puli zwiększa się o jedną na 6. poziomie barbarzyńcy (5 kości), "
        "12. poziomie (6 kości) i 17. poziomie (7 kości)."
    ),
    "h5059c8f8g9435g5e50g19c7g899613e62b54": (
        "Boska istota pomaga ci pozostać w walce. Dysponujesz pulą czterech kości k12, które możesz zużywać, "
        "aby się leczyć."
    ),
    "h94d2b863gce81ge85ag20a9gd351c1d2fbe8": (
        "Możesz zużyć jedno użycie Przysięgi kanału i rozdzielić tymczasowe punkty wytrzymałości między "
        "wybrane istoty w promieniu 9 m od siebie, wliczając w to siebie. Łączna liczba tych punktów wynosi "
        "2k8 plus twój poziom paladyna; rozdzielasz je między wybrane istoty według własnego uznania."
    ),
    "hfd1bcc8cg898egba47gb579gfd786513a783": (
        '<LSTag Type="Status" Tooltip="CHARMED">Zaurocz</LSTag> atakującego cię wroga. Jeśli to możliwe, '
        "zaatakuje on inny cel."
    ),
    "h02d99bfegfef1g8e2dg60b7g277ac219dbc2": (
        "Znasz ludowe lekarstwa i klątwy przekazywane w naukach Dawnych Dróg oraz potrafisz nasycać nimi "
        "wyplatane przez siebie niewielkie wiklinowe amulety. Zyskujesz następujące korzyści.\n\n"
        "Zawsze masz przygotowane czary Błogosławieństwo i Urok. Ponadto zyskujesz jedną komórkę czaru "
        "1. poziomu, której możesz użyć do ich rzucenia."
    ),
    "hdb90b6a2g422eg0fbeg786dgb67c50e37043": (
        "Atut: Tkacz amuletów\n\n"
        "Znasz pradawne rytuały podtrzymywane przez skrytych druidów i wiejskich znachorów w cienistych "
        "gajach pierwotnych lasów. Lekarstwa i klątwy wplecione w wiklinowe amulety mogą odpędzać pecha "
        "i chronić przed złem, ale równie dobrze sprowadzić mrok oraz gniew dawnych duchów.\n\n"
        "Tkacz amuletów. Zawsze masz przygotowane czary Błogosławieństwo i Urok. Ponadto zyskujesz jedną "
        "komórkę czaru 1. poziomu, której możesz użyć do ich rzucenia."
    ),
    "h470004cfg4199g24dfg3a04ge1085900eaf7": (
        "Gdy tobie lub widocznej przez ciebie istocie w promieniu 9 m nie powiedzie się rzut obronny, możesz "
        "użyć reakcji, aby dodać do rzutu premię i potencjalnie zmienić niepowodzenie w sukces. Premia jest "
        "równa twojemu modyfikatorowi Inteligencji (minimum +1).\n\n"
        "Z tej reakcji możesz skorzystać tyle razy, ile wynosi twój modyfikator Inteligencji (minimum raz). "
        "Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "he2f58070g7662g8b76gc3d9gce5303f3d8c8": (
        "Dom jest wszędzie tam, gdzie jesteś. Czerpiesz z cichej władzy Mrocznego Dworu nad cieniem i "
        "tajemnicą, otaczając siebie oraz sojuszników jego subtelną ochroną. W ramach akcji przywołujesz tę "
        "moc, aby stworzyć bezpieczne schronienie i natychmiast uzyskać korzyści krótkiego odpoczynku.\n\n"
        "Do następnego długiego odpoczynku ty i twoi sojusznicy zyskujecie premię +5 do testów Zręczności "
        '(<LSTag Type="Skills" Tooltip="Stealth">Skradanie się</LSTag>) i Mądrości '
        '(<LSTag Type="Skills" Tooltip="Perception">Percepcja</LSTag>).'
    ),
    "h7b17de26g4a12g2a89g2353gedd40e2fbe9a": (
        "Dom jest wszędzie tam, gdzie jesteś. Czerpiesz z cichej władzy Mrocznego Dworu nad cieniem i "
        "tajemnicą, otaczając siebie oraz sojuszników jego subtelną ochroną. W ramach akcji przywołujesz tę "
        "moc, aby stworzyć bezpieczne schronienie i natychmiast uzyskać korzyści krótkiego odpoczynku.\n\n"
        "Do następnego długiego odpoczynku ty i twoi sojusznicy zyskujecie premię +5 do testów Zręczności "
        '(<LSTag Type="Skills" Tooltip="Stealth">Skradanie się</LSTag>) i Mądrości '
        '(<LSTag Type="Skills" Tooltip="Perception">Percepcja</LSTag>).'
    ),
    "h4350095ege773ga624g7919g62f04bb30b95": (
        "Jeśli spudłujesz testem ataku czaru, możesz wydać 1 punkt zaklinania, aby przerzucić k20; musisz "
        "skorzystać z nowego wyniku.\n\n"
        "Możesz użyć opcji Poszukujący czar, nawet jeśli podczas rzucania tego czaru użyłeś już innej opcji metamagii."
    ),
    "h2eeadc40g0ba4g1146g9408g3a7f972a8ba4": (
        "W ramach akcji dodatkowej możesz wyczarować w dłoni broń paktu — wybraną broń prostą albo żołnierską "
        "do walki wręcz — lub związać się z dotkniętą bronią magiczną. Nie możesz związać się z bronią magiczną, "
        "jeśli jest do niej dostrojona inna osoba albo związał się z nią inny czarownik. Do końca więzi masz "
        "biegłość w posługiwaniu się tą bronią i możesz używać jej jako magicznego katalizatora.\n\n"
        "Gdy atakujesz związaną bronią, możesz używać modyfikatora Charyzmy zamiast modyfikatora Siły lub "
        "Zręczności w testach ataku i rzutach obrażeń. Możesz też sprawić, że broń zada obrażenia nekrotyczne, "
        "psychiczne, od światłości albo obrażenia swojego zwykłego typu.\n\n"
        "Więź kończy się, jeśli ponownie użyjesz akcji dodatkowej tej zdolności, jeśli przez co najmniej minutę "
        "broń będzie znajdować się dalej niż 1,5 m od ciebie albo jeśli umrzesz. Wyczarowana broń znika po "
        "zakończeniu więzi."
    ),
    "h252a159fg1973g1128g723dgcc172f2c22d4": (
        "Za każdym razem, gdy istota kończy turę w sferze, zyskuje tymczasowe punkty wytrzymałości w liczbie "
        "równej 1k6 plus twój poziom kleryka i kończy działający na nią efekt Zauroczenia albo Przerażenia."
    ),
    "h30d5708dgfa9eg4556ga8b6g4baa0e34f874": (
        "Wybierz jedną z poniższych opcji zdolności. Po każdym krótkim albo długim odpoczynku możesz zastąpić "
        "wybraną opcję drugą.\n\n"
        "Ucieczka przed hordą\nAtaki okazyjne przeciwko tobie są wykonywane z utrudnieniem.\n\n"
        "Obrona przed wielokrotnym atakiem\nGdy istota trafi cię atakiem, do końca tej tury ma utrudnienie "
        "we wszystkich pozostałych testach ataku przeciwko tobie."
    ),
    "h8933e173gb36agbf40ge97fg7e76f31c0d5c": (
        'Istotę nawiedzają jej najgorsze koszmary.<br><br>Otrzymuje [1] na turę i ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach cech</LSTag> oraz '
        '<LSTag Tooltip="AttackRoll">testach ataku</LSTag>.'
    ),
    "h02db6a63g3c71g5feeg9f17g4e0f97b6aa19": (
        'Łączy cię silna więź ze zwierzęcym towarzyszem. Twój modyfikator Mądrości jest dodawany do jego '
        '<LSTag Tooltip="ArmourClass">Klasy Pancerza</LSTag>, testów ataku i rzutów obrażeń.'
    ),
    "h8c201e1agf723gd526gdedfgb1cbcf2e8fc7": (
        "W ramach akcji dodatkowej możesz magicznie teleportować się na odległość do 9 m na widoczne, "
        "niezajęte miejsce. Możesz użyć tej cechy tyle razy, ile wynosi twoja premia z biegłości, a wszystkie "
        "zużyte użycia odzyskujesz po długim odpoczynku.\n\n"
        "Od 3. poziomu, gdy teleportujesz się za pomocą tej cechy, zyskujesz również odporność na wszystkie "
        "obrażenia do początku swojej następnej tury. W tym czasie wyglądasz widmowo i półprzezroczyście."
    ),
    "he30340c8gee67gea26g42dfg7428ad2ffc24": (
        '<LSTag Tooltip="MovementSpeed">Szybkość ruchu</LSTag> istoty zostaje zmniejszona o połowę.'
        '<br><br>Istota może wykonać tylko akcję albo '
        'akcję dodatkową.'
    ),
    "h1ad7e3a3g7b2fg4393g4b53g5a1bc9137cbd": (
        "Po osiągnięciu 5. poziomu postaci możesz skupić smoczą magię, aby tymczasowo zyskać zdolność lotu. "
        "W ramach akcji dodatkowej z twoich pleców wyrastają widmowe skrzydła. Utrzymują się przez 10 minut, "
        "dopóki ich nie schowasz (nie wymaga to akcji) albo dopóki nie uzyskasz stanu Obezwładnienia. W tym "
        "czasie twoja szybkość lotu jest równa twojej szybkości. Skrzydła wyglądają, jakby były stworzone z tej "
        "samej energii co twoje zionięcie. Po użyciu tej cechy nie możesz jej użyć ponownie do następnego długiego "
        "odpoczynku."
    ),
    "hb5fed628gc7a2g2040gd0adgb152d0d9aa4a": (
        "Medyk bojowy. Możesz przywrócić istocie 1k8 punktów wytrzymałości. Z tej zdolności możesz skorzystać "
        "tyle razy, ile wynosi twoja premia z biegłości, a wszystkie zużyte użycia odzyskujesz po długim odpoczynku.\n\n"
        "Leczenie. Za każdym razem, gdy przywracasz istocie punkty wytrzymałości, odzyskuje ona dodatkowe punkty "
        "wytrzymałości w liczbie równej twojej premii z biegłości."
    ),
    "h00c98c60g1486ge30fge973g756a8dffc456": (
        "„Broń zwana Prawdziwym Imieniem jest nierozerwalnie związana z historią Siedmiu Miast. Gdy diabły "
        "zawierają pakt, przyjmujący ofertę pieczętuje na ostrzu swoje prawdziwe imię i pozostawia je temu, "
        "kto złożył ofertę. Jeśli pakt zostanie złamany, ostrze ujawnia to imię i daje władzę nad zdrajcą.\n\n"
        "Mówi się, że ten, kto pozna prawdziwe imię samej broni, może przejąć wszystkie imiona związane z nią "
        "od chwili jej stworzenia. Wyobraź sobie władzę, jaką by to zapewniło.\n\n"
        "Poszukuję tego imienia od wieków. Gdy je znajdę, ostrze — i jego nosiciel — będą należeć do mnie”.\n\n"
        "— z osobistych zapisków piekielnego kanclerza Lazivosa"
    ),
    "h19fba472g52a7gb564g247bg818863c03630": (
        "Gdy tobie lub widocznej przez ciebie istocie w promieniu 9 m nie powiedzie się rzut obronny, możesz "
        "użyć reakcji, aby dodać do rzutu premię i potencjalnie zmienić niepowodzenie w sukces. Premia jest "
        "równa twojemu modyfikatorowi Inteligencji (minimum +1).\n\n"
        "Z tej reakcji możesz skorzystać tyle razy, ile wynosi twój modyfikator Inteligencji (minimum raz). "
        "Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h532c41a2g898dg391bgea84g9bed3cd65e57": (
        "Możesz użyć Aktu wiary, aby pokrzepić sojuszników kojącym zmierzchem.\n\n"
        "W ramach akcji unosisz święty symbol, a od ciebie rozchodzi się sfera zmierzchu o promieniu 9 m, "
        "wypełniona przyćmionym światłem. Sfera porusza się wraz z tobą i trwa przez minutę albo do chwili, gdy "
        "uzyskasz stan Obezwładnienia lub umrzesz. Za każdym razem, gdy istota kończy turę w sferze, zyskuje "
        "tymczasowe punkty wytrzymałości w liczbie równej 1k6 plus twój poziom kleryka i kończy działający na nią "
        "efekt Zauroczenia albo Przerażenia."
    ),
    "h7e9705fdg8018gea33g08e7g9a5b338d7d6a": (
        "W ramach akcji unosisz święty symbol, a od ciebie rozchodzi się sfera zmierzchu o promieniu 9 m, "
        "wypełniona przyćmionym światłem. Sfera porusza się wraz z tobą i trwa przez minutę albo do chwili, gdy "
        "uzyskasz stan Obezwładnienia lub umrzesz. Za każdym razem, gdy istota kończy turę w sferze, zyskuje "
        "tymczasowe punkty wytrzymałości w liczbie równej 1k6 plus twój poziom kleryka i kończy działający na nią "
        "efekt Zauroczenia albo Przerażenia."
    ),
    "h5f942db5g59f8g5849ga9beg2552e5c19da4": (
        "Za każdym razem, gdy istota kończy turę w sferze, zyskuje tymczasowe punkty wytrzymałości w liczbie "
        "równej 1k6 plus twój poziom kleryka i kończy działający na nią efekt Zauroczenia albo Przerażenia."
    ),
    "h0650634eg327bg1450gbcb7g99af88fe9574": (
        "Wybierz dwa czary maga ze szkoły swojej podklasy, każdy najwyżej 2. poziomu, i bezpłatnie dodaj je do "
        "swojej księgi czarów.\n\n"
        "Ponadto za każdym razem, gdy w tej klasie uzyskujesz dostęp do komórek czarów nowego poziomu, możesz "
        "bezpłatnie dodać do księgi jeden czar maga z tej szkoły. Wybrany czar musi mieć poziom, dla którego masz "
        "komórki czarów."
    ),
    "h46ea941fg771dgceb6g2492gb66d8a8c13e0": (
        "Boska istota pomaga ci pozostać w walce. Dysponujesz pulą czterech kości k12, które możesz zużywać, "
        "aby się leczyć. W ramach akcji dodatkowej możesz zużyć dowolną liczbę kości z puli, rzucić nimi i "
        "odzyskać punkty wytrzymałości w liczbie równej sumie wyników.\n\n"
        "Wszystkie zużyte kości odzyskujesz po długim odpoczynku.\n\n"
        "Maksymalna liczba kości w puli zwiększa się o jedną na 6. poziomie barbarzyńcy (5 kości), "
        "12. poziomie (6 kości) i 17. poziomie (7 kości)."
    ),
    "h83fd0391g6b2fgac96ga1a2gb0b7edabeb3b": (
        "Znasz ludowe lekarstwa i klątwy przekazywane w naukach Dawnych Dróg oraz potrafisz nasycać nimi "
        "wyplatane przez siebie niewielkie wiklinowe amulety. Zyskujesz następujące korzyści.\n\n"
        "Zawsze masz przygotowane czary Błogosławieństwo i Urok. Ponadto zyskujesz jedną komórkę czaru "
        "1. poziomu, której możesz użyć do ich rzucenia."
    ),
    "h1db10ba1g91aagc5a2g2acbg5853ba104450": (
        "Warunek wstępny: Smocze dziecię\n\n"
        "Gdy wpadasz w gniew, możesz emanować grozą.\n\n"
        "Zyskujesz jedno dodatkowe użycie zionięcia.\n\n"
        "Możesz zużyć jedno użycie zionięcia, aby ryknąć i zmusić każdą wybraną przez siebie istotę w promieniu "
        "9 m do wykonania rzutu obronnego na Mądrość. Przy niepowodzeniu cel zostaje Przerażony tobą na minutę."
    ),
    "h505c9691gb92dg0066g1bd8gee8dbadfa730": (
        'Warunek wstępny: Półork\n\nGdy uzyskasz <LSTag Tooltip="CriticalHit">trafienie krytyczne</LSTag> '
        "atakiem bronią do walki wręcz, rzucasz dodatkową kością obrażeń broni."
    ),
    "h3eabcb35gf264g4f8ag9c30g123cbc8fd2b8": (
        "Za każdym razem, gdy zadajesz obrażenia atakiem bez broni, możesz wybrać, czy zadaje on obrażenia od "
        "mocy, czy obrażenia swojego zwykłego typu."
    ),
    "h4b966c82g6ac4g74b4g1befg09e4bfb45f98": (
        "Twoja szybkość zwiększa się o 3 m.\n\nPonadto za każdym razem, gdy sojusznik po raz pierwszy w danej "
        "turze wejdzie w twoją Aurę ochrony albo rozpocznie w niej turę, jego szybkość zwiększa się o 3 m do "
        "końca jego następnej tury."
    ),
    "h3339cd6bg6f73ge757g76cdg991057f97dde": (
        "Mistrzostwo broni: Spowolnienie\n\nJeśli trafisz istotę tą bronią i zadasz jej obrażenia, możesz "
        "zmniejszyć jej szybkość o 3 m do początku swojej następnej tury."
    ),
    "hcb060b97gfe11gfd82gc6b9g3e44da81f15a": (
        "Mistrzostwo broni: Osłabienie\n\nJeśli trafisz istotę tą bronią, ma ona utrudnienie w następnym "
        "teście ataku wykonanym przed początkiem twojej następnej tury."
    ),
    "h10007b53gb4bcgbac3g9089g6d911c3cc5d4": (
        "Mistrzostwo broni: Nękanie\n\nJeśli trafisz istotę tą bronią i zadasz jej obrażenia, masz ułatwienie "
        "w następnym teście ataku przeciwko niej wykonanym przed końcem swojej następnej tury."
    ),
})

EXACT_OVERRIDES[
    "You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic weapon with a +[1] "
    "bonus to attack rolls and damage rolls. The spell ends early if you cast it again."
] = (
    "Dotykasz niemagicznej broni. Do zakończenia czaru staje się ona magiczna i zapewnia premię +[1] do "
    "testów ataku i rzutów na obrażenia. Czar kończy się wcześniej, jeśli rzucisz go ponownie."
)

UID_OVERRIDES.update({
    "hb5220d58g095fg5ae1g7115g72d15a96ef0c": (
        "Potrafisz w nadprzyrodzony sposób inspirować innych słowami, muzyką albo tańcem. Inspirację tę "
        "reprezentuje twoja kość Bardowskiej inspiracji, którą jest k6.\n\n"
        "Używanie Bardowskiej inspiracji. W ramach akcji dodatkowej możesz zainspirować inną istotę w "
        "promieniu 18 m, która cię widzi albo słyszy. Istota otrzymuje jedną z twoich kości Bardowskiej "
        "inspiracji. Może mieć tylko jedną taką kość naraz.\n\n"
        "Raz w ciągu następnej godziny, gdy istota nie zda testu k20, może rzucić kością Bardowskiej inspiracji "
        "i dodać wynik do rzutu k20, potencjalnie zmieniając niepowodzenie w powodzenie. Kość zostaje zużyta "
        "po wykonaniu rzutu.\n\n"
        "Liczba użyć. Możesz przyznać kość Bardowskiej inspiracji tyle razy, ile wynosi twój modyfikator "
        "Charyzmy (co najmniej raz). Wszystkie zużyte użycia odzyskujesz po długim odpoczynku.\n\n"
        "Na wyższych poziomach. Kość Bardowskiej inspiracji zmienia się po osiągnięciu określonych poziomów "
        "Barda, zgodnie z kolumną Kość bardowska w tabeli zdolności Barda: na 5. poziomie staje się k8, na 10. "
        "poziomie — k10, a na 15. poziomie — k12."
    ),
    "h2810e8cag53f2gddb2gb1bbg7d5f6848ec0b": (
        "Potrafisz w nadprzyrodzony sposób inspirować innych słowami, muzyką albo tańcem. Inspirację tę "
        "reprezentuje twoja kość Bardowskiej inspiracji, którą jest k6.\n\n"
        "Używanie Bardowskiej inspiracji. W ramach akcji dodatkowej możesz zainspirować inną istotę w "
        "promieniu 18 m, która cię widzi albo słyszy. Istota otrzymuje jedną z twoich kości Bardowskiej "
        "inspiracji. Może mieć tylko jedną taką kość naraz.\n\n"
        "Raz w ciągu następnej godziny, gdy istota nie zda testu k20, może rzucić kością Bardowskiej inspiracji "
        "i dodać wynik do rzutu k20, potencjalnie zmieniając niepowodzenie w powodzenie. Kość zostaje zużyta "
        "po wykonaniu rzutu.\n\n"
        "Liczba użyć. Możesz przyznać kość Bardowskiej inspiracji tyle razy, ile wynosi twój modyfikator "
        "Charyzmy (co najmniej raz). Wszystkie zużyte użycia odzyskujesz po długim odpoczynku.\n\n"
        "Na wyższych poziomach. Kość Bardowskiej inspiracji zmienia się po osiągnięciu określonych poziomów "
        "Barda, zgodnie z kolumną Kość bardowska w tabeli zdolności Barda: na 5. poziomie staje się k8, na 10. "
        "poziomie — k10, a na 15. poziomie — k12."
    ),
    "h5039598cg6db2g2d04g6e52gb5d4956c7773": (
        "Atut: Twardziel\n\nDorastałeś w dziczy, ucząc się przetrwania z dala od wygód cywilizacji. Pokonywanie "
        "niezwykłych niebezpieczeństw dzikich ostępów zwiększa twoją sprawność i poszerza wiedzę."
    ),
    "h6dbe3baeg32b7g2be3gc059gc25854510170": (
        "Możesz rzucić Mglisty krok w ramach reakcji, gdy otrzymujesz obrażenia.\n\n"
        "Ponadto zyskujesz następujące opcje Kroków fey.\n\n"
        'Znikający krok. Otrzymujesz stan <LSTag Type="Status" Tooltip="INVISIBLE">Niewidzialności</LSTag> '
        "do początku swojej następnej tury albo do chwili, gdy wykonasz test ataku, zadasz obrażenia lub "
        "rzucisz czar.\n\n"
        "Przerażający krok. Istoty w promieniu 3 m od opuszczonego przez ciebie miejsca albo miejsca, w którym "
        "się pojawiasz (wedle twojego wyboru), muszą wykonać udany rzut obronny na Mądrość przeciwko twojemu "
        "ST obrony przed czarami. Przy niepowodzeniu otrzymują 2k10 obrażeń psychicznych."
    ),
    "h6153da66gbfbeg1d0dgec8agfbc6490c04f5": (
        "Istoty w promieniu 3 m od opuszczonego przez ciebie miejsca albo miejsca, w którym się pojawiasz "
        "(wedle twojego wyboru), muszą wykonać udany rzut obronny na Mądrość przeciwko twojemu ST obrony "
        "przed czarami. Przy niepowodzeniu otrzymują 2k10 obrażeń psychicznych."
    ),
    "hfde09985geec3g307ag4015ga087801eec7f": (
        "Ramię w ramię. Gdy sojusznik w promieniu 1,5 m od ciebie podlega efektowi, który miałby go odepchnąć "
        "albo przyciągnąć, możesz w ramach reakcji temu zapobiec. Sojusznik nie może być Obezwładniony."
    ),
    "hae5d214ag6792g7325g5146gf48dfd5f7239": (
        "Ramię w ramię. Gdy sojusznik w promieniu 1,5 m od ciebie podlega efektowi, który miałby go odepchnąć "
        "albo przyciągnąć, możesz w ramach reakcji temu zapobiec. Sojusznik nie może być Obezwładniony."
    ),
    "h0326e7b1g8c73g586agce87gedf968fe63ea": (
        "Atut: Czujność\n\nPochodzisz z dumnego rodu rybaków lodowych z Dziesięciu Miast w Icewind Dale. "
        "Połów pstrąga pięściogłowego nie jest najbardziej chwalebnym zajęciem na Północy, ale to uczciwy "
        "sposób na życie. Wytrenowałeś swoje zmysły, by wyczuwać najlżejsze szarpnięcie żyłki, siłowałeś się "
        "z wielkimi pstrągami wyciąganymi z pokrytych lodem jezior i wypatroszyłeś tyle pstrągów "
        "pięściogłowych, że wielokrotnie wystarczyłyby, by wykarmić twoją wioskę. Te doświadczenia zahartowały "
        "twoje ciało i umysł do życia pełnego przygód.\n\n"
        "Ramię w ramię. Gdy sojusznik w promieniu 1,5 m od ciebie podlega efektowi, który miałby go odepchnąć "
        "albo przyciągnąć, możesz w ramach reakcji temu zapobiec. Sojusznik nie może być Obezwładniony."
    ),
    "h10a80e89g464fgbd0cgd70dg610b32e6acc3": (
        "Goliaci górują nad większością ludów i są odległymi potomkami olbrzymów. Każdy goliat nosi dary "
        "pierwszych olbrzymów, które objawiają się jako rozmaite nadprzyrodzone łaski — między innymi "
        "zdolność szybkiego wzrostu i tymczasowego dorównania posturą olbrzymim krewniakom.\n\n"
        "Cechy fizyczne goliatów przypominają olbrzymów z ich rodów. Niektórzy wyglądają jak olbrzymy "
        "kamienne, inni zaś jak ogniste. Niezależnie od pochodzenia goliaci wytyczyli w wieloświecie własną "
        "drogę, wolną od bratobójczych konfliktów, które od wieków pustoszą ród olbrzymów, i mierzą wyżej niż "
        "ich przodkowie."
    ),
    "h1201eb50gacb7ge804g6428g5470579075dc": (
        "Goliaci górują nad większością ludów i są odległymi potomkami olbrzymów. Każdy goliat nosi dary "
        "pierwszych olbrzymów, które objawiają się jako rozmaite nadprzyrodzone łaski — między innymi "
        "zdolność szybkiego wzrostu i tymczasowego dorównania posturą olbrzymim krewniakom.\n\n"
        "Cechy fizyczne goliatów przypominają olbrzymów z ich rodów. Niektórzy wyglądają jak olbrzymy "
        "kamienne, inni zaś jak ogniste. Niezależnie od pochodzenia goliaci wytyczyli w wieloświecie własną "
        "drogę, wolną od bratobójczych konfliktów, które od wieków pustoszą ród olbrzymów, i mierzą wyżej niż "
        "ich przodkowie."
    ),
    "h18ed8a2cgfbfbgc16ag59c2gdbdf16bfd5ca": (
        "Twoja wrodzona magia wywodzi się z sił chaosu, które leżą u podstaw porządku stworzenia. Być może ty "
        "albo jeden z twoich przodków zetknął się z surową magią, na przykład za sprawą portalu prowadzącego "
        "do Limbo lub Sfer Żywiołów. Być może pobłogosławiła cię istota fey albo naznaczył demon. Twoja magia "
        "może też być dziełem przypadku bez widocznej przyczyny. Niezależnie od źródła kłębi się w tobie, "
        "czekając na ujście."
    ),
})

for duplicate_uid in (
    "h285600aag7ea5gc76dg7ee0gf02eee80c3a6",
    "hc3d38c0eg2fe4g7216g4d25g664b8ca1c301",
    "h406d239cgf596g3642g0c30g97eb1a38e37a",
    "h680a104dg18d0g6bfeg6161ga38f884a1c38",
):
    UID_OVERRIDES[duplicate_uid] = (
        "Dotykasz chętnej istoty. Przez czas trwania czaru cel zyskuje szybkość lotu 18 m i może unosić się "
        "w miejscu. Gdy czar dobiegnie końca, cel spada, jeśli nadal znajduje się w powietrzu i nie potrafi "
        "powstrzymać upadku."
    )

UID_OVERRIDES.update({
    "h4ae962aag1f80gf20eg9ad2g481c0cb2a1fe": (
        "Po osiągnięciu poziomu Łowcy wskazanego w tabeli Czarów Wędrowca fey zawsze masz przygotowane "
        "wymienione w niej czary: na 3. poziomie — Zauroczenie osoby, na 5. poziomie — Krok przez mgłę, a na "
        "9. poziomie — Przyzwanie Fey."
    ),
    "hcbc2740fgebc3g29dbg5465ge353fe6de2d6": (
        "Skrywasz w sobie źródło energii psionicznej, reprezentowane przez kości energii psionicznej, które "
        "zasilają niektóre zdolności tej podklasy. Wraz z kolejnymi poziomami Łotrzyka zmieniają się liczba i "
        "rozmiar tych kości: na 3. poziomie masz cztery k6, na 5. poziomie — sześć k8, na 9. poziomie — osiem "
        "k8, a na 11. poziomie — osiem k10.\n\nPo krótkim odpoczynku odzyskujesz jedną zużytą kość energii "
        "psionicznej, a po długim odpoczynku — wszystkie."
    ),
    "h9446d065gc473g7595g3b13gfb953f314f52": (
        "Potrafisz utkać zasłonę psychicznych zakłóceń, aby się ukryć. W ramach akcji Magii otrzymujesz stan "
        '<LSTag Type="Status" Tooltip="INVISIBLE">Niewidzialności</LSTag> na 1 godzinę. Niewidzialność kończy '
        "się wcześniej natychmiast po tym, gdy zadasz istocie obrażenia albo zmusisz ją do wykonania rzutu "
        "obronnego."
    ),
    "hff09f5d5ga364g24e6ga7a8g00dbb675ea16": (
        "Potrafisz utkać zasłonę psychicznych zakłóceń, aby się ukryć. W ramach akcji Magii otrzymujesz stan "
        '<LSTag Type="Status" Tooltip="INVISIBLE">Niewidzialności</LSTag> na 1 godzinę. Niewidzialność kończy '
        "się wcześniej natychmiast po tym, gdy zadasz istocie obrażenia albo zmusisz ją do wykonania rzutu "
        "obronnego."
    ),
    "hd2d76fb0g487cg3ab3g3908g9f58ed8e7217": (
        "Po osiągnięciu określonych poziomów Zaklinacza wskazanych w tabeli Czarów psionicznych zawsze masz "
        "przygotowane wymienione w niej czary.\n\nNa 3. poziomie są to Ramiona Hadara, Wyciszenie emocji, "
        "Wykrycie myśli, Fałszywe podszepty i Okruch umysłu; na 5. poziomie dodatkowo — Głód Hadara; na 7. "
        "poziomie — Czarne macki Evarda; a na 9. poziomie — Telekineza."
    ),
    "hba43aa06gc80fg3f74gdf69g57af1f3cc5c1": (
        "Po osiągnięciu określonych poziomów Zaklinacza wskazanych w tabeli Czarów mechanizmu zawsze masz "
        "przygotowane wymienione w niej czary. Na 3. poziomie są to Pomoc, Leczenie ran, Mniejsze przywrócenie "
        "i Ochrona przed dobrem i złem; na 5. poziomie dodatkowo — Rozproszenie magii i Ochrona przed energią; "
        "na 7. poziomie — Swoboda ruchu; a na 9. poziomie — Większe przywrócenie."
    ),
    "h848282acg476egf71fgd7feg17ed2acf814f": (
        "Po osiągnięciu określonych poziomów Zaklinacza zawsze masz przygotowane następujące czary: na 3. "
        "poziomie — Leczenie ran, Pocisk wiodący, Mniejsze przywrócenie i Wypalający promień; na 5. poziomie "
        "dodatkowo — Aura witalności i Przeciwzaklęcie; na 7. poziomie — Tarcza ognia i Ściana ognia; a na "
        "9. poziomie — Większe przywrócenie i Słup ognia."
    ),
    "hd98d7d87g77cegbc88gd214g64ac7bacec24": (
        "Więź z tą boską domeną sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu poziomu "
        "Kleryka wskazanego w tabeli Czarów Domeny Umysłu zawsze masz przygotowane wymienione w niej czary: "
        "na 3. poziomie — Rozkaz, Wykrycie myśli, Fałszywe podszepty i Myślowy cierń; na 5. poziomie — "
        "Przeciwzaklęcie i Strach; na 7. poziomie — "
        '<LSTag Type="Spell" Tooltip="Target_Confusion">Zamęt</LSTag> i Urojony zabójca; '
        "a na 9. poziomie — Szum synaptyczny i Telekineza."
    ),
    "h793cd839gb6abg5b14g2409gcd0bd8f9ce42": (
        "Na 3. poziomie zawsze masz przygotowane Rozkaz, Wykrycie myśli, Fałszywe podszepty i Myślowy "
        "cierń; na 5. poziomie — Przeciwzaklęcie i Strach; na 7. poziomie — "
        '<LSTag Type="Spell" Tooltip="Target_Confusion">Zamęt</LSTag> i Urojony zabójca; '
        "a na 9. poziomie — Szum synaptyczny i Telekineza."
    ),
    "h822a72b8g17f5g73a6gd5f7g245ac996eb94": (
        "Po osiągnięciu poziomu Zaklinacza wskazanego w tabeli Czarów Cienia zawsze masz przygotowane "
        "wymienione w niej czary: na 3. poziomie — "
        '<LSTag Type="Spell" Tooltip="Target_Bane">Zguba</LSTag>, Ciemność, Zadawanie ran i Przejście bez '
        "śladu; na 5. poziomie — Głód Hadara i Strach; na 7. poziomie — "
        '<LSTag Type="Spell" Tooltip="Target_Invisibility_Greater">Większa niewidzialność</LSTag> i Urojony '
        'zabójca; a na 9. poziomie — <LSTag Type="Spell" Tooltip="Target_Contagion">Zaraza</LSTag> i '
        "Zabójcza chmura."
    ),
    "hce90f19eg2ee2g0ff4g4c21g7ebf85d46c9d": (
        "Na 3. poziomie zawsze masz przygotowane Zgubę, Ciemność, Zadawanie ran i Przejście bez śladu; na 5. "
        "poziomie — Głód Hadara i Strach; na 7. poziomie — "
        '<LSTag Type="Spell" Tooltip="Target_Invisibility_Greater">Większą niewidzialność</LSTag> i '
        "Urojonego zabójcę; a na 9. poziomie — Zarazę i Zabójczą chmurę."
    ),
    "he017d973g0291gbe65g86dbgfc62954d6af5": (
        "Szybkie powstanie. Gdy jesteś Powalony, możesz wstać, zużywając tylko 1,5 m ruchu.\n\n"
        "Skakanie. Raz na turę możesz wykonać Skok, zużywając tylko 3 m ruchu."
    ),
    "hac8cf59bgb29dg6896g2a11g689bf333570e": (
        "Szybkie powstanie. Gdy jesteś Powalony, możesz wstać, zużywając tylko 1,5 m ruchu.\n\n"
        "Skakanie. Raz na turę możesz wykonać Skok, zużywając tylko 3 m ruchu."
    ),
    "h3deb4586gfae5g7a55gadcagd4ee75ff94b8": (
        "Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator Charyzmy (co najmniej raz), lecz nie "
        "częściej niż raz na jeden rzut. Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "he0865db7gfb16g94fegbb02gd941d6db835a": (
        "Magia dżina sprawia, że po osiągnięciu określonych poziomów Paladyna zawsze masz przygotowane "
        "następujące czary: na 3. poziomie — Barwna kula i Grzmiące ugodzenie; na 5. poziomie dodatkowo — "
        "Lustrzane odbicia i Urojona siła; a na 9. poziomie — Lot i Forma gazowa."
    ),
    "head50b7eg3179gbc89g1334gbee0de9d925c": (
        "Więź z Nieprzerwanym Kręgiem sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu "
        "poziomu Druida wskazanego w tabeli Czarów Nieprzerwanego Kręgu zawsze masz przygotowane wymienione "
        "w niej czary: na 3. poziomie — Pętające uderzenie, Shillelagh, Lśniące ugodzenie i "
        'Prawdziwe uderzenie; na 5. poziomie — <LSTag Type="Spell" Tooltip="Target_Haste">Przyspieszenie</LSTag>; '
        "na 7. poziomie — Tarcza ognia; a na 9. poziomie — Słup ognia."
    ),
    "h99061a90g09cagcb07g6afegd32298d72981": (
        "Po osiągnięciu określonych poziomów Wynalazcy zawsze masz przygotowane czary wskazane w tabeli "
        "Czarów Alchemika: na 3. poziomie — Kojące słowo i Promień zatrucia; na 5. poziomie — Płomienna kula "
        "i Kwasowa strzała Melfa; a na 9. poziomie — Forma gazowa i Masowe kojące słowo."
    ),
    "hee79b7c5g14dagd8ecg3444ge2c7d3d25745": (
        "Po osiągnięciu określonych poziomów Wynalazcy zawsze masz przygotowane czary wskazane w tabeli "
        "Czarów Płatnerza: na 3. poziomie — Magiczny pocisk i Fala gromu; na 5. poziomie — Lustrzane odbicia "
        "i Trzask; a na 9. poziomie — Hipnotyczny wzór i Błyskawica."
    ),
    "hb830b235g9469g7dd2ga75agc175eb448a0b": (
        "Po osiągnięciu określonych poziomów Wynalazcy zawsze masz przygotowane następujące czary: na 3. "
        "poziomie — Tarcza i Fala gromu; na 5. poziomie — Wypalający promień i Trzask; a na 9. poziomie — "
        "Kula ognia i Przywołanie ognia zaporowego."
    ),
    "hd22a1ff8gaca7gd01cg610fgbe3a8ed48875": (
        "Od 3. poziomu zawsze masz przygotowane określone czary po osiągnięciu wskazanych poziomów tej klasy. "
        "Są dla ciebie czarami Wynalazcy, ale nie wliczają się do liczby czarów Wynalazcy, które możesz "
        "przygotować. Na 3. poziomie są to Heroizm i Tarcza; na 5. poziomie — Piętnujące ugodzenie i Ochronna "
        "więź; a na 9. poziomie — Aura witalności i Przywołanie ognia zaporowego."
    ),
    "h3b8a1f9dg4458ga3d3ga263gf4e1b90b9524": (
        "Więź z tą boską domeną sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu poziomu "
        "Kleryka wskazanego w tabeli Czarów Domeny Apokalipsy zawsze masz przygotowane wymienione w niej "
        "czary: na 3. poziomie — Ciemność, Piekielna reprymenda, Urojona siła i Fala gromu; na 5. poziomie — "
        "Głód Hadara i Strach; na 7. poziomie — Skaza i Burza lodu; a na 9. poziomie — Zabójcza chmura i "
        "Plaga owadów."
    ),
    "h7c50337fg49e2g1d8agf87ag04e30ad44c96": (
        "Na 3. poziomie zawsze masz przygotowane Ciemność, Piekielną reprymendę, Urojoną siłę i Falę gromu; "
        "na 5. poziomie — Głód Hadara i Strach; na 7. poziomie — Skazę i Burzę lodu; a na 9. poziomie — "
        "Zabójczą chmurę i Plagę owadów."
    ),
    "h78ec0f4cgdceeg4a48gd10ag8d7fa8a15f49": (
        "Po osiągnięciu poziomu Zaklinacza wskazanego w tabeli Czarów mrozu zawsze masz przygotowane "
        "wymienione w niej czary: na 3. poziomie — Ślepota, Lodowy nóż, Krok przez mgłę i Uśpienie; na 5. "
        "poziomie — Śnieżyca i Spowolnienie; na 7. poziomie — Tarcza ognia i Burza lodu; a na 9. poziomie — "
        "Stożek zimna i Przywołanie żywiołaka."
    ),
    "h633e7853gfe5cgc83fg46c5g12d2c8161229": (
        'Na 3. poziomie zawsze masz przygotowane <LSTag Type="Spell" Tooltip="Target_Blindness">Ślepotę</LSTag>, '
        "Lodowy nóż, Krok przez mgłę i Uśpienie; na 5. poziomie — Śnieżycę i Spowolnienie; na 7. poziomie — "
        "Tarczę ognia i Burzę lodu; a na 9. poziomie — Stożek zimna i Przywołanie żywiołaka."
    ),
    "he090be9bg8385g1850g97abg87aecc9a4555": (
        "Więź z tą boską domeną sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu poziomu "
        "Kleryka wskazanego w tabeli Czarów Domeny Grobu zawsze masz przygotowane wymienione w niej czary: na "
        "3. poziomie — Ochrona przed dobrem i złem, Fałszywe życie, Mniejsze przywrócenie, Promień osłabienia "
        "i Powstrzymanie śmierci; na 5. poziomie — Ożywienie i Wampiryczny dotyk; na 7. poziomie — Skaza i "
        "Osłona przed śmiercią; a na 9. poziomie — Rozproszenie dobra i zła oraz Masowe leczenie ran."
    ),
    "h32554089g3cb1g5105g77b7g4afa486c46cf": (
        "Na 3. poziomie zawsze masz przygotowane Ochronę przed dobrem i złem, Fałszywe życie, Mniejsze "
        "przywrócenie, Promień osłabienia i Powstrzymanie śmierci; na 5. poziomie — Ożywienie i Wampiryczny "
        "dotyk; na 7. poziomie — Skazę i Osłonę przed śmiercią; a na 9. poziomie — Rozproszenie dobra i zła "
        "oraz Masowe leczenie ran."
    ),
    "h02a16612g51dege910g582fg8824be4f2aee": (
        "Po osiągnięciu poziomu Łowcy wskazanego w tabeli Czarów Strażnika Pustki zawsze masz przygotowane "
        "wymienione w niej czary: na 3. poziomie — Gniewne ugodzenie, na 5. poziomie — Zbroja śmierci, a na "
        "9. poziomie — Widmowy rumak."
    ),
    "hd23192ffgdf59ga725g1c97g7e364650fe0c": (
        "Na 3. poziomie zawsze masz przygotowane Gniewne ugodzenie, na 5. poziomie — Zbroję śmierci, a na "
        "9. poziomie — Widmowego rumaka."
    ),
    "h7b73f5fagb632g4dd6gbb1bg52e10cb075ff": (
        "Więź z tą boską domeną sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu poziomu "
        "Kleryka wskazanego w tabeli Czarów Domeny Cienia zawsze masz przygotowane wymienione w niej czary: "
        'na 3. poziomie — <LSTag Type="Spell" Tooltip="Target_Bane">Zguba</LSTag>, Fałszywe życie, '
        '<LSTag Type="Spell" Tooltip="Target_Blindness">Ślepota</LSTag> i Ciemność; na 5. poziomie — '
        'Mignięcie i Strach; na 7. poziomie — Czarne macki i <LSTag Type="Spell" '
        'Tooltip="Target_Invisibility_Greater">Większa niewidzialność</LSTag>; a na 9. poziomie — Stożek zimna '
        "i Sen."
    ),
    "hb05d9f4bgc914g4d44g95b9ga646b28fd85b": (
        'Na 3. poziomie zawsze masz przygotowane Zgubę, Fałszywe życie, <LSTag Type="Spell" '
        'Tooltip="Target_Blindness">Ślepotę</LSTag> i Ciemność; na 5. poziomie — Mignięcie i Strach; na 7. '
        'poziomie — Czarne macki i <LSTag Type="Spell" Tooltip="Target_Invisibility_Greater">Większą '
        "niewidzialność</LSTag>; a na 9. poziomie — Stożek zimna i Sen."
    ),
    "h4ed71b8cg3ed3gd84eg3c79gb92ad8cf0e94": (
        "Po osiągnięciu określonych poziomów Zaklinacza zawsze masz przygotowane następujące czary: na 3. "
        "poziomie — Ostrze zielonego płomienia, Prawdziwe uderzenie, Heroizm, Magiczna broń, Lustrzane "
        'odbicia i Tarcza; na 5. poziomie — <LSTag Type="Spell" Tooltip="Target_Haste">Przyspieszenie</LSTag> '
        "i Widmowy rumak; na 7. poziomie — Osłona przed śmiercią i Kamienna skóra; a na 9. poziomie — "
        "Unieruchomienie potwora. Czary te nie wliczają się do liczby czarów, które możesz przygotować."
    ),
    "he9a93975g783agd634g2f29gb040a65e4d4f": (
        "Po osiągnięciu określonych poziomów Kleryka zawsze masz przygotowane następujące czary: na 3. "
        "poziomie — Tłuszcz, Palące ugodzenie, Rozgrzanie metalu i Magiczna broń; na 5. poziomie — Broń "
        "żywiołu i Ochrona przed energią; na 7. poziomie — Tarcza ognia i Ściana ognia; a na 9. poziomie — "
        "Słup ognia i Ściana kamienia. Czary te nie wliczają się do liczby czarów, które możesz przygotować."
    ),
    "hbcb1d930g4757g8ed9g69dagacdb27a4f791": (
        "Magia twojego patrona sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu "
        "wskazanych poziomów Czarownika automatycznie zyskujesz powiązane z nimi czary.\n\nNa 3. poziomie "
        "są to Pomoc, Leczenie ran, Pocisk wiodący, Mniejsze przywrócenie, Światło i Święty płomień; na 5. "
        "poziomie dodatkowo — Światło dzienne i Ożywienie; na 7. poziomie — Strażnik wiary i Ściana ognia; "
        "a na 9. poziomie — Większe przywrócenie."
    ),
    "h7bd1bb01g45ccge8e6g5722g3072b6b0bf23": (
        'Otrzymujesz stan <LSTag Type="Status" Tooltip="INVISIBLE">Niewidzialności</LSTag> do początku swojej '
        "następnej tury albo do chwili, gdy wykonasz test ataku, zadasz obrażenia lub rzucisz czar."
    ),
    "h34d645ffgccd0g672cg5920g5e1aa15ee5a7": (
        "Natychmiast po teleportacji ty i jedna widoczna istota w promieniu 3 m od ciebie zyskujecie 1k10 "
        "tymczasowych punktów wytrzymałości."
    ),
    "h7abb1184g0680g881dg18abgfc004e48f6e5": "Odświeżający krok",
    "h9b9091cdg68c3ga5edgce70g3588f2071f07": "Zyskaj 1k10 tymczasowych punktów wytrzymałości.",
    "h756fd0efg7178gaf40g2209ge695b89e27d9": "Prowokujący krok",
    "h444275c2g565cg45a9gdfbdg183d47facddb": (
        "Istoty w promieniu 3 m od opuszczonego przez ciebie miejsca muszą wykonać udany rzut obronny na "
        "Mądrość przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu mają utrudnienie w testach "
        "ataku przeciwko istotom innym niż ty do początku twojej następnej tury."
    ),
    "ha4fa9aabgb628g9f25g60a6g8ef2736d6490": "Prowokujący krok",
    "h81e4c4fcge764ge0d3g745cgea094c73c3cc": "Znikający krok",
})

EXACT_OVERRIDES[
    "Once per turn when you hit a creature with your pact weapon, you can expend a Pact Magic spell slot to "
    "deal an extra 1d8 Force damage to the target, plus another 1d8 per level of the spell slot, and you can "
    "give the target the Prone condition if it is Huge or smaller."
] = (
    "Raz na turę, gdy trafisz istotę bronią paktu, możesz zużyć komórkę czaru Magii Paktu, aby zadać celowi "
    "dodatkowe 1k8 obrażeń od mocy oraz kolejne 1k8 za każdy poziom zużytej komórki. Jeśli cel jest Ogromny "
    "lub mniejszy, możesz również nadać mu stan Powalenia."
)

EXACT_OVERRIDES.update({
    "Encouraging Song": "Zachęcająca pieśń",
    "Instrument Training": "Szkolenie muzyczne",
    "Bardic Damage": "Bardowskie obrażenia",
    "Bladework": "Kunszt klingi",
    "Focus": "Skupienie",
    "Inspired by Fear": "Natchnienie strachem",
    "Cavernous Sight": "Przepastny wzrok",
    "Stone Throw": "Rzut kamieniem",
})

UID_OVERRIDES.update({
    "h87d4e985gc3a3g6b66g2385g07e2b48896df": (
        'Możesz rzucić <LSTag Type="Spell" Tooltip="Target_DeathWard">Osłonę przed śmiercią</LSTag> '
        'bez zużywania <LSTag Tooltip="SpellSlot">komórki czaru</LSTag>.'
    ),
    "hc3c055e8g4d69gee62gad8cg75de8ea0fec1": (
        "Atut: Nowicjusz Rękawicy\n\nNie każdy, kto odpowiada na wezwanie wyższej siły, chce spędzać "
        "życie nad świętymi pismami w dusznej świątynnej apsydzie. Wstępując do Zakonu Rękawicy, "
        "obierasz drogę świętego wojownika. Jako rycerz Rękawicy okazujesz słuszną pogardę siłom zła, "
        "niezachwianą solidarność z towarzyszami broni i szczere współczucie ocalałym z wojny. Z bronią "
        "i świętym symbolem w dłoniach składasz przysięgę, że nie spoczniesz, dopóki światło sprawiedliwości "
        "nie rozproszy cienia chaosu nad całym Faerûnem."
    ),
    "hddb981a7g0a29gd059gf634g1b2d20e1a8fd": (
        "Gdy korzystasz ze zdolności Stań jako jedność (Nowicjusz Rękawicy), sojusznicy w promieniu "
        "1,5 m od ciebie są odporni na Powalenie i mają ułatwienie w rzutach obronnych na Siłę."
    ),
    "h4d3fa3f2g1f1aga0c3gb83bg94d626b6b33f": (
        "Gdy korzystasz ze zdolności Stań jako jedność (Nowicjusz Rękawicy), sojusznicy w promieniu "
        "1,5 m od ciebie są odporni na Powalenie i mają ułatwienie w rzutach obronnych na Siłę."
    ),
    "h06b8380ag7f73g106agdf63g8dabbadb964c": (
        "Odwet. Natychmiast po tym, jak istota w promieniu 1,5 m od ciebie trafi cię atakiem wręcz, "
        "możesz wykonać przeciwko niej atak okazyjny.\n\nWszechstronny najemnik. Wybierz umiejętność, "
        "w której masz biegłość. Zyskujesz w niej fachowość."
    ),
    "he09232a3g8429ge28bga994gd171ef3f3292": (
        "Odwet. Natychmiast po tym, jak istota w promieniu 1,5 m od ciebie trafi cię atakiem wręcz, "
        "możesz wykonać przeciwko niej atak okazyjny.\n\nWszechstronny najemnik. Wybierz umiejętność, "
        "w której masz biegłość. Zyskujesz w niej fachowość."
    ),
    "h717c2effgcfefg6531g04eeg3d6a10c88329": (
        "Zawierasz złowrogie przymierze z jednym z członków Martwej Trójki: Bane'em, Bhaalem albo Myrkulem. "
        'Wybór zapewnia ci odporność na określony typ obrażeń oraz powiązaną sztuczkę, dla której cechą '
        "bazową jest Inteligencja.\n\nJeśli wybierzesz Bane'a, zyskujesz odporność na obrażenia psychiczne "
        'i możesz rzucać <LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">Pomniejszą iluzję</LSTag>.\n\n'
        'Jeśli wybierzesz Bhaala, zyskujesz odporność na obrażenia od trucizny i możesz rzucać '
        '<LSTag Type="Spell" Tooltip="Shout_BladeWard">Osłonę przed orężem</LSTag>.\n\nJeśli wybierzesz '
        'Myrkula, zyskujesz odporność na obrażenia nekrotyczne i możesz rzucać Przeszywający dotyk.\n\n'
        'Wybrane bóstwo możesz zmienić po każdym długim odpoczynku.'
    ),
    "hed1840dbga25bga18bg158cg2e3656728e43": (
        "Zawierasz złowrogie przymierze z jednym z członków Martwej Trójki: Bane'em, Bhaalem albo Myrkulem. "
        "Wybór zapewnia ci odporność na określony typ obrażeń oraz powiązaną sztuczkę, dla której cechą "
        "bazową jest Inteligencja."
    ),
    "h7601f4ccg5ecfg89a8gf4d4gc425820bf2a2": (
        "Jeśli wybierzesz Bane'a, zyskujesz odporność na obrażenia psychiczne i możesz rzucać "
        '<LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">Pomniejszą iluzję</LSTag>.'
    ),
    "hb4a3c0b4g39f9g3519g8885g8624730cfa75": (
        'Jeśli wybierzesz Bhaala, zyskujesz odporność na obrażenia od trucizny i możesz rzucać '
        '<LSTag Type="Spell" Tooltip="Shout_BladeWard">Osłonę przed orężem</LSTag>.'
    ),
    "h6523df3dgbad7g0fafg867dg13134c55e3c3": (
        "Jeśli wybierzesz Myrkula, zyskujesz odporność na obrażenia nekrotyczne i możesz rzucać "
        "Przeszywający dotyk."
    ),
    "h58ee4755g4d7eg3830g0e23g9eeb9de00bf1": (
        'Zyskujesz odporność na obrażenia od trucizny i możesz rzucać '
        '<LSTag Type="Spell" Tooltip="Shout_BladeWard">Osłonę przed orężem</LSTag>.'
    ),
    "h6e38ab81gffdegf60dgddc7gdd71c617d269": (
        "Zyskujesz odporność na obrażenia nekrotyczne i możesz rzucać Przeszywający dotyk."
    ),
    "h4b3edb5dg700eg11d2gb46eg867808ec1738": (
        "Doświadczenie w zwalczaniu użytkowników magii zapewnia ci następujące korzyści.\n\n"
        "Przerwanie koncentracji. Każdy celny atak dystansowy, który wykonasz, rozprasza magię ochronną działającą "
        "na cel i przerywa jego koncentrację.\n\nStrzał antymagiczny. Gdy uzyskasz trafienie krytyczne przeciwko celowi "
        'objętemu efektem <LSTag Type="Status" Tooltip="GUT_SHOT">Strzału w brzuch</LSTag>, ograniczasz '
        "również jego zdolność do posługiwania się magią. Dopóki pocisk tkwi w celu, nie może on rzucać "
        "czarów ani wykonywać akcji Magii.\n\nObycie z magią. Gdy nie powiedzie ci się rzut obronny przeciwko "
        "czarowi lub efektowi magicznemu, możesz w ramach reakcji rzucić 1k6 i dodać wynik do rzutu, "
        "co może zmienić niepowodzenie w powodzenie."
    ),
    "hd8757627g198cg4659gbdcbgf8c916e4b023": (
        'Gdy w ramach akcji dodatkowej nałożysz pieczęć illriggera na istotę albo spalisz nałożoną na nią '
        'pieczęć, na 2 tury zyskujesz efekt <LSTag Type="Spell" Tooltip="Shout_BladeWard">Osłony przed '
        'orężem</LSTag>.'
    ),
    "h1b7aecd7g65c1g83b6g50ddg7fe12c1c16a8": (
        'Więź z Domeną Astralną sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu '
        'wskazanych poziomów kleryka automatycznie zyskujesz czary wymienione w tabeli Czarów Domeny '
        'Astralnej. Na 3. poziomie są to Rozmycie, Pocisk wiodący, <LSTag Type="Spell" '
        'Tooltip="Target_Invisibility">Niewidzialność</LSTag>, Szybkonogi i Gwiezdny ognik. Na 5. poziomie '
        'zyskujesz Mignięcie i Spowolnienie. Na 7. poziomie — Wypędzenie i Drzwi przez wymiary. '
        'Na 9. poziomie — Rozproszenie dobra i zła oraz Ścianę kamienia.'
    ),
    "h4bf8da96g64a3g0f5eg135bg7645978583b0": (
        "Kowal bitewny łączy umiejętności obrońcy i medyka: specjalizuje się w ochronie innych oraz "
        "naprawie zarówno wyposażenia, jak i leczeniu sprzymierzeńców. W pracy wspiera go stalowy obrońca — "
        "stworzony przez niego ochronny towarzysz."
    ),
    "h1ad514dega841gc35dg8804ga474e60b45ea": (
        'Gdy trafisz cel magiczną bronią albo gdy twój <LSTag Type="Spell" Tooltip="Target_SteelDefender">'
        'Stalowy obrońca</LSTag> trafi cel, możesz poprzez uderzenie wyzwolić niszczycielską energię. '
        'Cel otrzymuje dodatkowe 2k6 obrażeń od mocy.\n\nZamiast tego możesz wyzwolić energię odnawiającą, '
        'wybierając widoczną istotę lub przedmiot w promieniu 9 m. Energia uzdrawia wybrany cel, '
        'przywracając mu 2k6 punktów wytrzymałości.'
    ),
    "h72a8bf1agc8fbgec94g5bd1g5c0893342c80": (
        'Magia patrona sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu poziomu '
        'czarownika wskazanego w tabeli Czarów Nieumarłego zyskujesz wymienione w niej czary. Na 3. poziomie '
        'są to <LSTag Type="Spell" Tooltip="Target_Bane">Zguba</LSTag>, <LSTag Type="Spell" '
        'Tooltip="Target_Blindness">Ślepota</LSTag>, Urojona siła i Promień zatrucia. Na 5. poziomie — '
        'Rozmawianie z umarłymi oraz <LSTag Type="Spell" Tooltip="Target_AnimateDead">Animowanie zmarłego'
        '</LSTag>. Na 7. poziomie — <LSTag Type="Spell" Tooltip="Target_Invisibility_Greater">Większa '
        'niewidzialność</LSTag> i Urojony zabójca. Na 9. poziomie — Makabryczny taniec i Zabójcza chmura.'
    ),
    "h423f4d8eg647cg79b9g302bg9ad97549087a": (
        'Na 3. poziomie zyskujesz Zgubę, <LSTag Type="Spell" Tooltip="Target_Blindness">Ślepotę</LSTag>, '
        'Urojoną siłę i Promień zatrucia. Na 5. poziomie — Rozmawianie z umarłymi i Animowanie zmarłego. '
        'Na 7. poziomie — <LSTag Type="Spell" Tooltip="Target_Invisibility_Greater">Większą niewidzialność'
        '</LSTag> i Urojonego zabójcę. Na 9. poziomie — Makabryczny taniec i Zabójczą chmurę.'
    ),
    "hb012aa29g2700gd0c7g3c87g74a98a1affc6": (
        'Możesz magicznie wytwarzać z dłoni lepką, jedwabistą pajęczynę. W ramach akcji dodatkowej możesz '
        'użyć jej na jeden z poniższych sposobów.\n\n<LSTag Type="Spell" '
        'Tooltip="Target_ArachnoidStalker_Pull">Sieć przyciągająca</LSTag>. Traf istotę lub przedmiot w '
        'zasięgu [1] przylegającą pajęczyną i przyciągnij cel o maksymalnie [1]. Przemieścić można tylko '
        'cel rozmiaru dużego lub mniejszego, a istota może się oprzeć udanym rzutem obronnym na Zręczność. '
        'Sojusznik zawsze zostaje przyciągnięty.\n\n<LSTag Type="Spell" '
        'Tooltip="Target_ArachnoidStalker_WebSwing">Kołysanie na sieci</LSTag>. Wystrzel nić pajęczyny '
        'w widoczny punkt w zasięgu [1] i przyciągnij się do niego bez prowokowania ataków okazyjnych.\n\n'
        'Pajęczyna. W ramach tej samej akcji dodatkowej rzucasz czar Pajęczyna bez zużywania komórki czaru. '
        'Pajęczyna wypełnia obszar o promieniu [2] i znika po minucie, a schwytana w niej istota musi wykonać '
        'udany rzut obronny na Zręczność albo zostaje <LSTag Type="Status" Tooltip="WEB">Usidlona</LSTag>. '
        'Za pomocą tej zdolności możesz rzucić ten czar dwukrotnie. Jedno zużyte użycie odzyskujesz po '
        'krótkim odpoczynku, a wszystkie po długim odpoczynku.\n\nST rzutu obronnego wynosi 8 plus twój '
        'modyfikator Zręczności i premia z biegłości.'
    ),
    "hd5b90e52gc2cagaf46gca4cg4997c18e17fb": (
        'Przywołaj dzika, który rani wrogów <LSTag Type="Spell" Tooltip="Target_Tusk_Boar_Summon">Kłem'
        '</LSTag> i powala ich <LSTag Type="Spell" Tooltip="Rush_Rush_Boar_Summon">Szarżą</LSTag>.'
    ),
    "hafbed588gb94eg788agb035g22cf2f434eb4": (
        'Przywołaj pająka wilczego, który rzuca się na wrogów z <LSTag Type="Spell" '
        'Tooltip="Target_Bite_GiantSpider_Summon">Ugryzieniem</LSTag> i powala ich '
        '<LSTag Type="Spell" Tooltip="Rush_Rush_Boar_Summon">Szarżą</LSTag>.'
    ),
    "h67d9ca78g7e48g27e7g2e6bg3fd979f583a5": (
        'Przywołaj wilka, który szarpie wrogów <LSTag Type="Spell" Tooltip="Target_Bite_Wolf_Summon">'
        'Ugryzieniem</LSTag> i powala ich <LSTag Type="Spell" Tooltip="Rush_Rush_Boar_Summon">Szarżą</LSTag>.'
    ),
    "h1db10ba1g91aagc5a2g2acbg5853ba104450": (
        "Warunek wstępny: Drakon\n\nGdy wpadasz w gniew, możesz emanować grozą.\n\nZyskujesz jedno "
        "dodatkowe użycie zionięcia.\n\nMożesz zużyć jedno użycie zionięcia, aby ryknąć i zmusić każdą "
        "wybraną istotę w promieniu 9 m do wykonania rzutu obronnego na Mądrość. Przy niepowodzeniu cel "
        "zostaje Przerażony tobą na minutę."
    ),
    "h9034c86agb8d7g13ffge863g1561ec6ea096": (
        "Warunek wstępny: Drakon\n\nWyrastają ci łuski i pazury przypominające drakonich przodków.\n\n"
        "Twoje łuski twardnieją. Gdy nie nosisz pancerza, twoja KP może wynosić 13 + twój modyfikator "
        "Zręczności. Możesz używać tarczy i nadal korzystać z tej korzyści.\n\nNa końcach palców wyrastają "
        "ci chowane pazury. Ich wysunięcie lub schowanie nie wymaga akcji. Są naturalną bronią, której "
        "możesz używać do wykonywania ataków bez broni. Gdy trafisz takim atakiem z użyciem pazurów, "
        "zadajesz dodatkowe 1k4 obrażeń ciętych."
    ),
    "hc4d3f811g2a89g0e6dg5219gcf3bfa3167c3": (
        'Przybierz postać straszliwego wilka, który potrafi <LSTag Type="Spell" '
        'Tooltip="Shout_PackHowl_Wolf_Dire">zagrzewać</LSTag> sojuszników do walki i '
        '<LSTag Type="Spell" Tooltip="Target_Bite_Wolf_Dire_Wildshape">rozpraszać</LSTag> wrogów.'
    ),
    "hb219036fg4365gffedg71d5g938331069179": (
        'Omijanie osłony. Twoje <LSTag Tooltip="RangedWeaponAttack">ataki bronią dystansową</LSTag> nie '
        'otrzymują kar wynikających z <LSTag Tooltip="HighGroundRules">zasady przewagi wysokości</LSTag>.\n\n'
        'Strzelanie w zwarciu. Obecność w promieniu 1,5 m od wroga nie nakłada utrudnienia na twoje testy '
        'ataku bronią dystansową.\n\nDalekie strzały. Atakowanie dwuręczną bronią dystansową zwiększa jej '
        'zwykły zasięg do 27 m.'
    ),
    "h5b4e785ag06afgf727gca99g7e0aa28facda": (
        'Omijanie osłony. Twoje <LSTag Tooltip="RangedWeaponAttack">ataki bronią dystansową</LSTag> nie '
        'otrzymują kar wynikających z <LSTag Tooltip="HighGroundRules">zasady przewagi wysokości</LSTag>.\n\n'
        'Strzelanie w zwarciu. Obecność w promieniu 1,5 m od wroga nie nakłada utrudnienia na twoje testy '
        'ataku bronią dystansową.\n\nDalekie strzały. Atakowanie dwuręczną bronią dystansową zwiększa jej '
        'zwykły zasięg do 27 m.'
    ),
    "h28541eafg02e0g2a1ag2ebcgdcdb10c35901": (
        "Powal cel tarczą, nadając mu stan Powalenia."
    ),
    "h16a91f2cg659dg4a91gbb02g7dd759e681be": (
        "Ten giętki i mocny długi łuk nasycono podniosłą magią łowcy. Przesuwając palcami po gładkim "
        "jesionowym łęczysku, niemal czujesz ją niczym ducha zaklętego w uformowanym drewnie."
    ),
    "ha031b042gd64ag0b74g62b9g7aa92b2a2119": (
        "Potomek Trójki czerpie moc ze złowrogich bogów znanych we Wrotach Baldura jako Martwa Trójka: Zguby, "
        "boga tyranii; Bhaala, boga przemocy i mordu; oraz Myrkula, boga śmierci. Niektórzy łotrzykowie tej "
        "podklasy gorliwie oddają się tym trzem makabrycznym bóstwom, innych zaś sprowadza na tę ścieżkę "
        "klątwa. W obu przypadkach moc potomka przejawia się w rozmaitych okultystycznych darach oraz "
        "niezwykłym talencie do zadawania ciosów i wzbudzania trwogi.\n\nPotomkowie Trójki najczęściej "
        "występują we Wrotach Baldura, gdzie członkowie Martwej Trójki żyli jako śmiertelnicy, zanim osiągnęli "
        "boskość. Tajne kulty Zguby, Bhaala i Myrkula często zaliczają ich do swoich najcenniejszych agentów. "
        "Poza Wrotami Baldura świeckie gildie złodziei — takie jak Złodzieje Cienia z Amn czy Gildia Xanathara "
        "w Waterdeep — mogą powierzyć Potomkowi Trójki wyjątkowo krwawe zlecenie."
    ),
    "hcf74d85ag3ed2g6eecga0d3g6e6a0fa87154": (
        "Ryzyko płynie w żyłach rewolwerowców. Ci śmiali renegaci odrzucają tradycję i wytyczają własną "
        "drogę z niebezpieczną, toporną bronią palną w dłoniach. Słyną z tego, że wychodzą cało z opresji "
        "dzięki sprytowi, decyzjom podejmowanym w ułamku sekundy i niemałej dozie szczęścia.\n\nCzarny proch "
        "nie jest dla ludzi o słabych nerwach. Jego grzmot jest gwałtowny i nieprzewidywalny — to ledwie "
        "kontrolowana eksplozja skierowana ku wrogowi. Tylko prawdziwie nieustraszeni próbują go okiełznać. "
        "Rewolwerowcy mają jednak nerwy ze stali i pośród ogłuszającej kanonady miotają śmierć ze swoich "
        "pistoletów. Są ruchliwi i zuchwali, a w strzelaninach dobrze wiedzą, że od błyskawicznej decyzji "
        "i hartu ducha może zależeć życie.\n\nWybuchowy tryb życia rewolwerowca sprzyja wędrówkom i przygodom. "
        "Rewolwerowcy często najpierw strzelają, a dopiero potem zadają pytania, przez co zyskują niewielu "
        "przyjaciół i wielu wrogów. Większość podczas podróży zachowuje skrytość i dokłada wszelkich starań, "
        "by nie zwracać na siebie uwagi dawnych przeciwników mających z nimi rachunki do wyrównania."
    ),
    "hf1e041c0ga156g608cg02dfg22c1dad1bf3a": (
        "Uśmierzacze to ciężkozbrojni żołnierze śmierci z Piekła. Służą Dispaterowi i prowadzą natarcia "
        "we wszystkich większych piekielnych bitwach.\n\nDispater włada Dis, Miastem Wojny. Gdy Piekło "
        "najeżdża inny świat, to jego armia walczy i ginie. Uśmierzacze są mistrzami strategii, którzy "
        "dowodzą z pierwszej linii, wzbudzając w żołnierzach grozę i podziw. Wyniośli, pełni pychy i dumy, "
        "często przykładają przesadną wagę do własnego wyglądu.\n\nChoć należą do najbardziej rycerskich "
        "illriggerów, ich szlachetność jest wypaczona. Przyjmują i honorują wyzwania do pojedynku, a każdego, "
        "kto próbuje się wtrącić, szybko karzą. Kiedy jednak przegrywają, bez wahania oszukują, a gdy wygrywają, "
        "arogancko igrają z przeciwnikiem przed zadaniem ostatecznego ciosu.\n\nW chwili słabości lub rozpaczy "
        "władca innego świata może ujrzeć nieuchronną klęskę swojej armii i wezwać Dispatera. Zawsze chętny do "
        "siania waśni i niezgody arcydiabeł często odpowiada, wysyłając Uśmierzacza, by poprowadził wojska "
        "zdesperowanego władcy."
    ),
    "hc0cff11age80fgb13fgfd62g598157b9f427": (
        "Ciężkie oddziały szturmowe Dispatera muszą skutecznie dowodzić na polu bitwy i szybko eliminować "
        "wrogów. Uśmierzacze kierują się zasadami nakazującymi im prowadzić armie Piekła i toczyć wojnę "
        "z Dobrem w całej czasoprzestrzeni.\n\nDowodzenie z pierwszej linii. Ruszam na czele każdego natarcia, "
        "dodając odwagi swoim żołnierzom i wzbudzając trwogę we wrogach.\n\nDowódca. Gdziekolwiek się pojawię, "
        "wydaję rozkazy. Nie słucham tych, którym brak woli, by przewodzić.\n\nZwycięstwo za wszelką cenę. "
        "Szanuję dowódcę wroga i traktuję go honorowo. Gdy jednak dobywamy mieczy, używam każdego sposobu, "
        "by wygrać, i oczekuję od przeciwnika tego samego.\n\nŻołnierze giną. Życie moich żołnierzy nie ma "
        "dla mnie znaczenia — są zasobem, który poświęcam dla zwycięstwa."
    ),
    "h7dfa2a4bg13bfg7ea9g611cgc213f4b0ba43": (
        "Architekci ruiny to opanowani i wyrachowani rycerze magii służący Asmodeuszowi. Posługują się "
        "czarami, stalą i podstępem, aby zwyciężyć za wszelką cenę.\n\nAsmodeusz włada Acheronem, Miastem "
        "Strachu. Jego illriggerzy przemierzają czasoprzestrzeń, gromadząc tajemnice i czary służące do "
        "zwodzenia i przerażania przeciwników. Wojna, którą prowadzi z innymi arcydiabłami, jest wojną "
        "oszustwa i informacji.\n\nArchitekci ruiny sprawiają, że wrogowie Piekła czują się osaczeni i "
        "przechytrzeni. Są znakomitymi zaklętymi szermierzami na polu bitwy, choć niektórzy wolą badania, "
        "infiltrację i propagandę, aby prowadzić psychologiczną grę ze swą ofiarą. Gdy wreszcie stają z nią "
        "twarzą w twarz, przewaga należy do nich: wszystko zbadali, poczynili przygotowania i ścisnęli los "
        "w swej rękawicy, zmuszając go, by im sprzyjał. Nienasycenie zgłębiają mroczne sztuki, by uzbroić "
        "siebie i Asmodeusza w to, co niemożliwe."
    ),
    "h3c31b801g72c4g4016g8dbagc376fb17c919": (
        "Wstępując do Zakonu Spustoszenia, Architekci ruiny składają przysięgę Asmodeuszowi. Jej zasady "
        "zobowiązują ich do niszczenia wrogów Asmodeusza za pomocą potężnej magii, wzbudzania strachu "
        "i siania nieufności.\n\nPole bitwy umysłu. Zanim nasze armie się spotkają, napełnię cię grozą "
        "i zwątpieniem we własne siły. Pokonam cię bez kiwnięcia palcem.\n\nWłaściwa tajemnica. Gdy poznam "
        "twoje sekrety, poznam też twoją słabość.\n\nWiedza to potęga. Wiedza jest równie potężna jak stal. "
        "Poznaję każdy szczegół dotyczący wroga i przewiduję wszystkie jego posunięcia, matując go jeszcze "
        "przed rozpoczęciem gry.\n\nMagia podlega mojej woli. Przebiegłość jest równie potężna jak stal. "
        "Władam mroczną magią tajemną, aby zwodzić twoje zmysły, osłabiać determinację i wzmacniać własne "
        "ostrze. Twoi żołnierze zadrżą przed mrocznymi czarami, które mogą spowić moje ostrze."
    ),
    "h7d405f4ag1770gee29gfd7egc0479b1be286": (
        "Atut: Strażnik grobu\n\nW miejscu bliższym krainie umarłych niż żywych, ludzie troszczący się "
        "o wieczny spoczynek zmarłych budzą zarazem głęboki szacunek i niepokój. Parałeś się pracą grabarza, "
        "pracownika zakładu pogrzebowego i balsamisty. Niekiedy tylko ty potrafiłeś znaleźć życzliwe słowo, "
        "by uczcić pamięć tych, którzy odeszli. Dobrze znasz spustoszenie czynione przez nieumarłych i nie "
        "pozwalasz im zakłócać spoczynku powierzonych ci zmarłych.\n\nStrażnik grobu. Zyskujesz jedno użycie "
        "zdolności Akt wiary klasy kleryka i możesz za jego pomocą wywołać efekt Odpędzanie nieumarłych. "
        "Jeśli masz już Akt wiary, dodajesz to użycie do zdolności jednej wybranej klasy."
    ),
    "h374216bbgf985gc96cg64b3g959b101fd376": (
        "Obrażenia psychiczne zadawane Straszliwym uderzeniem zwiększają się do 2k8. Cel musi wykonać "
        "rzut obronny na Mądrość przeciwko ST rzutu obronnego przeciwko twoim czarom. Przy niepowodzeniu "
        "zostaje Przerażony do początku twojej następnej tury.\n\nDziałasz dość szybko, by zamienić chybienie "
        "w kolejne uderzenie. Gdy chybisz atakiem bronią, możesz bez dodatkowych kosztów wykonać jeszcze "
        "jeden atak bronią."
    ),
    "he28b1437g3278g7202g8a7dg0bb7c36a5d7a": (
        "Wydarzenie z przeszłości pozostawiło na tobie niezatarte piętno i nasyciło cię wrzącą magią. "
        "W ramach akcji dodatkowej możesz uwolnić tę magię na minutę, zyskując następujące korzyści:\n\n"
        "ST rzutów obronnych przeciwko twoim czarom zaklinacza zwiększa się o 1.\nMasz ułatwienie w testach "
        "ataku rzucanymi przez siebie czarami zaklinacza.\n\nMożesz skorzystać z tej zdolności dwukrotnie. "
        "Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h591ca3fag8585g7042gec5dgab33a05594bb": (
        "Wydarzenie z przeszłości pozostawiło na tobie niezatarte piętno i nasyciło cię wrzącą magią. "
        "W ramach akcji dodatkowej możesz uwolnić tę magię na minutę, zyskując następujące korzyści:\n\n"
        "ST rzutów obronnych przeciwko twoim czarom zaklinacza zwiększa się o 1.\nMasz ułatwienie w testach "
        "ataku rzucanymi przez siebie czarami zaklinacza.\n\nMożesz skorzystać z tej zdolności dwukrotnie. "
        "Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "hd8409099g42e6g3a17g9b47gc6bd4fec7de5": (
        "Jeśli nie masz już użyć Wrodzonej magii, możesz ją aktywować, wydając 2 punkty magii podczas "
        "wykonywania związanej z nią akcji dodatkowej.\n\nPonadto, gdy Wrodzona magia jest aktywna, "
        "ST rzutów obronnych przeciwko twoim czarom zwiększa się o 2 zamiast o 1."
    ),
    "h9e96b030g4a5fgfbd9g8d73g10831d134be3": (
        'Silna trucizna. Rzucane przez ciebie czary i wykonywane ataki ignorują <LSTag Tooltip="Resistant">'
        'odporność</LSTag> na obrażenia od trucizny. Ponadto, gdy zadajesz czarem obrażenia od trucizny, '
        'każdy wynik 1 na kości obrażeń traktujesz jak 2.\n\nWarzenie trucizny. Zyskujesz zestaw truciciela '
        'i biegłość w posługiwaniu się nim. Gdy zadasz istocie obrażenia od trucizny, musi ona wykonać udany '
        'rzut obronny na Kondycję albo zostaje <LSTag Type="Status" Tooltip="POISONED">Zatruta</LSTag>.'
    ),
    "he05ad460g276fg1990g8fccg4bd00b5d035a": (
        'Silna trucizna. Rzucane przez ciebie czary i wykonywane ataki ignorują <LSTag Tooltip="Resistant">'
        'odporność</LSTag> na obrażenia od trucizny. Ponadto, gdy zadajesz czarem obrażenia od trucizny, '
        'każdy wynik 1 na kości obrażeń traktujesz jak 2.'
    ),
    "haaf829fagd4d2g973eg987ag882a31fcb4ae": (
        "Natychmiast po rzuceniu czaru Ugodzenia możesz zużyć jedno użycie Mocy przysięgi i wywołać jeden "
        "z poniższych efektów.\n\nMiażdżący uścisk dao. Ziemia unosi się wokół celu, nadając mu stan "
        "Unieruchomienia.\n\nUcieczka dżinna. Teleportujesz się do widocznego, niezajętego miejsca w promieniu "
        "9 m i do końca swojej następnej tury przybierasz półmaterialną postać. W tej postaci masz odporność "
        "na obrażenia obuchowe, kłute i cięte oraz niewrażliwość na Powalenie i Unieruchomienie.\n\nFuria "
        "efreetiego. Cel otrzymuje dodatkowe 2k4 obrażeń od ognia, po czym płomienie przeskakują na wszystkich "
        "widocznych wrogów w promieniu 9 m od ciebie. Każdy z nich również otrzymuje 2k4 obrażeń od ognia.\n\n"
        "Fala marida. Cel i wszystkie wybrane przez ciebie istoty w emanacji o promieniu 3 m wykonują rzut "
        "obronny na Siłę przeciwko ST rzutu obronnego przeciwko twoim czarom. Przy niepowodzeniu istota zostaje "
        "odrzucona od ciebie o 4,5 m i Powalona."
    ),
    "h79a50a5ag645fgfec1g1742g3190589c1ba0": (
        "Cel i wszystkie wybrane przez ciebie istoty w emanacji o promieniu 3 m wykonują rzut obronny na Siłę "
        "przeciwko ST rzutu obronnego przeciwko twoim czarom. Przy niepowodzeniu istota zostaje odrzucona "
        "od ciebie o 4,5 m i Powalona."
    ),
    "h82f57f8fg4253ga79egce21gde7d5fe72f73": (
        "W ramach akcji wydychasz strumień potężnej energii. Każda istota w stożku o długości 4,5 m wykonuje "
        "rzut obronny na Zręczność przeciwko ST rzutu obronnego przeciwko twoim czarom. Przy niepowodzeniu "
        "otrzymuje obrażenia od ognia, a przy powodzeniu połowę tej wartości."
    ),
    "h520a3350gab70g330fge64fgd34f7914b820": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie Aktu wiary, aby otworzyć planarną szczelinę "
        "w widocznym punkcie w promieniu 18 m. Szczelina tworzy potężną próżnię w kuli o promieniu 4,5 m "
        "wokół tego punktu. Każda istota na tym obszarze wykonuje rzut obronny na Zręczność. Przy niepowodzeniu "
        "otrzymuje 1k8 plus twój poziom kleryka obrażeń od mocy i zostaje przyciągnięta o maksymalnie 4,5 m "
        "w stronę szczeliny. Przy powodzeniu otrzymuje tylko połowę obrażeń od mocy. Następnie szczelina znika."
    ),
    "h62513dd3g7a62g4659g151cg25df749019af": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie Aktu wiary, aby otworzyć planarną szczelinę "
        "w widocznym punkcie w promieniu 18 m. Szczelina tworzy potężną próżnię w kuli o promieniu 4,5 m "
        "wokół tego punktu. Każda istota na tym obszarze wykonuje rzut obronny na Zręczność. Przy niepowodzeniu "
        "otrzymuje 1k8 plus twój poziom kleryka obrażeń od mocy i zostaje przyciągnięta o maksymalnie 4,5 m "
        "w stronę szczeliny. Przy powodzeniu otrzymuje tylko połowę obrażeń od mocy. Następnie szczelina znika."
    ),
    "hc58f0177g4e5fgb789g4272g3e57d5e733b0": (
        "Więź z nieumarłością przenika twoje ciało i zapewnia ci następujące korzyści.\n\nNekrotyczna "
        "odporność. Masz odporność na obrażenia nekrotyczne. Podczas korzystania z Postaci grozy zyskujesz "
        "niewrażliwość na obrażenia nekrotyczne.\n\nBezbożne wskrzeszenie. Jeśli liczba twoich punktów "
        "wytrzymałości spadnie do 0, ale nie zginiesz od razu, możesz wywołać eksplozję śmiercionośnej energii. "
        "Każda wybrana przez ciebie istota w emanacji o promieniu 9 m wykonuje rzut obronny na Kondycję "
        "przeciwko ST rzutu obronnego przeciwko twoim czarom. Przy niepowodzeniu otrzymuje 2k10 plus twój "
        "modyfikator Charyzmy obrażeń nekrotycznych, a przy powodzeniu połowę tej wartości. Następnie liczba "
        "twoich punktów wytrzymałości zostaje ustawiona na dwukrotność twojego poziomu czarownika i zyskujesz "
        "1 poziom wyczerpania.\n\nPo użyciu tej korzyści musisz ukończyć krótki albo długi odpoczynek, "
        "zanim użyjesz jej ponownie."
    ),
    "h77baae07gb508ga5a7g250fg1e4e4b4a196c": (
        "Jeśli liczba twoich punktów wytrzymałości spadnie do 0, ale nie zginiesz od razu, możesz wywołać "
        "eksplozję śmiercionośnej energii. Każda wybrana przez ciebie istota w emanacji o promieniu 9 m "
        "wykonuje rzut obronny na Kondycję przeciwko ST rzutu obronnego przeciwko twoim czarom. Przy "
        "niepowodzeniu otrzymuje 2k10 plus twój modyfikator Charyzmy obrażeń nekrotycznych, a przy powodzeniu "
        "połowę tej wartości. Następnie liczba twoich punktów wytrzymałości zostaje ustawiona na dwukrotność "
        "twojego poziomu czarownika i zyskujesz 1 poziom wyczerpania."
    ),
    "h08797ed7gc753g8f41gd903g4ec54ed567d1": (
        "Kierujesz energię Morza Astralnego, uwalniając z siebie potok magii. Wybierz zimno albo światłość "
        "jako typ przekazywanej energii. Każda istota w stożku o długości 9 m wykonuje rzut obronny na "
        "Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego typu oraz dodatkowy efekt zależny od "
        "tego typu:\n\nZimno. Cel ma utrudnienie w następnym teście k20 wykonanym przed końcem twojej następnej "
        "tury.\nŚwiatłość. Cel zostaje Oślepiony do końca twojej następnej tury.\n\nPrzy powodzeniu cel otrzymuje "
        "tylko połowę obrażeń."
    ),
    "hcb079ee5g1c25gbdc5gf618gc2aef3acfd28": (
        'Cień. Cel zyskuje stan <LSTag Type="Status" Tooltip="INVISIBLE">Niewidzialności</LSTag> do końca '
        'swojej następnej tury albo do chwili, gdy wykona test ataku, zada obrażenia lub rzuci czar. Gdy '
        'Niewidzialność się kończy, każda istota w emanacji o promieniu 1,5 m wokół celu musi wykonać udany '
        'rzut obronny na Kondycję albo otrzymuje obrażenia nekrotyczne równe sumie dwóch rzutów kością twojej '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>.'
    ),
    "h373150f8gf513g0146g7190ge9494becea23": (
        "Tchórz. Cel oraz każda wybrana przez ciebie istota w emanacji o promieniu 9 m wokół niego musi "
        "wykonać udany rzut obronny na Mądrość albo zostaje Przerażona do początku twojej następnej tury. "
        "Przerażona istota ma szybkość zmniejszoną o połowę (zaokrąglając w dół) i może wykonać albo akcję, "
        "albo akcję dodatkową — nie obie."
    ),
    "h173fc315gc0d2g81edgd93dg3ddf2abd9626": (
        "Cel oraz każda wybrana przez ciebie istota w emanacji o promieniu 9 m wokół niego musi wykonać "
        "udany rzut obronny na Mądrość albo zostaje Przerażona do początku twojej następnej tury. Przerażona "
        "istota ma szybkość zmniejszoną o połowę (zaokrąglając w dół) i może wykonać albo akcję, albo akcję "
        "dodatkową — nie obie."
    ),
    "h1fe50343g3067g0a7cg5c9egd0f5250b5e84": (
        "Zyskujesz zdolność tworzenia kuli światła, która wybucha z niszczycielską siłą. W ramach akcji "
        "magicznie tworzysz kulę i rzucasz ją w wybrany punkt w promieniu 45 m. Tam przez krótką, lecz "
        "zabójczą chwilę eksploduje ona jako sfera światłości.\n\nKażda istota w kuli o promieniu 6 m musi "
        "wykonać udany rzut obronny na Kondycję albo otrzymuje 2k6 obrażeń od światłości. Istota znajdująca "
        "się za nieprzezroczystą pełną osłoną nie musi wykonywać tego rzutu.\n\nMożesz zwiększyć obrażenia, "
        "wydając punkty ki. Każdy wydany punkt, maksymalnie 3, zwiększa obrażenia o 2k6."
    ),
    "hc2eacb6dgfdd7gb76ag186cgecc6d2ed93b5": (
        "Teleportujesz się do widocznego, niezajętego miejsca w promieniu 9 m i do końca swojej następnej "
        "tury przybierasz półmaterialną postać. W tej postaci masz odporność na obrażenia obuchowe, kłute "
        "i cięte oraz niewrażliwość na Powalenie i Unieruchomienie."
    ),
    "h08615922g6a70gfeabg9ddeg3e421bcce131": (
        "Teleportujesz się do widocznego, niezajętego miejsca w promieniu 9 m i do końca swojej następnej "
        "tury przybierasz półmaterialną postać. W tej postaci masz odporność na obrażenia obuchowe, kłute "
        "i cięte oraz niewrażliwość na Powalenie i Unieruchomienie."
    ),
    "h2882b8f2g2c4dg9432gc6b0gd97aa3d6ec17": (
        "Teleportujesz się do widocznego, niezajętego miejsca w promieniu 9 m i do końca swojej następnej "
        "tury przybierasz półmaterialną postać. W tej postaci masz odporność na obrażenia obuchowe, kłute "
        "i cięte oraz niewrażliwość na Powalenie i Unieruchomienie."
    ),
    "he18e2299gab76g9494gca06g85d28e4049b1": (
        "Wikingowie to zaprawieni w boju wojownicy i żeglarze, którzy przemierzają morza Północy w poszukiwaniu "
        "chwały i łupów. Wyznawcy Drogi Łupieżcy kierują się własnym kodeksem honorowym, lecz podczas najazdów "
        "i wojny potrafią być bezlitośni. Słyną z mistrzowskiego władania włócznią i toporem oraz z wiary, "
        "że dzięki bohaterskim czynom na polu bitwy zasłużą na szczególne miejsce w salach umarłych."
    ),
    "h52252f05gb82agd434gc0a3g495ebfd2fb82": (
        "Legendy głoszą, że w pradawnych zakątkach świata czają się najstarsze i najbardziej krwiożercze "
        "potworności. Strażnicy pustki czczą takie istoty i czerpią z nich moc, przeobrażając się w bezlitosnych, "
        "potwornych obrońców przemierzających poszarpane wybrzeża, strome górskie turnie oraz inne mroczne "
        "i dzikie miejsca."
    ),
    "h1042549ag1908gfbe0g5f54g6b7fb0d8ba00": (
        "Podczas rzucania tego czaru wybierz jeden z poniższych efektów, który określa typ zadawanych "
        "obrażeń:\n\nPowietrze. Czar zadaje obrażenia od dźwięku. Każda istota, której nie powiedzie się "
        "rzut obronny, zostaje odepchnięta od ciebie o 3 m.\n\nZimny ogień. Czar zadaje obrażenia od zimna. "
        "Każda istota, której nie powiedzie się rzut obronny, zostaje Przerażona do początku twojej następnej "
        "tury.\n\nZiemia. Czar zadaje obrażenia obuchowe. Szybkość każdej istoty, której nie powiedzie się "
        "rzut obronny, zostaje zmniejszona do 0 do końca jej następnej tury.\n\nOgień. Czar zadaje obrażenia "
        "od ognia. Każda istota, której nie powiedzie się rzut obronny, staje w płomieniach i na koniec swojej "
        "następnej tury otrzymuje obrażenia od ognia. W ramach akcji może ugasić płomienie, dobrowolnie padając "
        "na ziemię i tarzając się. Ogień gaśnie również po polaniu wodą, zanurzeniu lub zduszeniu.\n\nWoda. "
        "Czar zadaje obrażenia od kwasu. Każda istota, której nie powiedzie się rzut obronny, zostaje Powalona."
        "\n\nKażda istota w stożku niszczycielskiej energii żywiołów o długości 9 m wykonuje rzut obronny na "
        "Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego typu, a przy powodzeniu połowę tej wartości."
    ),
    "hbdbf38edg682agb073g615cgd0646d705eb5": (
        "Powietrze. Czar zadaje obrażenia od dźwięku. Każda istota, której nie powiedzie się rzut obronny, "
        "zostaje odepchnięta od ciebie o 3 m.\n\nKażda istota w stożku niszczycielskiej energii żywiołów "
        "o długości 9 m wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego "
        "typu, a przy powodzeniu połowę tej wartości."
    ),
    "h7bd2461bgfa71g3829g28e1gaef49599b4e9": (
        "Zimny ogień. Czar zadaje obrażenia od zimna. Każda istota, której nie powiedzie się rzut obronny, "
        "zostaje Przerażona do początku twojej następnej tury.\n\nZiemia. Czar zadaje obrażenia obuchowe. "
        "Szybkość każdej istoty, której nie powiedzie się rzut obronny, zostaje zmniejszona do 0 do końca jej "
        "następnej tury.\n\nKażda istota w stożku niszczycielskiej energii żywiołów o długości 9 m wykonuje "
        "rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego typu, a przy powodzeniu "
        "połowę tej wartości."
    ),
    "hc45e0fa7gb4cege9f5g982fg7301666e820d": (
        "Ziemia. Czar zadaje obrażenia obuchowe. Szybkość każdej istoty, której nie powiedzie się rzut obronny, "
        "zostaje zmniejszona do 0 do końca jej następnej tury.\n\nKażda istota w stożku niszczycielskiej "
        "energii żywiołów o długości 9 m wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje "
        "obrażenia wybranego typu, a przy powodzeniu połowę tej wartości."
    ),
    "h8d7f1f17ge505g0aa1gebcag3a7e09bf05d6": (
        "Ogień. Czar zadaje obrażenia od ognia. Każda istota, której nie powiedzie się rzut obronny, staje "
        "w płomieniach i na koniec swojej następnej tury otrzymuje obrażenia od ognia. W ramach akcji może "
        "ugasić płomienie, dobrowolnie padając na ziemię i tarzając się. Ogień gaśnie również po polaniu wodą, "
        "zanurzeniu lub zduszeniu.\n\nKażda istota w stożku niszczycielskiej energii żywiołów o długości 9 m "
        "wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego typu, a przy "
        "powodzeniu połowę tej wartości."
    ),
    "haebb0bd5g858bg5610gf623g1dcd18a2a0dd": (
        "Woda. Czar zadaje obrażenia od kwasu. Każda istota, której nie powiedzie się rzut obronny, zostaje "
        "Powalona.\n\nKażda istota w stożku niszczycielskiej energii żywiołów o długości 9 m wykonuje rzut "
        "obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego typu, a przy powodzeniu połowę "
        "tej wartości."
    ),
    "h97c2a4b1gf596g1516g285eg988549b0ed6f": (
        "Przełamywanie koncentracji. Gdy zadasz obrażenia istocie utrzymującej koncentrację, ma ona utrudnienie "
        "w rzucie obronnym wykonywanym w celu jej podtrzymania.\n\nChroniony umysł. Gdy nie powiedzie ci się "
        "rzut obronny na Inteligencję, Mądrość albo Charyzmę, możesz zamiast tego odnieść powodzenie. Po użyciu "
        "tej korzyści musisz ukończyć krótki albo długi odpoczynek, zanim użyjesz jej ponownie."
    ),
    "hfc9071adg34ddg859egdda4g444a72c4713f": (
        "Przełamywanie koncentracji. Gdy zadasz obrażenia istocie utrzymującej koncentrację, ma ona utrudnienie "
        "w rzucie obronnym wykonywanym w celu jej podtrzymania.\n\nChroniony umysł. Gdy nie powiedzie ci się "
        "rzut obronny na Inteligencję, Mądrość albo Charyzmę, możesz zamiast tego odnieść powodzenie. Po użyciu "
        "tej korzyści musisz ukończyć krótki albo długi odpoczynek, zanim użyjesz jej ponownie."
    ),
    "h6ee711f7gf822ge79eg39abg3424b665f17d": (
        "Wywołujesz erupcję tlącego się piekielnego ognia wokół widocznej istoty w zasięgu."
    ),
    "h214e9d1dg45fcg6388gdc9cg6130d7c87cf2": (
        'Podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag> raz na turę możesz wypuścić macki '
        'cienistego dymu. Dym rozchodzi się na 3 m od ciebie we wszystkich kierunkach. Każda inna istota '
        'znajdująca się w dymie zostaje <LSTag Type="Status" Tooltip="BLINDED">Oślepiona</LSTag>.'
    ),
    "hc17eba4eg936fg2851g0508gb73011778121": (
        'Podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag> raz na turę możesz wypuścić macki '
        'cienistego dymu. Dym rozchodzi się na 3 m od ciebie we wszystkich kierunkach. Każda inna istota '
        'znajdująca się w dymie zostaje <LSTag Type="Status" Tooltip="BLINDED">Oślepiona</LSTag>.'
    ),
    "haf4865d4g944ag9cf5gf8b0g84b701adf954": (
        "Raz w każdej swojej turze, gdy wykonujesz atak bronią, możesz wykonać jeszcze jeden atak tą samą "
        "bronią przeciwko innej istocie. Musi się ona znajdować w promieniu 1,5 m od pierwotnego celu, "
        "w zasięgu broni, i nie może być przez ciebie zaatakowana wcześniej w tej turze."
    ),
    "hfd45d1c1g9dd3g206agfb7eg456c6af02ac0": (
        'Raz na <LSTag Tooltip="ShortRest">krótki odpoczynek</LSTag>, gdy podczas '
        '<LSTag Type="Status" Tooltip="RAGE">szału</LSTag> liczba twoich '
        '<LSTag Tooltip="HitPoints">punktów wytrzymałości</LSTag> miałaby spaść do [1], zamiast tego '
        'odzyskujesz punkty wytrzymałości w liczbie równej dwukrotności twojego poziomu barbarzyńcy '
        'i unikasz <LSTag Type="Status" Tooltip="DOWNED">Utraty przytomności</LSTag>.'
    ),
    "hd5f70284g45c5g71b8g7505g337ea5751295": (
        "Zyskujesz zdolność leczenia własnych ran. W ramach akcji dodatkowej możesz rzucić kością sztuk walki. "
        "Odzyskujesz punkty wytrzymałości w liczbie równej wynikowi rzutu plus twój modyfikator Mądrości "
        "(minimum 1 punkt).\n\nMożesz skorzystać z tej zdolności tyle razy, ile wynosi twój modyfikator Mądrości "
        "(minimum raz), a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h7d1b5755g3943g8854gdc14g83c3921a9c89": (
        'Przywołujesz widmowego rumaka w niezajętym miejscu obok celu, który natychmiast go dosiada.\n\n'
        'W każdej swojej turze rumak może wykonać jedną z następujących akcji: '
        '<LSTag Type="Spell" Tooltip="Shout_Dash">Sprint</LSTag>, Odstąpienie albo Unik.\n\n'
        'Gdy podczas jazdy na rumaku otrzymasz co najmniej 4 obrażenia, musisz wykonać rzut obronny na '
        'Zręczność o ST 8. Przy niepowodzeniu spadasz z rumaka i zostajesz Powalony na 1 turę.\n\n'
        'Rumaka może zobaczyć tylko gracz o czystym sercu.'
    ),
    "he5f0f47cg9e31g78f9g3de0gbcdc5fe67dd8": (
        'Przywołujesz widmowego rumaka w niezajętym miejscu obok celu, który natychmiast go dosiada.\n\n'
        'W każdej swojej turze rumak może wykonać jedną z następujących akcji: '
        '<LSTag Type="Spell" Tooltip="Shout_Dash">Sprint</LSTag>, Odstąpienie albo Unik.\n\n'
        'Gdy podczas jazdy na rumaku otrzymasz co najmniej 4 obrażenia, musisz wykonać rzut obronny na '
        'Zręczność o ST 8. Przy niepowodzeniu spadasz z rumaka i zostajesz Powalony na 1 turę.\n\n'
        'Rumaka może zobaczyć tylko gracz o czystym sercu.'
    ),
    "hfb72e3c9g9b45g5b84g8517gffe9d7e74d19": (
        'Możesz korzystać ze zdolności <LSTag Type="Spell" Tooltip="Target_FlurryOfHealing">Grad '
        'uzdrowienia</LSTag> i <LSTag Type="Spell" Tooltip="Target_FlurryOfHarm">Grad krzywdy</LSTag>.\n\n'
        'Łącznie możesz użyć tych korzyści tyle razy, ile wynosi twój modyfikator Mądrości (minimum raz). '
        'Wszystkie zużyte użycia odzyskujesz po długim odpoczynku.'
    ),
    "h4aa07c08gb93egab88g61e1g0ced3d3207e0": (
        "Gdy rzucasz czar co najmniej 1. poziomu uzyskany dzięki zdolności Psioniczne czary, możesz jak zwykle "
        "zużyć komórkę czaru albo wydać liczbę punktów magii równą poziomowi czaru. Czar rzucony za punkty "
        "magii nie wymaga komponentów werbalnych ani somatycznych. Nie wymaga też komponentów materialnych, "
        "chyba że czar je zużywa albo wskazuje ich koszt."
    ),
    "h9ff8c44bg3303gce13g6778gf58e24c5dda9": (
        "Twój patron uczy cię chronić umysł i ciało. Zyskujesz niewrażliwość na Zauroczenie.\n\nPonadto, "
        "natychmiast po tym, jak widoczna istota trafi cię testem ataku, możesz w ramach reakcji zmniejszyć "
        "otrzymane obrażenia o połowę (zaokrąglając w dół) i zadać napastnikowi obrażenia psychiczne równe "
        "obrażeniom, które ostatecznie otrzymasz."
    ),
    "h9fe00cb5g94cdg83e3g707ag20631bf85653": (
        "Natychmiast po tym, jak widoczna istota trafi cię testem ataku, możesz w ramach reakcji zmniejszyć "
        "otrzymane obrażenia o połowę (zaokrąglając w dół) i zadać napastnikowi obrażenia psychiczne równe "
        "obrażeniom, które ostatecznie otrzymasz."
    ),
    "ha4935cd2g4e6dg156ag2742g4ff317774e14": (
        "Po osiągnięciu 5. poziomu postaci możesz skupić smoczą magię i tymczasowo zyskać zdolność lotu. "
        "W ramach akcji dodatkowej wyrastają ci widmowe skrzydła. Utrzymują się przez 10 minut, dopóki ich "
        "nie schowasz (bez użycia akcji) albo nie zostaniesz Obezwładniony. W tym czasie zyskujesz szybkość "
        "lotu równą swojej szybkości. Skrzydła wyglądają, jakby powstały z tej samej energii co twoje zionięcie. "
        "Po użyciu tej cechy musisz ukończyć długi odpoczynek, zanim użyjesz jej ponownie."
    ),
    "h792db4a7g911aga472g7377ge4c0224fc65a": (
        "Po osiągnięciu 5. poziomu postaci możesz skupić smoczą magię i tymczasowo zyskać zdolność lotu. "
        "W ramach akcji dodatkowej wyrastają ci widmowe skrzydła. Utrzymują się przez 10 minut, dopóki ich "
        "nie schowasz (bez użycia akcji) albo nie zostaniesz Obezwładniony. W tym czasie zyskujesz szybkość "
        "lotu równą swojej szybkości. Skrzydła wyglądają, jakby powstały z tej samej energii co twoje zionięcie. "
        "Po użyciu tej cechy musisz ukończyć długi odpoczynek, zanim użyjesz jej ponownie."
    ),
    "hfa86f65dg33d6g9ea6g0948gfbf198214a31": (
        "Gdy używasz Kroku fey, przed teleportacją wybierz jedną widoczną istotę w promieniu 1,5 m od siebie. "
        "Musi wykonać udany rzut obronny na Mądrość albo zostaje Przerażona tobą do końca twojej następnej tury."
    ),
    "hee4eeb62g90f6g0d54g43a5g6045f299125f": (
        "Światło świtu pada na wybrany punkt w zasięgu. Do końca czaru lśni tam cylinder jasnego światła "
        "o promieniu 9 m i wysokości 12 m. Jest to światło słoneczne.\n\nGdy cylinder się pojawia, każda "
        "znajdująca się w nim istota wykonuje rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje 4k10 "
        "obrażeń od światłości, a przy powodzeniu połowę tej wartości. Istota wykonuje ten rzut również za każdym "
        "razem, gdy kończy turę w cylindrze.\n\nJeśli znajdujesz się w promieniu 18 m od cylindra, w ramach akcji "
        "dodatkowej możesz przesunąć go o maksymalnie 18 m."
    ),
    "h955ef661gc670g5024g8289g7b1595fc740c": (
        "Kosmiczna siła porządku przesyciła cię magią. Moc ta pochodzi z Mechanusa lub podobnej mu krainy — "
        "planu egzystencji ukształtowanego przez doskonale działające mechanizmy. Być może ty albo ktoś z "
        "twojego rodu został uwikłany w machinacje modronów, praworządnych istot zamieszkujących Mechanus. "
        "Możliwe nawet, że twój przodek wziął udział w Wielkim Marszu Modronów. Niezależnie od swego źródła "
        "tkwiąca w tobie moc porządku może wydawać się innym dziwna, lecz dla ciebie stanowi część rozległego "
        "i wspaniałego systemu."
    ),
    "h9ff8c44bg3303gce13g6778gf58e24c5dda9": (
        "Twój patron uczy cię chronić umysł i ciało. Zyskujesz niewrażliwość na Zauroczenie.\n\nPonadto "
        "natychmiast po tym, jak widoczna istota trafi cię testem ataku, możesz w ramach reakcji zmniejszyć "
        "otrzymane obrażenia o połowę (zaokrąglając w dół) i zadać napastnikowi obrażenia psychiczne równe "
        "obrażeniom, które ostatecznie otrzymasz."
    ),
    "h196d3642g2b8eg0c5ag525dg06fde33550c2": (
        "Atut: Uzdolniony\n\nLata, które cię ukształtowały, spędziłeś w skryptorium, klasztorze "
        "poświęconym zachowywaniu wiedzy albo urzędzie, gdzie nauczyłeś się pisać wyraźnym pismem i tworzyć "
        "starannie opracowane teksty. Być może sporządzałeś dokumenty państwowe lub przepisywałeś dzieła "
        "literackie. Możesz też mieć talent do poezji, prozy albo pracy naukowej. Przede wszystkim cechuje cię "
        "dbałość o szczegóły, dzięki której unikasz błędów w przepisywanych i tworzonych dokumentach."
    ),
    "he504b2a7g6a08gdabfgb8a9g1df72a68f86c": (
        "Atut: Uzdolniony\n\nChoć większość młodzieży w Chondath akceptuje czteroletni obowiązek służby "
        "wojskowej, buntowałeś się przeciwko tej autorytarnej próbie kontrolowania twojego życia. Wyrzekłeś "
        "się obywatelstwa, porzuciłeś nadane ci imię i pracowałeś jako korsarz na pierwszym statku, który "
        "chciał cię przyjąć. Od tamtej pory przemierzałeś Przesmyk Vilhon. Choć nigdy nie odpływałeś dalej "
        "niż kilkadziesiąt lig od lądu, nadrabiasz to rozległymi lokalnymi kontaktami i bogactwem doświadczeń."
    ),
    "h44bec492ga13fg76e5gfab8g3f1ba78481ca": (
        "Atut: Wtajemniczony (mag)\n\nChoć dżiny nie rządzą już Calimshanem, ich magia nadal jest "
        "powszechna w twojej ojczyźnie. Być może przypadkiem przywołałeś dżinna z magicznej lampy albo "
        "natrafiłeś na oazę strzeżoną przez marida. Dao mógł ocalić cię przed osuwiskiem, mogłeś też dobić "
        "targu z ifrytem w zamian za ulotne bogactwo. Jakkolwiek twój los skrzyżował się z losem dżina, to "
        "doświadczenie obdarzyło cię bystrym okiem, srebrnym językiem i niemałą dozą magii."
    ),
    "he15395feg34cbgfdbbgc738g75da56bca5d6": (
        "Atut: Dziki napastnik\n\nPrzez całe życie szkoliłeś się, by zostać członkiem Mistrzów Cienia — "
        "tajemniczej gildii złodziei, która zza kulis kontroluje krainę Thesk. Skradanie się i szybki refleks "
        "były jedynie początkiem twojej edukacji wśród Mistrzów Cienia; musiałeś również wyostrzyć swoją "
        "bezwzględność, by zapewnić bezpieczeństwo sekretom gildii. Jednak jeden błędny ruch doprowadził do "
        "twojego wygnania z zakonu. Teraz musisz podążać własną ścieżką."
    ),
    "hbeb4351eged06g5aa8g19cag2270bd60a6eb": (
        "Doświadczenie zdobyte podczas przetrwania w śmiertelnie niebezpiecznych miejscach pozwala ci "
        "wzmacniać nie tylko siebie, lecz także sojuszników. W ramach akcji Magii wybierz tyle widocznych "
        "istot, ile wynosi twój modyfikator Mądrości (co najmniej jedną). Każda wybrana istota odzyskuje "
        "punkty wytrzymałości w liczbie równej 1k10 plus twój poziom Łowcy i przez 1 godzinę ma ułatwienie "
        "w rzutach obronnych wykonywanych, aby uniknąć stanu Przerażenia lub go zakończyć.\n\nPo użyciu tej "
        "zdolności musisz ukończyć długi odpoczynek, zanim użyjesz jej ponownie."
    ),
    "h6827c922gd910gca98gee99gdbd9b0f178b1": (
        'Przybierz postać głębokiego rothé. W tej postaci możesz rzucać '
        '<LSTag Type="Spell" Tooltip="Target_DancingLights">Tańczące światła</LSTag> i atakować wrogów '
        '<LSTag Type="Spell" Tooltip="Rush_Rush_DeepRothe">Szarżą</LSTag>.'
    ),
    "hd9f88f32g2a3eg5ee1gdb45g1b062c876f03": (
        "Arcydiabły władające Siedmioma Miastami Piekła spiskują bez wytchnienia. Każdy z nich wiecznie "
        "knuje, jak podporządkować sobie pozostałych, zasiąść na Tronie Piekła, zjednoczyć Siedem Miast i "
        "wszystkie zamieszkujące je istoty piekielne oraz poprowadzić niewyczerpaną armię diabłów przez "
        "czasoprzestrzeń, aż spłoną wszystkie światy.\n\nIch elitarnymi agentami są illriggerzy. Ci piekielni "
        "rycerze, skrytobójcy, magowie i komandosi terroru panują nad polem bitwy, rozbijają ugrupowania "
        "wroga i realizują piekielne zamysły swego arcydiabła."
    ),
    "h5aa5a2a8gba10g31e1gabfeg038d2569ac84": (
        'Zyskujesz biegłość w umiejętności <LSTag Type="Skills" Tooltip="Stealth">Skradanie się</LSTag> '
        'oraz widzenie w ciemności. Ponadto zyskujesz możliwość '
        '<LSTag Type="Spell" Tooltip="Shout_Hide">Ukrycia się</LSTag> w ramach akcji dodatkowej.'
    ),
    "h28f9a741ga446ga31eg8889g3b0e1ddcb286": (
        "Jeśli wykonujesz test ataku czarem i chybisz, możesz wydać 1 Punkt Magii, aby ponownie rzucić k20; "
        "musisz wykorzystać nowy wynik.\n\nMożesz użyć Zaklęcia naprowadzającego nawet wtedy, gdy podczas "
        "rzucania tego czaru użyłeś już innej opcji metamagii."
    ),
    "h0089c30fg8c4dg346dg41fag7df171fac04f": (
        "Atut: Uderzenie olbrzymów\n\nChoć nie jesteś olbrzymem, dorastałeś pośród olbrzymów. Być może "
        "jako sierotę przygarnęła cię życzliwa rodzina kamiennych olbrzymów i wychowała jak własne dziecko. "
        "Możliwe też, że żyłeś w odciętej od świata prehistorycznej krainie pełnej olbrzymów, przerażających "
        "kolosów i potężnych dinozaurów.\n\nCoś w twoim otoczeniu — być może pożywienie lub woda, pierwotna "
        "magia przenikająca twój dom albo nałożone na ciebie bujne błogosławieństwo wzrostu — sprawiło, że "
        "osiągnąłeś niezwykłe rozmiary jak na przedstawiciela swojego gatunku. Dzięki tej magii nauczyłeś się "
        "ucieleśniać potęgę olbrzymów. Przywykłeś do życia w świecie znacznie większym od ciebie, co znajduje "
        "odzwierciedlenie w twoich umiejętnościach, nastawieniu i spojrzeniu na życie.\n\nUderzenie olbrzymów. "
        "Raz na turę, gdy trafisz cel atakiem bronią do walki wręcz albo atakiem dystansowym bronią miotaną, "
        "możesz nasycić atak dodatkowym efektem zależnym od wybranej korzyści: Chmur, Ognia, Mrozu, Wzgórz, "
        "Kamienia albo Burzy."
    ),
    "he0ef5905gc6d4gce1ag48ceg2478a264ead0": (
        "Od zarania dziejów śmiałkowie spoglądali niebezpieczeństwu prosto w oczy i walczyli z potworami. "
        "Przeżywali ci, którzy byli dostatecznie roztropni, by odpowiednio się uzbroić i dokładnie wiedzieć, "
        "gdzie uderzyć — albo rozpoznać chwilę, gdy należy się wycofać i wrócić z nowym planem.\n\nCzłonkowie "
        "Gildii Rzeźbiarzy to łowcy potworów wzywani zwykle wtedy, gdy osadzie zagraża bezpośrednie "
        "niebezpieczeństwo, a nie ma armii ani milicji, która mogłaby jej pomóc. Rzeźbiarze bez wahania "
        "wyruszają na spotkanie śmierci, uzbrojeni w lata treningu i wiedzę przekazywaną przez poprzedników."
    ),
    "h197a4fbbg54d8g3303g20b2ga713257e8f7a": (
        "Zyskujesz premię do rzutów obronnych na Kondycję równą twojemu modyfikatorowi Mądrości (minimum "
        "+1).\n\nPonadto raz na turę, gdy w postaci uzyskanej dzięki "
        '<LSTag Type="Passive" Tooltip="HollowWarden_3_WrathOfTheWild">Gniewowi dziczy</LSTag> trafisz '
        "istotę testem ataku, odzyskujesz punkty wytrzymałości w liczbie równej 1k10 plus twój modyfikator "
        "Mądrości, o ile w chwili trafienia jesteś Zakrwawiony."
    ),
    "h9978d0deg7d77g5755g43fbg0caf50e3b407": (
        "Moce twojego patrona głęboko odmieniają twoje ciało i magię, zapewniając następujące korzyści.\n\n"
        "Tajemna nekroza. Obrażenia nekrotyczne zadawane twoimi atakami, czarami Czarownika i zdolnościami "
        "Czarownika ignorują odporność na obrażenia nekrotyczne.\n\nGroźna nekroza. Rzucane przez ciebie "
        'czary i wykonywane ataki ignorują <LSTag Tooltip="Resistant">odporność</LSTag> na obrażenia '
        "nekrotyczne. Ponadto, gdy zadajesz obrażenia nekrotyczne czarem, w rzucie nie może wypaść [1].\n\n"
        "Nieumarła wytrzymałość. Nie musisz spać, a magia nie może cię uśpić."
    ),
    "h20a9acf5g3464g7749g7665g0da6684092ca": (
        'Objęta emanacją czaru <LSTag Type="Spell" Tooltip="Target_ConjureElementals_Minor_Container">'
        'Przywołanie mniejszego żywiołaka</LSTag>: podłoże pod tą istotą jest trudnym terenem, a ataki '
        'rzucającego zadają jej dodatkowe obrażenia.'
    ),
    "hf46c88e2g570bgc9f5g75e9g56ae359baec0": (
        "Gdy widoczna istota w promieniu 9 m od ciebie otrzyma obrażenia i stanie się Zakrwawiona (jej punkty "
        "wytrzymałości spadną poniżej [1]%), lecz nie spadnie do 0 punktów wytrzymałości, możesz w ramach "
        "reakcji teleportować się na widoczne wolne pole w promieniu 1,5 m od niej. Następnie możesz wykonać "
        "przeciwko niej jeden atak wręcz."
    ),
    "h0ffef888g07e1g2e7dgf090g1e02c22995ae": (
        "Ty albo jedna widoczna istota w promieniu 9 m od ciebie zyskuje tymczasowe punkty wytrzymałości "
        "w liczbie równej 1k4 plus twój modyfikator Charyzmy."
    ),
    "h15b91354gf2d6ga550g86cag97a1796054d7": (
        'Możesz nasycać swoje ciosy boską mocą. W każdej twojej turze, gdy twój '
        '<LSTag Type="Status" Tooltip="RAGE">szał</LSTag> jest aktywny, pierwsza istota trafiona przez ciebie '
        "bronią albo atakiem bez broni otrzymuje dodatkowe obrażenia w liczbie równej 1k6 plus połowa twojego "
        "poziomu Barbarzyńcy (zaokrąglając w dół). Za każdym razem wybierasz, czy dodatkowe obrażenia są "
        "nekrotyczne, czy od światłości."
    ),
    "h16aa8ef8g9057g8804g10e3g6c754af3589d": (
        "Gdy otrzymasz obrażenia od celu objętego twoją Klątwą, możesz w ramach reakcji zmniejszyć te obrażenia "
        "o 2k8 plus twój modyfikator Charyzmy. Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator "
        "Charyzmy, a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h179791c5gff57g15ddg6254g9297c342cf48": (
        "Gdy chybisz testem ataku dystansowego z użyciem broni, możesz zużyć jedną kość ryzyka (bez użycia "
        "akcji), aby zadać tej istocie obrażenia w liczbie równej wynikowi rzutu kością plus twój modyfikator "
        "Zręczności (co najmniej 1). Obrażenia są tego samego typu co obrażenia broni, a ich wartość może "
        "wzrosnąć wyłącznie wskutek zwiększenia modyfikatora cechy. Możesz użyć tego manewru tylko raz na turę."
    ),
    "h19bace45g8db7g181dgc420ge0fc17190c49": (
        'Gdy aktywujesz <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, twoje rysy wykrzywiają się, a ciało '
        "nabrzmiewa. Istoty, które ani teraz, ani wcześniej nie widziały twojej przemiany, nie rozpoznają cię. "
        "Ponadto podczas szału zyskujesz następujące korzyści:\n\nZamiast zwykłych obrażeń ataku bez broni "
        "możesz rzucić 1k8.\n\nGdy trafisz istotę atakiem bez broni, możesz odepchnąć ją o 3 m albo zmusić "
        "do wykonania rzutu obronnego na Kondycję o ST równym 8 plus twój modyfikator Siły i premia z "
        "biegłości. Przy niepowodzeniu istota otrzymuje stan Powalenia.\n\nZasięg twoich ataków bez broni "
        "zwiększa się o 1,5 m."
    ),
    "h1a0652aag04b6g8cb4gead0g81c1b91c9fb6": (
        "W ramach akcji dodatkowej stajesz się ucieleśnieniem przerażającej mocy swojego patrona. Poniższe "
        "korzyści utrzymują się przez 1 minutę, do chwili otrzymania stanu Obezwładnienia albo do zakończenia "
        "przemiany (bez użycia akcji). Możesz przemienić się tyle razy, ile wynosi twój modyfikator Charyzmy "
        "(co najmniej raz), a wszystkie zużyte użycia odzyskujesz po długim odpoczynku.\n\nPozór życia. "
        "Zyskujesz tymczasowe punkty wytrzymałości w liczbie równej 1k10 plus twój poziom Czarownika.\n\n"
        "Nieustraszona postać. Zyskujesz niewrażliwość na Przerażenie. Jeśli podczas przemiany jesteś "
        "Przerażony, stan ten natychmiast się kończy.\n\nPrzerażający awatar. Raz na turę, gdy trafisz istotę "
        "testem ataku, możesz zmusić ją do wykonania rzutu obronnego na Mądrość przeciwko twojemu ST obrony "
        "przed czarami. Przy niepowodzeniu cel otrzymuje stan Przerażenia do końca twojej następnej tury."
    ),
    "h211b59f7g914aga7a2gaf0eg6d3b97922133": (
        "Możesz otoczyć się ochronną magią. Gdy rzucasz czar odpychania z użyciem komórki czaru, możesz "
        "jednocześnie wykorzystać pasmo jego magii, aby stworzyć na sobie magiczną powłokę działającą do "
        "końca następnego długiego odpoczynku. Maksymalna liczba punktów wytrzymałości powłoki jest równa "
        "dwukrotności twojego poziomu Maga plus twój modyfikator Inteligencji. Za każdym razem, gdy otrzymujesz "
        "obrażenia, zamiast ciebie otrzymuje je powłoka. Jeśli masz odporność albo podatność na te obrażenia, "
        "uwzględnij ją przed odjęciem punktów wytrzymałości powłoki. Gdy obrażenia zmniejszą jej punkty "
        "wytrzymałości do 0, pozostałe obrażenia otrzymujesz ty. Powłoka z 0 punktów wytrzymałości nie może "
        "pochłaniać obrażeń, ale jej magia pozostaje aktywna.\n\nZa każdym razem, gdy rzucasz czar odpychania "
        "z użyciem komórki czaru, powłoka odzyskuje punkty wytrzymałości w liczbie równej dwukrotności poziomu "
        "tej komórki. Możesz też w ramach akcji dodatkowej zużyć komórkę czaru, aby przywrócić powłoce punkty "
        "wytrzymałości w liczbie równej dwukrotności poziomu zużytej komórki."
    ),
    "h26010d04g5728g38d0g7666g1a3a63e82e9a": (
        "Możesz nasycać broń energią psioniczną. Raz w każdej swojej turze, natychmiast po trafieniu atakiem "
        "celu w promieniu 9 m i zadaniu mu obrażeń bronią, możesz zużyć kość energii psionicznej. Rzuć tą "
        "kością; cel otrzymuje obrażenia od mocy w liczbie równej wynikowi plus twój modyfikator Inteligencji."
    ),
    "h269da4dcg7dabg981bg4001gfcda57b7c806": (
        "Bohaterska dusza. Na początku każdej swojej tury możesz wydać 1 punkt zaklinania, aby zyskać "
        "tymczasowe punkty wytrzymałości w liczbie równej 1k6 plus twój poziom Zaklinacza (bez użycia "
        "akcji).\n\nWrodzone władanie ostrzem. Gdy aktywna jest twoja zdolność Wrodzona magia i atakujesz "
        "bronią, w której masz biegłość, do testów ataku i rzutów obrażeń możesz używać modyfikatora Charyzmy "
        "zamiast modyfikatora Siły albo Zręczności.\n\nWyszkolenie bojowe. Zyskujesz biegłość w broni "
        "bojowej oraz wyszkolenie w lekkich i średnich pancerzach, a także tarczach."
    ),
    "h2bd86b9fg5a4bg7828gd29cg98815c2ef7d3": (
        'Wędrowiec. Cel zyskuje tymczasowe punkty wytrzymałości w liczbie równej wynikowi rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> plus twój '
        'poziom Barda. Dopóki cel ma te tymczasowe punkty wytrzymałości, jego szybkość zwiększa się o 3 m.'
    ),
    "h59958a6fg7ff5g9780g1b47g688c0909621b": (
        "Druidzi z Kręgu Snów pochodzą z krain silnie związanych z Feywild i jego sennymi domenami. Opieka nad "
        "światem natury czyni ich naturalnymi sprzymierzeńcami fey o dobrym charakterze. Druidzi ci pragną "
        "wypełniać świat cudami rodem ze snów. Ich magia leczy rany i niesie radość strapionym sercom, a "
        "chronione przez nich krainy są jasne i urodzajne — sen miesza się tam z rzeczywistością, a znużeni "
        "mogą znaleźć odpoczynek."
    ),
    "h5e78186dgabebg2b99g11acg070fef938db4": (
        "Twój pakt czerpie moc z Feywild. Wybierając tę podklasę, możesz zawrzeć układ z potężną istotą "
        "arcyfey, taką jak Książę Mrozu, Królowa Powietrza i Ciemności władająca Dworem Zmierzchu, Tytania z "
        "Letniego Dworu albo pradawna wiedźma. Możesz też zwrócić się do całego kręgu fey i utkać sieć "
        "przysług oraz długów. Kimkolwiek jest twój patron, często pozostaje nieprzenikniony i kapryśny."
    ),
    "h60b4a6b6g2c59g4b4cgb657g5872fb1a68d4": (
        "Otacza cię tajemnicza aura fey — dar istoty arcyfey albo skutek przemiany w jednym z miejsc Feywild. "
        "Niezależnie od tego, jak zdobyłeś magię fey, jesteś teraz Wędrowcem Fey. Twój radosny śmiech podnosi "
        "na duchu uciśnionych, a biegłość w walce napełnia wrogów grozą. Wesołość fey jest bowiem wielka, a "
        "ich gniew straszliwy."
    ),
    "h7eb96189g76dfg2301gb96dg3136060e0f85": (
        "Magia Feywild strzeże twojego umysłu. Zyskujesz niewrażliwość na Zauroczenie i Przerażenie."
    ),
    "h6dd099beg03a7ga0aeg02e2gf58c867f0877": (
        "Eladriny to elfy z Feywild — krainy niebezpiecznego piękna i bezkresnej magii. Dzięki tej magii "
        "eladrin może w mgnieniu oka przemieścić się z miejsca na miejsce. Każdy eladrin współbrzmi też z "
        "emocjami zaklętymi w Feywild pod postacią pór roku; powinowactwo to wpływa na jego nastrój i wygląd. "
        "Pora roku eladrina może się zmieniać, choć niektóre eladriny pozostają przy jednej na zawsze. Wybierz "
        "swoją porę roku albo wykonaj rzut zgodnie z tabelą Pory roku eladrinów. Cecha Trans pozwala ci "
        "zmieniać swoją porę roku."
    ),
    "h776cf198gb898g803bg64d1gcb1e15218f5e": (
        "Eladriny to elfy z Feywild — krainy niebezpiecznego piękna i bezkresnej magii. Dzięki tej magii "
        "eladrin może w mgnieniu oka przemieścić się z miejsca na miejsce. Każdy eladrin współbrzmi też z "
        "emocjami zaklętymi w Feywild pod postacią pór roku; powinowactwo to wpływa na jego nastrój i wygląd. "
        "Pora roku eladrina może się zmieniać, choć niektóre eladriny pozostają przy jednej na zawsze. Wybierz "
        "swoją porę roku albo wykonaj rzut zgodnie z tabelą Pory roku eladrinów. Cecha Trans pozwala ci "
        "zmieniać swoją porę roku."
    ),
    "hf21fda8cg4f60g9873gab75g019ed5359331": (
        "Eladriny to elfy z Feywild — krainy niebezpiecznego piękna i bezkresnej magii. Dzięki tej magii "
        "eladrin może w mgnieniu oka przemieścić się z miejsca na miejsce. Każdy eladrin współbrzmi też z "
        "emocjami zaklętymi w Feywild pod postacią pór roku; powinowactwo to wpływa na jego nastrój i wygląd. "
        "Pora roku eladrina może się zmieniać, choć niektóre eladriny pozostają przy jednej na zawsze. Wybierz "
        "swoją porę roku albo wykonaj rzut zgodnie z tabelą Pory roku eladrinów. Cecha Trans pozwala ci "
        "zmieniać swoją porę roku.\n\nPodobnie jak inne elfy, eladriny mogą żyć ponad 750 lat."
    ),
    "h623638f6g1485g2672g2bfcg30f7140b3b47": (
        "Eladriny to elfy z Feywild — krainy niebezpiecznego piękna i bezkresnej magii. Dzięki tej magii "
        "eladrin może w mgnieniu oka przemieścić się z miejsca na miejsce. Każdy eladrin współbrzmi też z "
        "emocjami zaklętymi w Feywild pod postacią pór roku; powinowactwo to wpływa na jego nastrój i wygląd. "
        "Pora roku eladrina może się zmieniać, choć niektóre eladriny pozostają przy jednej na zawsze. Wybierz "
        "swoją porę roku albo wykonaj rzut zgodnie z tabelą Pory roku eladrinów. Cecha Trans pozwala ci "
        "zmieniać swoją porę roku.\n\nPodobnie jak inne elfy, eladriny mogą żyć ponad 750 lat."
    ),
    "hae52b795gd7a8gaf4fg82deg89900f2668fe": (
        "Shadar-kai to elfy ze Sfery Cieni, pierwotnie przyciągnięte do tej budzącej grozę krainy przez Królową "
        "Kruków. Przez stulecia część z nich nadal jej służyła, inni zaś wyruszyli do Sfery Materialnej, aby "
        "wykuć własny los."
    ),
    "h08121305g3bafgf931g892bga7643105c0e6": (
        "Shadar-kai to elfy ze Sfery Cieni, pierwotnie przyciągnięte do tej budzącej grozę krainy przez Królową "
        "Kruków. Przez stulecia część z nich nadal jej służyła, inni zaś wyruszyli do Sfery Materialnej, aby "
        "wykuć własny los."
    ),
    "h446ae020gdccdg2b5bgde5ag55622edba1a8": (
        "Shadar-kai to elfy ze Sfery Cieni, pierwotnie przyciągnięte do tej budzącej grozę krainy przez Królową "
        "Kruków. Przez stulecia część z nich nadal jej służyła, inni zaś wyruszyli do Sfery Materialnej, aby "
        "wykuć własny los.\n\nNiegdyś shadar-kai byli istotami fey, podobnie jak pozostali elfi pobratymcy. "
        "Dziś, odmienieni przez ponurą energię Sfery Cieni, trwają na pograniczu życia i śmierci.\n\nShadar-kai "
        "mają skórę w odcieniach popiołu, a podczas pobytu w Sferze Cieni stają się wysuszeni i pomarszczeni, "
        "odzwierciedlając posępny charakter tej mrocznej sfery.\n\nPodobnie jak inne elfy, shadar-kai mogą "
        "żyć ponad 750 lat."
    ),
})

# Identical source rows are repeated for class progression and passive tooltips.
# Reuse the reviewed wording so those copies cannot drift apart.
for duplicate_uid in (
    "h60b8e3b3ge993g7677ge82egd9590a175841",
    "ha34e254dg39c8gc52bg7259gaa9e2bf59233",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h1a0652aag04b6g8cb4gead0g81c1b91c9fb6"]

UID_OVERRIDES["h790e3622gdcc2g6592g9c95g8de8f0b70afa"] = (
    "W ramach akcji dodatkowej stajesz się ucieleśnieniem przerażającej mocy swojego patrona. Poniższe "
    "korzyści utrzymują się przez 1 minutę, do chwili otrzymania stanu Obezwładnienia albo do zakończenia "
    "przemiany (bez użycia akcji). Możesz przemienić się tyle razy, ile wynosi twój modyfikator Charyzmy "
    "(co najmniej raz), a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
)
UID_OVERRIDES["h36874237g25b1g47eag13bdg179ffd6b4ec6"] = (
    "Raz na turę, gdy trafisz istotę testem ataku, możesz zmusić ją do wykonania rzutu obronnego na Mądrość "
    "przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu cel otrzymuje stan Przerażenia do końca "
    "twojej następnej tury."
)
UID_OVERRIDES.update({
    "hc7d9adccgd21cg6730g04c3g3a1c38c6c5a9": (
        'Ukochany. Cel odzyskuje punkty wytrzymałości w liczbie równej wynikowi rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> plus twój '
        'modyfikator Charyzmy.'
    ),
    "h5b47bba7gdab8g8410ga59dgef9c6100ab29": (
        'Strzelec wyborowy. Cel otrzymuje obrażenia od mocy w liczbie równej wynikowi rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> plus twój '
        'modyfikator Charyzmy.'
    ),
    "he73898ceg2342gac1agce15gffad564f5c59": (
        'Mściciel. Do końca twojej następnej tury każda istota, która trafi cel testem ataku wręcz, otrzymuje '
        'obrażenia od mocy w liczbie równej wynikowi rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>.'
    ),
    "h53224a2ag2d24g306bg844dge14be06ef6b9": (
        'Oszust. Cel wykonuje rzut obronny na Mądrość. Przy niepowodzeniu otrzymuje obrażenia psychiczne w '
        'liczbie równej dwóm wynikom rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> i ma stan '
        'Zauroczenia do początku twojej następnej tury. Przy powodzeniu otrzymuje połowę tych obrażeń.'
    ),
    "h809e5f68g6c1fg087fg4ebbgd6a42f20a3f2": (
        'Cel odzyskuje punkty wytrzymałości w liczbie równej wynikowi rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> plus twój '
        'modyfikator Charyzmy.'
    ),
    "ha93da29dg5863g46a5gb636gdc16581b4520": (
        'Cel otrzymuje obrażenia od mocy w liczbie równej wynikowi rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> plus twój '
        'modyfikator Charyzmy.'
    ),
    "h3c143767g21a8g66bcg6a21gf96dcfb36b88": (
        'Cel zyskuje tymczasowe punkty wytrzymałości w liczbie równej wynikowi rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> plus twój '
        'poziom Barda. Dopóki je ma, jego szybkość zwiększa się o 3 m.'
    ),
    "h8bd54844g8c51g684dg0147ga45b20304d23": (
        'Cel wykonuje rzut obronny na Mądrość. Przy niepowodzeniu otrzymuje obrażenia psychiczne w liczbie '
        'równej dwóm wynikom rzutu kością '
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag> i ma stan '
        'Zauroczenia do początku twojej następnej tury. Przy powodzeniu otrzymuje połowę tych obrażeń.'
    ),
    "h0da58492g230cg424fg00cdg006fb672dd4d": (
        "Wykonujesz zamaszysty ruch bronią używaną do rzucenia czaru, po czym znikasz i uderzasz niczym "
        "wicher. Pojawiasz się obok widocznej istoty w zasięgu i wykonujesz przeciwko niej atak czarem "
        "wręcz. Następnie przemykasz między pobliskimi wrogami i ponawiasz atak, uderzając łącznie do pięciu "
        "różnych istot. Każdy trafiony cel otrzymuje [1]."
    ),
    "h1fc6d592gcc27gfae8g9211ge723a0f1c0e7": (
        'Nawiedź istotę jej najgorszymi koszmarami. W każdej turze otrzymuje [1] oraz ma '
        '<LSTag Tooltip="Disadvantage">utrudnienie</LSTag> w '
        '<LSTag Tooltip="AbilityCheck">testach cech</LSTag> i '
        '<LSTag Tooltip="AttackRoll">testach ataku</LSTag>.'
    ),
    "hea231ad3g2d3cg3aedge6d0ge22e99d5107a": (
        "Wskazujesz miejsce w zasięgu. Pędzi ku niemu świetlista kula kwasu o średnicy 0,3 m, która wybucha "
        "w sferze o promieniu 6 m. Każda istota na tym obszarze wykonuje rzut obronny na Zręczność. Przy "
        "niepowodzeniu otrzymuje [1], a kolejne [2] na koniec swojej następnej tury. Przy powodzeniu otrzymuje "
        "tylko połowę początkowych obrażeń."
    ),
    "h61a4b68fgff5eg7169g07bfg95aab5c70a68": (
        "Unosisz broń używaną do rzucenia czaru i wykonujesz nią atak wręcz przeciwko jednej istocie w "
        "promieniu 1,5 m. Po trafieniu cel odczuwa zwykłe skutki ataku bronią, a ty możesz sprawić, że zielony "
        "ogień przeskoczy z niego na inną widoczną istotę w promieniu 1,5 m. Druga istota otrzymuje [1]."
    ),
    "hee7efdd5g7678gd390g9d02gfa6d6bde145c": (
        "Unosisz broń używaną do rzucenia czaru i wykonujesz nią atak wręcz przeciwko jednej istocie w "
        "promieniu 1,5 m. Po trafieniu cel odczuwa zwykłe skutki ataku bronią i emanuje mroczną energią do "
        "początku twojej następnej tury. Jeśli wcześniej wykona atak albo rzuci czar, otrzymuje [1], a czar "
        "się kończy."
    ),
    "h0799ae05gc440g5f2bg286ega9d23975a5e2": (
        "Dopóki cel jest Unieruchomiony kajdanami, na początku każdej swojej tury otrzymuje [1]. Na koniec "
        "każdej swojej tury może powtórzyć rzut obronny; przy powodzeniu odrzuca kajdany."
    ),
    "h3b399006gee4aga14cgffd2g777d4701d99c": (
        "Wirujące sztylety wypełniają powietrze. Każda istota, która zakończy turę w wirze, otrzymuje [1]."
    ),
    "h64efa14bg9e10g4990g8b4ag0101bcc881a9": (
        "Istotę spowija palące światło słoneczne. Na koniec każdej swojej tury otrzymuje [1]. Przy udanym "
        "rzucie obronnym nadal otrzymuje połowę obrażeń."
    ),
    "h1158b478ge2c6g812bgbf23gffe3f6e81257": (
        "Ciskasz wijącym się pociskiem krwi w istotę w zasięgu. Wykonaj przeciwko niej test ataku czarem "
        "dystansowym. Po trafieniu cel otrzymuje [1], a ty zyskujesz tymczasowe punkty wytrzymałości w liczbie "
        "równej swojej premii z biegłości."
    ),
    "hbbc19e32g5427g3585gaaabg3a72c966a807": (
        'Zadaj dodatkowe obrażenia od trucizny w liczbie równej '
        '<LSTag Tooltip="ProficiencyBonus">premii z biegłości</LSTag>. Po trafieniu otocz cel trującą chmurą, '
        'która może <LSTag Type="Status" Tooltip="POISONED">zatruć</LSTag> znajdujące się w niej istoty.'
    ),
    "hbd729210g3700g0c6dgfe28g7b0dc91aaae7": (
        "Przepastny wzrok. Zyskujesz widzenie w ciemności o zasięgu 18 m. Jeśli już masz widzenie w ciemności "
        "z innego źródła, jego zasięg zwiększa się o 18 m.\n\nRzut kamieniem. W ramach akcji dodatkowej możesz "
        "chwycić kamień i wykonać nim magiczny atak w jednym z dwóch wariantów: dystansowy atak bez broni "
        "oparty na Sile albo dystansowy atak czarem oparty na cesze bazowej dla twoich czarów. Oba warianty "
        "mają zasięg 18 m. Po trafieniu kamień zadaje 1k10 obrażeń od mocy, a cel musi wykonać udany rzut "
        "obronny na Siłę albo otrzymuje stan Powalenia. Możesz wykonać tę akcję dodatkową tyle razy, ile "
        "wynosi twoja premia z biegłości, a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "hc7b891e9gd9c0g1617g0233ga492c5e47dc7": (
        "Strzelanie w walce wręcz. Obecność wroga w promieniu 1,5 m nie powoduje utrudnienia w twoich testach "
        "ataku z kuszy.\n\nRaniący bełt. Gdy trafisz istotę atakiem dystansowym, możesz nałożyć na nią stan "
        '<LSTag Type="Status" Tooltip="GAPING_WOUND">Rozdzierających ran</LSTag>.'
    ),
    "h75559935g2e90ga5d1g57b2g1393773adde2": (
        "W ramach akcji dodatkowej możesz aktywować runę i wejść w stan proroczy na 1 minutę albo do chwili "
        "Obezwładnienia. Dopóki ten stan trwa, gdy ty albo inna widoczna istota w promieniu 18 m wykonuje test "
        "ataku, rzut obronny lub test cechy, możesz w ramach reakcji zapewnić temu rzutowi ułatwienie albo "
        "utrudnienie."
    ),
    "hf2959cc8g6d39ge50dg36c2gf91080392da0": (
        "Gdy ty albo inna widoczna istota w promieniu 18 m wykonuje test ataku, rzut obronny lub test cechy, "
        "możesz w ramach reakcji zapewnić temu rzutowi utrudnienie."
    ),
    "h33322b0egd4a5g9e80gdabdg3abd5d4b2ddc": (
        "Wybierz znajdujący się w zasięgu przedmiot o wadze od około 0,5 do 2,5 kg, którego nikt nie trzyma ani "
        "nie nosi. Przedmiot leci po linii prostej na odległość do 18 m w wybranym kierunku, a następnie spada "
        "na ziemię. Zatrzymuje się wcześniej, jeśli uderzy w twardą powierzchnię. Jeśli miałby uderzyć w "
        "istotę, wykonuje ona rzut obronny na Zręczność. Przy niepowodzeniu przedmiot trafia cel i zatrzymuje "
        "się. Gdy przedmiot w coś uderzy, zarówno on, jak i trafiony cel otrzymują obrażenia obuchowe."
    ),
    "hca055ee6g46b2g0e20gb49ag38f4471f10d5": (
        "Aura wiru. W ramach akcji dodatkowej otaczasz się aurą magicznego wichru i błyskawic, która sięga "
        "na 3 m od ciebie w każdym kierunku, lecz nie przenika przez pełną osłonę. Aura trwa do początku "
        "twojej następnej tury albo do chwili Obezwładnienia. Podczas jej działania masz odporność na obrażenia "
        "od elektryczności i dźwięku, a testy ataku przeciwko tobie mają utrudnienie. Ponadto za każdym razem, "
        "gdy inna istota rozpoczyna turę w aurze, możesz zmusić ją do wykonania rzutu obronnego na Siłę o ST "
        "równym 8 plus twoja premia z biegłości i wyższy z twoich modyfikatorów: Mądrości albo Charyzmy. Przy "
        "niepowodzeniu szybkość istoty zmniejsza się o połowę do początku jej następnej tury. Możesz wykonać tę "
        "akcję dodatkową tyle razy, ile wynosi twoja premia z biegłości, a wszystkie zużyte użycia odzyskujesz "
        "po długim odpoczynku."
    ),
    "h2b241e12gfd0agfaa6g72ddgad9ce029a10e": (
        "W ramach akcji dodatkowej otaczasz się aurą magicznego wichru i błyskawic, która sięga na 3 m od "
        "ciebie w każdym kierunku, lecz nie przenika przez pełną osłonę. Aura trwa do początku twojej następnej "
        "tury albo do chwili Obezwładnienia. Podczas jej działania masz odporność na obrażenia od elektryczności "
        "i dźwięku, a testy ataku przeciwko tobie mają utrudnienie. Ponadto za każdym razem, gdy inna istota "
        "rozpoczyna turę w aurze, możesz zmusić ją do wykonania rzutu obronnego na Siłę o ST równym 8 plus "
        "twoja premia z biegłości i wyższy z twoich modyfikatorów: Mądrości albo Charyzmy. Przy niepowodzeniu "
        "szybkość istoty zmniejsza się o połowę do początku jej następnej tury."
    ),
    "h846f6dc8g12d1g0e7ag1408g6768106740df": (
        "Podczas działania aury masz odporność na obrażenia od elektryczności i dźwięku, a testy ataku "
        "przeciwko tobie mają utrudnienie. Ponadto za każdym razem, gdy inna istota rozpoczyna turę w aurze, "
        "możesz zmusić ją do wykonania rzutu obronnego na Siłę o ST równym 8 plus twoja premia z biegłości i "
        "wyższy z twoich modyfikatorów: Mądrości albo Charyzmy. Przy niepowodzeniu szybkość istoty zmniejsza "
        "się o połowę do początku jej następnej tury."
    ),
    "h7fd38532g43ebgdddagfdb3gcddfd6e82835": (
        "Przejawiasz magię burzy właściwą olbrzymom burzowym, co zapewnia ci następujące korzyści:\n\nAura "
        "wiru. W ramach akcji dodatkowej otaczasz się aurą magicznego wichru i błyskawic, która sięga na 3 m "
        "od ciebie w każdym kierunku, lecz nie przenika przez pełną osłonę. Aura trwa do początku twojej "
        "następnej tury albo do chwili Obezwładnienia. Podczas jej działania masz odporność na obrażenia od "
        "elektryczności i dźwięku, a testy ataku przeciwko tobie mają utrudnienie. Ponadto za każdym razem, gdy "
        "inna istota rozpoczyna turę w aurze, możesz zmusić ją do wykonania rzutu obronnego na Siłę o ST równym "
        "8 plus twoja premia z biegłości i wyższy z twoich modyfikatorów: Mądrości albo Charyzmy. Przy "
        "niepowodzeniu szybkość istoty zmniejsza się o połowę do początku jej następnej tury. Możesz wykonać tę "
        "akcję dodatkową tyle razy, ile wynosi twoja premia z biegłości, a wszystkie zużyte użycia odzyskujesz "
        "po długim odpoczynku."
    ),
})

UID_OVERRIDES["h70f68e2egfe60g8371gc262g13645f286d18"] = (
    UID_OVERRIDES["h75559935g2e90ga5d1g57b2g1393773adde2"]
)

for duplicate_uid in (
    "h28a36b4cg27b2gab96g42b0gbade6f8162f6",
    "h32d2aff6ga0b0g13a1g550dgd7e4309b96fb",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h1fc6d592gcc27gfae8g9211ge723a0f1c0e7"]

for duplicate_uid in (
    "hb80e1becg530fgfb62gb3a6gb00bb6635067",
    "hdaa04befg3a9bg9a3dga72eg04c235ed8c01",
    "h46e9e82fg3994g14dageffdg4ecef2102490",
    "he983b2f2gd458g80bdg28d9g76d209dcf6d6",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h3b399006gee4aga14cgffd2g777d4701d99c"]

UID_OVERRIDES.update({
    "hde644cc1g1dc6g103bg095ege867e6fa22ad": (
        "Gdy otrzymujesz obrażenia od istoty znajdującej się w promieniu [1] od ciebie, możesz w ramach "
        "reakcji wykonać przeciwko niej jeden atak wręcz bronią albo atak bez broni."
    ),
    "he5c89bffgb42ege4daga349g64ec3fecb28f": (
        "W ramach akcji Magii kierujesz Święty Symbol na inną widoczną istotę w promieniu [1] od siebie i "
        "skupiasz na niej boską energię. Przywracasz jej punkty wytrzymałości albo zmuszasz ją do wykonania "
        "rzutu obronnego na Kondycję. Przy niepowodzeniu istota otrzymuje obrażenia nekrotyczne albo od "
        "światłości (według twojego wyboru). Przy powodzeniu otrzymuje połowę tych obrażeń (zaokrąglając w dół)."
    ),
    "hbb7ccd06g2737gdcf2gc167g21f32c9615fb": (
        "Z ciebie wybucha płonący blask, tworząc emanację o promieniu [1]. Każda wybrana przez ciebie istota, "
        "którą widzisz w jej obrębie, musi wykonać udany rzut obronny na Kondycję albo otrzymuje obrażenia od "
        "światłości."
    ),
    "ha7d55e66g6f97ga4b7g45b4g5829f0c36910": (
        "Gdy widoczna istota w promieniu [1] od ciebie wykonuje test ataku, możesz w ramach reakcji zapewnić "
        "temu testowi utrudnienie, wywołując rozbłysk światła, zanim atak trafi albo chybi.\n\nMożesz użyć "
        "tej zdolności tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz), a wszystkie zużyte "
        "użycia odzyskujesz po długim odpoczynku."
    ),
    "h6c1ab5a0g8a40g1755g2eacg01f53db2903f": (
        "Gdy widoczna istota w promieniu 9 m od ciebie wykonuje test ataku, możesz w ramach reakcji zapewnić "
        "temu testowi utrudnienie, wywołując rozbłysk światła, zanim atak trafi albo chybi."
    ),
    "hc973bce4g12d2g5a53g43a8g98cefe571124": (
        'Dopóki trwa twój <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, możesz w ramach reakcji uderzyć '
        "widmowymi gałęziami Drzewa Świata i przyciągnąć widoczną istotę w promieniu 9 m od siebie. Cel musi "
        "wykonać udany rzut obronny na Siłę (ST 8 + twój modyfikator Siły + premia z biegłości) albo zostaje "
        "przyciągnięty do 6 m prosto w twoją stronę. Po przyciągnięciu celu możesz zmniejszyć jego szybkość "
        "do 0 do początku swojej następnej tury."
    ),
    "h1d68851cgda5ag5482g75f2gc0f7b6817b16": (
        'Dopóki trwa twój <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, możesz w ramach reakcji uderzyć '
        "widmowymi gałęziami Drzewa Świata i przyciągnąć widoczną istotę w promieniu 9 m od siebie. Cel musi "
        "wykonać udany rzut obronny na Siłę (ST 8 + twój modyfikator Siły + premia z biegłości) albo zostaje "
        "przyciągnięty do 6 m prosto w twoją stronę. Po przyciągnięciu celu możesz zmniejszyć jego szybkość "
        "do 0 do początku swojej następnej tury."
    ),
    "hd5d65420g6479g285bg4c8ag03e208bc40e5": (
        'Dopóki trwa twój <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, pierwsza istota, którą trafisz w '
        "każdej swojej turze bronią albo atakiem bez broni, otrzymuje dodatkowe obrażenia od światłości równe "
        "sumie 1k6 i połowy twojego poziomu barbarzyńcy (zaokrąglonej w dół)."
    ),
    "h47b388afge0d2g2240g7d34g00c0f0fbd7f3": (
        'Dopóki trwa twój <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, pierwsza istota, którą trafisz w '
        "każdej swojej turze bronią albo atakiem bez broni, otrzymuje dodatkowe obrażenia nekrotyczne równe "
        "sumie 1k6 i połowy twojego poziomu barbarzyńcy (zaokrąglonej w dół)."
    ),
    "h650ea344gc449g2751g4692g5f60cf3d64d3": (
        "Tworzysz chwilowy krąg widmowych ostrzy, które omiatają przestrzeń wokół ciebie. Wszystkie pozostałe "
        "istoty w promieniu 1,5 m od ciebie muszą wykonać udany rzut obronny na Zręczność albo otrzymują [1]."
    ),
    "h6a4c6bc1g64e8gd02bg6b68g3e2d7bb52c48": (
        "Gdy widoczna istota trafia testem ataku inną istotę w promieniu [1] od ciebie, możesz w ramach reakcji "
        "zmniejszyć obrażenia otrzymane przez cel o 1k10 plus twoja premia z biegłości. Aby skorzystać z tej "
        "reakcji, musisz trzymać tarczę albo broń prostą lub bojową."
    ),
    "h2f17ec6fgaccfg9489ga33dg5178d82df62d": (
        "Gdy widoczna istota trafia testem ataku inną istotę w promieniu 1,5 m od ciebie, możesz w ramach "
        "reakcji zmniejszyć obrażenia otrzymane przez cel o 1k10 plus twoja premia z biegłości. Aby skorzystać "
        "z tej reakcji, musisz trzymać tarczę albo broń prostą lub bojową."
    ),
    "hbc14bfc3g2a23g0472g6c3bg1d7d1cdd6c67": (
        "Gdy widoczna istota atakuje inny cel niż ty, znajdujący się w promieniu [1] od ciebie, możesz w ramach "
        "reakcji zasłonić go trzymaną tarczą. Zapewniasz utrudnienie wywołującemu reakcję testowi ataku oraz "
        "wszystkim pozostałym testom ataku przeciwko temu celowi aż do początku swojej następnej tury, o ile "
        "pozostajesz w promieniu [1] od niego."
    ),
    "h7d366d57g2abcg334egec99gd574e5abbc31": (
        "W ramach akcji Magii możesz zużyć jedno użycie Dzikiej Postaci i wybrać punkt w promieniu 18 m od "
        "siebie. W sferze o promieniu 3 m, której środkiem jest ten punkt, pojawiają się na chwilę życiodajne "
        "kwiaty i ciernie wysysające życie. Wrogie istoty w sferze otrzymują 2k6 obrażeń nekrotycznych. "
        "Pozostałe istoty na tym obszarze odzyskują 2k6 punktów wytrzymałości.\n\nObrażenia i leczenie "
        "zwiększają się o 1k6 na 5. poziomie druida (3k6) i ponownie na 10. poziomie (4k6)."
    ),
    "hfce3b1a5gd494ge7ddge2b2gaa37f42771ce": (
        "Cel musi wykonać udany rzut obronny na Kondycję przeciwko twojemu ST obrony przed czarami albo "
        "otrzymuje obrażenia od zimna, a jeśli ma rozmiar duży lub mniejszy, zostaje odepchnięty do 4,5 m od "
        "ciebie. Aby określić obrażenia, rzuć tyloma k6, ile wynosi twój modyfikator Mądrości."
    ),
    "ha4121401g58f8gaedagc70dg1c134e1ef50a": (
        "Skrywasz w sobie źródło energii psionicznej, którą reprezentują kości energii psionicznej napędzające "
        "moce tej podklasy. Wraz z kolejnymi poziomami wojownika rosną liczba i rozmiar tych kości: na 3. "
        "poziomie masz cztery k6, na 5. poziomie sześć k8, na 9. poziomie osiem k8, a na 11. poziomie osiem "
        "k10.\n\nZdolności tej podklasy korzystające z kości energii psionicznej mogą używać wyłącznie jej "
        "kości. Niektóre moce zużywają kość zgodnie ze swoim opisem; nie możesz użyć takiej mocy, jeśli nie "
        "masz już żadnych niewykorzystanych kości energii psionicznej.\n\nPo krótkim odpoczynku odzyskujesz "
        "jedną zużytą kość energii psionicznej, a po długim odpoczynku — wszystkie.\n\nPole ochronne. Gdy ty "
        "albo inna widoczna istota w promieniu 9 m od ciebie otrzymuje obrażenia, możesz w ramach reakcji zużyć "
        "jedną kość energii psionicznej i nią rzucić. Zmniejszasz obrażenia o sumę wyniku rzutu i swojego "
        "modyfikatora Inteligencji (co najmniej o 1), tworząc chwilową osłonę z telekinetycznej mocy.\n\n"
        "Uderzenie psioniczne. Możesz nasycać broń siłą psioniczną. Raz na turę, natychmiast po trafieniu "
        "atakiem celu w promieniu 9 m od siebie i zadaniu mu obrażeń bronią, możesz zużyć kość energii "
        "psionicznej i nią rzucić. Cel otrzymuje obrażenia od mocy równe sumie wyniku rzutu i twojego "
        "modyfikatora Inteligencji.\n\nRuch telekinetyczny. Możesz poruszać przedmiotami i istotami za pomocą "
        "umysłu. W ramach akcji Magii wybierz widoczny cel w promieniu 9 m od siebie. Musi nim być luźny "
        "przedmiot o rozmiarze dużym lub mniejszym albo chętna istota inna niż ty. Przenosisz cel do 9 m na "
        "widoczne, niezajęte miejsce. Jeśli celem jest maleńki przedmiot, możesz zamiast tego przenieść go do "
        "swojej dłoni albo z niej."
    ),
    "hf80d830cg06deg648eg0d39g7c78218f5482": (
        "W ramach akcji Magii możesz wydać 1 punkt skupienia, dotknąć istoty i przywrócić jej punkty "
        "wytrzymałości w liczbie równej sumie wyniku rzutu kością Sztuk Walki i twojego modyfikatora Mądrości."
        "\n\nGdy używasz akcji dodatkowej wymagającej wydania punktu skupienia, możesz skorzystać z tej zdolności "
        "bez wydawania kolejnego punktu skupienia."
    ),
    "h0fc86f08g49ceg3decg4adfg5398a052f261": (
        "W ramach akcji Magii możesz wydać 1 punkt skupienia, dotknąć istoty i przywrócić jej punkty "
        "wytrzymałości w liczbie równej sumie wyniku rzutu kością Sztuk Walki i twojego modyfikatora Mądrości."
    ),
    "h94d2b863gce81ge85ag20a9gd351c1d2fbe8": (
        "Możesz zużyć jedno użycie Mocy przysięgi i rozdzielić tymczasowe punkty wytrzymałości między wybrane "
        "istoty w promieniu 9 m od siebie, wliczając w to siebie. Ich łączna liczba wynosi 2k8 plus twój poziom "
        "paladyna; rozdzielasz je między wybrane istoty według własnego uznania."
    ),
    "h46a88a7bg99ddgbfe4gc4aeg5843b027814d": (
        "Możesz zużyć jedno użycie Mocy przysięgi i rozdzielić tymczasowe punkty wytrzymałości między wybrane "
        "istoty w promieniu 9 m od siebie, wliczając w to siebie. Ich łączna liczba wynosi 2k8 plus twój poziom "
        "paladyna; rozdzielasz je między wybrane istoty według własnego uznania."
    ),
    "he4b6fb34g750cgd80agfb13ga652ce65321c": (
        "Twoje połączenie ze sferą absolutnego ładu pozwala ci porządkować chwile chaosu. Gdy widoczna istota "
        "w promieniu 18 m od ciebie ma wykonać rzut k20 z ułatwieniem albo utrudnieniem, możesz w ramach reakcji "
        "sprawić, że ułatwienie ani utrudnienie nie wpłynie na ten rzut.\n\nMożesz użyć tej zdolności tyle razy, "
        "ile wynosi twój modyfikator Charyzmy (co najmniej raz), a wszystkie zużyte użycia odzyskujesz po długim "
        "odpoczynku."
    ),
    "hbc25fac8gb48eg59a1gb63eg766af1e2e342": (
        "Twoje połączenie ze sferą absolutnego ładu pozwala ci porządkować chwile chaosu. Gdy widoczna istota "
        "w promieniu 18 m od ciebie ma wykonać rzut k20 z ułatwieniem albo utrudnieniem, możesz w ramach reakcji "
        "sprawić, że ułatwienie ani utrudnienie nie wpłynie na ten rzut."
    ),
    "h34d645ffgccd0g672cg5920g5e1aa15ee5a7": (
        "Natychmiast po teleportacji ty oraz jedna widoczna istota w promieniu 3 m od ciebie zyskujecie po "
        "1k10 tymczasowych punktów wytrzymałości."
    ),
    "h67022386g828fg30bag1c0cg215dae9c4f39": (
        'Nieumarłe istoty, które trafiają noszącą osobę, otrzymują [1]. Bestie, które ją trafiają, otrzymują '
        '<LSTag Type="Status" Tooltip="CHARMED">stan Zauroczenia</LSTag>.'
    ),
    "h008b1355g9855gf610g8c06gec5ceab5ab6f": (
        "Po zakończeniu krótkiego lub długiego odpoczynku możesz dać inspirujący występ — wygłosić przemowę, "
        "zaśpiewać albo zatańczyć. Z tej zdolności możesz skorzystać raz na krótki odpoczynek. Każdy sojusznik "
        "w promieniu 9 m od ciebie zyskuje wówczas tymczasowe punkty wytrzymałości w liczbie równej sumie "
        "poziomu swojej postaci i twojej premii z biegłości."
    ),
    "hbba7650bg2c8bga26fga741g9eb4b22d5870": (
        "Twoje sztuczki zadające obrażenia wpływają nawet na istoty, które unikają najgroźniejszych skutków. "
        "Gdy rzucasz sztuczkę na istotę i chybiasz testem ataku albo cel wykonuje udany rzut obronny przeciwko "
        "sztuczce, otrzymuje on połowę jej obrażeń (jeśli je zadaje), ale nie doznaje żadnych dodatkowych efektów."
    ),
    "h347e6fe4g42a8g22ecgdb29gefc97f004483": (
        "Tworzysz długą, wysysającą życie mackę cienia, którą uderzasz widoczną istotę w zasięgu.\n\nWykonaj "
        "przeciwko celowi test ataku czarem dystansowym. Po trafieniu cel otrzymuje obrażenia nekrotyczne. "
        "Ponownie wykonaj rzut kośćmi obrażeń czaru i zyskaj tymczasowe punkty wytrzymałości w liczbie równej "
        "wynikowi."
    ),
})

for duplicate_uid in (
    "h3e1aea80g4740gaa01gfe95g3cd0d19d1bdd",
    "h2ee98c20g6713gb372g573dgca45f15d691f",
    "hbbfab3begf9cdg6052g4ac5g7eaf747c1f9a",
    "h063372f4g1033g08f6g55abgb32a96fe2615",
):
    UID_OVERRIDES[duplicate_uid] = (
        "Osłonę reprezentuje tyle k8, ile punktów zaklinania wydano na jej utworzenie. Gdy osłonięta istota "
        "otrzymuje obrażenia, może zużyć dowolną liczbę tych kości i nimi rzucić, aby zmniejszyć obrażenia o "
        "sumę wyników."
    )

UID_OVERRIDES["h5d57e46bg1ebeg7a15g45a1g5dee2e76459e"] = UID_OVERRIDES[
    "h3e1aea80g4740gaa01gfe95g3cd0d19d1bdd"
]

for duplicate_uid in (
    "ha3aeca2ag84a7g9aa2gc23cg0d41a7036cc2",
    "hfe85ad95g8cb3g8eecg7ca9g7f8ee3255f42",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h008b1355g9855gf610g8c06gec5ceab5ab6f"]

UID_OVERRIDES.update({
    "h2b042bbdga167g0335g0c96gd2fc48c2ea13": (
        "Przywołujesz duchy natury, które przez czas trwania czaru przemykają wokół ciebie w emanacji o "
        "promieniu 3 m. Za każdym razem, gdy emanacja obejmie pole widocznej istoty, a także wtedy, gdy widoczna "
        "istota wejdzie w emanację lub zakończy w niej turę, możesz zmusić ją do wykonania rzutu obronnego na "
        "Mądrość. Przy niepowodzeniu otrzymuje obrażenia od mocy, a przy powodzeniu — połowę tych obrażeń. "
        "Dana istota wykonuje ten rzut nie częściej niż raz na turę.\n\nPonadto przez czas trwania czaru możesz "
        "wykonywać Odstąpienie w ramach akcji dodatkowej."
    ),
    "h621ec36dg3794g4862g4538gb2c4399f06cd": (
        'Gdy widoczna istota w promieniu 9 m od ciebie otrzymuje obrażenia, możesz w ramach reakcji sprawić, '
        'że twoja <LSTag Type="Passive" Tooltip="ArcaneWard">magiczna powłoka</LSTag> pochłonie te obrażenia.'
    ),
    "h5bee8c93gf2c8gd340g65cfge6d42d8c4a32": (
        "Możesz użyć Mocy przysięgi, aby emanować aurą grozy. Zmuszasz każdą wybraną przez siebie widoczną "
        "istotę w promieniu 9 m od ciebie do wykonania rzutu obronnego na Mądrość. Przy niepowodzeniu istota "
        "otrzymuje stan Przerażenia na 1 minutę. Na koniec każdej swojej tury może powtórzyć rzut obronny; "
        "powodzenie kończy ten stan."
    ),
    "h391dd984g6a8cge5b0g94c0g187d5c88d2a9": (
        'Rzuć kością <LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>. '
        "Istota zyskuje tymczasowe punkty wytrzymałości w liczbie równej sumie wyniku rzutu i twojego "
        "modyfikatora Charyzmy (co najmniej 2). Gdy istota zyskuje tymczasowe punkty wytrzymałości w ten "
        "sposób, może natychmiast w ramach reakcji przemieścić się na odległość do swojej szybkości bez "
        "prowokowania ataków okazyjnych albo wykonać akcję Uniku."
    ),
    "h0c4b99c4g1ad3gb7f0g11fbgb55e06b4ac67": (
        "W swojej turze możesz w ramach akcji dodatkowej zakończyć ten czar, sprawiając, że broń rozbłyśnie "
        "światłością. Każda wybrana przez ciebie widoczna istota w promieniu 9 m od broni musi wykonać rzut "
        "obronny na Kondycję. Przy niepowodzeniu otrzymuje 4k8 obrażeń od światłości i stan Oślepienia na "
        "1 minutę. Przy powodzeniu otrzymuje połowę tych obrażeń i nie zostaje oślepiona. Oślepiona istota "
        "może powtórzyć rzut obronny na koniec każdej swojej tury; powodzenie kończy ten stan."
    ),
    "h995a037cg1d3bg4dbcg8935g9bbef7559f53": (
        "Lśni tu walec palącego światła słonecznego. Istoty znajdujące się w nim w chwili jego pojawienia się "
        "oraz kończące w nim turę otrzymują [1]. Przy udanym rzucie obronnym nadal otrzymują połowę obrażeń."
    ),
    "hcade1749gdcc0g1f97g1533gca440242cfde": (
        "Możesz użyć Mocy przysięgi, aby nasycić swoją obecność ochronną mocą wiary. Wybierz widoczne istoty "
        "w promieniu 9 m od siebie w liczbie nieprzekraczającej twojego modyfikatora Charyzmy (co najmniej "
        "jedną). Przez 1 minutę ty i wybrane istoty wykonujecie z ułatwieniem rzuty obronne na Inteligencję, "
        "Mądrość i Charyzmę."
    ),
    "h4a8a3d05ged7ag55e3g1276g814259823391": (
        "Natychmiast po użyciu Kroku Fey każda wybrana przez ciebie widoczna istota w promieniu 1,5 m od "
        "ciebie otrzymuje obrażenia od ognia równe twojej premii z biegłości."
    ),
    "h7d9f76degac92g087cg01abg39b7a8899657": (
        "Jedna wybrana przez ciebie widoczna istota w zasięgu słyszy w swoim umyśle dysonansową melodię. Cel "
        "wykonuje rzut obronny na Mądrość. Przy niepowodzeniu otrzymuje obrażenia psychiczne i musi poświęcić "
        "swoją następną turę, aby oddalić się od ciebie tak bardzo, jak zdoła. Przy powodzeniu otrzymuje tylko "
        "połowę obrażeń."
    ),
    "h162775ecg7b9egc133g5182g07c9126dbe3d": (
        'Dopóki trwa twój <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, możesz używać '
        '<LSTag Type="Spell" Tooltip="Shout_PackHowl_Barbarian">Pobudzającego wycia</LSTag>, a twoi '
        'sojusznicy wykonują z <LSTag Tooltip="Advantage">ułatwieniem</LSTag> '
        '<LSTag Tooltip="AttackRoll">testy ataku</LSTag> przeciwko wrogom w promieniu [1] od ciebie.'
    ),
    "h4384b84egd766gbe0ag574age428758d17bf": (
        "Natychmiast po tym, jak widoczna istota w promieniu 9 m od ciebie trafi cię testem ataku i zada ci "
        "obrażenia, możesz w ramach reakcji odpowiedzieć wyczarowanym podmuchem lodu. Istota musi wykonać rzut "
        "obronny na Kondycję (ST wynosi 8 + twoja premia z biegłości + wyższy z twoich modyfikatorów: Siły "
        "albo Mądrości). Przy niepowodzeniu otrzymuje obrażenia od zimna równe sumie 1k8 i twojej premii z "
        "biegłości, a jej szybkość zmniejsza się do 0 do końca jej następnej tury."
    ),
    "he83b406cg6857g3e88gd60dg2ef8a8d31d88": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie Dzikiej Postaci, aby przejawić otaczającą cię "
        "emanację morskiej bryzy o promieniu 1,5 m. Emanacja kończy się wcześniej, jeśli ją zakończysz (bez "
        "użycia akcji), przejawisz ponownie albo otrzymasz stan Obezwładnienia.\n\nGdy przejawiasz emanację, "
        "a także w ramach akcji dodatkowej w kolejnych turach, możesz wybrać inną widoczną istotę w jej "
        "obrębie. Cel musi wykonać udany rzut obronny na Kondycję przeciwko twojemu ST obrony przed czarami "
        "albo otrzymuje obrażenia od zimna, a jeśli ma rozmiar duży lub mniejszy, zostaje odepchnięty do 4,5 m "
        "od ciebie. Aby określić obrażenia, rzuć tyloma k6, ile wynosi twój modyfikator Mądrości."
    ),
    "h5e33a0bdg4748gf679g1d0fg141a368e3366": (
        "Zrodzony z lodu. Masz odporność na obrażenia od zimna.\n\nLodowy odwet. Natychmiast po tym, jak "
        "widoczna istota w promieniu 9 m od ciebie trafi cię testem ataku i zada ci obrażenia, możesz w ramach "
        "reakcji odpowiedzieć wyczarowanym podmuchem lodu. Istota musi wykonać rzut obronny na Kondycję (ST "
        "wynosi 8 + twoja premia z biegłości + wyższy z twoich modyfikatorów: Siły albo Mądrości). Przy "
        "niepowodzeniu otrzymuje obrażenia od zimna równe sumie 1k8 i twojej premii z biegłości, a jej "
        "szybkość zmniejsza się do 0 do końca jej następnej tury. Możesz użyć tej reakcji tyle razy, ile wynosi "
        "twoja premia z biegłości, a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h6f92df19gb6e4g35bcga428gb96710c1d8ac": (
        "Przejawiasz lodową moc właściwą olbrzymom lodowym, co zapewnia ci następujące korzyści:\n\nZrodzony "
        "z lodu. Masz odporność na obrażenia od zimna.\n\nLodowy odwet. Natychmiast po tym, jak widoczna "
        "istota w promieniu 9 m od ciebie trafi cię testem ataku i zada ci obrażenia, możesz w ramach reakcji "
        "odpowiedzieć wyczarowanym podmuchem lodu. Istota musi wykonać rzut obronny na Kondycję (ST wynosi 8 "
        "+ twoja premia z biegłości + wyższy z twoich modyfikatorów: Siły albo Mądrości). Przy niepowodzeniu "
        "otrzymuje obrażenia od zimna równe sumie 1k8 i twojej premii z biegłości, a jej szybkość zmniejsza się "
        "do 0 do końca jej następnej tury. Możesz użyć tej reakcji tyle razy, ile wynosi twoja premia z "
        "biegłości, a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
})

for duplicate_uid in (
    "haf633c9dg1492gf659gb336g2332cda3f768",
    "h96663848g22b6g4fd3g0749gcca87a42edab",
    "hfbad83efgcb7cg321ag47a0g402ce027568b",
    "hc98c1c9egd99agca86ged41g2a76a0c61645",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h2b042bbdga167g0335g0c96gd2fc48c2ea13"]

for duplicate_uid in (
    "hcd21cc8fgd961g0feeg16afgf78a1e0a3fba",
    "h221aec9fgee6dgf291gdaedg74950253b4a2",
    "h97912cc4g21bfg2c6egbd0cgbc22ad403d83",
    "h6df157b5g12d3g2b2bgd643g1dd6b4025001",
    "hb4209506g884fg3190g8d94g0432d0658315",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h621ec36dg3794g4862g4538gb2c4399f06cd"]

UID_OVERRIDES.update({
    "hc58f0177g4e5fgb789g4272g3e57d5e733b0": (
        "Więź z nieumarłością przenika twoje ciało i zapewnia ci następujące korzyści.\n\nNekrotyczna "
        "odporność. Masz odporność na obrażenia nekrotyczne. Podczas korzystania z Postaci Grozy zyskujesz "
        "niewrażliwość na obrażenia nekrotyczne.\n\nBezbożne wskrzeszenie. Gdy twoje punkty wytrzymałości "
        "spadną do 0, ale nie zginiesz od razu, możesz sprawić, że twoje ciało wybuchnie śmiercionośną energią. "
        "Każda wybrana przez ciebie istota w emanacji o promieniu 9 m, której źródłem jesteś, wykonuje rzut "
        "obronny na Kondycję przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu otrzymuje obrażenia "
        "nekrotyczne równe sumie 2k10 i twojego modyfikatora Charyzmy, a przy powodzeniu — połowę tych obrażeń. "
        "Następnie twoje punkty wytrzymałości wynoszą dwukrotność twojego poziomu czarownika, a ty zyskujesz "
        "1 poziom Wyczerpania.\n\nPo użyciu tej korzyści musisz ukończyć krótki albo długi odpoczynek, zanim "
        "użyjesz jej ponownie."
    ),
    "h0397fcaag1719g76a6g53f7g803d71e9392d": (
        "Przejawiasz wytrzymałość właściwą olbrzymom wzgórzowym, co zapewnia ci następujące korzyści:"
        "\n\nPrzedmurze. Gdy zostajesz poddany efektowi, który nadałby ci stan Powalenia, możesz w ramach reakcji "
        "zachować równowagę i nie otrzymać tego stanu.\n\nŻelazny żołądek. Za każdym razem, gdy odzyskujesz "
        "punkty wytrzymałości, odzyskujesz dodatkowe punkty w liczbie równej swojemu modyfikatorowi Kondycji."
    ),
    "h6c2e1510g127eg4a2eg3cbfg9e940ea8f6e8": (
        "Wymaga co najmniej 7. poziomu illriggera.\n\nGdy spalasz co najmniej jedną pieczęć na objętej "
        "interdyktem istocie, możesz w ramach reakcji wywołać wokół niej wybuch piekielnej energii. Każda "
        "wybrana przez ciebie istota w promieniu 3 m od celu wykonuje rzut obronny na Zręczność. Przy "
        "niepowodzeniu otrzymuje tyle samo obrażeń tego samego typu, ile pieczęcie zadały objętej interdyktem "
        "istocie, a przy powodzeniu — połowę tych obrażeń."
    ),
    "hf03822e2g7af0g67edg9165g36461a798fbc": (
        "Twój Tajemny Pancerz zyskuje dodatkowe korzyści zależne od modelu.\n\nPancernik. Kość obrażeń "
        "Niszczyciela Mocy zwiększa się do 2k6 obrażeń od mocy. Ponadto twój zasięg zwiększa się o 3 m."
        "\n\nObrońca. Kość obrażeń Impulsu Gromu zwiększa się do 1k10 obrażeń od dźwięku. Ponadto za każdym "
        "razem, gdy widoczna istota zbliża się do ciebie na odległość do 1,5 m, możesz wykonać przeciwko niej "
        "atak okazyjny.\n\nInfiltrator. Kość obrażeń Wyrzutni Błyskawic zwiększa się do 2k6 obrażeń od "
        "elektryczności. Każda istota, która otrzyma obrażenia od elektryczności z Wyrzutni Błyskawic, zostaje "
        "Porażona."
    ),
    "hb63bc4e3g2375g28c1gc6f9g87176ffa864b": (
        "Tworzone przez ciebie Niesamowite Działo staje się bardziej niszczycielskie i zapewnia następujące "
        "korzyści.\n\nDetonacja. Gdy otrzymujesz obrażenia, możesz w ramach reakcji rozkazać działu "
        "detonować. Każda wroga istota w promieniu 6 m od ciebie wykonuje rzut obronny na Zręczność przeciwko "
        "twojemu ST obrony przed czarami. Przy niepowodzeniu otrzymuje 3k10 obrażeń od mocy, a przy powodzeniu "
        "— połowę tych obrażeń. Z tej zdolności możesz skorzystać raz na krótki odpoczynek.\n\nSiła ognia. "
        "Rzuty obrażeń działa oraz liczba tymczasowych punktów wytrzymałości zapewnianych przez Obrońcę "
        "zwiększają się o 1k8."
    ),
    "h1acefdf8gda2eg7c3cg5653ge46c213d3330": (
        "Wiesz, że najskuteczniejszym sposobem zabicia potwora jest trafienie we właściwej chwili w jego "
        "najczulszy punkt. Za wcześnie — cios ześlizgnie się po celu. Za późno — potwór może cię wypatroszyć."
        "\n\nGdy widoczna istota w promieniu 18 m od ciebie obiera ciebie albo inną istotę za cel ataku wręcz "
        "lub dystansowego, możesz w ramach reakcji wykonać przeciwko napastnikowi jeden atak bronią."
    ),
    "h49e72c1cg2d7bgc3fbg7e56gdbf9203830ad": (
        "Gdy otrzymujesz obrażenia od celu objętego twoją Klątwą, możesz w ramach reakcji zmniejszyć je o 2k8 "
        "plus swój modyfikator Charyzmy. Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator "
        "Charyzmy, a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h58289e87g34a5g2ffdg308dge576a637a4d7": (
        "Grzmot burzy (olbrzym burzowy). Gdy otrzymujesz obrażenia od istoty w promieniu 18 m od ciebie, możesz "
        "w ramach reakcji zadać jej 1k8 obrażeń od dźwięku."
    ),
    "hfe6b221fg701bg9db4gdb32ga44f7bac6573": (
        "Gdy się przemieniasz oraz na początku każdej swojej kolejnej tury, każda wybrana przez ciebie istota "
        "w emanacji o promieniu 3 m, której źródłem jesteś, wykonuje rzut obronny na Mądrość przeciwko twojemu "
        "ST obrony przed czarami. Przy niepowodzeniu otrzymuje stan Przerażenia do początku twojej następnej tury."
    ),
})

UID_OVERRIDES["hf03aeb95g5dbbg3147g324cg388502cbfe2e"] = UID_OVERRIDES[
    "h49e72c1cg2d7bgc3fbg7e56gdbf9203830ad"
]

UID_OVERRIDES["h573bf455gce7agc4a2gb934gf7147ae4c160"] = UID_OVERRIDES[
    "h5bee8c93gf2c8gd340g65cfge6d42d8c4a32"
]
UID_OVERRIDES["h55809fbag7bd0g427fgaea4gcc7103f95f2c"] = UID_OVERRIDES[
    "hcade1749gdcc0g1f97g1533gca440242cfde"
]

UID_OVERRIDES.update({
    "h37be3b80g09fbg170eg2b7cg065997dc9bf9": (
        "Jedna widoczna istota w promieniu 9 m od ciebie otrzymuje 1k4 obrażeń od ognia."
    ),
    "hf4271cc8ge175g82fcg26deg011060d3570a": (
        "Jedna widoczna istota w promieniu 9 m od ciebie otrzymuje 1k4 obrażeń od światłości."
    ),
    "h4d2b70ecgee46g15a5g5c0bga91856311ba5": (
        "Czerpiesz moc z dziwnych, pradawnych koszmarów tej krainy. Wyrastają z ciebie nienaturalne narośla, "
        "takie jak krwawe poroże lub gnijące kły, a twój cień wydłuża się albo wije wokół ciebie. W ramach "
        "akcji dodatkowej możesz zużyć jedno użycie Ulubionego Wroga, aby przybrać upiorną postać i zyskać "
        "poniższe korzyści na 1 minutę, do chwili Obezwładnienia lub śmierci albo do zakończenia przemiany (bez "
        "użycia akcji).\n\nPradawny pancerz. Twoje ciało spowijają zgniła kora i zwierzęca szczecina, co "
        "zapewnia ci premię +1 do KP. Premia wzrasta do +2 na 11. poziomie łowcy.\n\nKrążąca zemsta. "
        "Natychmiast po tym, jak widoczna istota w promieniu 1,5 m od ciebie zada obrażenia tobie albo jednemu "
        "z twoich sojuszników, możesz wykonać przeciwko niej atak okazyjny.\n\nNiepokojąca aura. Gdy się "
        "przemieniasz oraz na początku każdej swojej kolejnej tury, każda wybrana przez ciebie istota w "
        "emanacji o promieniu 3 m, której źródłem jesteś, wykonuje rzut obronny na Mądrość przeciwko twojemu "
        "ST obrony przed czarami. Przy niepowodzeniu otrzymuje stan Przerażenia do początku twojej następnej "
        "tury."
    ),
    "hd4469619g376dg9d74gbfb4gb103475e4356": (
        "Natychmiast po tym, jak widoczna istota w promieniu 1,5 m od ciebie zada obrażenia tobie albo jednemu "
        "z twoich sojuszników, możesz wykonać przeciwko niej atak okazyjny."
    ),
    "he39926bdgdb3ag2cd8gd6c1g17c647980ce1": (
        "Nasycasz dotykaną broń świętą mocą. Do końca czaru broń emituje jasne światło w promieniu 9 m oraz "
        "słabe światło na kolejnych 9 m. Ponadto trafienia atakami tą bronią zadają dodatkowe 2k8 obrażeń od "
        "światłości. Jeśli nie jest jeszcze bronią magiczną, staje się nią na czas trwania czaru.\n\nW swojej "
        "turze możesz w ramach akcji dodatkowej zakończyć ten czar, sprawiając, że broń rozbłyśnie światłością. "
        "Każda wybrana przez ciebie widoczna istota w promieniu 9 m od broni musi wykonać rzut obronny na "
        "Kondycję. Przy niepowodzeniu otrzymuje 4k8 obrażeń od światłości i stan Oślepienia na 1 minutę. Przy "
        "powodzeniu otrzymuje połowę tych obrażeń i nie zostaje oślepiona. Oślepiona istota może powtórzyć rzut "
        "obronny na koniec każdej swojej tury; powodzenie kończy ten stan."
    ),
})

UID_OVERRIDES["h552007ebg0886g488bgccfag99d4097696ee"] = UID_OVERRIDES[
    "h4d2b70ecgee46g15a5g5c0bga91856311ba5"
]

UID_OVERRIDES.update({
    "h57810054gfe7fgd3feg857agf79b5362dc6c": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie Dzikiej Postaci, aby przejawić otaczającą cię "
        "emanację morskiej bryzy o promieniu 1,5 m. Emanacja kończy się wcześniej, jeśli ją zakończysz (bez "
        "użycia akcji), przejawisz ponownie albo otrzymasz stan Obezwładnienia."
    ),
    "h6630050ag4420g70e6g6f4fg79b677ca4518": (
        "Zyskujesz stoicki spokój, który wzmacnia twoją determinację. Masz niewrażliwość na stan Przerażenia. "
        "Korzyść ta nie działa, gdy masz stan Obezwładnienia."
    ),
    "h0dcdc1c9g2349g6dc5g0490g2bd7268e6913": (
        "Dotykasz jednej chętnej istoty i wybierasz obrażenia od kwasu, zimna, ognia, elektryczności albo "
        "trucizny. Do końca czaru cel może w ramach akcji Magii zionąć stożkiem o długości 4,5 m. Każda istota "
        "na tym obszarze wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego "
        "typu, a przy powodzeniu — połowę tych obrażeń."
    ),
})

UID_OVERRIDES["hf8470c53gc4a7gf584g96f0g33c340603191"] = UID_OVERRIDES[
    "h57810054gfe7fgd3feg857agf79b5362dc6c"
]

ELEMENTAL_EXHALATION_BODY = (
    "Powietrze. Czar zadaje obrażenia od dźwięku. Każda istota, której nie powiedzie się rzut obronny, "
    "zostaje odepchnięta od ciebie o 3 m.\n\nZimny ogień. Czar zadaje obrażenia od zimna. Każda istota, "
    "której nie powiedzie się rzut obronny, otrzymuje stan Przerażenia do początku twojej następnej tury."
    "\n\nZiemia. Czar zadaje obrażenia obuchowe. Szybkość każdej istoty, której nie powiedzie się rzut obronny, "
    "zmniejsza się do 0 do końca jej następnej tury.\n\nOgień. Czar zadaje obrażenia od ognia. Każda istota, "
    "której nie powiedzie się rzut obronny, staje w płomieniach i na koniec swojej następnej tury otrzymuje "
    "obrażenia od ognia. W ramach akcji może ugasić płomienie, dobrowolnie otrzymując stan Powalenia i "
    "przetaczając się po ziemi. Ogień gaśnie również po polaniu wodą, zanurzeniu lub zduszeniu.\n\nWoda. "
    "Czar zadaje obrażenia od kwasu. Każda istota, której nie powiedzie się rzut obronny, otrzymuje stan "
    "Powalenia.\n\nKażda istota w stożku niszczycielskiej energii żywiołów o długości 9 m wykonuje rzut "
    "obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego typu, a przy powodzeniu — połowę "
    "tych obrażeń."
)
UID_OVERRIDES["h85c7508bg337bg1507gd4ebg434eb4cc892b"] = ELEMENTAL_EXHALATION_BODY
UID_OVERRIDES["h1042549ag1908gfbe0g5f54g6b7fb0d8ba00"] = (
    "Podczas rzucania tego czaru wybierz jeden z poniższych efektów, który określa typ zadawanych obrażeń:"
    "\n\n" + ELEMENTAL_EXHALATION_BODY
)

UID_OVERRIDES.update({
    "hd68a192ag408cg0b94ge1bcgb6efd87c7b6a": (
        "Możesz wpleść magię fey w pieśń albo taniec, aby napełnić innych wigorem. W ramach akcji dodatkowej "
        "możesz zużyć jedno użycie bardowskiej inspiracji i rzucić jej kością. Następnie wybierz maksymalnie "
        "tyle innych istot w promieniu [1] od siebie, ile wynosi twój modyfikator Charyzmy (co najmniej jedną)."
        "\n\nKażda z tych istot zyskuje tymczasowe punkty wytrzymałości w liczbie równej dwukrotności wyniku "
        "rzutu kością bardowskiej inspiracji i do końca swojej następnej tury może się przemieszczać bez "
        "prowokowania ataków okazyjnych."
    ),
    "h719facf1g5f1cg71c4gbf18g0bc0200d571d": (
        "Każda z tych istot zyskuje tymczasowe punkty wytrzymałości w liczbie równej dwukrotności wyniku "
        "rzutu kością bardowskiej inspiracji i do końca swojej następnej tury może się przemieszczać bez "
        "prowokowania ataków okazyjnych."
    ),
    "h202adf83g5a60g677dg2f14g1cbdfc06aeab": (
        "W ramach akcji dodatkowej możesz rzucić kością Sztuk Walki. Odzyskujesz punkty wytrzymałości w "
        "liczbie równej sumie wyniku rzutu i twojego modyfikatora Mądrości (co najmniej 1 punkt)."
    ),
    "h060adb3eg6617g9283g226fg6d070eb47c88": (
        "W ramach akcji Magii możesz zużyć jedno użycie Mocy przysięgi tej klasy, aby przepełnić wrogów "
        "trwogą. Unosząc Święty Symbol albo broń, wybierasz maksymalnie tyle widocznych istot w promieniu [1] "
        "od siebie, ile wynosi twój modyfikator Charyzmy (co najmniej jedną). Każdy cel musi wykonać udany "
        "rzut obronny na Mądrość albo otrzymuje stan Przerażenia na 1 minutę."
    ),
    "h60d6e7c1gc8cag3d1dgdaedg0d81cb025d8b": (
        "Pierwotne siły dodają ci sił podczas wędrówek. W ramach akcji Magii możesz zyskać tymczasowe punkty "
        "wytrzymałości w liczbie równej sumie 1k8 i twojego modyfikatora Mądrości (co najmniej 1). Możesz użyć "
        "tej akcji tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz), a wszystkie zużyte użycia "
        "odzyskujesz po długim odpoczynku."
    ),
    "hf0903b4fgdab0g610fgf651g1cf01ed26e14": (
        "Gdy trafisz istotę atakiem bronią, możesz zadać jej dodatkowe 2k6 obrażeń psychicznych. Z tej korzyści "
        "możesz skorzystać tylko raz na turę i tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej "
        "raz). Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h1296e788gbe31g8450g4a0cg6c2851fe0b5f": (
        "Możesz zużyć jedno użycie zionięcia, aby ryknąć i zmusić każdą wybraną istotę w promieniu 9 m od "
        "ciebie do wykonania rzutu obronnego na Mądrość. Przy niepowodzeniu cel otrzymuje stan Przerażenia "
        "na 1 minutę."
    ),
    "h1fa402eeg7070g07b2gbfbaga67c4ad37e78": (
        "W ramach akcji dodatkowej możesz sprawić, że trzymana broń do walki wręcz przez 10 tur emituje słabe "
        "światło w promieniu 3 m. Jest to światło słoneczne. Dopóki broń lśni, zadaje obrażenia od światłości "
        "zamiast obrażeń zwykłego typu.\n\nGdy uzyskasz trafienie krytyczne atakiem bronią do walki wręcz, "
        "możesz dodatkowo rzucić jedną kością obrażeń tej broni i dodać wynik do obrażeń."
    ),
    "h89b6e006g139bgf893g9a7dg642ea772fd27": (
        "W ramach akcji dodatkowej możesz sprawić, że trzymana broń do walki wręcz przez 10 tur emituje słabe "
        "światło w promieniu 3 m. Jest to światło słoneczne. Dopóki broń lśni, zadaje obrażenia od światłości "
        "zamiast obrażeń zwykłego typu."
    ),
    "h3b19ec2fg1828gff82g805cg351bdc1b191b": (
        "W ramach akcji Magii wybierz maksymalnie tyle widocznych istot, ile wynosi twój modyfikator Mądrości "
        "(co najmniej jedną). Każda wybrana istota odzyskuje punkty wytrzymałości w liczbie równej sumie 1k10 "
        "i twojego poziomu łowcy, a przez 1 godzinę wykonuje z ułatwieniem rzuty obronne pozwalające uniknąć "
        "stanu Przerażenia albo go zakończyć."
    ),
    "h39e677d5ged8fgc431g5486g61bd08885fd5": (
        "Zawsze masz przygotowany czar Znak Łowcy. Możesz rzucić go tyle razy, ile wynosi twój modyfikator Siły "
        "(co najmniej raz), a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h8993f01fgfd8fg8b11g17cdg458c682aad00": (
        "Wymaga co najmniej 7. poziomu illriggera.\n\nGdy w ramach akcji dodatkowej umieszczasz albo "
        "przenosisz pieczęć na istotę o rozmiarze dużym lub mniejszym, możesz aktywować tę łaskę (bez użycia "
        "akcji). Przywołujesz piekielne łańcuchy, które chwytają cel i zmuszają go do wykonania rzutu obronnego "
        "na Siłę. Przy niepowodzeniu możesz przyciągnąć cel do 3 m w swoją stronę albo nadać mu stan "
        "Pochwycenia do końca swojej następnej tury."
    ),
    "h55235fc0g6321g25e2gcdefgc2244237ac56": (
        "Zyskujesz zdolność przepowiadania zagłady istoty. W ramach akcji dodatkowej wybierz widoczną istotę "
        "w promieniu 36 m od siebie. Do początku twojej następnej tury testy ataku przeciwko niej mają "
        "ułatwienie."
    ),
    "h469b91e3g1e80g366cg1b58gaf7e45b960a9": (
        "Możesz użyć Aktu wiary, aby przyspieszyć zagładę istoty. W ramach akcji dodatkowej zużyj jedno użycie "
        "Aktu wiary i wybierz widoczną istotę w promieniu 36 m od siebie. Przez 10 minut test ataku przeciwko "
        "niej zapewnia trafienie krytyczne przy wyniku 19 albo 20 na k20."
    ),
    "h0eff4b29g54dbgb8d1gfe4ege253bef014b6": (
        "Możesz użyć Aktu wiary, aby odmienić los istoty. W ramach akcji dodatkowej zużyj jedno użycie Aktu "
        "wiary i wybierz widoczną istotę w promieniu 36 m od siebie. Ma ona utrudnienie w następnym rzucie "
        "obronnym przeciwko twoim czarom wykonanym przed końcem twojej następnej tury."
    ),
    "h834e8d02gd8f9g2e05ge709gc3ecb8d0d3da": (
        "Przybierasz przerażający wyraz twarzy, aby nastraszyć widoczną istotę w zasięgu. Cel musi wykonać "
        "udany rzut obronny na Mądrość albo otrzymuje stan Przerażenia do początku twojej następnej tury."
    ),
    "hdfb7e043ga3ecgc3afg13c5g96138794e52b": (
        "Poznajesz uniwersalny język tańca. W ramach akcji dodatkowej możesz zużyć jedno użycie "
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>, aby '
        "zatańczyć i pokrzepić inną wybraną istotę, która cię widzi.\n\nRzuć kością bardowskiej inspiracji. "
        "Istota zyskuje tymczasowe punkty wytrzymałości w liczbie równej sumie wyniku rzutu i twojego "
        "modyfikatora Charyzmy (co najmniej 2). Następnie może natychmiast w ramach reakcji przemieścić się na "
        "odległość do swojej szybkości bez prowokowania ataków okazyjnych albo wykonać akcję Uniku."
    ),
    "h9cda9df5g341bg90cag16e9gfc25dc9df498": (
        "Gdy używasz Kroku Fey, możesz dotknąć chętnej istoty w promieniu 1,5 m od siebie. Teleportuje się ona "
        "zamiast ciebie i pojawia na wybranym przez ciebie widocznym, niezajętym miejscu w promieniu 9 m od "
        "ciebie."
    ),
    "h37aea667gb412g84d3gd6f8g8a195d4ea3d0": (
        "Broń emituje jasne światło w promieniu 9 m oraz słabe światło na kolejnych 9 m. Ponadto jej trafienia "
        "zadają dodatkowe 2k8 obrażeń od światłości. Jeśli nie jest jeszcze bronią magiczną, staje się nią na "
        "czas trwania czaru."
    ),
})

for duplicate_uid in (
    "hd927a3dfg462bg2162g0ddegc1f29c11bb86",
    "hf3f5c8f9g2b3bg1058g7715gee2645709a64",
    "h52a153aag53d8g2658g72aegc55c7baffc11",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h719facf1g5f1cg71c4gbf18g0bc0200d571d"]

UID_OVERRIDES["hf0938809g82f6ge8a7gea01gff762cf6f570"] = UID_OVERRIDES[
    "h060adb3eg6617g9283g226fg6d070eb47c88"
]
for duplicate_uid in (
    "hb07fc0ddg58b4ga6acgedc3gd632be720493",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h55235fc0g6321g25e2gcdefgc2244237ac56"]
UID_OVERRIDES["h7ffa0044gb8c8g868fg7f1fgf74e697c363e"] = UID_OVERRIDES[
    "h469b91e3g1e80g366cg1b58gaf7e45b960a9"
]
UID_OVERRIDES["h420df6cbg0932g5e3dgc009g752d63452593"] = UID_OVERRIDES[
    "h0eff4b29g54dbgb8d1gfe4ege253bef014b6"
]

UID_OVERRIDES.update({
    "h9ac2c1d5gd0dcga37bgf4d5gb17546182f77": (
        "Odepchnięcie. Gdy trafisz istotę atakiem zadającym obrażenia obuchowe, możesz przesunąć ją o 1,5 m "
        "na niezajęte miejsce, jeśli cel jest od ciebie większy najwyżej o jeden rozmiar.\n\nWzmocnione trafienie "
        "krytyczne. Gdy uzyskasz trafienie krytyczne zadające istocie obrażenia obuchowe, testy ataku "
        "przeciwko niej mają ułatwienie do początku twojej następnej tury."
    ),
    "h5f23ece1gd28eg37b5gb2f7g57554d7c8da9": (
        "Przebicie. Gdy trafisz istotę atakiem zadającym obrażenia kłute, możesz przerzucić jedną kość "
        "obrażeń ataku i musisz użyć nowego wyniku.\n\nWzmocnione trafienie krytyczne. Gdy uzyskasz trafienie "
        "krytyczne zadające istocie obrażenia kłute, możesz rzucić dodatkową kością obrażeń podczas określania "
        "dodatkowych obrażeń kłutych otrzymanych przez cel."
    ),
    "hfd222472gd8acg6b69g6068g2840b34f0315": (
        "Podcięcie. Gdy trafisz istotę atakiem zadającym obrażenia cięte, możesz zmniejszyć jej szybkość o "
        "3 m do początku swojej następnej tury.\n\nWzmocnione trafienie krytyczne. Gdy uzyskasz trafienie "
        "krytyczne zadające istocie obrażenia cięte, wykonuje ona z utrudnieniem testy ataku do początku "
        "twojej następnej tury."
    ),
    "he62f99bbgc9f2g862dg2430gdefa25e39624": (
        "Odepchnięcie. Raz na turę, gdy trafisz istotę atakiem zadającym obrażenia obuchowe, możesz przesunąć "
        "ją o 1,5 m na niezajęte miejsce, jeśli cel jest od ciebie większy najwyżej o jeden rozmiar.\n\n"
        "Wzmocnione trafienie krytyczne. Gdy uzyskasz trafienie krytyczne zadające istocie obrażenia obuchowe, "
        "testy ataku przeciwko niej mają ułatwienie do początku twojej następnej tury."
    ),
    "hf202d0a0gaaf3ge15bgc2f1g94f60d8193aa": (
        "Przebicie. Raz na turę, gdy trafisz istotę atakiem zadającym obrażenia kłute, możesz przerzucić jedną "
        "kość obrażeń ataku i musisz użyć nowego wyniku.\n\nWzmocnione trafienie krytyczne. Gdy uzyskasz "
        "trafienie krytyczne zadające istocie obrażenia kłute, możesz rzucić dodatkową kością obrażeń podczas "
        "określania dodatkowych obrażeń kłutych otrzymanych przez cel."
    ),
    "he322b215g4b74g107eg1abfg1d7e848abd23": (
        "Podcięcie. Raz na turę, gdy trafisz istotę atakiem zadającym obrażenia cięte, możesz zmniejszyć jej "
        "szybkość o 3 m do początku swojej następnej tury.\n\nWzmocnione trafienie krytyczne. Gdy uzyskasz "
        "trafienie krytyczne zadające istocie obrażenia cięte, wykonuje ona z utrudnieniem testy ataku do "
        "początku twojej następnej tury."
    ),
    "h63f9716cgc2d1g6fcbg46fcg4c5e77c4be1d": (
        "Twój lud poniósł wiele porażek i odniósł wiele daremnych zwycięstw w wojnach z Cieniem. Śmiertelny "
        "gniew, który twoi pobratymcy żywią wobec Nieprzyjaciela, nasyca twoją broń blaskiem zimnego ognia."
        "\n\nW ramach akcji dodatkowej możesz sprawić, że trzymana broń do walki wręcz przez 10 tur emituje "
        "słabe światło w promieniu 3 m. Jest to światło słoneczne. Dopóki broń lśni, zadaje obrażenia od "
        "światłości zamiast obrażeń zwykłego typu.\n\nGdy uzyskasz trafienie krytyczne atakiem bronią do "
        "walki wręcz, możesz dodatkowo rzucić jedną kością obrażeń tej broni i dodać wynik do obrażeń."
    ),
    "hd43fb4c9g35d7g9ab6g9cc2g37fbd18e9590": (
        "Gdy uzyskasz trafienie krytyczne przeciwko istocie, możesz wezwać ją do poddania się. Cel musi "
        "wykonać udany rzut obronny na Mądrość przeciwko ST obrony przed twoimi manewrami albo otrzymuje stan "
        "Przerażenia na 1 minutę. Na koniec każdej swojej tury może powtórzyć rzut obronny; powodzenie kończy "
        "ten stan."
    ),
    "hb9a7c09eg9f65g5801gb3e4gb060b99c7378": (
        "Gdy uzyskasz trafienie krytyczne zadające istocie obrażenia cięte, wykonuje ona z utrudnieniem testy "
        "ataku do początku twojej następnej tury."
    ),
    "hb0b2260fg01d4gf52agf9f4g93f90248b7e1": (
        "Gdy uzyskasz trafienie krytyczne zadające istocie obrażenia obuchowe, testy ataku przeciwko niej mają "
        "ułatwienie do początku twojej następnej tury."
    ),
    "h0fb46065g45fege74age2e5g0f1ff68942df": (
        "Każda wybrana przez ciebie istota w sferze o promieniu 1,5 m, której środkiem jest punkt w zasięgu, "
        "musi wykonać udany rzut obronny na Mądrość albo otrzymuje stan Obezwładnienia do końca swojej "
        "następnej tury. Następnie powtarza rzut obronny. Jeśli drugi rzut się nie powiedzie, otrzymuje "
        '<LSTag Type="Status" Tooltip="SLEEP">stan Nieprzytomności</LSTag> na czas trwania czaru. Czar '
        "przestaje działać na cel, gdy ten otrzyma obrażenia albo gdy ktoś w promieniu 1,5 m od niego użyje "
        "akcji, aby go obudzić."
    ),
    "h156a3a97g9e6bg053egabdeg9a8bfdfcdee2": (
        "Raz na turę, gdy zadasz obrażenia istocie oznaczonej twoim Znakiem Łowcy, możesz również zadać "
        "dodatkowe obrażenia tego czaru innej widocznej istocie w promieniu [1] od pierwszego celu."
    ),
    "hf4670cedg622ag16adgd7fbgf472400d198b": (
        "Medyk bojowy. Możesz przywrócić istocie 1k8 punktów wytrzymałości. Z tej zdolności możesz skorzystać "
        "tyle razy, ile wynosi twoja premia z biegłości, a wszystkie zużyte użycia odzyskujesz po długim "
        "odpoczynku.\n\nLeczenie. Za każdym razem, gdy przywracasz istocie punkty wytrzymałości, odzyskuje ona "
        "dodatkowe punkty w liczbie równej twojej premii z biegłości."
    ),
    "h20e4b6b0g60edg473ag9aeeg93ed1d74cd27": (
        "Chmurna ucieczka. Gdy widoczna istota trafia cię testem ataku, możesz w ramach reakcji zyskać "
        "odporność na obrażenia tego ataku. Następnie teleportujesz się na widoczne, niezajęte miejsce w "
        "promieniu 9 m od siebie. Możesz użyć tej reakcji tyle razy, ile wynosi twoja premia z biegłości, a "
        "wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "hc775738fg65a3g6054g75e4gc06c1a9d36eb": (
        "Gdy widoczna istota trafia cię testem ataku, możesz w ramach reakcji zyskać odporność na obrażenia "
        "tego ataku. Następnie teleportujesz się na widoczne, niezajęte miejsce w promieniu 9 m od siebie."
    ),
    "hb284f5d4gf341g5049g2ce3g9ea223e41a38": (
        "Natychmiast po użyciu Kroku Fey maksymalnie dwie wybrane przez ciebie widoczne istoty w promieniu 3 m "
        "od ciebie muszą wykonać udany rzut obronny na Mądrość albo otrzymują stan Zauroczenia na 1 minutę, "
        "do chwili, gdy ty lub twoi towarzysze zadacie im jakiekolwiek obrażenia."
    ),
    "hed9510fdg4a6dge76dgaa9bg643066cb6cf5": (
        "Każda wybrana przez ciebie istota w sferze o promieniu 4,5 m, której środkiem jesteś, wykonuje rzut "
        "obronny na Zręczność (ST wynosi 8 + twoja premia z biegłości + wyższy z twoich modyfikatorów: Siły "
        "albo Mądrości). Przy niepowodzeniu otrzymuje obrażenia od ognia równe sumie 1k8 i twojej premii z "
        "biegłości oraz stan Oślepienia do początku twojej następnej tury. Przy powodzeniu otrzymuje tylko "
        "połowę obrażeń."
    ),
})

for duplicate_uid in (
    "h4fcec4c9gde1eg19b6gebddg9af35fef4ff5",
    "h2ba0acdeg33d2g33c7g5f83gb4c34e1444c0",
    "ha765fffag4904gfe52g8d54gd4472a83f8fc",
    "h804ad0f1g6cb1ge2ecg1066g91b9c7f2effa",
    "h47a0106cg9a69g79a5g7f31g8c859cf2dd61",
    "hd31e4d13g939ag101eg9e56g93956331fc9c",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h0fb46065g45fege74age2e5g0f1ff68942df"]

UID_OVERRIDES.update({
    "h5c65e74bgcca7gff2agc4abg0700018dda54": (
        "Zrodzony z płomieni. Masz odporność na obrażenia od ognia.\n\nPalący zapłon. Gdy w swojej turze "
        "wykonujesz akcję Ataku, możesz zastąpić jeden atak magicznym wybuchem płomieni. Każda wybrana przez "
        "ciebie istota w sferze o promieniu 4,5 m, której środkiem jesteś, wykonuje rzut obronny na Zręczność "
        "(ST wynosi 8 + twoja premia z biegłości + wyższy z twoich modyfikatorów: Siły albo Mądrości). Przy "
        "niepowodzeniu otrzymuje obrażenia od ognia równe sumie 1k8 i twojej premii z biegłości oraz stan "
        "Oślepienia do początku twojej następnej tury. Przy powodzeniu otrzymuje tylko połowę obrażeń. Możesz "
        "użyć Palącego zapłonu tyle razy, ile wynosi twoja premia z biegłości, ale nie częściej niż raz na turę. "
        "Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h34aa43d4geb01g6558gc027g96c6c82fe37d": (
        "Przejawiasz bojową moc właściwą olbrzymom ognia, co zapewnia ci następujące korzyści:\n\nZrodzony "
        "z płomieni. Masz odporność na obrażenia od ognia.\n\nPalący zapłon. Gdy w swojej turze wykonujesz "
        "akcję Ataku, możesz zastąpić jeden atak magicznym wybuchem płomieni. Każda wybrana przez ciebie "
        "istota w sferze o promieniu 4,5 m, której środkiem jesteś, wykonuje rzut obronny na Zręczność (ST "
        "wynosi 8 + twoja premia z biegłości + wyższy z twoich modyfikatorów: Siły albo Mądrości). Przy "
        "niepowodzeniu otrzymuje obrażenia od ognia równe sumie 1k8 i twojej premii z biegłości oraz stan "
        "Oślepienia do początku twojej następnej tury. Przy powodzeniu otrzymuje tylko połowę obrażeń. Możesz "
        "użyć Palącego zapłonu tyle razy, ile wynosi twoja premia z biegłości, ale nie częściej niż raz na turę. "
        "Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h29832775g4de3gb8f5ge5d0g6d6aabe5c831": (
        "Możesz użyć Palącego zapłonu tyle razy, ile wynosi twoja premia z biegłości, ale nie częściej niż raz "
        "na turę. Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h83181830gd3c7g58d8g177cg06253bfa37db": (
        "Przejawiasz zwodniczą magię właściwą olbrzymom chmurowym, co zapewnia ci następującą korzyść:"
        "\n\nChmurna ucieczka. Gdy widoczna istota trafia cię testem ataku, możesz w ramach reakcji zyskać "
        "odporność na obrażenia tego ataku. Następnie teleportujesz się na widoczne, niezajęte miejsce w "
        "promieniu 9 m od siebie. Możesz użyć tej reakcji tyle razy, ile wynosi twoja premia z biegłości, a "
        "wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h1e4b1002g6774g3698g6495gb47ef39af956": (
        "Zyskujesz jedno użycie zionięcia.\n\nMożesz zużyć jedno użycie zionięcia, aby ryknąć i zmusić każdą "
        "wybraną istotę w promieniu 9 m od ciebie do wykonania rzutu obronnego na Mądrość. Przy niepowodzeniu "
        "cel otrzymuje stan Przerażenia na 1 minutę."
    ),
    "h44cd6db6gdaa7gaac2g514cg11ae3a98f828": (
        "W ramach akcji dodatkowej możesz sprawić, że trzymana broń do walki wręcz przez 10 tur emituje słabe "
        "światło w promieniu 3 m. Jest to światło słoneczne. Dopóki broń lśni, zadaje obrażenia od światłości "
        "zamiast obrażeń zwykłego typu."
    ),
    "h304ba6eegcc14g44c6g7640g0b3b0cf81a62": (
        "W ramach akcji Magii możesz zyskać tymczasowe punkty wytrzymałości w liczbie równej sumie 1k8 i "
        "twojego modyfikatora Mądrości (co najmniej 1). Możesz użyć tej akcji tyle razy, ile wynosi twój "
        "modyfikator Mądrości (co najmniej raz), a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "hc95f4dcfg8caeg69e9gc8b5ge035fe1dc1a3": (
        "W ramach akcji Magii możesz zyskać tymczasowe punkty wytrzymałości w liczbie równej sumie 1k8 i "
        "twojego modyfikatora Mądrości (co najmniej 1)."
    ),
    "h9dbb965ag2bcegf72bg5bb2gc4f359dca388": (
        'Przez 10 minut masz <LSTag Type="Status" Tooltip="INVISIBLE">stan Niewidzialności</LSTag>. Efekt '
        "kończy się wcześniej, jeśli go zakończysz (bez użycia akcji), wykonasz atak albo rzucisz czar."
    ),
    "h4016a9a2g8d51g2860gce0aga3dae07e0895": (
        'Próbujesz zmusić mało inteligentną istotę do posłuszeństwa. Istota o '
        '<LSTag Tooltip="Intelligence">Inteligencji</LSTag> 3 lub niższej musi wykonać udany '
        '<LSTag Tooltip="SavingThrow">rzut obronny</LSTag> na '
        '<LSTag Tooltip="Intelligence">Inteligencję</LSTag> albo zostaje przez ciebie '
        '<LSTag Type="Status" Tooltip="AWAKEN">Zdominowana</LSTag> do chwili ukończenia '
        '<LSTag Tooltip="LongRest">długiego odpoczynku</LSTag>.'
    ),
    "h9aa052ddgf617g4344ga11dg4ad49e29159e": (
        'Możesz użyć Mocy przysięgi, aby spróbować <LSTag Type="Status" Tooltip="TURNED">odpędzić</LSTag> '
        "istotę pozaplanarną. Każda aberracja, istota niebiańska, istota fey, żywiołak albo czart w promieniu "
        "9 m od ciebie musi wykonać udany rzut obronny na Mądrość albo zostaje odpędzona na 1 minutę. "
        "Odpędzona istota musi uciekać i nie może się do ciebie zbliżyć."
    ),
    "ha4715411g6f47gaa79ge8b7gb92d8781f1b0": (
        "Uczysz się dwóch wybranych czarów. Mogą one pochodzić z list czarów kleryka, druida i maga w "
        "dowolnym połączeniu."
    ),
})

UID_OVERRIDES["h3c5b5f7eg291agf227g9011gc0565f5cdd4d"] = UID_OVERRIDES[
    "hc95f4dcfg8caeg69e9gc8b5ge035fe1dc1a3"
]

UID_OVERRIDES.update({
    "h31748432g34ebg740cgf353g2071d6cae486": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie Aktu wiary, aby stworzyć doskonałą wizualną "
        "iluzję siebie na widocznym, niezajętym miejscu w promieniu [1]. Iluzja trwa 1 minutę. W ramach akcji "
        "dodatkowej możesz przenieść ją o maksymalnie [1] na inne widoczne, niezajęte miejsce."
    ),
    "h0c6d3ec2g7683g7e9fg7d62g08a6874b3c5f": (
        "Możesz zużyć jedno użycie Aktu wiary, aby rzucić Tarczę Wiary albo Broń Duchową bez zużywania komórki "
        "czaru. Czar rzucony w ten sposób nie wymaga Koncentracji i trwa 1 minutę, ale kończy się wcześniej, "
        "jeśli rzucisz go ponownie, otrzymasz stan Obezwładnienia albo zginiesz."
    ),
    "h4b611e19g3e33g0533g1f8cg44ab465667b3": (
        "Przenosisz się magicznie i pojawiasz ponownie w rozbłysku księżycowego światła. W ramach akcji "
        "dodatkowej teleportujesz się na odległość do [1] na widoczne, niezajęte miejsce. Możesz użyć tej "
        "zdolności tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz), a wszystkie zużyte użycia "
        "odzyskujesz po długim odpoczynku."
    ),
    "h61388cf8g2c44ge32ege2c8gd43ed94d46c8": (
        "Masz talent do taktyki na polu bitwy i poza nim. Możesz zużyć jedno użycie Drugiego Oddechu, aby "
        "zwiększyć swoje szanse na sukces. Rzuć 1k10 i dodaj wynik do testu cechy, co może zmienić niepowodzenie "
        "w powodzenie."
    ),
    "h1d1a9875g453ag1a74g99c0g7c41137717d6": (
        "Rzucasz [1] śnieżkami w wybrany punkt w zasięgu. Każda śnieżka obejmuje sferę o promieniu 1,5 m, "
        "której środkiem jest ten punkt. Każda istota na obszarze wykonuje rzut obronny na Zręczność. Przy "
        "niepowodzeniu otrzymuje [2] za każdą śnieżkę, a przy powodzeniu — połowę tych obrażeń."
    ),
    "h11246ce1g1053g5998g5c40ga6494d732ee0": (
        "Gdy ty albo inna widoczna istota w promieniu 9 m od ciebie otrzymuje obrażenia, możesz w ramach "
        "reakcji zużyć jedną kość energii psionicznej i nią rzucić. Zmniejszasz obrażenia o sumę wyniku rzutu "
        "i swojego modyfikatora Inteligencji (co najmniej o 1), tworząc chwilową osłonę z telekinetycznej mocy."
    ),
    "he0b3dcccga1b5gd89bgf47ag768a98964bc3": (
        "Gdy ktoś inny niż ty sprowadzi istotę w promieniu 3 m od ciebie do 0 punktów wytrzymałości, zyskujesz "
        "tymczasowe punkty wytrzymałości w liczbie równej sumie twojego modyfikatora Charyzmy i poziomu "
        "czarownika (co najmniej 1)."
    ),
    "hc9360440gfe54g46f9gbb9dge1b352d710ba": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie Dzikiej Postaci, aby przybrać wyjątkową Smoczą "
        "Postać. Stajesz się wówczas średnim smokiem poruszającym się na czterech łapach, ale zachowujesz swoje "
        "zwykłe statystyki i zmysły.\n\nPo przybraniu Smoczej Postaci zyskujesz tymczasowe punkty "
        "wytrzymałości w liczbie równej trzykrotności swojego poziomu druida. Możesz atakować pazurami i używać "
        "zionięcia. Zyskujesz szybkość latania równą dwukrotności swojej szybkości oraz odporność na obrażenia "
        "od kwasu, zimna, ognia, elektryczności i trucizny."
    ),
    "ha2bb03e3g700ag8cdagaff7gd4fdd097b625": (
        "Uczysz się odpierać ciosy skierowane w ciebie, twojego wierzchowca i inne pobliskie istoty. Gdy ty albo "
        "widoczna istota w promieniu 1,5 m od ciebie zostaje trafiona atakiem, a ty trzymasz broń do walki "
        "wręcz lub tarczę, możesz w ramach reakcji rzucić 1k8. Dodaj wynik do KP celu przeciwko temu atakowi, "
        "co może zmienić trafienie w chybienie."
    ),
    "h9f5052c1ga6c8ga38cg6399gbc4405cf0442": (
        "Uczysz się przywoływać magię runiczną, aby chronić sojuszników. Gdy inna widoczna istota w promieniu "
        "18 m od ciebie zostaje trafiona testem ataku, możesz w ramach reakcji zmusić napastnika do ponownego "
        "rzutu k20 i użycia nowego wyniku."
    ),
    "h80b3909egdd5dg9771g4878g32dff4066380": (
        "Gdy ty albo inna widoczna istota w promieniu 18 m od ciebie wykonuje test ataku, rzut obronny lub test "
        "cechy, możesz w ramach reakcji zapewnić temu rzutowi ułatwienie."
    ),
    "hf1d142d7g41e9g9a72g6d5cgf6c2fa588579": (
        "Zyskujesz premię +1 do rzutów obronnych za każdą wrogą istotę w promieniu 3 m od ciebie, maksymalnie +5."
    ),
    "heca0b0d3g54dbgf86cg916cg906977301869": (
        "Gdy spalasz co najmniej jedną pieczęć na objętej interdyktem istocie, możesz w ramach reakcji wywołać "
        "wokół niej wybuch piekielnej energii. Każda wybrana przez ciebie istota w promieniu 3 m od celu "
        "wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje tyle samo obrażeń tego samego typu, "
        "ile pieczęcie zadały objętej interdyktem istocie, a przy powodzeniu — połowę tych obrażeń."
    ),
    "h8dc48af4gcdf0gdb45g88c4g86ba48d298cb": (
        "W ramach akcji przywołujesz władzę Dispatera. Wykonujesz atak bronią i wybierasz maksymalnie tyle "
        "chętnych, widocznych istot w promieniu 9 m od siebie, ile wynosi twoja premia z biegłości. Każda z nich "
        "może w ramach reakcji wykonać atak bronią albo rzucić zadającą obrażenia sztuczkę o czasie rzucania "
        "równym 1 akcji.\n\nPo użyciu tej akcji musisz ukończyć krótki albo długi odpoczynek, zanim użyjesz "
        "jej ponownie."
    ),
    "heb2a7f7ag521bg6a02g5dffg52cdf49a9788": (
        "Uczysz się regenerować dzięki dzikiej, zwierzęcej magii płynącej w twoich żyłach. W ramach akcji "
        "dodatkowej możesz zużyć jedno użycie Dzikiej Postaci, aby odzyskać punkty wytrzymałości w liczbie "
        "równej sumie 2k6 i twojego poziomu druida. Leczenie zwiększa się o 1k6 na 5. poziomie druida (3k6 plus "
        "poziom druida) i ponownie na 10. poziomie (4k6 plus poziom druida)."
    ),
    "h2f932b68g4347ga354g521cgc438d3f99c6d": (
        "Gdy widoczna istota w promieniu 18 m od ciebie obiera ciebie albo inną istotę za cel ataku wręcz lub "
        "dystansowego, możesz w ramach reakcji wykonać przeciwko napastnikowi jeden atak bronią."
    ),
    "hb5512cccg4740g2f7dg76e9gd4d73b16a044": (
        "Gdy ty albo widoczna Zakrwawiona istota w promieniu 18 m od ciebie zostaje trafiona testem ataku, "
        "możesz w ramach reakcji zmniejszyć obrażenia tego ataku o połowę (zaokrąglając w dół)."
    ),
    "h5360cb80gee7ag0e61g2927g4eace8e2c5e6": (
        "Gdy widoczna istota w promieniu 9 m od ciebie ma wykonać udany rzut obronny, możesz w ramach reakcji "
        "zużyć jedno użycie Aktu wiary i zapewnić temu rzutowi utrudnienie, wnikając w umysł celu, zanim wynik "
        "zostanie rozstrzygnięty."
    ),
    "h373150f8gf513g0146g7190ge9494becea23": (
        "Tchórz. Cel oraz każda wybrana przez ciebie istota w emanacji o promieniu 9 m, której źródłem jest "
        "cel, muszą wykonać rzut obronny na Mądrość. Przy niepowodzeniu otrzymują stan Przerażenia do początku twojej "
        "następnej tury. Dopóki istota jest Przerażona, jej szybkość zmniejsza się o połowę (zaokrąglając w dół) "
        "i może ona wykonać akcję albo akcję dodatkową, ale nie obie."
    ),
    "h55dbf30agbd12g301dga596g935c9cd3ab5e": (
        "Srebrzysta energia wybucha z ciebie linią o długości 36 m i szerokości 1,5 m. Każda wybrana przez "
        "ciebie istota w linii wykonuje rzut obronny na Siłę. Przy niepowodzeniu otrzymuje obrażenia od mocy i "
        "stan Powalenia, a przy powodzeniu — tylko połowę obrażeń."
    ),
    "h102e9b14g2c12gd739gf2fegff7c28ae9efe": (
        "Przywołujesz niebiańskiego ducha. Pojawia się w anielskiej postaci na widocznym, niezajętym miejscu "
        "w zasięgu i korzysta z bloku statystyk Niebiańskiego Ducha."
    ),
    "h77baae07gb508ga5a7g250fg1e4e4b4a196c": (
        "Gdy twoje punkty wytrzymałości spadną do 0, ale nie zginiesz od razu, możesz sprawić, że twoje ciało "
        "wybuchnie śmiercionośną energią. Każda wybrana przez ciebie istota w emanacji o promieniu 9 m, której "
        "źródłem jesteś, wykonuje rzut obronny na Kondycję przeciwko twojemu ST obrony przed czarami. Przy "
        "niepowodzeniu otrzymuje obrażenia nekrotyczne równe sumie 2k10 i twojego modyfikatora Charyzmy, a "
        "przy powodzeniu — połowę tych obrażeń. Następnie twoje punkty wytrzymałości wynoszą dwukrotność "
        "twojego poziomu czarownika, a ty zyskujesz 1 poziom Wyczerpania."
    ),
    "ha9361cceg5dd0g35ecg1949g313ca2768512": (
        "Przedmurze. Gdy zostajesz poddany efektowi, który nadałby ci stan Powalenia, możesz w ramach reakcji "
        "zachować równowagę i nie otrzymać tego stanu.\n\nŻelazny żołądek. Za każdym razem, gdy odzyskujesz "
        "punkty wytrzymałości, odzyskujesz dodatkowe punkty w liczbie równej swojemu modyfikatorowi Kondycji."
    ),
    "h625d9005geaaagf264gd451g2b3a70bba135": (
        "Gdy zostajesz poddany efektowi, który nadałby ci stan Powalenia, możesz w ramach reakcji zachować "
        "równowagę i nie otrzymać tego stanu."
    ),
})

UID_OVERRIDES["hc1cce658gb841g21b6gb82bgc5fddc780327"] = UID_OVERRIDES[
    "h1d1a9875g453ag1a74g99c0g7c41137717d6"
]
UID_OVERRIDES["he7d011e0gaae4g9343gae55g467fb0606a35"] = UID_OVERRIDES[
    "ha2bb03e3g700ag8cdagaff7gd4fdd097b625"
]
UID_OVERRIDES["hc87e44d6gbe9cg19ceg0681g7bf7a87f2bd0"] = UID_OVERRIDES[
    "h9f5052c1ga6c8ga38cg6399gbc4405cf0442"
]
UID_OVERRIDES["h81b4dc8dg3da9gf440gb6ccgfc1f97fafdf6"] = UID_OVERRIDES[
    "h8dc48af4gcdf0gdb45g88c4g86ba48d298cb"
]
UID_OVERRIDES["hc24409fagede8g0aaag1ad3g32c2949bb667"] = UID_OVERRIDES[
    "heb2a7f7ag521bg6a02g5dffg52cdf49a9788"
]
for duplicate_uid in (
    "h34c68c98gf84cgb2fcgd117g22156d427b46",
    "h7d224144gf1bcgdd1cg66e2g767541b3331e",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["hb5512cccg4740g2f7dg76e9gd4d73b16a044"]
UID_OVERRIDES["hd056c493g818eg1d13g8842g31b9217e79e6"] = UID_OVERRIDES[
    "h5360cb80gee7ag0e61g2927g4eace8e2c5e6"
]
UID_OVERRIDES["h173fc315gc0d2g81edgd93dg3ddf2abd9626"] = UID_OVERRIDES[
    "h373150f8gf513g0146g7190ge9494becea23"
]
for duplicate_uid in (
    "h173a0fccg668ag5a93gc996gfe83b0867a07",
    "hf1f2ce33g9f28ga79dg8ad9g713bd9d1afd1",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h621ec36dg3794g4862g4538gb2c4399f06cd"]


# Full rewrites of entries whose baseline translation preserved the rules but
# produced broken Polish syntax or mistranslated a game term.  Repeated handles
# intentionally share one reviewed text so their UI variants cannot drift.
UID_OVERRIDES.update({
    "h530230d7ge34cg06b9g06a3ge16228b8a608": (
        "Każda z tych istot zyskuje tymczasowe punkty wytrzymałości w liczbie równej dwukrotności wyniku "
        "rzutu kością bardowskiej inspiracji i może poruszać się bez prowokowania ataków okazyjnych do końca "
        "swojej następnej tury."
    ),
    "h05f1c3ebg02fcg677cga473g464cac2d584f": (
        "Wbijasz kolec energii psionicznej w umysł jednej widocznej istoty w zasięgu. Cel wykonuje rzut "
        "obronny na Mądrość. Przy niepowodzeniu otrzymuje obrażenia psychiczne, a przy powodzeniu — połowę "
        "tych obrażeń. Przy niepowodzeniu znasz również położenie celu aż do zakończenia czaru. Dopóki masz "
        "tę wiedzę, cel nie może się przed tobą ukryć, a jeśli ma "
        "<LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">stan Niewidzialności</LSTag>, nie czerpie z niego "
        "żadnych korzyści przeciwko tobie."
    ),
    "haddaa3c4ga780gc6c0g5533g2da826d6931f": (
        "Wywołujesz wybuch energii psionicznej w wybranym punkcie w zasięgu. Każda istota w sferze o "
        "promieniu [1], której środkiem jest ten punkt, wykonuje rzut obronny na Inteligencję. Przy "
        "niepowodzeniu otrzymuje obrażenia psychiczne, a przy powodzeniu — połowę tych obrażeń.\n\nPrzy "
        "niepowodzeniu myśli celu zostają również zmącone na 1 minutę. Przez ten czas cel odejmuje 1k6 od "
        "wszystkich swoich testów ataku i cech oraz od rzutów obronnych na Kondycję wykonywanych w celu "
        "utrzymania Koncentracji. Na koniec każdej swojej tury cel powtarza rzut obronny na Inteligencję, "
        "kończąc ten efekt na sobie przy powodzeniu."
    ),
    "h25a52b4bg965bga6bdgaee9gb81edcb888e9": (
        "W dzikiej postaci zyskujesz następujące korzyści.\n\nKsiężycowy blask. Każdy twój atak w "
        "dzikiej postaci może zadawać obrażenia zwykłego typu albo obrażenia od światłości. Wybierasz typ "
        "obrażeń za każdym razem, gdy trafiasz takim atakiem.\n\nZwiększona wytrzymałość. Możesz dodawać "
        "swój modyfikator Mądrości do rzutów obronnych na Kondycję."
    ),
    "h62e16743gcb72g9068gb2d0gb1a62ea9d321": (
        "Nauczyłeś się czerpać z mocy Shadowfell, dzięki czemu zyskujesz następujące korzyści.\n\nCiemność. "
        "Możesz zużyć 1 punkt skupienia, aby rzucić czar Ciemność bez komponentów. Gdy rzucasz go za pomocą "
        "tej zdolności, widzisz w jego obszarze. Dopóki czar trwa, na początku każdej swojej tury możesz "
        "przenieść jego obszar ciemności na pole w promieniu [1] od siebie.\n\nWidzenie w ciemności. Zyskujesz "
        "widzenie w ciemności o zasięgu [1]. Jeśli już je masz, jego zasięg zwiększa się o 18 m.\n\nMroczne "
        "widziadła. Znasz czar <LSTag Type=\"Spell\" Tooltip=\"Target_ImprovedMinorIllusion\">Pomniejsza "
        "iluzja</LSTag>. Cechą bazową rzucania tego czaru jest Mądrość."
    ),
    "h32ed567egee36g91e1g2accgb992c0f4d730": (
        "Podczas nauki magii wybierasz również inną dziedzinę specjalizacji. Wybierz jedną z poniższych "
        "umiejętności, w której masz biegłość: <LSTag Type=\"Skills\" Tooltip=\"Arcana\">Wiedza "
        "tajemna</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"History\">Historia</LSTag>, Śledztwo, "
        "<LSTag Type=\"Skills\" Tooltip=\"Medicine\">Medycyna</LSTag>, <LSTag Type=\"Skills\" "
        "Tooltip=\"Nature\">Natura</LSTag> albo <LSTag Type=\"Skills\" Tooltip=\"Religion\">Religia</LSTag>. "
        "Zyskujesz specjalizację w wybranej umiejętności."
    ),
    "h215cfcadg8e38gf1d3g5cbfgf68a823d6955": (
        "Drzewcowe uderzenie. Natychmiast po wykonaniu akcji Ataku i zaatakowaniu kijem bojowym, włócznią "
        "albo bronią o właściwościach Ciężka i Dalekosiężna możesz w ramach akcji dodatkowej wykonać atak "
        "wręcz przeciwległym końcem broni. Atak zadaje obrażenia obuchowe, a jego kością obrażeń jest k4."
        "\n\nReakcyjne uderzenie. Gdy trzymasz kij bojowy, włócznię albo broń o właściwościach Ciężka i "
        "Dalekosiężna, możesz w ramach reakcji wykonać jeden atak wręcz przeciwko istocie, która znajdzie się "
        "w zasięgu tej broni."
    ),
    "h355c781dg7ea0g31c3g7904g5e09dcd7d24d": (
        "Ślepowidzenie. Masz ślepowidzenie o zasięgu 3 m.\n\nMgła wojny. ST wymagane do uzyskania stanu "
        "Niewidzialności za pomocą akcji Ukrycia wynosi 15 zamiast 20."
    ),
    "ha908486dgac97g5080g2fcdg248197559140": (
        "Rozmowa ze zwierzętami. Zawsze masz przygotowany czar Rozmowa ze zwierzętami i możesz rzucać go, "
        "zużywając dowolne posiadane komórki czarów.\n\nZgrany zespół. Gdy wykonujesz akcję Pomocy, możesz "
        "w ramach tej samej akcji zamienić się miejscami z przychylnym sojusznikiem w promieniu 1,5 m od "
        "siebie. Ten ruch nie prowokuje ataków okazyjnych."
    ),
    "h3ab69a8agd42agbda7g29dbgb432d976003a": (
        "Atut: Nowicjusz Szmaragdowej Enklawy\n\nJako opiekun Szmaragdowej Enklawy troszczysz się o tych, "
        "którzy dbają o świat. Wraz z innymi członkami Enklawy lub na własną rękę opanowałeś umiejętności "
        "niezbędne do życia w zgodzie z naturą: tropienie zwierzyny, odnajdywanie przydatnych ziół, a nawet "
        "przewidywanie pogody. Wykorzystujesz te talenty, aby zachować równowagę między cywilizacją a dziczą "
        "oraz oczyszczać świat z wynaturzonych istot.\n\nRozmowa ze zwierzętami. Zawsze masz przygotowany czar "
        "Rozmowa ze zwierzętami i możesz rzucać go, zużywając dowolne posiadane komórki czarów.\n\nZgrany "
        "zespół. Gdy wykonujesz akcję Pomocy, możesz w ramach tej samej akcji zamienić się miejscami z "
        "przychylnym sojusznikiem w promieniu 1,5 m od siebie. Ten ruch nie prowokuje ataków okazyjnych."
    ),
    "h2c90402dgbf9bg9e7eg0564g9741710af3b2": (
        "Gdy nie powiedzie ci się test cechy z użyciem umiejętności albo narzędzia, w którym masz biegłość, "
        "możesz rzucić jedną kością energii psionicznej i dodać wynik do testu, co może zmienić niepowodzenie "
        "w powodzenie. Kość zostaje zużyta tylko wtedy, gdy test zakończy się dzięki temu powodzeniem."
    ),
    "h62045b01g1a09g4697g2c04gdffed6c1900a": (
        "Gdy otrzymujesz obrażenia, możesz w ramach reakcji rzucić 1k12. Dodaj do wyniku swój modyfikator "
        "Kondycji i zmniejsz otrzymane obrażenia o uzyskaną sumę."
    ),
    "h8fd47ec3gac34g4144g6243g234bbbbbb9ae": (
        "Cel musi wykonać rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje [1], a ty odzyskujesz punkty "
        "wytrzymałości w liczbie równej zadanym obrażeniom. Przy powodzeniu cel otrzymuje połowę tych obrażeń, "
        "a ty odzyskujesz punkty wytrzymałości w liczbie równej zadanym obrażeniom."
    ),
    "hab1f563cgd118gb03bg41b5g1316f04ab315": (
        "Gdy otrzymujesz obrażenia, możesz w ramach reakcji nakazać armacie wybuchnąć. Każda wroga istota w "
        "promieniu 6 m od ciebie wykonuje rzut obronny na Zręczność przeciwko twojemu ST obrony przed "
        "czarami. Przy niepowodzeniu otrzymuje 3k10 obrażeń od mocy, a przy powodzeniu — połowę tych obrażeń. "
        "Możesz użyć tej zdolności raz na krótki odpoczynek."
    ),
    "hfdadc829g334eg78cegcbaegac19146a68cc": (
        "W ramach akcji Magii możesz wyzwolić z ostrza skupioną wiązkę błyskawic tworzącą linię o długości "
        "18 m i szerokości 1,5 m. Każda istota w linii wykonuje rzut obronny na Zręczność o ST 15. Przy "
        "niepowodzeniu otrzymuje 4k6 obrażeń od elektryczności, a przy powodzeniu — połowę tych obrażeń."
    ),
    "ha688aa5dgc9bege050gd0f4gd8a5d10c7791": (
        "Twoja potęga umysłu wzrasta, dzięki czemu roztaczasz uspokajającą projekcję w emanacji o promieniu "
        "3 m, której źródłem jesteś. Projekcja jest nieaktywna, gdy masz stan Obezwładnienia.\n\nTy i twoi "
        "sojusznicy znajdujący się w projekcji zyskujecie premię +2 do rzutów obronnych na Inteligencję, "
        "Mądrość i Charyzmę.\n\nJeśli w pobliżu znajduje się inny kleryk Domeny Umysłu, istota może "
        "jednocześnie korzystać tylko z jednej Kotwicy Gestalt."
    ),
    "h949175afg7b78g0963gee66g437f1ebddb65": (
        "Twoja potęga umysłu wzrasta, dzięki czemu roztaczasz uspokajającą projekcję w emanacji o promieniu "
        "3 m, której źródłem jesteś. Projekcja jest nieaktywna, gdy masz stan Obezwładnienia.\n\nTy i twoi "
        "sojusznicy znajdujący się w projekcji zyskujecie premię +2 do rzutów obronnych na Inteligencję, "
        "Mądrość i Charyzmę."
    ),
    "hc68e827eg501cgbab0ga48egb7055d764e5b": (
        "Przywołujesz słup czarodziejskiego ognia w cylindrze o promieniu 6 m i wysokości 6 m, którego środkiem "
        "jest wybrany punkt w zasięgu. Obszar cylindra jest jasno oświetlony. Gdy cylinder się pojawia, każda "
        "znajdująca się w nim istota wykonuje rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje obrażenia "
        "od światłości, a przy powodzeniu — połowę tych obrażeń. Istota wykonuje ten rzut również wtedy, gdy "
        "po raz pierwszy w swojej turze wejdzie na obszar czaru albo zakończy tam turę, lecz nie częściej niż "
        "raz na turę.\n\nPonadto za każdym razem, gdy istota w cylindrze rzuca czar, wykonuje rzut obronny na "
        "Kondycję. Przy niepowodzeniu czar rozprasza się bez żadnego efektu, a akcja, akcja dodatkowa albo "
        "reakcja zużyta na jego rzucenie przepada.\n\nPodczas rzucania tego czaru możesz wskazać istoty, na "
        "które nie będzie on działać."
    ),
    "h05279eecg66b6g48b2gd7bbg31b8b9364190": (
        "W wybranym kierunku rozchodzi się od ciebie linia ryczącego ognia o długości 9 m i szerokości 1,5 m. "
        "Każda istota w linii wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia od "
        "ognia, a przy powodzeniu — połowę tych obrażeń."
    ),
    "ha71f769bge1a3g46dfg432fga8899602df6a": (
        "Podpalacz. Cel wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia od ognia "
        "równe sumie czterech rzutów kością <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">"
        "bardowskiej inspiracji</LSTag>, a przy powodzeniu — połowę tych obrażeń."
    ),
    "hec346c79gf7e0ga44egbc79gbe72af6c9ba3": (
        "Cel wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia od ognia równe sumie "
        "czterech rzutów kością <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">bardowskiej "
        "inspiracji</LSTag>, a przy powodzeniu — połowę tych obrażeń."
    ),
    "h029cddf2gf1b9g86a2g45e7g18bf046b40f1": (
        "Wyzwalasz falę wirujących cieni, która wypełnia przylegający do ciebie obszar. Każda istota w "
        "3-metrowym sześcianie ciemności, którego źródłem jesteś, wykonuje rzut obronny na Mądrość. Przy "
        "niepowodzeniu otrzymuje 2k8 obrażeń psychicznych i stan Oślepienia do początku twojej następnej tury. "
        "Przy powodzeniu otrzymuje połowę tych obrażeń i nie zostaje Oślepiona."
    ),
    "hb4eeb71eg4ea7gf2cdg4726g7e2a70934cc5": (
        "Wybuch zimnej energii rozchodzi się od ciebie w stożku o długości 9 m. Każda istota na tym obszarze "
        "wykonuje rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje obrażenia od zimna i zostaje uwięziona "
        "w lodowych formacjach na 1 turę, co zmniejsza jej szybkość do 0. Przy powodzeniu otrzymuje połowę "
        "tych obrażeń i nie zostaje uwięziona w lodzie."
    ),
    "ha9fe2937g7f92g0c7bg387bge95b2c6fd446": (
        "W ramach akcji dodatkowej możesz podnieść kamień i wykonać nim magiczny atak. Jest to dystansowy "
        "atak czarem o zasięgu 18 m, wykorzystujący twoją cechę bazową rzucania czarów. Przy trafieniu kamień "
        "zadaje 1k10 obrażeń od mocy, a cel musi wykonać udany rzut obronny na Siłę (ST wynosi 8 + twoja "
        "premia z biegłości + twój modyfikator cechy bazowej rzucania czarów) albo otrzymuje stan Powalenia."
    ),
})

UID_OVERRIDES["h3dd5e7b4g4865gbd7bged74gd82f6e53d20d"] = UID_OVERRIDES[
    "h215cfcadg8e38gf1d3g5cbfgf68a823d6955"
]
UID_OVERRIDES["h0df1df8cg4144g5ee4g0641gab98d991d8dc"] = UID_OVERRIDES[
    "h355c781dg7ea0g31c3g7904g5e09dcd7d24d"
]
UID_OVERRIDES["h9dd6f816g7d8eg2378g9af9g3b609e271919"] = UID_OVERRIDES[
    "ha908486dgac97g5080g2fcdg248197559140"
]

SHEEP_FORM_TEXT = (
    "Zmieniasz się w owcę do początku swojej następnej tury. W tej postaci masz stan Obezwładnienia i "
    "podatność na wszystkie obrażenia. Jeśli twoje punkty wytrzymałości spadną do 0, natychmiast wracasz do "
    "swojej zwykłej postaci."
)
for duplicate_uid in (
    "he8a359d2g85c2g4182g876cg6b35007745eb",
    "hd4eb497cg5894g467ega7feg4d27550eff7f",
    "h5809be0ega7e9g4091gb93cg6307099b32e3",
    "hca1d09ecgac01g45a5gbf6ag1a6c36f93c81",
):
    UID_OVERRIDES[duplicate_uid] = SHEEP_FORM_TEXT

MOONBEAM_TEXT = (
    "Blady, srebrzysty promień pada na cylinder o promieniu 1,5 m i wysokości 12 m, którego środkiem jest "
    "wybrany punkt w zasięgu. Do zakończenia czaru cylinder jest słabo oświetlony. W kolejnych turach możesz "
    "w ramach akcji Magii przenieść cylinder na odległość do 18 m.\n\nGdy cylinder się pojawia, każda "
    "znajdująca się w nim istota wykonuje rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje obrażenia od "
    "światłości, a przy powodzeniu — połowę tych obrażeń. Istota wykonuje ten rzut również wtedy, gdy obszar "
    "czaru przesunie się na jej pole albo gdy zakończy w nim turę, lecz nie częściej niż raz na turę."
)
for duplicate_uid in (
    "hb5c8a2c2gcb05g89ceg701dg519dda931a2d",
    "hc24592adg7667g3703g77f3g28bd0167f967",
    "h2a605fbbg9e30g5d2fg99cfge3895f1bc658",
    "h3d8e9323g4462gb81dg88e1g83c02f1a2c2b",
    "heee3ac7dg3b5cg3d93geb1dgae3f70c163c3",
):
    UID_OVERRIDES[duplicate_uid] = MOONBEAM_TEXT

THUNDER_EMANATION_TEXT = (
    "Przez czas trwania czaru grzmiące pogłosy wypełniają emanację o promieniu 3 m, której źródłem jesteś. "
    "Za każdym razem, gdy emanacja obejmuje pole istoty, a także gdy istota wchodzi w emanację albo kończy w "
    "niej turę, wykonuje rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje obrażenia od dźwięku, a przy "
    "powodzeniu — połowę tych obrażeń. Istota wykonuje ten rzut tylko raz na turę.\n\nPonadto masz odporność "
    "na obrażenia od dźwięku, a dystansowe testy ataku przeciwko tobie mają utrudnienie."
)
for duplicate_uid in (
    "ha911b6bdg2959g695ag9c06gb0936ebd052e",
    "h656c049cg0ff4g758bge643g1386718cedb8",
    "hf67f7f88ga42fgb7c6g3526gd17410ea4287",
):
    UID_OVERRIDES[duplicate_uid] = THUNDER_EMANATION_TEXT

INNATE_WEAPON_MAGIC_TEXT = (
    "Gdy zdolność Wrodzone Czarnoksięstwo jest aktywna, podczas ataku bronią, którą biegle się posługujesz, "
    "możesz używać modyfikatora Charyzmy zamiast Siły albo Zręczności w testach ataku i rzutach na obrażenia."
)
for duplicate_uid in (
    "h11d402ccg5d0ag742bgf457g44dda07625c7",
    "he6de2090g4ec1g94fdg1c3fgd41c1e984607",
):
    UID_OVERRIDES[duplicate_uid] = INNATE_WEAPON_MAGIC_TEXT

FRIGHTENED_UNTIL_NEXT_TURN_TEXT = "Masz stan Przerażenia do końca swojej następnej tury."
for duplicate_uid in (
    "h1f99f5cdg1051g4c3ag9aaeg3de12140280c",
    "h444dcbd8ge750g47a1g8435g2ef2a86cd29d",
    "hdd3aa3bag0467g4cbdg8137ge567f9ff8c1e",
    "h77ea0c5eg60afg490bgb41ag743886d5dd25",
):
    UID_OVERRIDES[duplicate_uid] = FRIGHTENED_UNTIL_NEXT_TURN_TEXT

ARCANE_WARDS_TEXT = (
    "Przez czas trwania efektu tajemne bariery chronią cię przed magią. Masz ułatwienie w rzutach obronnych "
    "przeciwko czarom i efektom magicznym oraz odporność na obrażenia od czarów."
)
for duplicate_uid in (
    "hba127cc1ga142gbe30g42a0gefcf3b5c831e",
    "h9f0fa794gdfc2ge2f8gcf06g046d97ef0b1d",
):
    UID_OVERRIDES[duplicate_uid] = ARCANE_WARDS_TEXT

UID_OVERRIDES.update({
    "h637a148fgbbb7g2269gfdd1g3f81fddd5949": (
        "W ramach akcji Magii możesz zużyć 2 punkty skupienia, aby wywołać wybuch energii żywiołów w sferze "
        "o promieniu [1], której środkiem jest punkt w odległości do [2] od ciebie. Wybierz typ obrażeń: od "
        "kwasu, zimna, ognia, elektryczności albo dźwięku.\n\nKażda istota w sferze wykonuje rzut obronny "
        "na Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego typu równe sumie trzech rzutów twoją "
        "kością sztuk walki, a przy powodzeniu — połowę tych obrażeń."
    ),
    "hc9341211ge6c1g1fd9gddbeg13315817fedb": (
        "Zyskujesz biegłość w dwóch wybranych umiejętnościach spośród następujących: "
        "<LSTag Type=\"Skills\" Tooltip=\"Arcana\">Wiedza tajemna</LSTag>, "
        "<LSTag Type=\"Skills\" Tooltip=\"History\">Historia</LSTag>, "
        "<LSTag Type=\"Skills\" Tooltip=\"Nature\">Natura</LSTag> albo "
        "<LSTag Type=\"Skills\" Tooltip=\"Religion\">Religia</LSTag>. Zyskujesz specjalizację w obu "
        "wybranych umiejętnościach."
    ),
    "hfd4a4e4dg3a3eg0bd1g2716gc7e32738a35f": (
        "Czerpiesz ze swojej siły życiowej, aby się uleczyć. Rzuć [1] niewydanymi kośćmi wytrzymałości i "
        "odzyskaj punkty wytrzymałości w liczbie równej sumie wyników oraz twojego modyfikatora cechy bazowej "
        "rzucania czarów. Następnie wydajesz te kości."
    ),
    "h8adb922fgacb1g0f7fg68fagec7157198cc9": (
        "Twój patron obdarza cię zdolnością przemieszczania się między granicami sfer. Możesz rzucić Mglisty "
        "krok bez zużywania komórki czaru tyle razy, ile wynosi twój modyfikator Charyzmy (co najmniej raz), "
        "a wszystkie zużyte użycia odzyskujesz po długim odpoczynku.\n\nPonadto za każdym razem, gdy rzucasz "
        "ten czar, możesz wybrać jeden z poniższych dodatkowych efektów.\n\nOżywczy krok. Natychmiast po "
        "teleportacji ty i jedna widoczna istota w promieniu 3 m od ciebie zyskujecie po 1k10 tymczasowych "
        "punktów wytrzymałości.\n\nProwokujący krok. Istoty w promieniu 3 m od opuszczonego przez ciebie pola "
        "muszą wykonać udany rzut obronny na Mądrość przeciwko twojemu ST obrony przed czarami. W przeciwnym "
        "razie do początku twojej następnej tury mają utrudnienie w testach ataku przeciwko istotom innym "
        "niż ty."
    ),
    "h444275c2g565cg45a9gdfbdg183d47facddb": (
        "Istoty w promieniu 3 m od opuszczonego przez ciebie pola muszą wykonać udany rzut obronny na Mądrość "
        "przeciwko twojemu ST obrony przed czarami. W przeciwnym razie do początku twojej następnej tury mają "
        "utrudnienie w testach ataku przeciwko istotom innym niż ty."
    ),
    "hcf424f73gfc0dg7cc2gd583ga378200e953d": (
        "Gdy Pieśń klingi jest aktywna, zyskujesz następujące korzyści.\n\nZwinność. Zyskujesz premię do KP "
        "równą swojemu modyfikatorowi Inteligencji (co najmniej +1), a twoja szybkość zwiększa się o 3 m. "
        "Ponadto testy Zręczności (<LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Akrobatyka</LSTag>) mają "
        "ułatwienie.\n\nKunszt klingi. Gdy atakujesz bronią, którą biegle się posługujesz, możesz używać "
        "modyfikatora Inteligencji zamiast Siły albo Zręczności w testach ataku i rzutach na obrażenia."
        "\n\nSkupienie. Gdy wykonujesz rzut obronny na Kondycję, aby utrzymać Koncentrację, możesz dodać do "
        "wyniku swój modyfikator Inteligencji."
    ),
    "h1669b47agf0fagd245g92f2g0e39a2c90370": (
        "Zwinność. Zyskujesz premię do KP równą swojemu modyfikatorowi Inteligencji (co najmniej +1), a "
        "twoja szybkość zwiększa się o 3 m. Ponadto testy Zręczności "
        "(<LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Akrobatyka</LSTag>) mają ułatwienie.\n\nKunszt "
        "klingi. Gdy atakujesz bronią, którą biegle się posługujesz, możesz używać modyfikatora Inteligencji "
        "zamiast Siły albo Zręczności w testach ataku i rzutach na obrażenia.\n\nSkupienie. Gdy wykonujesz "
        "rzut obronny na Kondycję, aby utrzymać Koncentrację, możesz dodać do wyniku swój modyfikator "
        "Inteligencji."
    ),
    "hede9123cg6b75g7af2ge6a9g09aa7751575f": (
        "Gdy atakujesz bronią, którą biegle się posługujesz, możesz używać modyfikatora Inteligencji zamiast "
        "Siły albo Zręczności w testach ataku i rzutach na obrażenia."
    ),
    "h352f38e9g6190gf239gf947g79ecb474c84f": (
        "Zyskujesz biegłość we wszystkich żołnierskich broniach do walki wręcz, które nie mają właściwości "
        "Dwuręczna ani Ciężka. Możesz używać broni do walki wręcz, którą biegle się posługujesz, jako "
        "magicznego skupienia dla swoich czarów maga.\n\nZyskujesz też biegłość w jednej wybranej "
        "umiejętności spośród następujących: <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Akrobatyka</LSTag>, "
        "<LSTag Type=\"Skills\" Tooltip=\"Athletics\">Atletyka</LSTag>, "
        "<LSTag Type=\"Skills\" Tooltip=\"Performance\">Występy</LSTag> albo "
        "<LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Perswazja</LSTag>."
    ),
    "h8c1cf02dg530eg20c8ge29dgf4ccedf5993c": (
        "Gdy w swojej turze zużywasz co najmniej 1 punkt zaklinania w ramach akcji Magii albo akcji "
        "dodatkowej, możesz wywołać jeden z poniższych wybranych efektów magicznych. Możesz zrobić to tylko "
        "raz na turę.\n\nWzmacniające płomienie. Ty albo jedna widoczna istota w promieniu 9 m od ciebie "
        "zyskujecie 1k4 plus twój modyfikator Charyzmy tymczasowych punktów wytrzymałości.\n\nŚwietlisty "
        "ogień. Jedna widoczna istota w promieniu 9 m od ciebie otrzymuje 1k4 obrażeń od ognia albo światłości "
        "(wedle twojego wyboru)."
    ),
    "hc87bcd1cg1649gb998g7e26g83dd5ad52f38": (
        "Gdy zadajesz obrażenia bronią dystansową, która zwykle nie pozwala dodać modyfikatora cechy do rzutu "
        "na obrażenia, mimo to go dodajesz. Jeśli już dodajesz ten modyfikator, cel otrzymuje dodatkowe 1k8 "
        "obrażeń tego samego typu co broń."
    ),
    "h7ac87358g45e1g10c6ga7c3g85b624d04c91": (
        "Gdy nie powiedzie ci się test Inteligencji, Mądrości albo Charyzmy lub rzut obronny na jedną z tych "
        "cech, możesz zużyć jedną kość ryzyka i dodać jej wynik do rzutu, co może zmienić niepowodzenie w "
        "powodzenie. Możesz użyć tego manewru tylko raz na turę."
    ),
    "h99e9e197g55f2g72f5g3b37g75a3f15b60bc": (
        "Jesteś ekspertem w posługiwaniu się bronią palną. Możesz dodawać swój modyfikator cechy do rzutów na "
        "obrażenia zadawane atakami z broni palnej."
    ),
    "h3ce77d91geeefg513cga446gb56d92a559cd": (
        "Gdy twój atak trafia albo chybia cel, broń lub amunicja przemienia się w linię magicznej energii o "
        "szerokości 1,5 m, sięgającą na zwykły zasięg broni. Linia obejmuje pierwotny cel ataku. Każda istota "
        "w linii wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia od mocy równe "
        "zwykłym obrażeniom broni, a przy powodzeniu — połowę tych obrażeń."
    ),
    "h567842fbg3adcgb2d8ga509g4f0c4fef8cc5": (
        "Armata wyrzuca ogień w stożku o długości 4,5 m. Każda istota na tym obszarze wykonuje rzut obronny "
        "na Zręczność przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu otrzymuje obrażenia od "
        "ognia, a przy powodzeniu — połowę tych obrażeń. Łatwopalne przedmioty w stożku, które nie są noszone "
        "ani trzymane, zaczynają płonąć."
    ),
    "hb033a976g4cccgdbedg5c40ge3ee8016bca2": (
        "Gdy rzucasz czar Shillelagh, możesz nasycić mocą natury dowolną trzymaną broń do "
        "walki wręcz. Możesz zdecydować, że broń zachowuje swoją zwykłą kość obrażeń, zamiast zmieniać ją na "
        "k8. Ponadto możesz używać dowolnej broni, którą biegle się posługujesz, jako magicznego skupienia dla "
        "swoich czarów druida."
    ),
    "hac6a3cd4g227dg6382g6388g92a7edb553be": (
        "Uderzasz mocą umysłu w jedną widoczną istotę w zasięgu. Cel wykonuje rzut obronny na Inteligencję. "
        "Przy niepowodzeniu otrzymuje obrażenia psychiczne i nie może używać reakcji do końca swojej następnej "
        "tury. Ponadto w swojej następnej turze może wykonać akcję albo akcję dodatkową, ale nie obie. Przy "
        "powodzeniu otrzymuje połowę obrażeń i nie podlega żadnym innym efektom czaru."
    ),
    "h1b6a7023gadf1g5468g1b86gda2cac4d8e2b": (
        "Masz ułatwienie w rzutach obronnych wykonywanych, aby uniknąć albo zakończyć stan Przerażenia."
    ),
    "h50b49a89g7327gee14gb91dg12153f8b0fd5": "Masz karę –5 do inicjatywy.",
    "hff4e6b44g07dbg7d46g1dfbg11ee89aaef5b": (
        "Masz biegłość w jednej z następujących umiejętności: "
        "<LSTag Type=\"Skills\" Tooltip=\"Insight\">Intuicja</LSTag>, "
        "<LSTag Type=\"Skills\" Tooltip=\"Perception\">Percepcja</LSTag> albo "
        "<LSTag Type=\"Skills\" Tooltip=\"Survival\">Sztuka przetrwania</LSTag>."
    ),
    "h282b4762g8c1dgbed2ga8d4g5feabffdd2b7": (
        "Masz biegłość w jednej z następujących umiejętności: Intuicja, Percepcja albo Sztuka przetrwania."
    ),
    "h268f496ag5b58g49c9g3c99ga0cd4839f89f": (
        "Jeśli masz mistrzostwo w posługiwaniu się toporem bojowym, długim mieczem albo włócznią, możesz "
        "dodać swoją premię z biegłości do rzutu na obrażenia tą bronią."
    ),
})

for duplicate_uid in (
    "h34d5fc08g03dage117ge30cge3bac9365062",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h8c1cf02dg530eg20c8ge29dgf4ccedf5993c"]
UID_OVERRIDES["h86b389a9gfe27g7353g9f20g12d9431a57fa"] = UID_OVERRIDES[
    "h99e9e197g55f2g72f5g3b37g75a3f15b60bc"
]

LIGHTNING_AMMUNITION_TEXT = (
    "Gdy twój atak trafia albo chybia cel, używana broń lub amunicja przemienia się w błyskawicę. Zamiast "
    "obrażeń i innych efektów ataku cel otrzymuje 4k8 obrażeń od elektryczności przy trafieniu albo połowę "
    "tych obrażeń przy chybieniu. Każda istota w promieniu 3 m od celu otrzymuje 2k8 obrażeń od "
    "elektryczności."
)
for duplicate_uid in (
    "hc421c06eg7266g8444g3e70g03d5b5fcf166",
    "hbc4b3cdeg1f95g6b65gad88g180de678c0b5",
    "h13cf2c9bg80e6g0163g3e81g9d59cc051df8",
):
    UID_OVERRIDES[duplicate_uid] = LIGHTNING_AMMUNITION_TEXT

HEROIC_INSPIRATION_REROLL_TEXT = (
    "Jeśli masz heroiczną inspirację, możesz ją zużyć natychmiast po rzucie dowolną kością, aby wykonać ten "
    "rzut ponownie."
)
UID_OVERRIDES["h43bcb1b9g7661gd847g5c69g16cf92019e88"] = HEROIC_INSPIRATION_REROLL_TEXT
UID_OVERRIDES["hd9193a10g8e78g28bagc22eg90d1be20c4d7"] = (
    "Po każdym długim odpoczynku zyskujesz heroiczną inspirację. " + HEROIC_INSPIRATION_REROLL_TEXT
)
UID_OVERRIDES["hd06d9d97g3639gb022g0e2eg25f5ab8ca49e"] = (
    "Po każdym długim odpoczynku zyskujesz <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">"
    "heroiczną inspirację</LSTag>. " + HEROIC_INSPIRATION_REROLL_TEXT
)

DRAGONS_TERROR_TAGGED_TEXT = (
    "Smocza groza. W ramach akcji Magii możesz napełnić grozą jedną widoczną istotę w promieniu 9 m od "
    "siebie. Cel musi wykonać udany rzut obronny na Mądrość albo otrzymuje stan Przerażenia do końca twojej "
    "następnej tury.\n\nNatchnienie strachem. Gdy sprawisz, że istota otrzymuje stan Przerażenia, a ty jesteś "
    "źródłem jej strachu, zyskujesz <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">heroiczną "
    "inspirację</LSTag>. Po użyciu tej korzyści musisz ukończyć krótki albo długi odpoczynek, zanim użyjesz "
    "jej ponownie."
)
DRAGONS_TERROR_PLAIN_TEXT = (
    "Smocza groza. W ramach akcji Magii możesz napełnić grozą jedną widoczną istotę w promieniu 9 m od "
    "siebie. Cel musi wykonać udany rzut obronny na Mądrość albo otrzymuje stan Przerażenia do końca twojej "
    "następnej tury.\n\nNatchnienie strachem. Gdy sprawisz, że istota otrzymuje stan Przerażenia, a ty jesteś "
    "źródłem jej strachu, zyskujesz heroiczną inspirację. Po użyciu tej korzyści musisz ukończyć krótki albo "
    "długi odpoczynek, zanim użyjesz jej ponownie."
)
UID_OVERRIDES["h5648b3eag0325g46d8g5cd1g0463117aab6a"] = DRAGONS_TERROR_TAGGED_TEXT
UID_OVERRIDES["hc477acf9gaec4g36b5g7d0bg06d04d9b41f4"] = DRAGONS_TERROR_PLAIN_TEXT
UID_OVERRIDES["h7859cbddgc1d2g2fb6g37e8ge9fff27abfce"] = (
    "W ramach akcji Magii możesz napełnić grozą jedną widoczną istotę w promieniu 9 m od siebie. Cel musi "
    "wykonać udany rzut obronny na Mądrość albo otrzymuje stan Przerażenia do końca twojej następnej tury."
)
UID_OVERRIDES["h9ce67cb6ga5b0ga13bg7785g0b5aae8510f3"] = (
    "Atut: Nowicjusz Kultu Smoka\n\nJesteś nowicjuszem Kultu Smoka. Odnalazłeś komórkę kultu albo zostałeś "
    "do niej wprowadzony, po czym dowiodłeś, że uosabiasz cenione przez smoczych kultystów wartości: "
    "dwulicowość, dyskrecję i determinację. W zamian za przysięgę służby kult zapewnił ci towarzystwo innych "
    "czcicieli smoków oraz dostęp do zasobów, które mogą pomóc ci pogłębić wiedzę tajemną i okultystyczną."
    "\n\n" + DRAGONS_TERROR_PLAIN_TEXT
)

UID_OVERRIDES["h8c1cf02dg530eg20c8ge29dgf4ccedf5993c"] = (
    "Gdy w swojej turze zużywasz co najmniej 1 punkt zaklinania w ramach akcji Magii albo akcji dodatkowej, "
    "możesz wywołać jeden z poniższych wybranych efektów magicznych. Możesz zrobić to tylko raz na turę."
    "\n\nWzmacniające płomienie. Wybierz siebie albo jedną widoczną istotę w promieniu 9 m od ciebie. Wybrana "
    "istota zyskuje tymczasowe punkty wytrzymałości w liczbie równej sumie 1k4 i twojego modyfikatora "
    "Charyzmy.\n\nŚwietlisty ogień. Jedna widoczna istota w promieniu 9 m od ciebie otrzymuje 1k4 obrażeń od "
    "ognia albo światłości (wedle twojego wyboru)."
)
UID_OVERRIDES["h34d5fc08g03dage117ge30cge3bac9365062"] = UID_OVERRIDES[
    "h8c1cf02dg530eg20c8ge29dgf4ccedf5993c"
]

for duplicate_uid in (
    "he41177dagaf29g13c8gc756g66414bcb409d",
    "h894a8c5dg5c28g7d23gb198gb51499628687",
):
    UID_OVERRIDES[duplicate_uid] = (
        "Studiowanie obrzędów pogrzebowych i troska o spoczynek zmarłych uczyniły z ciebie pośrednika między "
        "światem żywych a światem umarłych. Zyskujesz następujące korzyści.\n\nBoski kanał. Zyskujesz jedno "
        "użycie zdolności Akt wiary klasy kleryka i możesz za jego pomocą wywołać efekt „Odpędzanie "
        "nieumarłych”. Jeśli masz już Akt wiary, dodajesz to użycie do tej zdolności z jednej wybranej klasy."
    )
UID_OVERRIDES["h7d405f4ag1770gee29gfd7egc0479b1be286"] = (
    "Atut: Strażnik grobu\n\nW miejscu położonym bliżej krainy umarłych niż krainy żywych, osoby dbające o wieczny "
    "spoczynek zmarłych budzą zarówno głęboki szacunek, jak i niepokój. Parałeś się pracą grabarza, "
    "pracownika zakładu pogrzebowego i balsamisty. Niekiedy tylko ty potrafiłeś znaleźć życzliwe słowo, aby "
    "uczcić pamięć zmarłych. Dobrze znasz spustoszenie czynione przez nieumarłych i nie pozwalasz im zakłócać "
    "spoczynku powierzonych ci ciał.\n\nStrażnik grobu. Zyskujesz jedno użycie zdolności Akt wiary klasy "
    "kleryka i możesz za jego pomocą wywołać efekt „Odpędzanie nieumarłych”. Jeśli masz już Akt wiary, "
    "dodajesz to użycie do tej zdolności z jednej wybranej klasy."
)

UID_OVERRIDES.update({
    "h2d199d0egf3a1ga886gf931gb46f01ab73e5": (
        "Potężne czarowanie. Dodajesz swój modyfikator Mądrości do obrażeń zadawanych dowolną sztuczką "
        "kleryka."
    ),
    "h363f8861g503bg174cgc576g28e60841fa32": (
        "Gdy atak trafia cię i zadaje obrażenia obuchowe, kłute albo sieczne, możesz w ramach reakcji "
        "zmniejszyć łączną liczbę otrzymywanych obrażeń. Zmniejszasz ją o sumę 1k10, swojego modyfikatora "
        "Zręczności i poziomu mnicha.\n\nJeśli zmniejszy to obrażenia do 0, możesz zużyć 1 punkt ki, aby użyć "
        "Przekierowania ataku."
    ),
    "h658ed514ge9dcg9a0fg207fg2dacf4e5e1ad": (
        "Szkolenie muzyczne. Zyskujesz biegłość w posługiwaniu się trzema instrumentami muzycznymi."
        "\n\nZachęcająca pieśń. Po ukończeniu krótkiego albo długiego odpoczynku możesz zagrać pieśń na "
        "instrumencie, którym biegle się posługujesz, i obdarzyć bardowską inspiracją słyszących ją "
        "sojuszników. Możesz w ten sposób wpłynąć na tyle osób, ile wynosi twoja premia z biegłości."
    ),
    "hbc4803a8gd847gc698gdcb8g8e6853f62ff5": (
        "Szkolenie muzyczne. Zyskujesz biegłość w posługiwaniu się trzema instrumentami muzycznymi."
        "\n\nZachęcająca pieśń. Po ukończeniu krótkiego albo długiego odpoczynku możesz zagrać pieśń na "
        "instrumencie, którym biegle się posługujesz, i obdarzyć heroiczną inspiracją słyszących ją "
        "sojuszników. Możesz w ten sposób wpłynąć na tyle osób, ile wynosi twoja premia z biegłości."
    ),
    "h7d579a81g52d6g1a4cg3fe1ge97bcb251943": (
        "Gdy nie nosisz pancerza ani nie dzierżysz tarczy, zyskujesz następujące korzyści.\n\nWirtuoz "
        "tańca. Masz ułatwienie we wszystkich testach Charyzmy "
        "(<LSTag Type=\"Skills\" Tooltip=\"Performance\">Występy</LSTag>) związanych z tańcem.\n\nObrona "
        "bez pancerza. Twoja bazowa Klasa Pancerza wynosi 10 plus twoje modyfikatory Zręczności i Charyzmy."
        "\n\nZwinne ciosy. Gdy w ramach akcji, akcji dodatkowej albo reakcji zużywasz jedno użycie bardowskiej "
        "inspiracji, możesz w ramach tej samej czynności wykonać jeden atak bez broni.\n\nBardowskie "
        "obrażenia. W testach ataku bez broni możesz używać Zręczności zamiast Siły. Gdy zadajesz obrażenia "
        "atakiem bez broni, zamiast zwykłych obrażeń możesz zadać obrażenia obuchowe równe sumie wyniku rzutu "
        "kością bardowskiej inspiracji i swojego modyfikatora Zręczności. Ten rzut nie zużywa kości."
    ),
    "h1f6491c1gcf0ag5432gd45cg4c396aeb83ed": (
        "Części twojego ciała pokrywają również łuski przypominające smocze. Gdy nie nosisz pancerza, twoja "
        "bazowa Klasa Pancerza wynosi 10 plus twoje modyfikatory Zręczności i Charyzmy."
    ),
    "h3a16b87eg8dd3g9578gd609gbf2f106aa676": (
        "Twoje oczy na chwilę stają się bezdennie czarne, a z pleców wyrastają nielotne, widmowe skrzydła. "
        "Wszystkie istoty poza twoimi sojusznikami w promieniu 3 m od ciebie muszą wykonać udany rzut obronny "
        "na Charyzmę albo otrzymują stan Przerażenia do końca twojej następnej tury."
    ),
    "h42d34c6cg2c2dg6152g7c9dg22ed3a5cedc7": (
        "Ciskasz dezorientującą magiczną siłę w jedną istotę w zasięgu. Cel wykonuje rzut obronny na "
        "Kondycję. Przy niepowodzeniu otrzymuje obrażenia od mocy, jego szybkość zmniejsza się o połowę do "
        "początku twojej następnej tury, a w swojej następnej turze może wykonać tylko akcję albo akcję "
        "dodatkową — nie obie. Przy powodzeniu otrzymuje jedynie połowę obrażeń."
    ),
    "ha9c3ab13g3fb0g8a2eg5ee1gfbd234126c3d": (
        "Przywołujesz falę wody, która rozbija się na obszarze w zasięgu. Obszar może mieć do 9 m długości, "
        "3 m szerokości i 3 m wysokości. Każda istota na tym obszarze wykonuje rzut obronny na Zręczność. "
        "Przy niepowodzeniu otrzymuje 4k8 obrażeń obuchowych i stan Powalenia. Przy powodzeniu otrzymuje "
        "połowę tych obrażeń i nie zostaje Powalona."
    ),
    "h7cc9c7a3g7fbcga1fbg2066g70dad117ebee": (
        "W ramach akcji dodatkowej używanej do aktywowania tej zdolności rzucasz czar Sieć bez zużywania "
        "komórki czaru (ST wynosi 8 + twój modyfikator Zręczności + twoja premia z biegłości). Możesz rzucić "
        "ten czar za pomocą tej zdolności dwa razy. Jedno zużyte użycie odzyskujesz po krótkim odpoczynku, a "
        "wszystkie — po długim odpoczynku."
    ),
    "he9d03706g649dg72b5g3adeg7dd6358e9597": (
        "Możesz ciskać żarzącymi się pociskami magicznej światłości.\n\nZyskujesz nową opcję ataku, której "
        "możesz użyć w ramach akcji Ataku. Ten specjalny atak jest dystansowym atakiem czarem o zasięgu 9 m. "
        "Masz w nim biegłość i dodajesz swój modyfikator Zręczności do testów ataku oraz rzutów na obrażenia. "
        "Atak zadaje obrażenia od światłości, a jego kością obrażeń jest k6. Kość ta zmienia się wraz z twoimi "
        "poziomami mnicha zgodnie z kolumną Sztuki walki w tabeli Mnicha.\n\nGdy w swojej turze wykonujesz "
        "akcję Ataku i używasz w jej ramach tego specjalnego ataku, możesz zużyć 1 punkt ki, aby w ramach "
        "akcji dodatkowej wykonać go dwukrotnie.\n\nPo zyskaniu zdolności Dodatkowy atak możesz użyć tego "
        "specjalnego ataku zamiast dowolnego ataku wykonywanego w ramach akcji Ataku."
    ),
    "h3417c2f4ga7d6g44c0g8e09gb8c2f51b93d3": (
        "Ciskasz w istotę żarzący się pocisk magicznej światłości. Dodajesz swój modyfikator Zręczności do "
        "testu ataku i rzutu na obrażenia, a pocisk zadaje obrażenia od światłości równe wynikowi rzutu twoją "
        "kością sztuk walki."
    ),
    "h0a69a08cgd46bg610cg36d9g3f28fabc55f5": (
        "Przejawiasz fizyczne talenty właściwe olbrzymom kamiennym, dzięki czemu zyskujesz następujące "
        "korzyści:\n\nPrzepastny wzrok. Zyskujesz widzenie w ciemności o zasięgu 18 m. Jeśli masz już "
        "widzenie w ciemności z innego źródła, jego zasięg zwiększa się o 18 m.\n\nRzut kamieniem. W ramach "
        "akcji dodatkowej możesz podnieść kamień i wykonać nim jeden z dwóch magicznych ataków: dystansowy "
        "atak bez broni wykorzystujący Siłę albo dystansowy atak czarem wykorzystujący twoją cechę bazową "
        "rzucania czarów. Oba mają zasięg 18 m. Przy trafieniu kamień zadaje 1k10 obrażeń od mocy, a cel musi "
        "wykonać udany rzut obronny na Siłę albo otrzymuje stan Powalenia. Możesz użyć tej akcji dodatkowej "
        "tyle razy, ile wynosi twoja premia z biegłości, a wszystkie zużyte użycia odzyskujesz po długim "
        "odpoczynku."
    ),
    "h7fd3e98dg8cddgd47cg0aeag9f03355feaaa": (
        "Dwie sztuczki. Uczysz się dwóch wybranych sztuczek z list czarów kleryka, druida albo maga. Gdy "
        "wybierasz ten atut, wybierz Inteligencję, Mądrość albo Charyzmę jako cechę bazową rzucania tych "
        "czarów.\n\nCzar 1. poziomu. Wybierz jeden czar 1. poziomu z tej samej listy co sztuczki. Zawsze masz "
        "ten czar przygotowany i zyskujesz jedną komórkę czaru 1. poziomu, którą możesz zużyć, aby go rzucić."
    ),
    "h95ef44fegf44dg26b7g490bg4d2254baeba6": (
        "Gdy podlegasz efektowi, który pozwala ci wykonać rzut obronny na Zręczność, aby otrzymać tylko "
        "połowę obrażeń, przy powodzeniu nie otrzymujesz żadnych obrażeń, a przy niepowodzeniu — tylko połowę."
    ),
    "h5f226a79g1b15g405cgf870gf64805e10151": (
        "Promień wysysającej energii wystrzeliwuje od ciebie ku jednej istocie w zasięgu. Cel wykonuje rzut "
        "obronny na Kondycję. Przy powodzeniu ma utrudnienie w następnym teście ataku wykonanym przed początkiem "
        "twojej następnej tury.\n\nPrzy niepowodzeniu przez czas trwania czaru ma utrudnienie we wszystkich "
        "testach k20 opartych na Sile i odejmuje 1k8 od wszystkich swoich rzutów na obrażenia. Na koniec każdej "
        "swojej tury cel powtarza rzut obronny, kończąc czar przy powodzeniu."
    ),
    "h6f9f97e3gf464g5501g588eg5db8ef9b538f": (
        "Przez czas trwania czaru cel ma utrudnienie we wszystkich testach k20 opartych na Sile i odejmuje "
        "1k8 od wszystkich swoich rzutów na obrażenia. Na koniec każdej swojej tury powtarza rzut obronny, "
        "kończąc czar przy powodzeniu."
    ),
    "hfd0a6b5aga1ceg3d50gd059gcb8b4baca023": (
        "W ramach akcji Magii dotykasz istoty i rzucasz tyloma kośćmi k4, ile wynosi twoja premia z "
        "biegłości. Istota odzyskuje punkty wytrzymałości w liczbie równej sumie wyników."
    ),
    "h41691e6fg7ecbgcaa8ga939gf512c0bc7016": (
        "W ramach akcji Magii dotykasz istoty i rzucasz tyloma kośćmi k4, ile wynosi twoja premia z "
        "biegłości. Istota odzyskuje punkty wytrzymałości w liczbie równej sumie wyników. Po użyciu tej "
        "zdolności musisz ukończyć długi odpoczynek, zanim użyjesz jej ponownie."
    ),
    "h05daeb7eg0489g5774g293ag23a57911c159": (
        "Jeśli nie masz właściwości Ekspert od broni palnej, nie dodajesz modyfikatora cechy do rzutów na "
        "obrażenia tą bronią."
    ),
    "h2e7b3769ge52cgfb5egdbebg36be70787259": (
        "Twoje ataki bez broni są magiczne i zyskują premię do "
        "<LSTag Tooltip=\"AttackRoll\">testów ataku</LSTag> oraz rzutów na obrażenia."
    ),
    "h173f2271g9da2gd017g9775gb5ad0a0ac5b8": (
        "W ramach akcji dodatkowej możesz podnieść kamień i wykonać nim magiczny dystansowy atak bez broni "
        "o zasięgu 18 m, wykorzystujący Siłę. Przy trafieniu kamień zadaje 1k10 obrażeń od mocy, a cel musi "
        "wykonać udany rzut obronny na Siłę (ST wynosi 8 + twoja premia z biegłości + wyższy z twoich "
        "modyfikatorów: Siły albo Zręczności) albo otrzymuje stan Powalenia."
    ),
    "h08f86230g6e53ga6e6g6abfg870e7ec18f88": (
        "Masz niewrażliwość na stan Zatrucia oraz odporność na typ obrażeń powiązany z krainą wybraną obecnie "
        "dla zdolności Czary Kręgu: ogień (jałowa), zimno (polarna), elektryczność (umiarkowana) albo trucizna "
        "(tropikalna)."
    ),
    "hb0b38705ga312g7e31g9767g722d245f3d33": (
        "Gdy twój <LSTag Type=\"Status\" Tooltip=\"RAGE\">szał</LSTag> nie jest aktywny, masz odporność na "
        "obrażenia psychiczne. Gdy szał jest aktywny, masz odporność na wszystkie typy obrażeń z wyjątkiem "
        "obrażeń od mocy i psychicznych."
    ),
    "hbf2c5134g52beg6d66g0aa1ga4e82c15a448": (
        "Masz ułatwienie w rzutach obronnych przeciwko czarom i efektom magicznym oraz odporność na obrażenia "
        "od czarów."
    ),
})

for duplicate_uid in (
    "h83187c75g7360g6a76g69b2g056444294567",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h95ef44fegf44dg26b7g490bg4d2254baeba6"]
for duplicate_uid in (
    "h204f9579g57ceg19e1g0cd5g863a58542053",
    "h58d34c7bgba94g21d5gf05ag4ed5c0aea0ab",
    "h0b14dd67gb5f5gc96dg4d31g57097dbedd01",
    "h2eb3007dg66b1g256cg24e5g51538a8f09c9",
    "h07724cb8g58c2g9aaag313cg5be5871047e1",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h5f226a79g1b15g405cgf870gf64805e10151"]
UID_OVERRIDES["h204f9579g57ceg19e1g0cd5g863a58542053"] = (
    "Promień wysysającej energii wystrzeliwuje od ciebie ku jednej istocie w zasięgu. Cel wykonuje rzut "
    "obronny na Kondycję. Przy powodzeniu ma utrudnienie w następnym teście ataku wykonanym przed początkiem "
    "twojej następnej tury."
)
UID_OVERRIDES["hafe832f4g5639gf264g68a3ge1ab2fdd021c"] = UID_OVERRIDES[
    "h05daeb7eg0489g5774g293ag23a57911c159"
]

UID_OVERRIDES.update({
    "h35551526g84e1g78f3g1277g241f3a6077bb": (
        "Raz na turę, gdy trafiasz istotę swoją bronią paktu, możesz zadać jej dodatkowe 1k6 obrażeń. Możesz "
        "też wydać jedną ze swoich kości wytrzymałości, rzucić nią i odzyskać punkty wytrzymałości w liczbie "
        "równej sumie wyniku oraz swojego modyfikatora Kondycji (co najmniej 1 punkt)."
    ),
    "hffd4abcage782g546dgaeacgc8fe055bd42e": (
        "W ramach akcji dodatkowej zyskujesz na 1 minutę moc olbrzyma. Stajesz się Duży, masz ułatwienie w "
        "testach Siły i rzutach obronnych na Siłę, a twoje ataki bronią i ataki bez broni przy trafieniu "
        "zadają dodatkowe 1k6 obrażeń."
    ),
    "h80302dc6gefa4ga829g206ag2011c0e0baca": (
        "Gdy trafiasz istotę atakiem bronią, możesz aktywować runę i przywołać płonące kajdany. Cel otrzymuje "
        "dodatkowe 2k6 obrażeń od ognia oraz stan Unieruchomienia na 1 minutę. Dopóki jest Unieruchomiony "
        "kajdanami, na początku każdej swojej tury otrzymuje 2k6 obrażeń od ognia. Na koniec każdej swojej tury "
        "cel powtarza rzut obronny, rozpraszając kajdany przy powodzeniu."
    ),
    "h0738e060g6dbdgd884ga7eag9103f532652e": (
        "Dopóki cel jest Unieruchomiony kajdanami, na początku każdej swojej tury otrzymuje 2k6 obrażeń od "
        "ognia. Na koniec każdej swojej tury powtarza rzut obronny, rozpraszając kajdany przy powodzeniu."
    ),
    "h4ee31ebcgb443g419agf6c4gb829136d660a": (
        "Uderzasz widoczną istotę w zasięgu biczem szkarłatnej energii, tworząc więź między sobą a celem. Cel "
        "musi wykonać udany rzut obronny na Kondycję albo otrzymuje 4k4 obrażeń od ognia i zostaje Uwiązany. "
        "Uwiązana istota otrzymuje 2k4 obrażeń od ognia na początku każdej swojej tury. Na koniec każdej swojej "
        "tury może powtórzyć rzut obronny, kończąc efekt przy powodzeniu."
    ),
    "h50f91c1cgccffgefd8g17f1g12dfc280157d": (
        "Wypowiadasz krótką inwokację, tworząc czarną poświatę wokół dłoni, po czym ciskasz trzema promieniami "
        "ciemności w jeden lub kilka celów w zasięgu. Możesz dowolnie rozdzielić promienie między cele. Dla "
        "każdego promienia wykonaj dystansowy atak czarem; przy trafieniu promień zadaje 1k10 obrażeń od "
        "zimna. Trafiony cel musi wykonać udany rzut obronny na Kondycję albo nie może używać reakcji do "
        "początku swojej następnej tury."
    ),
    "h9bba05a0ga2fag0a19gfc1egb6a0b1880e7a": (
        "Przez czas trwania efektu dotkniętą istotę otacza atramentowa aura. Cel ma ułatwienie w rzutach "
        "obronnych przed śmiercią. Ponadto raz na turę, gdy istota w promieniu 1,5 m od celu trafia go atakiem "
        "wręcz, napastnik otrzymuje 2k4 obrażeń nekrotycznych."
    ),
    "h5ed5413eg93c7gb24cg21d8g7901b49c4c83": (
        "Rozpoczynasz szeptaną pieśń żałobną, której magicznie wtórują wyjące duchy i inne złowieszcze znaki. "
        "Przez czas trwania efektu roztaczasz aurę w emanacji o promieniu 9 m. Gdy tworzysz aurę oraz na "
        "początku każdej swojej tury, dopóki aura trwa, możesz zmusić jedną znajdującą się w niej istotę do "
        "wykonania rzutu obronnego na Kondycję. Przy niepowodzeniu istota otrzymuje 3k8 obrażeń nekrotycznych."
    ),
    "hea3f9087gcfa4gad7eg1453gcafb3a204579": (
        "Przez czas trwania efektu możesz zmusić jedną znajdującą się w nim istotę do wykonania rzutu "
        "obronnego na Kondycję. Przy niepowodzeniu istota otrzymuje 3k8 obrażeń nekrotycznych."
    ),
    "h73861110g988dg24c3g72e2gfe79f0ecaf49": (
        "Przy nieudanym rzucie obronnym na Mądrość cel zostaje uwięziony we śnie i nie czerpie żadnych "
        "korzyści z odpoczynku. Gdy się budzi, otrzymuje 3k6 obrażeń psychicznych."
    ),
    "he100fd97g8c61g7accgc8ecg6628146a240d": (
        "Twoja nieustępliwość potrafi wyczerpać nawet najwytrzymalszych wrogów. Gdy trafiasz istotę bronią, a "
        "cel nie ma pełnych punktów wytrzymałości, broń zadaje mu dodatkowe 1k8 obrażeń. Możesz zadać te "
        "dodatkowe obrażenia tylko raz na turę."
    ),
})

for duplicate_uid in (
    "h9c70dde9ga77cgb33fgf511g497c918b7702",
    "hd20da03ag764eg50f6g5b4dga5c0e396f838",
):
    UID_OVERRIDES[duplicate_uid] = UID_OVERRIDES["h9bba05a0ga2fag0a19gfc1egb6a0b1880e7a"]
UID_OVERRIDES["hb0fea27dgc56fg62a0ge057g7c9ddc6f463e"] = (
    "Cel jest uwięziony we śnie i nie czerpie żadnych korzyści z odpoczynku. Gdy się budzi, otrzymuje 3k6 "
    "obrażeń psychicznych."
)

UID_OVERRIDES.update({
    "h1844772eg802eg78e4g4c43g59d82d32b9d4": (
        "Magia, nauka albo ich nieprzewidywalne połączenie trwale cię odmieniły. Wybierz jedno z poniższych "
        "widocznych ulepszeń ciała. O ile go nie ukryjesz, jego natura jest oczywista — mogą o tym świadczyć "
        "szwy, przeszczepione części ciał innych istot albo implanty.\n\n"
        "Naturalny pancerz. Łuski, płytki albo gruba skóra zapewniają ci KP równą 10 plus twoje modyfikatory "
        "Zręczności i Kondycji.\n\n"
        "Broń naturalna. Masz pazury, kły, rogi albo inną naturalną broń, której możesz używać do ataków bez "
        "broni. Przy trafieniu zadają one 1k6 obrażeń.\n\n"
        "Widzenie nocne. Zyskujesz widzenie w ciemności na odległość 18 m. Jeśli już je masz, jego zasięg "
        "zwiększa się o 9 m."
    ),
    "h724861ebg88f2g481bg1282g74ea90aa0663": (
        "Magia, nauka albo ich nieprzewidywalne połączenie trwale cię odmieniły. Wybierz jedno z poniższych "
        "widocznych ulepszeń ciała. O ile go nie ukryjesz, jego natura jest oczywista — mogą o tym świadczyć "
        "szwy, przeszczepione części ciał innych istot albo implanty.\n\n"
        "Naturalny pancerz. Łuski, płytki albo gruba skóra zapewniają ci KP równą 10 plus twoje modyfikatory "
        "Zręczności i Kondycji.\n\n"
        "Broń naturalna. Masz pazury, kły, rogi albo inną naturalną broń, której możesz używać do ataków bez "
        "broni. Przy trafieniu zadają one 1k6 obrażeń.\n\n"
        "Widzenie nocne. Zyskujesz widzenie w ciemności na odległość 18 m. Jeśli już je masz, jego zasięg "
        "zwiększa się o 9 m."
    ),
    "he2a10ea7ge923ge756g16a5gec995e896057": (
        "Projektujesz zbroję tak, by w walce przemieniała cię w górującego nad wrogami kolosa. Zapewnia "
        "następujące zdolności:\n\n"
        "Siłowy niszczyciel. Ze zbroi wysuwa się magiczna kula wyburzeniowa albo młot. Niszczyciel jest prostą "
        "bronią do walki wręcz z właściwością Dalekosiężna i przy trafieniu zadaje 1k10 obrażeń od mocy. Gdy "
        "trafisz nim istotę mniejszą od ciebie o co najmniej jedną kategorię rozmiaru, możesz odepchnąć ją od "
        "siebie albo przyciągnąć do siebie na odległość do 3 m.\n"
        "Olbrzymia postura. W ramach akcji dodatkowej przekształcasz i powiększasz swoją zbroję na 1 minutę."
    ),
    "h59b9ca7dgb3a7g13d9gaca8g5cb0cc11512f": (
        "Projektujesz zbroję z myślą o walce na pierwszej linii. Zapewnia następujące zdolności:\n\n"
        "Gromowy impuls. Uderzeniami zbroi możesz wyzwalać ogłuszające fale. Impuls jest prostą bronią do "
        "walki wręcz i przy trafieniu zadaje 1k8 obrażeń od dźwięku. Trafiona nim istota ma utrudnienie w "
        "testach ataku przeciwko celom innym niż ty do początku twojej następnej tury.\n"
        "Pole obronne. Gdy jesteś Zakrwawiony, możesz w ramach akcji dodatkowej zyskać tymczasowe punkty "
        "wytrzymałości w liczbie równej twojemu poziomowi Wynalazcy. Tracisz je, jeśli zdejmiesz zbroję."
    ),
    "h9d97ea6eg0369g70aag3edegb0ac7465f9b3": (
        "Dostosowujesz zbroję do bardziej dyskretnych przedsięwzięć. Zapewnia następujące zdolności:\n\n"
        "Wyrzutnia błyskawic. Na zbroi pojawia się węzeł przypominający klejnot, z którego możesz strzelać "
        "błyskawicami. Wyrzutnia jest prostą bronią dystansową i przy trafieniu zadaje 1k6 obrażeń od "
        "elektryczności. Raz w każdej swojej turze, gdy trafisz nią istotę, możesz zadać temu celowi dodatkowe "
        "1k6 obrażeń od elektryczności.\n"
        "Wzmocniony krok. Twoja szybkość zwiększa się o 1,5 m.\n"
        "Pole tłumiące. Masz ułatwienie w testach Zręczności "
        '(<LSTag Type="Skills" Tooltip="Stealth">Skradanie się</LSTag>).' 
    ),
    "hf03822e2g7af0g67edg9165g36461a798fbc": (
        "Twoja magiczna zbroja zyskuje dodatkowe korzyści zależne od modelu.\n\n"
        "Drednot. Kość obrażeń Siłowego niszczyciela zwiększa się do 2k6, a twój zasięg zwiększa się o 3 m.\n\n"
        "Strażnik. Kość obrażeń Gromowego impulsu zwiększa się do 1k10. Ponadto za każdym razem, gdy widoczna "
        "istota zbliży się na odległość 1,5 m od ciebie, możesz wykonać przeciwko niej atak okazyjny.\n\n"
        "Infiltrator. Kość obrażeń Wyrzutni błyskawic zwiększa się do 2k6. Każda istota, która otrzyma od niej "
        "obrażenia od elektryczności, zostaje Porażona."
    ),
    "h76260c1cg2fd0ga2b1gf453g7108d2706083": (
        "Zawarłeś pakt ze świadomą magiczną bronią i przeklętymi siłami uwięzionymi w jej ostrzu. Może to być "
        "miecz noszony u boku Czarownika albo osławiona broń przechowywana w odległym miejscu, która "
        "przenosi swoją moc przez wieloświat, by realizować przebiegłe plany. Tym, którzy godzą się spełniać "
        "ich kaprysy, ci nieodgadnieni patroni zapewniają moc nakładania złowrogich klątw, zadawania "
        "druzgocących ciosów i wzmacniania swoich dzierżycieli."
    ),
    "h4336900ag6e5egc73bgadb8g0a8300eeb536": (
        "Magia twojego patrona sprawia, że zawsze masz przygotowane określone czary. Gdy osiągasz poziom "
        "Czarownika wskazany w tabeli Czarów Hexblade’a, od tej pory zawsze masz przygotowane wymienione w "
        "niej czary. Na 3. poziomie są to "
        '<LSTag Type="Spell" Tooltip="Shout_ArcaneVigor">Magiczna krzepa</LSTag>, Urok, Magiczna broń, '
        "Tarcza i Gniewne ugodzenie; na 5. poziomie — Nałożenie klątwy i Przywołanie ognia zaporowego; na "
        "7. poziomie — Swoboda ruchu i Wstrząsające ugodzenie; na 9. poziomie — Uderzenie stalowego wiatru."
    ),
    "h6b8ec4b1g6350g0a0ag1d7dgc74d66ad8dd7": (
        "Na 3. poziomie zyskujesz Magiczną krzepę, Urok, Magiczną broń, Tarczę i Gniewne ugodzenie; na 5. "
        "poziomie — Nałożenie klątwy i Przywołanie ognia zaporowego; na 7. poziomie — Swobodę ruchu i "
        "Wstrząsające ugodzenie; na 9. poziomie — Uderzenie stalowego wiatru."
    ),
    "ha92a78f3ge96agd47egb8ddg6ad716d3cc56": (
        "Urok Hexblade’a. Możesz rzucić Urok bez zużywania komórki czaru tyle razy, ile wynosi twój "
        "modyfikator Charyzmy (co najmniej raz). Wszystkie zużyte użycia odzyskujesz po długim odpoczynku. "
        "Gdy rzucasz Urok, widmowa broń przypominająca twojego patrona zaczyna krążyć wokół objętego nim celu."
        "\n\nManewry Hexblade’a. Raz na turę, gdy trafisz atakiem cel objęty twoim Urokiem, możesz wywołać jeden z "
        "następujących dodatkowych efektów:\n\nWysysające cięcie, Dręczące ostrze, Hamujące piętno"
    ),
    "h83838ad6gee6dg6e8fg5d57g389e936516fb": (
        "Moc twojego patrona pozwala ci wysysać siły życiowe z przeklętych wrogów i zapewnia następujące "
        "korzyści.\n\nGłodny urok. Ilekroć objęty twoim Urokiem cel spada wskutek twoich działań do 0 punktów "
        "wytrzymałości, odzyskujesz punkty wytrzymałości w liczbie równej 1k8 plus twój modyfikator "
        "Charyzmy.\n\nNieuniknione ostrze. Raz na turę, gdy chybisz testem ataku przeciwko celowi objętemu "
        "twoim Urokiem, możesz zadać mu 1k6 obrażeń nekrotycznych."
    ),
    "hbc1ef353geeb2g5ddeg7ab9gd396c0474ea5": (
        "Możesz rzucić Urok bez zużywania komórki czaru tyle razy, ile wynosi twój modyfikator Charyzmy "
        "(co najmniej raz). Wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h95ae390fg24d7g8dcfg466dgacb161d58057": (
        "Cel wykonuje rzut obronny na Mądrość przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu, "
        "gdy przed początkiem twojej następnej tury wykona po raz pierwszy test ataku przeciwko istocie innej "
        "niż ty, otrzyma 1k6 obrażeń nekrotycznych."
    ),
    "h61d275d7g23e9gcb80g1af5g7d1bceb17545": (
        "Cel wykonuje rzut obronny na Mądrość przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu, "
        "gdy przed początkiem twojej następnej tury wykona po raz pierwszy test ataku przeciwko istocie innej "
        "niż ty, otrzyma 1k6 obrażeń nekrotycznych."
    ),
    "h7ab53afeg6536g6c48g43eagddb5bf8b087e": (
        "Ilekroć cel objęty twoim Urokiem spada do 0 punktów wytrzymałości, odzyskujesz punkty wytrzymałości "
        "w liczbie równej 1k8 plus twój modyfikator Charyzmy."
    ),
    "h06a155bfgfa73g3924g9442gc7875f6aba6d": (
        "Gdy atakujesz bronią dystansową, używasz modyfikatora Siły zarówno w teście ataku, jak i w rzucie "
        "na obrażenia. Musisz użyć tego samego modyfikatora w obu rzutach. Jeśli w tej turze pokonasz nie "
        "więcej niż połowę swojej szybkości i trafisz istotę atakiem bronią dystansową, możesz w ramach akcji "
        "dodatkowej sprawić, że atak zada dodatkowe 1k4 obrażeń tego samego typu co broń."
    ),
    "hf54abe92g0c59g3206g795cg205f29ea03b8": (
        "Trzymana przez ciebie broń zostaje nasycona mocą natury. Przez czas trwania czaru możesz używać "
        "swojej cechy bazowej zaklęć zamiast Siły w testach ataku i rzutach na obrażenia ataków wręcz tą "
        "bronią, a jej kość obrażeń zmienia się na k8. Jeśli atak zadaje obrażenia, są to obrażenia od mocy."
        "\n\nCzar kończy się wcześniej, jeśli rzucisz go ponownie albo wypuścisz broń z dłoni.\n\n"
        "Ulepszenie sztuczki. Kość obrażeń zmienia się na k10 na 5. poziomie i na k12 na 10. poziomie."
    ),
    "hf61e69c2g84a1g28cdg2869gee89659329d6": (
        "Trzymana przez ciebie maczuga albo kostur zostaje nasycony mocą natury. Przez czas trwania czaru "
        "możesz używać swojej cechy bazowej zaklęć zamiast Siły w testach ataku i rzutach na obrażenia ataków "
        "wręcz tą bronią, a jej kość obrażeń zmienia się na k8. Jeśli atak zadaje obrażenia, są to obrażenia "
        "od mocy.\n\nCzar kończy się wcześniej, jeśli rzucisz go ponownie albo wypuścisz broń z dłoni.\n\n"
        "Ulepszenie sztuczki. Kość obrażeń zmienia się na k10 na 5. poziomie i na k12 na 10. poziomie."
    ),
    "h3221afd4gbd95g5f89gf4acg938204cab057": (
        "W testach ataku i rzutach na obrażenia główną bronią do walki wręcz możesz używać modyfikatora "
        "Inteligencji zamiast Siły albo Zręczności. Broń zadaje obrażenia od mocy."
    ),
    "h8e8224d7ga1a1g482bgf5aag3bb63ab21237": (
        "W testach ataku i rzutach na obrażenia główną bronią do walki wręcz możesz używać modyfikatora "
        "Inteligencji zamiast Siły albo Zręczności. Broń zadaje obrażenia od dźwięku."
    ),
    "h112f8efbg04d4g1b62ge6d4ge233852a7ea5": (
        "W testach ataku i rzutach na obrażenia główną bronią dystansową możesz używać modyfikatora "
        "Inteligencji zamiast Zręczności. Broń zadaje obrażenia od elektryczności."
    ),
    "hae57f052gfdcbgdab2g3137g2a46d1f2494b": (
        "W ramach akcji dodatkowej możesz zwiększyć w tej turze zabójczość swoich ataków dystansowych bronią "
        "kensei. Każdy cel trafiony takim atakiem otrzymuje dodatkowe 1k4 obrażeń tego samego typu co broń. "
        "Korzyść utrzymuje się do końca bieżącej tury."
    ),
    "h05735036ge53dgb166gd088g232b4ce9dad9": (
        "W ramach akcji dodatkowej możesz zwiększyć w tej turze zabójczość swoich ataków dystansowych bronią "
        "kensei. Każdy cel trafiony takim atakiem otrzymuje dodatkowe 1k4 obrażeń tego samego typu co broń. "
        "Korzyść utrzymuje się do końca bieżącej tury."
    ),
    "h37c2f505g74b4gdbc0gdcaagf075f1ac1bdb": (
        "W ramach akcji dodatkowej możesz zwiększyć w tej turze zabójczość swoich ataków dystansowych bronią "
        "kensei. Każdy cel trafiony takim atakiem otrzymuje dodatkowe 1k4 obrażeń tego samego typu co broń. "
        "Korzyść utrzymuje się do końca bieżącej tury."
    ),
    "h9f1e6475gc9fcgf100g58dbg0d0896886dfb": (
        "Potrafisz dodatkowo wzmacniać swoją broń za pomocą ki. W ramach akcji dodatkowej możesz wydać 1 "
        "punkt ki, aby dotknięta przez ciebie broń kensei zyskała premię do testów ataku i rzutów na obrażenia. "
        "Premia utrzymuje się przez 1 minutę albo do ponownego użycia tej zdolności."
    ),
    "h01b344bfgb2ffg91fcg0c56gee5f0fb1bf6f": (
        "Potrafisz dodatkowo wzmacniać swoją broń za pomocą ki. W ramach akcji dodatkowej możesz wydać 1 "
        "punkt ki, aby dotknięta przez ciebie broń kensei zyskała premię do testów ataku i rzutów na obrażenia. "
        "Premia utrzymuje się przez 1 minutę albo do ponownego użycia tej zdolności."
    ),
    "hb071d3c2g373ag7bc8gf0d5g10bf8a344624": (
        "Potrafisz dodatkowo wzmacniać swoją broń za pomocą ki. W ramach akcji dodatkowej możesz wydać 1 "
        "punkt ki, aby dotknięta przez ciebie broń kensei zyskała premię do testów ataku i rzutów na obrażenia. "
        "Premia utrzymuje się przez 1 minutę albo do ponownego użycia tej zdolności."
    ),
    "hc89adc48gff23ge491g6563g134f3a4d1c41": (
        "Cel wykonuje rzut obronny na Kondycję przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu "
        "nie może wykonywać ataków okazyjnych, a jego szybkość zmniejsza się o połowę do początku twojej "
        "następnej tury."
    ),
    "h9a19d8f9g6000gec74g2e00g5462feeee031": (
        "Cel wykonuje rzut obronny na Kondycję przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu "
        "nie może wykonywać ataków okazyjnych, a jego szybkość zmniejsza się o połowę do początku twojej "
        "następnej tury."
    ),
})


# Full editorial rewrites for rows where a mechanically correct baseline still
# read like a literal translation. Spell names follow the shipped Polish BG3
# localization; setting terms follow its established proper names.
UID_OVERRIDES.update({
    "hd7701b33g6b2fg2417gbd20g2eb61af61f00": (
        "Magia twojego patrona sprawia, że zawsze masz przygotowane określone czary. Na wskazanych poziomach "
        "czarownika zyskujesz dodatkowe czary zgodnie z tabelą Czarów Arcyfey; od tej chwili są one dla ciebie "
        "zawsze przygotowane.\n\n"
        "Na 3. poziomie zyskujesz Wyciszenie emocji, Blask faerie, Mglisty krok, Urojoną siłę i Uśpienie. "
        "Na 5. poziomie zyskujesz Mignięcie i Rozrost roślin. Na 7. poziomie zyskujesz Dominację nad bestią "
        "oraz <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">Większą niewidzialność</LSTag>. "
        "Na 9. poziomie zyskujesz Dominację nad osobą i Pozory."
    ),
    "h2f17ec6fgaccfg9489ga33dg5178d82df62d": (
        "Gdy widoczna istota trafia atakiem inną istotę w promieniu 1,5 m od ciebie, możesz w ramach reakcji "
        "zmniejszyć obrażenia zadane celowi o 1k10 plus twoją premię z biegłości. Aby skorzystać z tej reakcji, "
        "musisz trzymać tarczę albo broń prostą lub bojową."
    ),
    "he09a0c77g31aeg7362g892bg7bdd827aa73e": (
        "Atut: Twardziel\n\n"
        "Główną formacją strzegącą prawa we Wrotach Baldura jest Płonąca Pięść — potężna gildia najemników "
        "dowodzona przez wielkiego księcia miasta. Niegdyś służyłeś w jej szeregach. Nauczyłeś się tam "
        "uprzedzać kłopoty samym groźnym spojrzeniem, a w razie potrzeby przyjmować na siebie śmiertelne "
        "ciosy. Czynni i emerytowani najemnicy Płonącej Pięści uchodzą za jednych z najtwardszych i najbardziej "
        "wytrzymałych wojowników Wybrzeża Mieczy, a ty zamierzasz podtrzymać tę reputację."
    ),
    "hfabda183g7436g881egc8e9gf6ec8a6a8cb3": (
        "Atut: Agent Sojuszu Lordów\n\n"
        "Przysiągłeś wierność jednemu z miast należących do Sojuszu Lordów. Jako agent Sojuszu musisz "
        "przestrzegać jego zasad oraz działać na rzecz bezpieczeństwa i dobrobytu Wybrzeża Mieczy. Masz "
        "przynosić honor i chwałę rodowi swego pana — czy to zabezpieczając szlaki handlowe dla kupieckiego "
        "lorda z Waterdeep, czy zgładzając potwory grasujące w górnym biegu rzeki od Daggerfordu. Wyszkolono "
        "cię w walce mieczem i sztuce rządzenia, dlatego równie sprawnie posługujesz się ostrzem, co piórem.\n\n"
        "Inspirujące uderzenie. Raz na turę, gdy zadasz istocie trafienie krytyczne, zyskujesz heroiczną "
        "inspirację.\n\n"
        "Przywrócenie honoru. Gdy widoczny wróg zada ci obrażenia, masz ułatwienie w następnym teście ataku "
        "przeciwko niemu wykonanym przed końcem swojej następnej tury."
    ),
    "h4f5ef875gef6dg93aag6e38g370f1fde0a68": (
        "Pokrzepienie sojusznika. W ramach akcji dodatkowej dodajesz otuchy jednemu widocznemu sojusznikowi "
        "w promieniu 9 m. Zyskuje on tymczasowe punkty wytrzymałości w liczbie równej 2k6 plus twoja premia "
        "z biegłości. Możesz użyć tej akcji dodatkowej tyle razy, ile wynosi twoja premia z biegłości, a "
        "wszystkie zużyte użycia odzyskujesz po długim odpoczynku.\n\n"
        "Ostatni bastion. Gdy jesteś Zakrwawiony, masz ułatwienie w testach ataku."
    ),
    "hc31d5eb8g73cdgf87bg7969geb0fc56b1687": (
        "Wstępując do Zakonu Spustoszenia, Rycerze Krwi składają przysięgę Sutekhowi. Jej przykazania "
        "zobowiązują ich do władania bezbożną magią krwi, wymuszania posłuszeństwa i siania grozy.\n\n"
        "Ich siła jest ich słabością. Biorę na cel najpotężniejszych spośród moich wrogów, ponieważ ich "
        "żywotność zapewni mi zwycięstwo.\n\n"
        "Grzech wymaga cierpienia. Sprzeciw wobec mnie jest herezją. Zanim moi wrogowie zaznają porażki, "
        "muszą zapłacić cierpieniem za swoją niewiarę.\n\n"
        "Wierność zostaje nagrodzona. Moje dary sprawiają, że sojusznicy polegają na mnie — i na rozlewie "
        "krwi, który mnie wzmacnia.\n\n"
        "Miłosierdzie jest potęgą. Niosąc pomoc sojusznikom, dowodzę ogromu swojej mocy. Ilekroć przywracam "
        "życie, przypominam im, jak łatwo mogę je odebrać."
    ),
    "h9396a6b8g3db1g53cdg44f1g9a5eb3c07ec2": (
        "Twoja reputacja sprawiła, że nawet potwory żerujące na strachu innych zaczęły bać się ciebie. Gdy "
        "trafisz istotę atakiem wykonywanym w ramach reakcji, możesz zmusić ją do rzutu obronnego na Mądrość. "
        "Przy niepowodzeniu otrzymuje stan Przerażenia do końca twojej następnej tury. ST tego rzutu wynosi 8 "
        "plus twój modyfikator Inteligencji i premia z biegłości."
    ),
    "h9ab20eb3gc598g3449gb504g354483f2972b": (
        "Gdy aktywujesz <LSTag Type=\"Status\" Tooltip=\"RAGE\">szał</LSTag> i trafisz istotę atakiem bez "
        "broni, możesz zmusić ją do rzutu obronnego na Kondycję (ST 8 plus twój modyfikator Siły i premia "
        "z biegłości). Przy niepowodzeniu istota otrzymuje stan Powalenia."
    ),
    "h5f50c057g3d01g7209ga5aeg4ccd4c74e397": (
        "Twoje ruchy nabierają takiego wdzięku, że nawet najbardziej bezduszni wrogowie żałują, iż przerwali "
        "twój taniec. Ilekroć istota trafi cię atakiem okazyjnym albo atakiem wykonanym, gdy korzystasz z "
        "akcji Uniku, otrzymuje obrażenia psychiczne w liczbie równej twojemu modyfikatorowi Charyzmy plus "
        "połowa twojego poziomu barda (zaokrąglona w dół).\n\n"
        "Ponadto zawsze masz przygotowane Zauroczenie osoby i możesz rzucać ten czar bez komponentu "
        "werbalnego. Za pomocą tej zdolności możesz rzucić go bez zużywania komórki czaru; jest wówczas "
        "rzucany jako czar 3. kręgu, a cele nie zyskują ułatwienia w rzutach obronnych z powodu walki z tobą "
        "lub twoimi sojusznikami. Gdy rzucisz czar w ten sposób, nie możesz zrobić tego ponownie aż do "
        "ukończenia długiego odpoczynku."
    ),
    "h4e44007fg48fbg0a5ag6a60g8458e847f21e": "Poziom 3: Tkanie pajęczyn",
    "hb012aa29g2700gd0c7g3c87g74a98a1affc6": (
        "Potrafisz magicznie wytwarzać z dłoni lepkie, jedwabiste pajęczyny. W ramach akcji dodatkowej możesz "
        "użyć ich na jeden z poniższych sposobów.\n\n"
        "<LSTag Type=\"Spell\" Tooltip=\"Target_ArachnoidStalker_Pull\">Pajęczyna przyciągająca</LSTag>. "
        "Traf istotę albo obiekt w zasięgu [1] lepką pajęczyną i przyciągnij cel do siebie na odległość do "
        "[1]. Przemieścić można tylko cel rozmiaru dużego lub mniejszego, a istota może oprzeć się efektowi, "
        "wykonując udany rzut obronny na Zręczność. Sojusznik zawsze zostaje przyciągnięty.\n\n"
        "<LSTag Type=\"Spell\" Tooltip=\"Target_ArachnoidStalker_WebSwing\">Huśtanie na pajęczynie</LSTag>. "
        "Wystrzel nić pajęczyny w widoczny punkt w zasięgu [1] i przyciągnij się do niego bez prowokowania "
        "ataków okazyjnych.\n\n"
        "Pajęczyna. W ramach tej samej akcji dodatkowej rzucasz czar Pajęczyna bez zużywania komórki czaru. "
        "Pajęczyny wypełniają obszar o promieniu [2] i znikają po 1 minucie. Istota, która się w nich znajdzie, "
        "musi wykonać udany rzut obronny na Zręczność albo zostaje "
        "<LSTag Type=\"Status\" Tooltip=\"WEB\">Usidlona</LSTag>. Za pomocą tej zdolności możesz rzucić ten "
        "czar dwukrotnie. Jedno zużyte użycie odzyskujesz po krótkim odpoczynku, a wszystkie po długim "
        "odpoczynku.\n\n"
        "ST rzutu obronnego wynosi 8 plus twój modyfikator Zręczności i premia z biegłości."
    ),
})

UID_OVERRIDES.update({
    "h6b384962g5a7bg33e2g8993g0708cacc7834": "Zasada: Dobywanie broni",
    "h7e686044g6737gd055gea94g27a7a4c34341": (
        "Gdy wykonujesz atak w ramach akcji Ataku, możesz dobyć używanej do niego broni. Obejmuje to "
        "wyjęcie broni z pochwy albo podniesienie jej."
    ),
    "h40481577g00cege926g9b8cg4479348271b0": (
        "Do początku twojej następnej tury testy ataku przeciwko tobie mają utrudnienie, a ty wykonujesz "
        "rzuty obronne na Zręczność z ułatwieniem."
    ),
    "h77f164a8g908ag78fdg969cg13b085d02634": (
        "Gdy twoje punkty wytrzymałości spadną do 0, tracisz przytomność i musisz wykonywać rzuty obronne "
        "przed śmiercią. Po 3 powodzeniach przestajesz się wykrwawiać i twój stan się stabilizuje. Po 3 "
        "niepowodzeniach giniesz. Jeśli na k20 wypadnie 20, odzyskujesz 1 punkt wytrzymałości.\n\n"
        "Stan ten kończy się, gdy odzyskasz dowolną liczbę punktów wytrzymałości. Jeśli sojusznik "
        "<LSTag Type=\"Spell\" Tooltip=\"Target_Help\">udzieli ci Pomocy</LSTag>, odzyskujesz 1 punkt "
        "wytrzymałości."
    ),
    "hd91b86adge685g5c21gf879g457242b186f2": (
        "Gdy masz stan Powalenia, podlegasz następującym efektom:\n\n"
        "Ograniczenie ruchu. Aby wstać i zakończyć ten stan, musisz zużyć ruch równy połowie swojej "
        "szybkości. Jeśli twoja szybkość wynosi 0, nie możesz wstać.\n\n"
        "Ataki. Test ataku przeciwko tobie ma ułatwienie, jeśli napastnik znajduje się w promieniu [1] od "
        "ciebie. W przeciwnym razie test ma utrudnienie."
    ),
    "h4d9f934eg7721gfb63gcff8gb411e659dc78": "Zasada: Jeden czar z komórki na turę",
    "hd3ffb028g9755g52adgf223g4bb289eebf93": (
        "W jednej turze możesz zużyć tylko jedną komórkę czaru. Oznacza to na przykład, że nie możesz w tej "
        "samej turze rzucić jednego czaru z komórki w ramach akcji Magii, a drugiego w ramach akcji dodatkowej."
    ),
    "hb60d9b3bg491bg7056g1bd9gc752b67bfd56": "Rąbnięcie",
    "h57100728g823cg76f4g4795g878063b680ae": (
        "Gdy trafisz istotę atakiem wręcz tą bronią, możesz wykonać nią atak wręcz przeciwko drugiej istocie, "
        "która znajduje się w promieniu [1] od pierwszego celu i w zasięgu twojej broni. Przy trafieniu druga "
        "istota otrzymuje obrażenia broni, ale nie dodajesz do nich modyfikatora cechy, chyba że jest ujemny. "
        "Ten dodatkowy atak możesz wykonać tylko raz na turę."
    ),
    "h240aa2f4g6571ge23eg8142g83ee7b985b8d": "Draśnięcie",
    "h0fbee9aag6abeg6294g3fd8gbeb26ffd19f6": (
        "Gdy chybisz istotę atakiem tą bronią, możesz zadać jej obrażenia równe modyfikatorowi cechy użytemu "
        "w teście ataku. Obrażenia są tego samego typu co obrażenia broni i można je zwiększyć wyłącznie przez "
        "zwiększenie tego modyfikatora."
    ),
    "hdbe460a9gf800gdb75g15bbg2b81a80fe8ab": "Nacięcie",
    "h84f8977cg06ecg1e31gebd6g21e4b7346121": (
        "Dodatkowy atak wynikający z właściwości Lekka możesz wykonać w ramach akcji Ataku zamiast akcji "
        "dodatkowej. Ten dodatkowy atak możesz wykonać tylko raz na turę."
    ),
    "h694f6a66g0531g98f0ga23eg525e146eb4d7": (
        "Gdy trafisz tą bronią istotę rozmiaru dużego lub mniejszego, możesz odepchnąć ją od siebie na "
        "odległość do [1]."
    ),
    "haf74199bg92cbg93dega0fbgebb535603f83": "Osłabienie",
    "h6846e460g6aecg1e76g52c0g8c751abe8744": (
        "Gdy trafisz istotę tą bronią, ma ona utrudnienie w następnym teście ataku wykonanym przed początkiem "
        "twojej następnej tury."
    ),
    "hb839de91gb995ge42eg62b9g1dd41fe4da4b": "Spowolnienie",
    "h7773a857g54d9g0e61gc338g5671eef1378d": (
        "Gdy trafisz istotę tą bronią i zadasz jej obrażenia, możesz zmniejszyć jej szybkość o [1] do początku "
        "swojej następnej tury. Jeśli istota zostanie trafiona więcej niż raz bronią z tą właściwością, łączne "
        "zmniejszenie szybkości nie może przekroczyć [1]."
    ),
    "h5af643b9gd1b7g259cg51cegf17292ec2f43": (
        "Gdy trafisz istotę tą bronią, możesz zmusić ją do rzutu obronnego na Kondycję (ST 8 plus modyfikator "
        "cechy użyty w teście ataku i twoja premia z biegłości). Przy niepowodzeniu istota otrzymuje stan "
        "Powalenia."
    ),
    "hdfca5f76g305cgff0cg0532gbc6b23ff9367": "Nękanie",
    "hf0019ff2g27f5g13abg7a86g646b2f8a1f55": (
        "Gdy trafisz istotę tą bronią i zadasz jej obrażenia, masz ułatwienie w następnym teście ataku "
        "przeciwko niej wykonanym przed końcem swojej następnej tury."
    ),
    "h3a51e8b8gf631gf9b1g55bdg6af9de9235ef": "Topór dwuręczny, halabarda",
    "hfdefde84gd74bg13d6g3599g34e7bc9cbafe": "Glewia, miecz dwuręczny",
    "h0de5940ag21a0gff32gb8dfg01c84e54f73e": "Sztylet, młot lekki, sierp, sejmitar",
    "h6fd4a879g6dd9g5936gc329gc012af72f9c6": "Maczuga, pika, młot bojowy, kusza ciężka",
    "h05a1ab8cg6b39gabd2g55c7g3a1f851c31fb": "Buława, włócznia, kiścień, miecz długi, morgensztern, nadziak",
    "h53e29765gaf78g1680g5805g24b5594244ac": "Pałka, oszczep, kusza lekka, łuk długi, muszkiet, bicz",
    "h8ab19fdega28dg1fd1g0de1gc672bac4e6d3": "Drąg, topór bojowy, młot dwuręczny, trójząb",
    "hd724f72fgcda8gb6acgb5c4gd95d169dd0b4": "Toporek, łuk krótki, rapier, miecz krótki, kusza ręczna, pistolet",
    "h8c28362ag369agee34gc8d4g6ccec5460b53": (
        "Wyszkolenie w walce pozwala ci korzystać z właściwości mistrzostwa broni.\n\n"
        "Na określonych poziomach klasy zyskujesz możliwość używania właściwości mistrzostwa kolejnych "
        "rodzajów broni."
    ),
    "ha33a602cg9bb2gec42g889dg5983a5346c84": (
        "Możesz nasycić się pierwotną mocą zwaną <LSTag Type=\"Status\" Tooltip=\"RAGE\">szałem</LSTag>, "
        "która zapewnia niezwykłą siłę i wytrzymałość. Jeśli nie nosisz ciężkiego pancerza, możesz wpaść w "
        "szał w ramach akcji dodatkowej.\n\n"
        "Możesz wpadać w szał tyle razy, ile wskazuje kolumna Szały w tabeli cech barbarzyńcy dla twojego "
        "poziomu. Jedno zużyte użycie odzyskujesz po krótkim odpoczynku, a wszystkie po długim odpoczynku."
    ),
    "h07ac58a7gdc95gd7d3g0b48g2015e769d0d0": (
        "Barbarzyńcy podążający Ścieżką Drzewa Świata łączą się poprzez swój "
        "<LSTag Type=\"Status\" Tooltip=\"RAGE\">szał</LSTag> z kosmicznym drzewem Yggdrasil. Rośnie ono "
        "wśród Sfer Zewnętrznych, łącząc je ze sobą i ze Sferą Materialną. Barbarzyńcy ci czerpią z magii "
        "drzewa żywotność i zdolność podróżowania między wymiarami."
    ),
    "he8e15200g5d16g3cfag9fd3g57eec75fb43b": (
        "Przyjmij postać kota, który potrafi przemykać niezauważony i "
        "<LSTag Type=\"Spell\" Tooltip=\"Shout_Distract_Cat_Summon\">miauczeć</LSTag>, aby odwracać uwagę "
        "przeciwników."
    ),
    "h6dea9c47g93a0g6397g3d9eg04b5e5b83704": "Poziom 10: Pancerz uroków",
    "h338cdd4dg57cdg382agd382g6e2930e3713f": "Pancerz uroków",
    "h49e72c1cg2d7bgc3fbg7e56gdbf9203830ad": (
        "Gdy otrzymujesz obrażenia od celu objętego twoim Urokiem, możesz w ramach reakcji zmniejszyć je o "
        "2k8 plus swój modyfikator Charyzmy. Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator "
        "Charyzmy, a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h16aa8ef8g9057g8804g10e3g6c754af3589d": (
        "Gdy otrzymujesz obrażenia od celu objętego twoim Urokiem, możesz w ramach reakcji zmniejszyć je o "
        "2k8 plus swój modyfikator Charyzmy. Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator "
        "Charyzmy, a wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "h99831797g4294g8465g0eb9g7df78a5c76a0": "Walka w zwarciu",
    "h313bab3cg67c1gfa03ge6f3g354db3046e48": "Przemyślana odpowiedź (wręcz)",
    "he03aadf1g28cbg5549g778fgff77ace6f7ba": "Przemyślana odpowiedź (dystansowa)",
    "h87d3e26ag5e53gdf92g801cg4e8c26aac78e": "Mag bitewny: Grzmiące ostrze",
    "ha738254bg5dbag724ag511ag8d59cf1fed09": "Mag bitewny: Ostrze zielonego płomienia",
    "h7e0866bbgdec1g07c2g7725gef3c6eb68247": "Mag bitewny: Prawdziwe uderzenie",
    "h664f7fdag1793g4256gd73cga50bae7c538a": "Mag bitewny: Mściwe ostrze",
})

UID_OVERRIDES.update({
    "he54ffab7g9288g792age85bg3fc0a39a63db": "Poziom 1: Szał",
    "h59454ac0g0de7g8defg7a22g0fd1397b1f85": (
        "Wojownicy psioniczni budzą potęgę umysłu, aby wzmocnić swoje ciało. Korzystają z mocy psionicznej, "
        "nasycając nią ciosy bronią, uderzając energią telekinetyczną i tworząc bariery z siły mentalnej."
    ),
    "h9d72f0d7g2c0egb1bbgde11g3864f11ceed2": (
        "Duszostrze atakuje umysłem, przecinając zarówno fizyczne, jak i psychiczne bariery. Łotrzykowie tej "
        "podklasy odkrywają w sobie moc psioniczną i wykorzystują ją w swoim fachu. Zdolności te mogły "
        "prześladować cię od dzieciństwa, ujawniając pełnię potencjału dopiero pod wpływem trudów życia "
        "poszukiwacza przygód. Być może zamiast tego odszukałeś zakon adeptów psioniki i przez lata uczyłeś "
        "się przejawiać swoją moc."
    ),
    "h92b0f41cg7222g57a1gf293g5f9b67f6c76a": (
        "Gdy trafisz istotę rozmiaru dużego lub mniejszego sztuczką czarownika wymagającą testu ataku, możesz "
        "odepchnąć ją od siebie na odległość do [1]."
    ),
    "h12ae9a64g3bfcg9c68gbc56g02b570979b53": "Istota została potępiona mocą Piekła.",
    "h23954313g9d62ge28ag34a3ga9b81bf374a2": (
        "Gdy trafisz istotę atakiem bronią do walki wręcz, możesz w ramach reakcji zadać jej dodatkowe [1]. "
        "Istota ma utrudnienie w następnym teście ataku wykonanym przed początkiem twojej następnej tury."
    ),
    "h72b0b6aeg9cf5g4b5fg0d9cg171c4820c0cd": (
        "Gdy istota trafi cię atakiem, ma utrudnienie we wszystkich pozostałych testach ataku przeciwko tobie "
        "w tej turze."
    ),
    "haa6b6306gc9beg2335g7d38gc8a89fd7d942": (
        "Gdy leczysz inną istotę, zyskuje ona następujący efekt: ilekroć przed końcem czaru zostaje obrana za "
        "cel ataku, napastnik odejmuje 1k4 od testu ataku."
    ),
    "hbba7650bg2c8bga26fga741g9eb4b22d5870": (
        "Twoje sztuczki zadające obrażenia działają nawet na istoty, które unikną ich najgroźniejszych skutków. "
        "Gdy rzucasz taką sztuczkę na istotę i chybiasz atakiem albo cel wykonuje udany rzut obronny, otrzymuje "
        "on połowę obrażeń sztuczki (jeśli je zadaje), lecz nie podlega żadnym jej dodatkowym efektom."
    ),
    "hf8f856a3g364eg768aga7acgb37b33220ee5": (
        "Noc nauczyła cię czujności. W ramach akcji dotknij jednej istoty — może nią być twoja postać — aby "
        "zapewnić jej premię +5 do następnego testu Inicjatywy. Korzyść natychmiast się kończy, gdy ponownie "
        "użyjesz tej zdolności."
    ),
    "hd82204a6g3799gdefdg1b5egd96a90423f8e": (
        "Noc nauczyła cię czujności. W ramach akcji dotknij jednej istoty — może nią być twoja postać — aby "
        "zapewnić jej premię +5 do następnego testu Inicjatywy. Korzyść natychmiast się kończy, gdy ponownie "
        "użyjesz tej zdolności."
    ),
    "h0221fc2dgce10g295eg2d4agd7d6c48ba873": (
        "Poza walką możesz poświęcić 1 minutę na oporządzenie swojego wierzchowca i opiekę nad nim. Następnie "
        "wierzchowiec zyskuje tymczasowe punkty wytrzymałości w liczbie równej dwukrotności twojego poziomu "
        "łotrzyka."
    ),
    "h169d7ad1g382fg6e64gd7bag6b40733be6b3": (
        "Możesz poświęcić 1 minutę na oporządzenie swojego wierzchowca i opiekę nad nim. Następnie wierzchowiec "
        "zyskuje tymczasowe punkty wytrzymałości w liczbie równej dwukrotności twojego poziomu łotrzyka."
    ),
    "hc426f330gcc3fge554g4368gf9e59e055631": (
        "Możesz poświęcić 1 minutę na oporządzenie swojego wierzchowca i opiekę nad nim. Następnie wierzchowiec "
        "zyskuje tymczasowe punkty wytrzymałości w liczbie równej dwukrotności twojego poziomu łotrzyka."
    ),
})

UID_OVERRIDES.update({
    "hb863e7fcg144ag2f29gf920g0935073a7b56": "Poziom 10: Plugawy urok",
    "h8719a67ag57begdc42g8448g9aa4c0635f13": (
        "Twój obcy patron obdarza cię potężną klątwą. Zawsze masz przygotowany Urok. Gdy rzucasz ten czar i "
        "wybierasz cechę, przez czas jego trwania cel ma utrudnienie również w rzutach obronnych na wybraną "
        "cechę."
    ),
    "h8c7613e8g0898g642cg3ecagacb04ea736f7": "Plugawy urok: Siła",
    "ha93766bcge230gbf23g5b7cgae5b74ac50c3": "Plugawy urok: Zręczność",
    "ha5080f3bg7a16gdf7cg0ad8gf7cb0751f103": "Plugawy urok: Kondycja",
    "h9d72d302gdd5dg712agaafdg2baf7f5356d6": "Plugawy urok: Inteligencja",
    "hf2ca41adg3416g331eg5d18g8165647c1fa4": "Plugawy urok: Mądrość",
    "hb09d35e6g4dd1g0784g8c7fgc7f20e0d9670": "Plugawy urok: Charyzma",
    "hb6a93cc1gf0edgea86g2a35gf0e952666978": (
        "Istota otrzymuje od czarującego dodatkowe [1]. Ma też <LSTag Tooltip=\"Disadvantage\">utrudnienie"
        "</LSTag> w <LSTag Tooltip=\"AbilityCheck\">testach</LSTag> Siły i "
        "<LSTag Tooltip=\"SavingThrow\">rzutach obronnych</LSTag> na Siłę."
    ),
    "h99a0b10fg027fga188g2137g2653a7759874": (
        "Istota otrzymuje od czarującego dodatkowe [1]. Ma też <LSTag Tooltip=\"Disadvantage\">utrudnienie"
        "</LSTag> w <LSTag Tooltip=\"AbilityCheck\">testach</LSTag> Zręczności i "
        "<LSTag Tooltip=\"SavingThrow\">rzutach obronnych</LSTag> na Zręczność."
    ),
    "ha1b537d6gb014g4e76gdd96g37cbe829c37c": (
        "Istota otrzymuje od czarującego dodatkowe [1]. Ma też <LSTag Tooltip=\"Disadvantage\">utrudnienie"
        "</LSTag> w <LSTag Tooltip=\"AbilityCheck\">testach</LSTag> Kondycji i "
        "<LSTag Tooltip=\"SavingThrow\">rzutach obronnych</LSTag> na Kondycję."
    ),
    "h85242573gb807g8f1eg76beg922d8d905e93": (
        "Istota otrzymuje od czarującego dodatkowe [1]. Ma też <LSTag Tooltip=\"Disadvantage\">utrudnienie"
        "</LSTag> w <LSTag Tooltip=\"AbilityCheck\">testach</LSTag> Inteligencji i "
        "<LSTag Tooltip=\"SavingThrow\">rzutach obronnych</LSTag> na Inteligencję."
    ),
    "h3c6667d4gfa1bgc9b9g5be0gb270c5c555d5": (
        "Istota otrzymuje od czarującego dodatkowe [1]. Ma też <LSTag Tooltip=\"Disadvantage\">utrudnienie"
        "</LSTag> w <LSTag Tooltip=\"AbilityCheck\">testach</LSTag> Mądrości i "
        "<LSTag Tooltip=\"SavingThrow\">rzutach obronnych</LSTag> na Mądrość."
    ),
    "h99239365g1e0eg35cfgc2edg0a2bbfb668ae": (
        "Istota otrzymuje od czarującego dodatkowe [1]. Ma też <LSTag Tooltip=\"Disadvantage\">utrudnienie"
        "</LSTag> w <LSTag Tooltip=\"AbilityCheck\">testach</LSTag> Charyzmy i "
        "<LSTag Tooltip=\"SavingThrow\">rzutach obronnych</LSTag> na Charyzmę."
    ),
    "h425e3ae9ge949g55bbg3aecg26401432f816": (
        "Gdy inspirujesz sojusznika za pomocą <LSTag Type=\"Spell\" Tooltip=\"Target_BardicInspiration\">"
        "Bardowskiej inspiracji</LSTag>, zyskujesz [1] w liczbie równej swojemu poziomowi barda."
    ),
    "h4b3bbd82gcfdegf0b2g8843g1b27f8c2a5b8": (
        "Gdy inspirujesz sojusznika za pomocą <LSTag Type=\"Spell\" Tooltip=\"Target_BardicInspiration\">"
        "Bardowskiej inspiracji</LSTag>, odzyskuje on również [1] w liczbie równej wynikowi rzutu twoją kością "
        "<LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">bardowskiej inspiracji</LSTag>."
    ),
    "h67022386g828fg30bag1c0cg215dae9c4f39": (
        "Nieumarłe istoty, które trafią noszącego, otrzymują [1]. Bestie, które go trafią, otrzymują "
        "<LSTag Type=\"Status\" Tooltip=\"CHARMED\">stan Zauroczenia</LSTag>."
    ),
    "he7cabbf1ge807gac91g4abcgfb35ab2c9647": "Kość wytrzymałości: k6",
    "h5ef2c7b9g9a55g39f5g3136gac436a7a1d84": "Kość wytrzymałości: k8",
    "hc0a574f2g927fg6104gda6dg115f48564c90": "Kość wytrzymałości: k10",
    "ha21b6867g8c9ag6927g327eg5540215147d3": "Kość wytrzymałości: k12",
    "h8bfb7f80g721ag09e2gdb7dg65a174f7dcc5": "Możesz wydawać kości wytrzymałości, aby odzyskiwać punkty wytrzymałości.",
    "h67791a1age70fg0b79gb82fgb57afe86a787": "Możesz wydawać kości wytrzymałości, aby odzyskiwać punkty wytrzymałości.",
    "h9d8184d6gf0c0ga54fg90cdgd24b60276c11": "Możesz wydawać kości wytrzymałości, aby odzyskiwać punkty wytrzymałości.",
    "hccd9a187g5ef0g2ac6g358dg004b907a372c": "Możesz wydawać kości wytrzymałości, aby odzyskiwać punkty wytrzymałości.",
    "hda98b41agfc26g23d3g9dafg4d09cb0cc2d8": "Użyj kości wytrzymałości",
    "h9a5993cagb688g4704g8ed3gd3d161fe6ef5": "Użyj kości wytrzymałości: k6",
    "h3e687a50gd1a3g26feg6792ged6ab0a5dc00": "Użyj kości wytrzymałości: k8",
    "h9df0d5e3gb8b4g35c0g6ef3gc428f067f2a7": "Użyj kości wytrzymałości: k10",
    "hd6b15ae8g883dgdf02gd6abg7ee0b10eb571": "Użyj kości wytrzymałości: k12",
    "h4fbdbfa6g8ef2g4e61g0c7bg465466a0df32": "Zasada: Kości wytrzymałości",
    "hfd791ef7g7534g8fdcgba6ag9741c29e31d4": (
        "Opis klasy określa rodzaj kości wytrzymałości twojej postaci (zwanych też kośćmi wytrzymałości). Na "
        "1. poziomie postać ma 1 taką kość. Możesz wydawać kości wytrzymałości, aby odzyskiwać punkty "
        "wytrzymałości."
    ),
    "hfaef3824g8845gb735gf4dfgd86da7822941": (
        "Wybierz jeden czar 1. kręgu ze szkoły wróżenia lub uroków. Zawsze masz przygotowany ten czar oraz "
        "Mglisty krok. Otrzymujesz również jedną komórkę czaru 1. kręgu i jedną komórkę 2. kręgu."
    ),
    "h9dd19073g7262gabe8g561dga56e7269712b": (
        "Wybierz jeden czar 1. kręgu ze szkoły wróżenia lub uroków. Zawsze masz przygotowany ten czar oraz "
        "Mglisty krok. Otrzymujesz również jedną komórkę czaru 1. kręgu i jedną komórkę 2. kręgu."
    ),
    "h0c8f8629gcdb5g21d2g6ba3g68301d16a9ea": (
        "Wybierz jeden czar 1. kręgu ze szkoły iluzji lub nekromancji. Zawsze masz przygotowany ten czar oraz "
        "<LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility\">Niewidzialność</LSTag>. Otrzymujesz również "
        "jedną komórkę czaru 1. kręgu i jedną komórkę 2. kręgu."
    ),
    "hbd7f0193ge427g3d75gc0adgfdba8212fb8b": (
        "Wybierz jeden czar 1. kręgu ze szkoły iluzji lub nekromancji. Zawsze masz przygotowany ten czar oraz "
        "<LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility\">Niewidzialność</LSTag>. Otrzymujesz również "
        "jedną komórkę czaru 1. kręgu i jedną komórkę 2. kręgu."
    ),
    "h3e078741g3071gaa98ga931g651f9cac58d8": "Dotknięty przez Fey",
})

BOND_SPELL_END_TEXT = (
    "Czar kończy się, gdy twoje punkty wytrzymałości spadną do 0. Kończy się również, jeśli zostanie ponownie "
    "rzucony na którąkolwiek z połączonych istot. Działa tylko wtedy, gdy ty i cel znajdujecie się nie dalej "
    "niż 18 m od siebie."
)
for duplicate_uid in (
    "hca956f6fg7446gdf7fg60bag36e7853ca0c9",
    "hd0f268c5ga792g388ag89beg27993a801b4e",
    "hddf1d80agc605gd10ageadfg364f889fcd0e",
    "hfb95ce72g8252ge83fg5316gf6e8f6c45584",
    "hacd0f311gff68ge0cegd678g80ea9a8ee794",
    "h1cf67618gcdc1g9bf0g352egd9e5052a34ad",
    "hd3e9c567g2905g672bg0224gf1c8ec229255",
    "h917f9908g4fcbge66dgb997gdac87ffc4aff",
):
    UID_OVERRIDES[duplicate_uid] = BOND_SPELL_END_TEXT

UID_OVERRIDES.update({
    "hf17390fdg279dg4294gb86ag4e1049c6b097": (
        "Lód okrywa ciebie i twoją ofiarę szronem, chroniąc cię i krępując jej ruchy. Gdy rzucasz Znak łowcy, "
        "zyskujesz tymczasowe punkty wytrzymałości w liczbie równej 1k10 plus twój poziom łowcy.\n\n"
        "Ponadto istota oznaczona twoim Znakiem łowcy nie może wykonywać akcji Odstąpienia."
    ),
    "h61ea7154gfc5cg2d12gf82ega36108b6e52c": "Poziom 3: Czary zimowego wędrowca",
    "h4d24d172g9754g69f8g404agfcebc39ded6a": (
        "Na 3. poziomie zyskujesz zdolność Czary zimowego wędrowca. Magia twojej ścieżki sprawia, że zawsze "
        "masz przygotowane określone czary. Na 3. poziomie zyskujesz Lodowy nóż, na 5. poziomie — "
        "Unieruchomienie osoby, a na 9. poziomie — Zdjęcie klątwy."
    ),
    "h225798f8g19eag252fgafe7gb82f389f37c8": "Poziom 7: Krzepiąca dusza",
    "hd373a822gfb21g38dfge5a8g77c001185e3a": "Poziom 11: Przeszywająca odpłata",
    "hcf64a967g8805ge99bg1ff7ga0cb9cd0764c": "Przeszywająca odpłata",
    "h2dc72da7geb6fg6757g65b9g28c64f77f068": "Przeszywająca odpłata",
    "h4ff1d8aeg3628g34f5gd2e0gf05e758e89f6": "Przeszywająca odpłata",
    "hb6e753d8g25f2gee18g87d6gdda8a5857b4c": (
        "Gdy istota trafi cię atakiem, możesz w ramach reakcji zmusić ją do rzutu obronnego na Mądrość "
        "przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu cel otrzymuje "
        "<LSTag Type=\"Status\" Tooltip=\"STUNNED\">stan Ogłuszenia</LSTag> na 2 tury.\n\n"
        "Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz), a "
        "wszystkie zużyte użycia odzyskujesz po długim odpoczynku."
    ),
    "hae8770acg873fg844dgedd5g825cc772d72c": (
        "Gdy istota trafi cię atakiem, możesz w ramach reakcji zmusić ją do rzutu obronnego na Mądrość "
        "przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu cel otrzymuje "
        "<LSTag Type=\"Status\" Tooltip=\"STUNNED\">stan Ogłuszenia</LSTag> do końca twojej następnej tury."
    ),
    "h7683213dgcd67g8a04g76bdg263469054d80": (
        "Gdy istota trafi cię atakiem, możesz w ramach reakcji zmusić ją do rzutu obronnego na Mądrość "
        "przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu cel otrzymuje "
        "<LSTag Type=\"Status\" Tooltip=\"STUNNED\">stan Ogłuszenia</LSTag> na 2 tury."
    ),
    "hfc2052ffgc5b0gbd9agca4bg0c13d926684c": "Przysięga Szlachetnych Dżinów",
    "h1e8b4682gc0aag5810g20f4gffc2487083b4": (
        "Paladyni związani Przysięgą Szlachetnych Dżinów oddają cześć siłom Sfer Żywiołów. Czerpią moc z "
        "czterech rodzajów dżinów: dao, władców ziemi; dżinów, władców powietrza; ifrytów, władców ognia; "
        "oraz maridów, władców wody. W Faerûnie wielu paladynów składających tę przysięgę pochodzi z "
        "Calimshanu, krainy pełnej dżinów."
    ),
    "he8fec49dgf4c3g6a97g790bg3a7f505054bf": (
        "Przepływa przez ciebie pierwotna, wiecznie zmienna moc księżyca, zapewniając następujące korzyści.\n\n"
        "Inspirujące zaćmienie. Gdy w ramach akcji dodatkowej dajesz istocie kość "
        "<LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">bardowskiej inspiracji</LSTag>, możesz "
        "otrzymać <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">stan Niewidzialności</LSTag> i w ramach tej "
        "samej akcji teleportować się na odległość do 9 m na widoczne, wolne pole. Niewidzialność trwa do "
        "początku twojej następnej tury, lecz kończy się wcześniej natychmiast po wykonaniu testu ataku, "
        "zadaniu obrażeń albo rzuceniu czaru.\n\n"
        "Księżycowa witalność. Raz na turę, gdy za pomocą czaru przywracasz istocie punkty wytrzymałości, "
        "możesz wydać kość bardowskiej inspiracji i zwiększyć liczbę przywróconych punktów o wynik rzutu tą "
        "kością. Szybkość istoty zwiększa się również o 3 m do końca jej następnej tury."
    ),
    "h4b8c5fb1g0cb0gdf42g5d1bgd60b7110c837": "Inspirujące zaćmienie",
    "ha0ddac76g013eg8574g0831g4fde2e2fef92": "Inspirujące zaćmienie",
    "h354b3d9ag3986g5438g5c7fg5f7f7196c4c4": (
        "Gdy w ramach akcji dodatkowej dajesz istocie kość "
        "<LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">bardowskiej inspiracji</LSTag>, możesz "
        "otrzymać <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">stan Niewidzialności</LSTag> i w ramach tej "
        "samej akcji teleportować się na odległość do 9 m na widoczne, wolne pole. Niewidzialność trwa do "
        "początku twojej następnej tury, lecz kończy się wcześniej natychmiast po wykonaniu testu ataku, "
        "zadaniu obrażeń albo rzuceniu czaru."
    ),
    "h976048b3gf9c6gba32g7185g9373737f96b8": (
        "Gdy w ramach akcji dodatkowej dajesz istocie kość "
        "<LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">bardowskiej inspiracji</LSTag>, możesz "
        "otrzymać <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">stan Niewidzialności</LSTag> i w ramach tej "
        "samej akcji teleportować się na odległość do 9 m na widoczne, wolne pole. Niewidzialność trwa do "
        "początku twojej następnej tury, lecz kończy się wcześniej natychmiast po wykonaniu testu ataku, "
        "zadaniu obrażeń albo rzuceniu czaru."
    ),
    "h88fd7cb1g4a94g8ad2g4bf8ga268d1168276": "Szybkość istoty zwiększa się również o 3 m.",
    "h81c2cbd1ge2a2g4781g89a2gf1b79723f601": (
        "Raz na turę, gdy za pomocą czaru przywracasz istocie punkty wytrzymałości, możesz wydać kość "
        "<LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">bardowskiej inspiracji</LSTag> i "
        "zwiększyć liczbę przywróconych punktów o wynik rzutu tą kością. Szybkość istoty zwiększa się również "
        "o 3 m do końca jej następnej tury."
    ),
    "h4ee892fdg07d1g3e46ga80bg74e493bcf181": (
        "Inspirujące uderzenie. Raz na turę, gdy zadasz istocie trafienie krytyczne, zyskujesz heroiczną "
        "inspirację.\n\n"
        "Przywrócenie honoru. Gdy widoczny wróg zada ci obrażenia, masz ułatwienie w następnym teście ataku "
        "przeciwko niemu wykonanym przed końcem swojej następnej tury."
    ),
    "hd43fb4c9g35d7g9ab6g9cc2g37fbd18e9590": (
        "Gdy zadasz istocie trafienie krytyczne, możesz wezwać ją do poddania się. Cel musi wykonać udany "
        "rzut obronny na Mądrość przeciwko ST obrony przed twoimi manewrami albo otrzymuje stan Przerażenia "
        "na 1 minutę. Na koniec każdej swojej tury może powtórzyć rzut obronny; powodzenie kończy ten stan."
    ),
    "h72f4b7bfg9dc1g5310g811agafb995e4a1c4": (
        "Raz na turę, gdy trafisz istotę atakiem bronią dystansową, możesz zmusić ją do rzutu obronnego na "
        "Siłę. Przy niepowodzeniu cel otrzymuje stan Unieruchomienia na 2 tury."
    ),
    "h8dcb95d2ga517g32ebg6912g7069289dcf67": "Głodny urok",
    "hca29dcb5g220cg55c3g2c6dgb8a635486d83": "Głodny urok",
    "h7ab53afeg6536g6c48g43eagddb5bf8b087e": (
        "Ilekroć punkty wytrzymałości celu objętego twoim Urokiem spadną do 0, odzyskujesz punkty "
        "wytrzymałości w liczbie równej 1k8 plus twój modyfikator Charyzmy."
    ),
    "hf03aeb95g5dbbg3147g324cg388502cbfe2e": (
        "Gdy otrzymujesz obrażenia od celu objętego twoim Urokiem, możesz w ramach reakcji zmniejszyć je o "
        "2k8 plus swój modyfikator Charyzmy. Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator "
        "Charyzmy, a wszystkie użycia odzyskujesz po długim odpoczynku."
    ),
    "hdd54bf99g06bfg8a6cg5904g1e14b2426411": (
        "Na początku swojej tury możesz wydać 1 punkt skupienia, aby nasycić się energią żywiołów. Energia "
        "utrzymuje się przez 10 minut. Dopóki ta cecha jest aktywna, zyskujesz następujące korzyści.\n\n"
        "Zasięg. Gdy wykonujesz atak bez broni, jego zasięg jest o [1] większy niż zwykle, ponieważ energia "
        "żywiołów rozciąga się wokół ciebie.\n\n"
        "Uderzenia żywiołów. Za każdym razem, gdy trafisz atakiem bez broni, możesz wybrać, aby zamiast "
        "zwykłego typu obrażeń zadawał obrażenia od kwasu, zimna, ognia, elektryczności albo dźwięku. Gdy "
        "zadajesz nim obrażenia jednego z tych typów, możesz również zmusić cel do wykonania rzutu obronnego "
        "na Siłę. Przy niepowodzeniu możesz przemieścić cel o maksymalnie [1] w swoją stronę albo od siebie, "
        "gdy wiruje wokół niego energia żywiołów."
    ),
    "h103f93c5g91eeg4b52g3977gd60b8e4ef8da": "Harmonia żywiołów: Kwas",
    "h1778d7a2g0b0cga6a0gcfcdg8f6f656d1e50": "Harmonia żywiołów: Zimno",
    "he11f6bc3ga347g550fg0466g52c1a9c5aad4": "Harmonia żywiołów: Zimno",
    "h5644171bg3f2cg52f1gc8dcgc1e6b38d6a9b": "Harmonia żywiołów: Ogień",
    "hb648df73g12d6gb0b3g24e3g1c88ad261547": "Harmonia żywiołów: Ogień",
    "h60fd53fcgbe77gcb48gd29dg52f09c53ad87": "Harmonia żywiołów: Elektryczność",
    "habb49dadg47e5gc5bag6c56g45bf51c0e30c": "Harmonia żywiołów: Elektryczność",
    "h459ce897gc32bgf940g855egc984bd313c7c": "Harmonia żywiołów: Dźwięk",
    "h33483b7agbd7cg35c6gf796g0a198715f127": "Harmonia żywiołów: Dźwięk",
    "h1441fb09g0c66g1899g0bf1g7aee316c859c": "Uderzenia żywiołów: Przyciągnięcie",
    "h02454f9dg7610g957dg5d40g829bab542a09": "Uderzenia żywiołów: Odepchnięcie",
    "h36e08fceg5a47gf889gc415g5a67ba284ba1": (
        "Z twoich dłoni wyzwala się fala mocy wymierzona w istotę w zasięgu. Cel wykonuje rzut obronny na "
        "Kondycję. Przy niepowodzeniu otrzymuje 2k6 obrażeń od mocy i ma stan "
        '<LSTag Type="Status" Tooltip="STUNNED">Ogłuszenia</LSTag> do końca swojej następnej tury. '
        "Przy powodzeniu otrzymuje tylko obrażenia."
    ),
    "h36a27d43gd5ebg8776g906dg475087a01734": (
        "Możesz wykorzystać mistyczną moc nocy, aby wznieść się w powietrze. Gdy znajdujesz się w półmroku "
        "albo ciemności, możesz w ramach akcji dodatkowej magicznie zyskać na 1 minutę szybkość lotu równą "
        "swojej szybkości poruszania się. Możesz użyć tej akcji dodatkowej tyle razy, ile wynosi twój "
        "modyfikator Mądrości, a wszystkie użycia odzyskujesz po długim odpoczynku."
    ),
    "hd00a3cd4g9f52gd499g2530gb2fb01ccdeba": (
        "Możesz wykorzystać mistyczną moc nocy, aby wznieść się w powietrze. Gdy znajdujesz się w półmroku "
        "albo ciemności, możesz w ramach akcji dodatkowej magicznie zyskać na 1 minutę szybkość lotu równą "
        "swojej szybkości poruszania się. Możesz użyć tej akcji dodatkowej tyle razy, ile wynosi twój "
        "modyfikator Mądrości, a wszystkie użycia odzyskujesz po długim odpoczynku."
    ),
    "hf790b35fg5b7ege376ge7e5gfdcf78fcbf35": (
        "Dodaj otuchy sojusznikowi. W ramach akcji dodatkowej dodajesz otuchy jednemu widocznemu sojusznikowi "
        "w promieniu 9 m. Sojusznik zyskuje tymczasowe punkty wytrzymałości w liczbie równej 2k6 plus twoja "
        "premia z biegłości. Możesz użyć tej akcji dodatkowej tyle razy, ile wynosi twoja premia z biegłości, "
        "a wszystkie użycia odzyskujesz po długim odpoczynku.\n\n"
        "Ostatni bastion. Gdy jesteś Zakrwawiony, masz ułatwienie w testach ataku."
    ),
    "h74764f94g16bbg3291g6bf1g64f2467c1d2d": (
        "W ramach akcji dodatkowej dodajesz otuchy jednemu widocznemu sojusznikowi w promieniu 9 m. "
        "Sojusznik zyskuje tymczasowe punkty wytrzymałości w liczbie równej 2k6 plus twoja premia z "
        "biegłości. Możesz użyć tej akcji dodatkowej tyle razy, ile wynosi twoja premia z biegłości, a "
        "wszystkie użycia odzyskujesz po długim odpoczynku."
    ),
    "h1e510414g6658gde2bgccc5g70c12902a1fb": (
        "Cel ma utrudnienie w następnym rzucie obronnym wykonanym przed początkiem twojej następnej tury."
    ),
    "hca3e32abg4341g51e2ga8f4gba89522cb18f": (
        "Cel ma utrudnienie w następnym rzucie obronnym wykonanym przed początkiem twojej następnej tury."
    ),
    "hb1f27e8cg3c25g45d2gfff0gf52a143b7438": (
        "Gdy istota zada ci obrażenia atakiem wręcz, możesz w ramach reakcji wydać 1 punkt boskości, aby "
        "wykonać przeciwko niej atak wręcz. Do rzutu na obrażenia dodajesz premię równą swojemu "
        "modyfikatorowi Mądrości."
    ),
    "hdb2b4b09g8d02ge0d3g8eeagd0b7b294e1c2": (
        "Gdy istota zada ci obrażenia atakiem wręcz, możesz w ramach reakcji wydać 1 punkt boskości, aby "
        "wykonać przeciwko niej atak wręcz. Do rzutu na obrażenia dodajesz premię równą swojemu "
        "modyfikatorowi Mądrości."
    ),
    "h7b2e4d19gc63fg41a8gb95egf2c8a3d716b0": (
        "W swojej turze może rzucić jeden z przygotowanych przez kleryka czarów, zużywając jego komórkę "
        "czaru oraz korzystając z jego ST obrony przed czarami i premii do ataku czarami."
    ),
    "h6f81c3a5g47deg4b92g8a03gd15f92c7be48": (
        "W swojej turze może rzucić jedną ze sztuczek kleryka, korzystając z jego ST obrony przed czarami "
        "i premii do ataku czarami."
    ),
    "hab5f59ebgf7a8g70bag4453g8c9195f80563": (
        "Cel zostaje odepchnięty od ciebie o [1]. Następnie możesz przemieścić się prosto w jego stronę na "
        "odległość równą maksymalnie połowie swojej szybkości, nie prowokując ataków okazyjnych."
    ),
    "h0eff4b2bgeb61g4e62ga1ffg3b4f777317e1": (
        "Szybkość celu zostaje zmniejszona o [1] do początku twojej następnej tury. Cel może być objęty tylko "
        "jednym Podcięciem ścięgna naraz — działa najnowsze."
    ),
    "hd21b5d53gc033g82abgfcdag21730bb83c68": (
        'Jeśli użyjesz Szaleńczego ataku podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag>, '
        "zadajesz dodatkowe obrażenia pierwszemu celowi trafionemu w swojej turze atakiem opartym na Sile. "
        "Aby określić dodatkowe obrażenia, rzuć tyloma k6, ile wynosi twoja premia do obrażeń "
        '<LSTag Type="Status" Tooltip="RAGE">szału</LSTag>, i zsumuj wyniki. Obrażenia są tego samego typu '
        "co obrażenia broni albo ataku bez broni użytego do wykonania ataku."
    ),
    "h0e7ef600g82aegeba0g077eg2ddad69731f8": (
        'Otacza cię dzika magia barbarzyńcy. Twoja <LSTag Tooltip="ArmourClass">Klasa Pancerza</LSTag> '
        "zwiększa się o wartość równą twojej premii do obrażeń szału, dopóki trwa twój "
        '<LSTag Type="Status" Tooltip="RAGE">szał</LSTag>.'
    ),
    "h04fd168age75cg9dadgeb9bgce0ceddefc4c": (
        "W ramach akcji dodatkowej możesz wykonać jeden atak bronią albo atak bez broni. Możesz użyć tej "
        "akcji dodatkowej tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz). Wszystkie "
        "użycia odzyskujesz po krótkim albo długim odpoczynku."
    ),
    "h8686f980g14cdg48cdg0923g21540c804c00": (
        "W ramach akcji dodatkowej możesz wykonać jeden atak bronią albo atak bez broni."
    ),
    "ha052e514g0261g1570g0745g00d44f89cc3d": (
        "Gdy ty albo istota w promieniu 9 m od ciebie chybi testem ataku, możesz zużyć jedno użycie Aktu "
        "wiary i zapewnić temu testowi premię +10, dzięki czemu atak może trafić. Jeśli w ten sposób wspierasz "
        "test ataku innej istoty, musisz użyć reakcji."
    ),
    "hc6dea6aag9290gf3cegeb8ag0351bd8d0fc5": (
        "W ramach akcji dodatkowej możesz użyć Dzikiej postaci, aby przemienić się w znaną postać bestii. "
        "Przemianę możesz zakończyć wcześniej w ramach akcji dodatkowej. Dzikiej postaci możesz użyć "
        "dwukrotnie. Jedno użycie odzyskujesz po krótkim odpoczynku, a wszystkie po długim odpoczynku. Gdy "
        "przyjmujesz Dziką postać, zyskujesz tymczasowe punkty wytrzymałości w liczbie równej swojemu "
        "poziomowi Druida. Nie możesz rzucać czarów, ale przemiana nie przerywa koncentracji ani w żaden inny "
        "sposób nie zakłóca działania wcześniej rzuconego czaru."
    ),
    "h2e1bf345gb5fcg3bbag17c4g7ac514e8455e": (
        "Gdy przyjmujesz Dziką postać, zyskujesz tymczasowe punkty wytrzymałości w liczbie równej swojemu "
        "poziomowi Druida."
    ),
    "h1cfad235g00bdg10bfgf085g60ac289d2534": (
        "Pierwotne uderzenie. Raz na turę, gdy trafisz istotę testem ataku bronią albo atakiem postaci bestii "
        "podczas Dzikiej postaci, możesz zadać celowi dodatkowo [1]."
    ),
    "h97d1904cg83d1gdb83ge2b8gfb2e45881c92": (
        "Podczas Dzikiej postaci możesz rzucać czary Kręgu Księżyca."
    ),
    "h7133dd62g2ff3g5631g286cgfb7c7edec60f": (
        "Do końca działania czaru masz odporność na obrażenia od światłości, a twoje ataki wręcz zadają "
        "przy trafieniu dodatkowo [1]."
    ),
    "hf0a594f4gbcafg3438g8e4cg19d60ca756cd": (
        "Do końca działania czaru masz odporność na obrażenia od światłości, a twoje ataki wręcz zadają "
        "przy trafieniu dodatkowo [1]."
    ),
    "h019511d5gb330g2cd9gd860g84e25789d117": (
        'Pojawia się na tobie konstelacja mądrego smoka. Gdy wykonujesz '
        '<LSTag Tooltip="SavingThrow">rzut obronny</LSTag>, aby utrzymać '
        '<LSTag Tooltip="Concentration">koncentrację</LSTag> na czarze, wynik 9 albo niższy traktujesz jak 10.'
    ),
    "h4c44c0abg262cg8e6egf06cg92cf676855e3": (
        "Możesz wydać 1 punkt skupienia, aby w ramach akcji dodatkowej wykonać zarówno akcję Odstąpienia, "
        "jak i Uniku."
    ),
    "h83374bedgf40agd759g1784gd9c5f24545a3": (
        'Możesz wydać 1 punkt skupienia, aby w ramach akcji dodatkowej wykonać zarówno akcję Odstąpienia, '
        'jak i <LSTag Type="Spell" Tooltip="Shout_Dash">Sprintu</LSTag>. Do końca tej tury odległość twojego '
        "skoku jest podwojona."
    ),
    "hfaa042d3gf744gb60fg226bgaec318afadb8": (
        "Odzyskujesz wszystkie wydane punkty skupienia. Następnie rzuć swoją kością Sztuk walki i odzyskaj "
        "punkty wytrzymałości w liczbie równej swojemu poziomowi Mnicha plus wynik rzutu.\n\nPo użyciu tej "
        "cechy nie możesz użyć jej ponownie aż do zakończenia długiego odpoczynku."
    ),
    "hadba9481g03c7gb0e4g2fc9gf098670ca5a9": (
        "Możesz przywoływać duchy zmarłych, aby wzmacniać siebie i swoich sojuszników. Gdy w ramach akcji "
        "dodatkowej dajesz istocie kość "
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>, możesz '
        "przywołać moc losowego ducha. Aby określić, którego ducha przywołujesz, rzuć kością bardowskiej "
        "inspiracji i sprawdź tabelę Duchy z zaświatów. Pozostaje on przywołany, dopóki go nie uwolnisz albo "
        "nie ukończysz długiego odpoczynku.\n\n"
        "Kontrolowane przywołanie. W ramach akcji dodatkowej możesz zużyć jedno użycie bardowskiej inspiracji "
        "i przywołać wybranego ducha. W takim przypadku wybierz ducha z tabeli Duchy z zaświatów zamiast "
        "wykonywać rzut. Numer odpowiadający wybranemu duchowi nie może być większy niż największa wartość na twojej "
        "kości bardowskiej inspiracji. Na przykład, jeśli jest nią k8, możesz wybrać dowolnego ducha aż do "
        "Cienia włącznie.\n\n"
        '<LSTag Type="Spell" Tooltip="Target_UnleashingASpirit">Uwolnienie ducha</LSTag>. W ramach akcji '
        "Magii możesz uwolnić jednego z przywołanych duchów. Wybierz na jego cel jedną widoczną istotę w "
        "promieniu 9 m od siebie. Duch wywołuje wówczas swój efekt. Jeśli wymaga on rzutu obronnego, jego ST "
        "jest równy twojemu ST obrony przed czarami Barda."
    ),
    "hb5b80dd1g369bg905ag47a7g28e7465806d8": (
        "Możesz przywoływać duchy zmarłych, aby wzmacniać siebie i swoich sojuszników. Gdy w ramach akcji "
        "dodatkowej dajesz istocie kość "
        '<LSTag Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>, możesz '
        "przywołać moc losowego ducha. Aby określić, którego ducha przywołujesz, rzuć kością bardowskiej "
        "inspiracji i sprawdź tabelę Duchy z zaświatów. Pozostaje on przywołany, dopóki go nie uwolnisz albo "
        "nie ukończysz długiego odpoczynku."
    ),
    "h0f7b9f58g4722gc431g724fgbbd26f346b33": (
        "Twoje oddanie objawia się jako sprawiedliwa moc. Dysponujesz pulą punktów boskości równą 1 plus twój "
        "modyfikator Mądrości (co najmniej 1). Wszystkie wydane punkty boskości odzyskujesz po krótkim albo "
        "długim odpoczynku.\n\nPonadto za każdym razem, gdy uświęconym ostrzem zabijesz Wynaturzenie, Bestię, "
        "Czarta albo Nieumarłego o SW 1/2 lub wyższym, odzyskujesz 1 wydany punkt boskości."
    ),
    "h5b6f609dg9e15g8c7cg33f8gbe509d75e00e": (
        "Po wykonaniu uświęconym ostrzem akcji Ataku możesz w ramach akcji dodatkowej wydać 1 punkt boskości, "
        "aby wykonać nim dodatkowy atak. Do testu ataku dodajesz premię równą swojemu modyfikatorowi Mądrości "
        "(co najmniej +1)."
    ),
    "h12a804eegfe14gb540gf10eg7e12569c4945": (
        "W ramach akcji dodatkowej możesz wydać 1 punkt boskości, aby wykonać nim dodatkowy atak. Do testu "
        "ataku dodajesz premię równą swojemu modyfikatorowi Mądrości (co najmniej +1)."
    ),
    "he8be7bbbg7ac3ge2fegb60egac3d86538826": (
        "Barbarzyńców definiuje szał, który pozwala im wyzwalać krótkie, lecz potężne fale zniszczenia. "
        "Niewielu jest dość odważnych albo nierozważnych, by zgłębiać ezoteryczne techniki psychologiczne "
        "oddzielające szał od reszty psychiki i rozszczepiające tożsamość na dwie części: ego oraz id. Gdy "
        "panuje ego, Rozszczepieni — jak nazywa się tych Barbarzyńców — wykazują opanowanie i spryt rzadko "
        "spotykane u innych przedstawicieli tej klasy. Kiedy zaś pozwalają przejąć kontrolę id, ich oblicza "
        "stają się potworne, a ciała nabrzmiewają od szału przybierającego fizyczną postać."
    ),
    "hcdd6b1c9gc361g1c98gc596g4eefab4fdf0f": (
        'Gdy twój <LSTag Type="Status" Tooltip="RAGE">szał</LSTag> nie jest aktywny, możesz w ramach akcji '
        "dodatkowej wykonać akcję Odstąpienia albo Pomocy. Podczas szału twoje testy ataku bez broni "
        "skutkują trafieniem krytycznym przy wyniku 19 albo 20 na k20."
    ),
    "h2c508ab1g6e88g9fc6g8d98gf93c24fc5e1a": (
        'Gdy podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag> trafisz istotę atakiem bez broni, '
        "możesz odepchnąć ją o 3 m."
    ),
    "h2c05bd1dg9548g9d0ag66dbgd31ce3af6dab": (
        'Gdy trafisz wroga <LSTag Tooltip="OpportunityAttack">atakiem okazyjnym</LSTag>, możesz zmniejszyć '
        "jego szybkość do 0 do końca bieżącej tury. W swojej następnej turze twoja "
        '<LSTag Tooltip="MovementSpeed">szybkość poruszania się</LSTag> zwiększa się o [1].'
    ),
    "h59454ac0g0de7g8defg7a22g0fd1397b1f85": (
        "Wojownicy psioniczni budzą moc swoich umysłów, by wzmocnić fizyczną potęgę. Wykorzystują energię "
        "psioniczną do nasycania ciosów broni, uderzania telekinetyczną siłą i tworzenia barier z energii "
        "umysłu."
    ),
    "hdb025275gf26dg03dfg7370g4dddf3f0ffb9": (
        'W ramach akcji dodatkowej, którą wykorzystujesz, aby wpaść w '
        '<LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, możesz przemieścić się na odległość równą '
        "maksymalnie połowie swojej szybkości."
    ),
    "h8a6990cbg9b40g71f3gb9cfg5c82ea25fcf2": (
        "Domena Umysłu wysławia potęgę śmiertelnego umysłu i ukierunkowuje energię psychiczną, aby chronić "
        "wiernych oraz razić wrogów. Moc tę najczęściej kojarzy się ze Ścieżką Światła albo riedrańską "
        "Ścieżką Inspiracji, lecz mogą ją opanować również wyznawcy daelkyrów. Wizje Xoriatu potrafią "
        "doprowadzić kapłana do szaleństwa, ale mogą też odsłonić śmiertelne tajemnice umysłu."
    ),
    "hf0be6fffg6e33g9c45g69bdg8f11958d0454": (
        "Ciskasz czarodziejską energią w jedną istotę albo obiekt w zasięgu. Wykonaj przeciwko celowi "
        "dystansowy test ataku czarem. Przy trafieniu cel otrzymuje obrażenia wybranego przez ciebie typu: "
        "od kwasu, zimna, ognia, elektryczności, trucizny, psychiczne albo od dźwięku.\n\nCzasem magia "
        "gwałtownie przybiera na sile i zadaje dodatkowe obrażenia. Prawdopodobieństwo takiej magicznej fali "
        "zwiększa się za każdym razem, gdy obrażenia tej sztuczki rosną na wyższych poziomach."
    ),
    "h4ed8c047g25f9g2d20g185eg45a7a0f16ff5": (
        "Ty i twoi sojusznicy macie odporność na obrażenia od kwasu, zimna, ognia, elektryczności i dźwięku, "
        "gdy znajdujecie się w twojej Aurze ochrony."
    ),
    "h9b2090d2g2df9ga6b6g06e6g8c2dc62f5763": (
        "Mają odporność na obrażenia od kwasu, zimna, ognia, elektryczności i dźwięku."
    ),
    "h2a98d2a4g6136gc14eg1cb9g3739feecfebf": (
        "Dotknięta przez ciebie istota zostaje magicznie nasycona regeneracyjnymi właściwościami krwi "
        "trolla. Podczas działania czaru cel odzyskuje 5 punktów wytrzymałości na początku każdej swojej "
        "tury, jeśli ma co najmniej 1 punkt wytrzymałości, i automatycznie odnosi powodzenie w rzutach "
        "obronnych przed śmiercią."
    ),
    "hebd09d64gbff3g6d56gd342gcb0e1169f115": (
        "Dotknięta przez ciebie istota zostaje magicznie nasycona regeneracyjnymi właściwościami krwi "
        "trolla. Podczas działania czaru cel odzyskuje 5 punktów wytrzymałości na początku każdej swojej "
        "tury, jeśli ma co najmniej 1 punkt wytrzymałości, i automatycznie odnosi powodzenie w rzutach "
        "obronnych przed śmiercią."
    ),
    "h04a42f0bg5327gaeb5gd711g78bbff1f0780": (
        "Jeśli efekt miałby zabić cię natychmiast bez rzutów obronnych przed śmiercią albo bez zadawania "
        "obrażeń zmniejszyć twoje punkty wytrzymałości bezpośrednio do 0, zamiast tego pozostają ci punkty "
        "wytrzymałości w liczbie równej twojemu poziomowi. Po użyciu tej korzyści nie możesz użyć jej "
        "ponownie aż do zakończenia długiego odpoczynku."
    ),
    "h09b18db4g2c3fg8d01g01b6g0d3e69735925": (
        "Jeśli efekt miałby zabić cię natychmiast bez rzutów obronnych przed śmiercią albo bez zadawania "
        "obrażeń zmniejszyć twoje punkty wytrzymałości bezpośrednio do 0, zamiast tego pozostają ci punkty "
        "wytrzymałości w liczbie równej twojemu poziomowi. Po użyciu tej korzyści nie możesz użyć jej "
        "ponownie aż do zakończenia długiego odpoczynku."
    ),
    "h748a060egc16cg7d82gf97eg22830dd0c9f1": (
        "Gdy rzucony przez ciebie czar z użyciem komórki czaru przywraca istocie punkty wytrzymałości, w "
        "turze rzucenia czaru odzyskuje ona dodatkowe punkty wytrzymałości w liczbie równej 2 plus poziom "
        "zużytej komórki czaru."
    ),
    "h6f58f448gfe00g1b2agab56g46c8bf14ca5f": (
        "Czary leczące, które rzucasz na innych, leczą również ciebie. Natychmiast po rzuceniu z użyciem "
        "komórki czaru, który przywraca punkty wytrzymałości co najmniej jednej istocie innej niż ty, "
        "odzyskujesz punkty wytrzymałości w liczbie równej 2 plus poziom zużytej komórki czaru."
    ),
    "h2035dcdeg7b97g47a9gcfb1gb7bc1f9c6cb9": (
        "W ramach akcji Magii możesz zużyć jedno użycie Aktu wiary, aby objawić swoją magiczną wiedzę. "
        "Wybierz jeden czar Domeny Wiedzy albo szkoły Wieszczenia. W ramach tej samej akcji rzucasz wybrany "
        "czar bez zużywania komórki czaru."
    ),
    "h59f8cb26gc1aag4dc3g0939ge1b311504647": (
        "Znasz druidzki — sekretny język Druidów. Podczas nauki tej pradawnej mowy udało ci się również "
        "odblokować magię porozumiewania się ze zwierzętami; zawsze masz przygotowany czar Rozmawianie ze "
        "zwierzętami."
    ),
    "hab240831g4170g3e19gaf78ge733be05a5f1": (
        "Zawsze masz przygotowany czar Boskie ugodzenie. Możesz go również rzucić bez zużywania komórki "
        "czaru, lecz po takim użyciu musisz ukończyć długi odpoczynek, zanim zrobisz to ponownie."
    ),
    "h8d9bb995gd364g7b4fgd6f8gb78ed0bdda9b": (
        "Możesz przywołać na pomoc nieziemskiego wierzchowca. Zawsze masz przygotowany czar Znalezienie "
        "wierzchowca.\n\nMożesz go również rzucić raz bez zużywania komórki czaru, a możliwość tę odzyskujesz "
        "po długim odpoczynku."
    ),
    "hd5715a4dge184g890agee7ag4f904fb90c6b": (
        "Poznałeś sekrety rozmaitych tradycji magicznych. Za każdym razem, gdy osiągasz poziom Barda — w tym "
        "również ten poziom — i zwiększa się wartość w kolumnie Przygotowane czary w tabeli cech Barda, "
        "możesz wybrać dowolne nowe przygotowane czary z list czarów Barda, Kleryka, Druida i Maga. Wybrane "
        "czary są dla ciebie czarami Barda (listę czarów każdej klasy znajdziesz w jej opisie). Ponadto za "
        "każdym razem, gdy zastępujesz czar przygotowany dla tej klasy, możesz zastąpić go czarem z jednej z "
        "tych list."
    ),
    "h0452adf6gbffcga716g8490gdad124c18bb6": (
        "Tryb nauki czarów jest aktywny. Wszystkie czary Kleryka zostają dodane do twojej listy czarów.\n\n"
        "Wybranie czaru do rzucenia natychmiast uczy cię go na stałe — nie potrzebujesz prawidłowego celu ani "
        "nie musisz kończyć rzucania.\n\nPo wybraniu czaru tryb się kończy."
    ),
    "he3771dbcg23f0g570dg2d5egf79cec30d589": (
        "Tryb nauki czarów jest aktywny. Wszystkie czary Druida zostają dodane do twojej listy czarów.\n\n"
        "Wybranie czaru do rzucenia natychmiast uczy cię go na stałe — nie potrzebujesz prawidłowego celu ani "
        "nie musisz kończyć rzucania.\n\nPo wybraniu czaru tryb się kończy."
    ),
    "hffa4fb6cg516eg4f17g0656geecaebcd5045": (
        "Tryb nauki czarów jest aktywny. Wszystkie czary Maga zostają dodane do twojej listy czarów.\n\n"
        "Wybranie czaru do rzucenia natychmiast uczy cię go na stałe — nie potrzebujesz prawidłowego celu ani "
        "nie musisz kończyć rzucania.\n\nPo wybraniu czaru tryb się kończy."
    ),
    "hc35093b5g5ceag870eg966fg55e93a47c7ca": (
        "Gdy wykonujesz rzut na obrażenia od ognia zadawane przez rzucony czar, możesz przerzucić każdą 1, "
        "która wypadła na kości obrażeń od ognia.\n\nZa każdym razem, gdy rzucasz czar zadający obrażenia od "
        "ognia, możesz spowić się płomieniami do końca swojej następnej tury. Dopóki płomienie są obecne, "
        "każda istota, która trafi cię atakiem wręcz, otrzymuje 1k4 obrażeń od ognia."
    ),
    "h6ac5e4a1g208fg4753g01cegcda7a5d0e025": (
        "Możesz rzucać czary ze szkoły iluzji bez komponentów werbalnych. Ponadto gdy rzucasz czar iluzji o "
        "zasięgu co najmniej 3 m, jego zasięg zwiększa się o 50%. W ramach akcji dodatkowej możesz rzucić "
        '<LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">Pomniejszą iluzję</LSTag>.'
    ),
    "h9ec6f533ga820gcfd6g8b9fgb737db30a70b": (
        "Zawsze masz przygotowane czary Przywołanie bestii i Przywołanie fey. Możesz rzucić iluzoryczną "
        "wersję każdego z nich bez zużywania komórki czaru. Gdy rzucisz w ten sposób którykolwiek z tych "
        "czarów, musisz ukończyć długi odpoczynek, zanim ponownie użyjesz go w ten sposób."
    ),
    "h18867071gc581g6029g538cg5893e7b59e95": (
        "Za każdym razem, gdy rzucasz czar, używając Materiałów alchemicznych jako Magicznego Fokusa, "
        "dodajesz premię do jednego rzutu wykonywanego w ramach tego czaru. Musi to być rzut przywracający "
        "punkty wytrzymałości albo rzut na obrażenia od kwasu, ognia lub trucizny. Premia jest równa twojemu "
        "modyfikatorowi Inteligencji (co najmniej +1)."
    ),
    "h9a4105a9gfdc3gae60g418egbcaf9bcae6b8": (
        "Możesz rzucić Mniejsze przywrócenie bez zużywania komórki czaru i bez przygotowania go, pod "
        "warunkiem że jako Magicznego Fokusa użyjesz Materiałów alchemicznych. Możesz zrobić to tyle razy, "
        "ile wynosi twój modyfikator Inteligencji (co najmniej raz), a wszystkie użycia odzyskujesz po "
        "ukończeniu długiego odpoczynku."
    ),
    "hd05b9c65g79acgf13egbf4ag94ac102d1cb3": (
        "Możesz używać swojej Tajemnej broni palnej jako Magicznego Fokusa dla czarów Wynalazcy. Gdy "
        "rzucasz przez nią czar Wynalazcy, rzuć 1k8. Do jednego rzutu na obrażenia tego czaru dodajesz "
        "premię równą uzyskanemu wynikowi."
    ),
    "h46113845g2cf8g2693g39begd296035270d7": (
        "Gdy zadajesz czarem obrażenia od zimna istocie rozmiaru dużego lub mniejszego, możesz spróbować "
        "zamrozić ją w miejscu. Jeśli to zrobisz, jej szybkość zmniejsza się o 4,5 m. Gdy zadajesz czarem "
        "obrażenia od zimna, dodajesz do nich swój modyfikator Charyzmy. Masz odporność na obrażenia od zimna."
    ),
    "h637fd45bg14ebg37d7g4fd0g0b738fa63f79": (
        "Uczysz się uderzać wrogów siłą umysłu. Gdy rzucasz czar Kleryka zadający obrażenia od światłości "
        "albo psychiczne, każdy jego cel otrzymuje dodatkowe obrażenia psychiczne równe twojemu "
        "modyfikatorowi Charyzmy."
    ),
    "h1f7e75eeg7bcfgc6fcg1e98g66c7fa6ad334": (
        "Wybierz trzy sztuczki z listy czarów dowolnej klasy. Zawsze masz je przygotowane i są dla ciebie "
        "czarami Czarownika."
    ),
    "h7388ec5cg457dg1ca4ge8c5g3185c4df0a9b": (
        "Twoja więź z boskością pozwala ci poznawać czary Kleryka. Za każdym razem, gdy osiągasz 3., 5., "
        "7. albo 9. poziom Zaklinacza, poznajesz dodatkowe czary z listy czarów Kleryka. Stają się dla "
        "ciebie czarami Zaklinacza, ale nie wliczają się do liczby znanych ci czarów Zaklinacza.\n\n"
        'Poziom 3: dwie <LSTag Tooltip="Cantrip">sztuczki</LSTag>, dwa czary 1. poziomu i dwa czary 2. '
        "poziomu.\nPoziom 5: dwa czary 3. poziomu.\nPoziom 7: dwa czary 4. poziomu.\nPoziom 9: dwa "
        "czary 5. poziomu."
    ),
    "hea8f653bga035g6444ga74bg7a2cc46f5a2b": (
        "Potrafisz tworzyć krótkotrwałe szczeliny w strukturze rzeczywistości i sięgać przez nie. Gdy "
        "rzucasz czar o zasięgu dotyku, możesz zamiast tego zwiększyć jego zasięg do 9 m. Możesz użyć tej "
        "zdolności tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz), a wszystkie użycia "
        "odzyskujesz po ukończeniu długiego odpoczynku."
    ),
    "h79149a3eg42f1g8dd3g1119g9fb383489e99": (
        "Gdy rzucasz czar Czarownika zadający obrażenia, możesz zmienić ich typ na psychiczne. Ponadto gdy "
        "rzucasz czar Czarownika ze szkoły uroków albo iluzji, możesz zrobić to bez komponentów werbalnych "
        "i somatycznych."
    ),
    "hf17390fdg279dg4294gb86ag4e1049c6b097": (
        "Lód pokrywa szronem ciebie i twoją ofiarę, chroniąc cię i krępując jej ruchy. Gdy rzucasz Znak "
        "łowcy, zyskujesz tymczasowe punkty wytrzymałości w liczbie równej 1k10 plus twój poziom Łowcy.\n\n"
        "Ponadto istota oznaczona twoim Znakiem łowcy nie może wykonywać akcji Odstąpienia."
    ),
    "ha574dfdfgf055g69c1g9889gce2fffa674e6": (
        "Czarna Strzała, która powaliła smoka Smauga, mogła być do tego przeznaczona, lecz ręka, która "
        "posłała ją z taką siłą, była niezwykle mocna. Gdy rzucasz włócznią albo napinasz łuk, dbasz o "
        "pewny chwyt i celny strzał.\n\nPodczas ataku bronią dystansową używasz modyfikatora Siły zarówno "
        "do testu ataku, jak i rzutu na obrażenia; do obu musisz użyć tego samego modyfikatora. Jeśli w tej "
        "samej turze przemieścisz się najwyżej o połowę swojej szybkości i trafisz istotę atakiem z broni "
        "dystansowej, możesz w ramach akcji dodatkowej sprawić, że atak zada dodatkowe 1k4 obrażeń typu "
        "zadawanego przez broń."
    ),
    "h1862f304g5affgfe27g9f72g632fb90f977f": (
        "Studiujesz przede wszystkim czary, które blokują, odpędzają lub chronią — usuwają szkodliwe "
        "efekty, wypędzają złowrogie wpływy i osłaniają słabszych. Magowie szkoły odpychania są poszukiwani, "
        "gdy złowrogie duchy wymagają egzorcyzmu, miejsca trzeba zabezpieczyć przed magicznym szpiegostwem, "
        "a portale do innych sfer egzystencji — zamknąć. Drużyny poszukiwaczy przygód cenią ich za ochronę "
        "przed rozmaitymi wrogimi czarami i innymi atakami."
    ),
    "h33ead399g18efg529agdf5dg0a4cac22bf2b": (
        "Zyskujesz zdolność nasycania broni lub zbroi magią. Po ukończeniu długiego odpoczynku możesz "
        "dotknąć jednego niemagicznego przedmiotu będącego zbroją albo bronią prostą lub bojową. Do końca "
        "następnego długiego odpoczynku albo do twojej śmierci przedmiot staje się magiczny i zapewnia premię "
        "+1 do KP, jeśli jest zbroją, albo premię +1 do testów ataku i rzutów na obrażenia, jeśli jest bronią.\n\n"
        "Po użyciu tej zdolności nie możesz użyć jej ponownie, dopóki nie ukończysz długiego odpoczynku."
    ),
    "hefcf1e0bge10fg7393g82e0g78428fef9233": (
        "Możesz dotknąć jednego niemagicznego przedmiotu będącego zbroją albo bronią prostą lub bojową. Do "
        "końca następnego długiego odpoczynku albo do twojej śmierci przedmiot staje się magiczny i zapewnia "
        "premię +1 do KP, jeśli jest zbroją, albo premię +1 do testów ataku i rzutów na obrażenia, jeśli "
        "jest bronią."
    ),
    "hfc73e10fg17e9g9f07gc85fg541d0d54d67b": (
        'Raz na turę, gdy chybisz atakiem przeciwko celowi, możesz na [1] tur otoczyć go '
        '<LSTag Type="Status" Tooltip="FAERIE_FIRE">Blaskiem faerie</LSTag>.'
    ),
    "h603f364eg76f2g4896gd3eeg723e7e1e85a7": (
        "Wchłonąłeś pierwotną magię, która niesie echo potęgi olbrzymów. Raz na turę, gdy trafisz cel "
        "atakiem wręcz bronią albo atakiem dystansowym bronią miotaną, możesz nasycić atak dodatkowym "
        "efektem zależnym od wybranej korzyści. Możesz użyć tego atutu tyle razy, ile wynosi twoja premia "
        "z biegłości, a wszystkie użycia odzyskujesz po ukończeniu długiego odpoczynku."
    ),
    "h928f5df7ga251g34dbg0162g20a1a67d1a84": (
        "Wchłonąłeś pierwotną magię, która niesie echo potęgi olbrzymów. Gdy wybierasz ten atut, wybierz "
        "jedną z wymienionych poniżej korzyści. Raz na turę, gdy trafisz cel atakiem wręcz bronią albo "
        "atakiem dystansowym bronią miotaną, możesz nasycić atak dodatkowym efektem zależnym od wybranej "
        "korzyści:"
    ),
    "hb8891366g1f90g73e0ge8d1ge4a2ec9f47e0": (
        "Twoja magia rodzi się z odłamków Wiecznego Serca — jądra i siły napędzającej rozrastające się "
        "pustkowia Wiecznego Lodowca. Moc ta mogła przejść na ciebie po przodkach, którzy strzegli magicznego "
        "jądra lodowca, albo zostać ci narzucona podczas przypadkowego spotkania z samym zaklętym lodem. "
        "Niezależnie od jej źródła jesteś wcieleniem zimna."
    ),
    "h3aac9e83g2f2ag85ddgcf84ge7224ea85b8b": (
        "Położenie istoty jest zawsze znane rzucającemu aż do końca czaru. Istota nie może "
        '<LSTag Type="Spell" Tooltip="Shout_Hide">ukryć się</LSTag> przed rzucającym, a jeśli ma stan '
        '<LSTag Type="Status" Tooltip="INVISIBLE">Niewidzialności</LSTag>, nie odnosi z niego żadnych '
        "korzyści wobec rzucającego."
    ),
    "hb7d8ce7cga74egd272g4ed3gebe2eec3f346": (
        "Istota objęta tą cechą zyskuje tymczasowe punkty wytrzymałości. Aby określić ich liczbę, rzuć "
        'tyloma k6, ile wynosi premia Barbarzyńcy do obrażeń od <LSTag Type="Status" Tooltip="RAGE">'
        "szału</LSTag>, i zsumuj wyniki."
    ),
    "h789e4f7cgbbfdgd136g7526g0cb392afcf9d": (
        "Za pomocą umysłu możesz poruszać przedmiotami i istotami. W ramach akcji Magii wybierz jeden "
        "widoczny cel w promieniu 9 m od siebie. Musi nim być luźny przedmiot rozmiaru dużego lub mniejszego "
        "albo chętna istota inna niż ty. Przenosisz cel na odległość do 9 m na widoczne, niezajęte miejsce. "
        "Jeśli celem jest maleńki przedmiot, możesz zamiast tego przenieść go do swojej dłoni albo z niej."
    ),
    "hbb495285gca5fg5ea5g19a8g7daed758d05f": (
        "Nikt nie może odczytać twoich myśli telepatycznie ani w inny sposób, chyba że na to pozwolisz. Masz "
        "również odporność na obrażenia psychiczne, a gdy istota zadaje ci takie obrażenia, otrzymuje taką "
        "samą ich liczbę."
    ),
    "hf28a6857g5521g1f6eg1195g302e7c01246f": (
        "Za każdym razem, gdy cel nie zda rzutu obronnego przeciwko rzuconemu przez ciebie Przeciwzaklęciu, "
        "odzyskujesz 1k4 punktów zaklinania."
    ),
    "hbc96befbg7948g8e5cgd0a9g9e23446bdc7b": (
        "Masz ułatwienie w rzutach obronnych przeciwko czarom. Ponadto gdy zadajesz obrażenia istocie "
        "utrzymującej koncentrację, ma ona utrudnienie w rzucie obronnym wykonywanym w celu jej podtrzymania."
    ),
    "he87b5a9cg9c3ag1b7fg2fefg3f7ae0ff3ef9": (
        "Gdy rzucasz ten czar z użyciem komórki czaru 4. lub wyższego poziomu, zwiększasz swoją szybkość o "
        "[1] za każdy poziom komórki powyżej 3. Czar zadaje dodatkowe [2] za każdy poziom komórki powyżej 3."
    ),
    "h5f480b91gf52bg2751g6254gdd8113ff8e2e": (
        "Gdy rzucasz ten czar, wokół chętnego celu w zasięgu pojawia się elastyczny egzoszkielet pokryty "
        "cierniami. Cel zyskuje [1] tymczasowych punktów wytrzymałości. Jeśli przed końcem czaru istota trafi "
        "cel testem ataku wręcz, otrzymuje obrażenia kłute równe liczbie tymczasowych punktów wytrzymałości "
        "utraconych wskutek tego ataku. Czar kończy się wcześniej, gdy cel nie ma już żadnych przyznanych "
        "przez niego tymczasowych punktów wytrzymałości."
    ),
    "hf4db5d55g3f59g3137gd662g4504298dce7d": (
        "Zyskuje [1] tymczasowych punktów wytrzymałości. Jeśli przed końcem czaru istota trafi cel testem "
        "ataku wręcz, otrzymuje obrażenia kłute równe liczbie tymczasowych punktów wytrzymałości utraconych "
        "wskutek tego ataku. Czar kończy się wcześniej, gdy cel nie ma już żadnych przyznanych przez niego "
        "tymczasowych punktów wytrzymałości."
    ),
    "h4b636d62g474cg4604ga98egff95e23fd181": "Czar ten został poznany dzięki atutowi Wtajemniczony w magię.",
    "hbb5691a5g5880g56bdg40c2g576cef554451": (
        'Wydaj punkty zaklinania, aby odblokować <LSTag Tooltip="SpellSlot">komórkę czaru</LSTag>. '
        "Utworzenie kolejnej komórki czaru tego samego poziomu nie przyniesie efektu, dopóki ta nie zostanie "
        "użyta."
    ),
    "hc69907d4g8c9eg708ag8797ge1e6e4d47653": (
        'Wydaj [1] punktów zaklinania, aby odblokować <LSTag Tooltip="SpellSlot">komórkę czaru</LSTag> [2]. '
        "poziomu. Utworzenie kolejnej komórki czaru tego samego poziomu nie przyniesie efektu, dopóki ta nie "
        "zostanie użyta."
    ),
    "h112c7e0eg78abgd915gaaeag4b58bbd6c408": (
        'Gdy korzystasz z tej akcji, nie podlegasz ograniczeniu <LSTag Type="Status" '
        'Tooltip="ONE_SPELL_WITH_A_SPELL_SLOT_PER_TURN">Jeden czar z komórką czaru na turę</LSTag>.'
    ),
    "h9adf7805gb424g309ag6e71g53eca41cd8d5": (
        'Możesz zmienić swoją sztuczkę, wybierając inną z poniższej listy czarów Maga. Sztuczka ta nie '
        'zużywa <LSTag Tooltip="SpellSlot">komórek czarów</LSTag> i możesz rzucać ją do woli.'
    ),
    "h38834643g8993gebb9g329bg7091b7ffff24": (
        "Gdy rzucasz Rękę maga, możesz zrobić to w ramach akcji dodatkowej i uczynić widmową dłoń "
        'Niewidzialną. Może ona również próbować okradać kieszenie, wykonując test Zręczności '
        '(<LSTag Type="Skills" Tooltip="SleightOfHand">Zwinne dłonie</LSTag>) z użyciem twojego '
        "modyfikatora do tego testu."
    ),
    "h58d3ea5cg20f9gc47cg638cg148f2229c69f": "Rzuć czar na istotę wychodzącą poza zasięg.",
    "h35af86fcg2186gfbc2g672fgcbee62e25113": (
        "Jeśli masz dość miejsca, w ramach akcji dodatkowej możesz zmienić swój rozmiar na duży. Przemiana "
        "trwa 10 minut albo do chwili, gdy ją zakończysz (bez akcji). W tym czasie masz ułatwienie w testach "
        "Siły, a twoja szybkość zwiększa się o 3 m. Po użyciu tej cechy nie możesz użyć jej ponownie, dopóki "
        "nie ukończysz długiego odpoczynku."
    ),
    "hc2d61264g8816g804bg2a62g2c5d7e343f46": (
        "W ramach akcji dodatkowej możesz magicznie teleportować się na odległość do 9 m na widoczne, "
        "niezajęte miejsce."
    ),
    "hbe719ba9g332bgafefgf142g2c86ce3fd743": (
        "Cel musi wykonać rzut obronny na Mądrość. Przy niepowodzeniu otrzymuje stan Przerażenia na 1 "
        "minutę.\n\nPrzerażony cel powtarza rzut obronny na końcu każdej swojej tury. Przy powodzeniu "
        "efekt się kończy."
    ),
    "h3af4f15fgffa3gf824ga850g5f3edec1f758": (
        "Łącząc ekstrakty, możesz sporządzić dwa roztwory alchemiczne zamiast jednego, jeśli odniesiesz "
        'powodzenie w <LSTag Tooltip="AbilityCheck">teście</LSTag> <LSTag Type="Skills" '
        'Tooltip="Medicine">Medycyny</LSTag> o <LSTag Tooltip="DifficultyClass">ST</LSTag> 15.'
    ),
})

UID_OVERRIDES["h12940965g725dg2c79gd30cg6b45c140c9be"] = UID_OVERRIDES[
    "h748a060egc16cg7d82gf97eg22830dd0c9f1"
]

ABILITY_DRAIN_TEXT = (
    "Istota odejmuje 1k6 od swoich testów ataku i cech oraz od rzutów obronnych na Kondycję wykonywanych "
    "w celu podtrzymania koncentracji. Na końcu każdej swojej tury wykonuje rzut obronny na Inteligencję; "
    "przy powodzeniu efekt się kończy."
)
for duplicate_uid in (
    "h9e56e88cg0481g2c87g52e7g140df577385c",
    "hd6166cf1gbef5ga79eg976cg003cafe77c08",
):
    UID_OVERRIDES[duplicate_uid] = ABILITY_DRAIN_TEXT

MULTIPLE_SLOTTED_SPELLS_TEXT = (
    "W swojej turze możesz rzucić więcej niż jeden czar zużywający komórkę czaru. Po skorzystaniu z tej "
    "korzyści nie możesz zrobić tego ponownie, dopóki nie ukończysz długiego odpoczynku."
)
for duplicate_uid in (
    "hf825d6a4g01fbg9069gd8b6gd7c305318fc8",
    "h46ad0c90g0874gdcd5g9dbdg6328d1abaf2f",
):
    UID_OVERRIDES[duplicate_uid] = MULTIPLE_SLOTTED_SPELLS_TEXT

SHADOW_RESTRAINT_TEXT = (
    "Możesz użyć Aktu wiary, aby zwrócić przeciwko istocie jej własny cień. W ramach akcji wybierz jedną "
    "widoczną istotę w promieniu 9 m od siebie. Jej cień unieruchamia ją do końca twojej następnej tury. "
    "Możesz użyć tej zdolności nawet wtedy, gdy cel znajduje się w miejscu, w którym nie rzuca cienia."
)
for duplicate_uid in (
    "hbcbd58e8g49cfg974bg8aabgdc71760d819a",
    "h7630efebgc128g1a88g3056g3cd8dbd6ce14",
):
    UID_OVERRIDES[duplicate_uid] = SHADOW_RESTRAINT_TEXT

PROTECTIVE_SPELL_TEXT = (
    "Dotykasz przyjaznej istoty. Gdy otrzyma obrażenia przed końcem czaru, zmniejsza łączną wartość tych "
    "obrażeń o 1k4. Istota może skorzystać z tego czaru tylko raz na turę."
)
for duplicate_uid in (
    "hd537bc94g933ag4203ga905g390b91aed106",
    "hb291dd01gaa36gf848g9cb2g11776f6a95ba",
    "h9d6a4e32g87edg4607g6cd5g19197e4e0034",
    "h1e40a51eg6772g87d3ga8a6gd8b5dcc5e0f0",
):
    UID_OVERRIDES[duplicate_uid] = PROTECTIVE_SPELL_TEXT

SPIKE_GROWTH_FEATURE_TEXT = (
    "Zawsze masz przygotowany czar Wzrost kolców. Możesz rzucić go raz bez zużywania komórki czaru, a "
    "możliwość tę odzyskujesz po krótkim odpoczynku. Czar rzucony w ten sposób nie wymaga koncentracji."
)
for duplicate_uid in (
    "h99dd2a82gb360g8747g2eafg30d4b056f72d",
    "hd23656cfg57f8g9378gb515g69eaf09ae893",
):
    UID_OVERRIDES[duplicate_uid] = SPIKE_GROWTH_FEATURE_TEXT

WILD_MAGIC_SURGE_TEXT = (
    "Rzucane przez ciebie czary mogą wyzwalać przypływy nieposkromionej magii. Raz na turę, natychmiast po "
    "rzuceniu czaru z użyciem komórki czaru, możesz rzucić 1k20. Jeśli wypadnie 20, wykonaj rzut w tabeli "
    "Przypływ dzikiej magii, aby wywołać magiczny efekt."
)
for duplicate_uid in (
    "h81877b18gdacfg553cge0c9g65813ccf4557",
    "hb1afe5dagdd44g9fb0ga44bgfc95f9dd8e59",
):
    UID_OVERRIDES[duplicate_uid] = WILD_MAGIC_SURGE_TEXT

RADIANT_PENETRATION_TEXT = (
    'Rzucane przez ciebie czary i wykonywane ataki ignorują <LSTag Tooltip="Resistant">odporność</LSTag> '
    "na obrażenia od światłości. Ponadto, gdy zadajesz czarem obrażenia od światłości, w rzucie nie może "
    "wypaść 1."
)
for duplicate_uid in (
    "h94e22d9cg05ceg0802gc712g372cd3b8f030",
    "hf7ce49baga00eg630eg2b32g38d71accc648",
):
    UID_OVERRIDES[duplicate_uid] = RADIANT_PENETRATION_TEXT

DAMAGE_DICE_ADVANTAGE_TEXT = (
    "Do końca swojej następnej tury podczas rzucania czaru zadającego obrażenia rzucasz każdą kością "
    "obrażeń dwukrotnie i wykorzystujesz wyższy wynik."
)
for duplicate_uid in (
    "hd2a63fa4g8bc3g40d0gadafgbe4c69f9832c",
    "h5cb55472gb6b7g47b1g89e1g030b53720520",
    "hb2ec585cg90ddg450ag98dagbeb32d75fa7d",
    "ha4eee424g6b14g40beg8738g0cec17ad0409",
    "h81455b0dge9d7gec74g4a50gc7fa88afc73e",
):
    UID_OVERRIDES[duplicate_uid] = DAMAGE_DICE_ADVANTAGE_TEXT

INVISIBILITY_BREAK_TEXT = (
    'Przez 1 minutę masz stan <LSTag Type="Status" Tooltip="INVISIBLE">Niewidzialności</LSTag>. '
    "Niewidzialność kończy się natychmiast po wykonaniu przez ciebie testu ataku, zadaniu obrażeń albo "
    "rzuceniu czaru."
)
for duplicate_uid in (
    "hb3d1182cg5d54g444cgb977g26e77a6a099e",
    "h3f87293dg3247g4d73gb758gf7485044db3c",
    "hb4ffbe2cg154fg4614ga481g770425e23306",
    "h8382539fg0076g44d2gb673g042eb6831f24",
):
    UID_OVERRIDES[duplicate_uid] = INVISIBILITY_BREAK_TEXT

SEEKING_SPELL_TEXT = (
    "Jeśli wykonasz test ataku czarem i chybisz, możesz wydać 1 punkt zaklinania, aby ponownie rzucić k20; "
    "musisz wykorzystać nowy wynik.\n\nMożesz użyć Naprowadzanego czaru nawet wtedy, gdy podczas rzucania "
    "tego czaru użyłeś już innej opcji metamagii."
)
for duplicate_uid in (
    "h4350095ege773ga624g7919g62f04bb30b95",
    "h28f9a741ga446ga31eg8889g3b0e1ddcb286",
):
    UID_OVERRIDES[duplicate_uid] = SEEKING_SPELL_TEXT

MUSICIAN_FEATURE_TEXT = (
    "Szkolenie muzyczne. Zyskujesz biegłość w posługiwaniu się trzema instrumentami muzycznymi.\n\n"
    "Zachęcająca pieśń. Po ukończeniu krótkiego albo długiego odpoczynku możesz zagrać pieśń na "
    "instrumencie, którym biegle się posługujesz, i obdarzyć heroiczną inspiracją sojuszników, którzy ją "
    "usłyszą. Możesz w ten sposób wpłynąć na liczbę sojuszników równą twojej premii z biegłości."
)
for duplicate_uid in (
    "h658ed514ge9dcg9a0fg207fg2dacf4e5e1ad",
    "hbc4803a8gd847gc698gdcb8g8e6853f62ff5",
):
    UID_OVERRIDES[duplicate_uid] = MUSICIAN_FEATURE_TEXT

BARDIC_INSPIRATION_TEXT = (
    "Potrafisz w nadprzyrodzony sposób inspirować innych słowami, muzyką albo tańcem. Inspirację tę "
    "reprezentuje kość bardowskiej inspiracji, która początkowo jest k6.\n\n"
    "Korzystanie z bardowskiej inspiracji. W ramach akcji dodatkowej możesz zainspirować inną istotę w "
    "promieniu 18 m, która cię widzi albo słyszy. Otrzymuje ona jedną z twoich kości bardowskiej inspiracji. "
    "Istota może mieć tylko jedną taką kość naraz.\n\n"
    "Raz w ciągu następnej godziny, gdy istota nie zda testu k20, może rzucić kością bardowskiej inspiracji "
    "i dodać wynik do rzutu k20, co może zmienić niepowodzenie w powodzenie. Kość zostaje zużyta po wykonaniu "
    "rzutu.\n\n"
    "Liczba użyć. Możesz obdarzyć istotę kością bardowskiej inspiracji tyle razy, ile wynosi twój modyfikator "
    "Charyzmy (co najmniej raz). Wszystkie użycia odzyskujesz po ukończeniu długiego odpoczynku.\n\n"
    "Na wyższych poziomach. Kość bardowskiej inspiracji zmienia się po osiągnięciu określonych poziomów "
    "Barda, zgodnie z kolumną Kość bardowskiej inspiracji w tabeli cech Barda: na 5. poziomie staje się k8, "
    "na 10. poziomie — k10, a na 15. poziomie — k12."
)
for duplicate_uid in (
    "hb5220d58g095fg5ae1g7115g72d15a96ef0c",
    "h2810e8cag53f2gddb2gb1bbg7d5f6848ec0b",
):
    UID_OVERRIDES[duplicate_uid] = BARDIC_INSPIRATION_TEXT

PSIONIC_FLIGHT_TEXT = (
    "W ramach akcji dodatkowej możesz przelecieć na wybrane miejsce, zużywając tylko 3 m ruchu. Po użyciu "
    "tej akcji dodatkowej nie możesz zrobić tego ponownie, dopóki nie ukończysz krótkiego albo długiego "
    "odpoczynku, chyba że zużyjesz kość energii psionicznej, aby odnowić jej użycie (bez akcji)."
)
for duplicate_uid in (
    "h53a46d69g6181g8c48g7c48g569803d1df00",
    "ha42816f3g2b46g7a69gebb9g476dfa5e4f31",
):
    UID_OVERRIDES[duplicate_uid] = PSIONIC_FLIGHT_TEXT

ADRENALINE_RUSH_FULL_TEXT = (
    'W ramach akcji dodatkowej możesz wykonać akcję <LSTag Type="Spell" Tooltip="Shout_Dash">Sprintu'
    "</LSTag>. Gdy to robisz, zyskujesz tymczasowe punkty wytrzymałości w liczbie równej swojej premii z "
    "biegłości.\n\nMożesz użyć tej cechy tyle razy, ile wynosi twoja premia z biegłości, a wszystkie użycia "
    "odzyskujesz po ukończeniu krótkiego albo długiego odpoczynku."
)
UID_OVERRIDES["h8306332bg4a42gfdaag8e32g05d5b2d0a005"] = ADRENALINE_RUSH_FULL_TEXT
UID_OVERRIDES["he98b170fg0b2bg4502g8a0fg3f8f765d62aa"] = ADRENALINE_RUSH_FULL_TEXT.split("\n\n", 1)[0]

UID_OVERRIDES["h0d82190dg72f2gae71g7ce4g614bca53783f"] = (
    'Otrzymujesz premię do <LSTag Tooltip="SpellDifficultyClass">ST rzutów przeciwko swoim czarom</LSTag> '
    'oraz <LSTag Tooltip="AttackRoll">testów ataku</LSTag> czarami.'
)
SPELLCASTING_WEAPON_BONUS_TEXT = (
    'Ta broń zapewnia premię +[1] do testów ataku, rzutów obrażeń, '
    '<LSTag Tooltip="SpellDifficultyClass">ST rzutów przeciwko swoim czarom</LSTag> oraz '
    '<LSTag Tooltip="AttackRoll">testów ataku</LSTag> czarami.'
)
for duplicate_uid in (
    "h5fe7400ag82f7g6073g3bcbgd343cec9bd16",
    "h99e76e2eg9ad8ge1c9g7478g77f49aa7113e",
):
    UID_OVERRIDES[duplicate_uid] = SPELLCASTING_WEAPON_BONUS_TEXT

UID_OVERRIDES["hb0fdd4d9g503ege786g4e88g495448e216a3"] = (
    'Jeśli posiadacz zda test <LSTag Type="Skills" Tooltip="Medicine">Medycyny</LSTag> o ST 15, '
    'może wytworzyć dwa ekstrakty alchemiczne.'
)

EXACT_OVERRIDES[
    "As a Bonus Action, you give yourself Advantage on your next attack roll on the current turn. You can use this "
    "feature only if you haven’t moved during this turn, and after you use it, your Speed is 0 until the end of the "
    "current turn."
] = (
    "W ramach akcji dodatkowej zapewniasz sobie Ułatwienie w następnym teście ataku w tej turze. "
    "Możesz skorzystać z tej cechy tylko wtedy, gdy nie poruszałeś się w tej turze. Po jej użyciu twoja "
    "Szybkość wynosi 0 do końca bieżącej tury."
)

EXACT_OVERRIDES[
    "Orcs trace their creation to Gruumsh, a powerful god who roamed the wide open spaces of the Material Plane. "
    "Gruumsh equipped his children with gifts to help them wander great plains, vast caverns, and churning seas and "
    "to face the monsters that lurk there. Even when they turn their devotion to other gods, orcs retain Gruumsh’s "
    "gifts: endurance, determination, and the ability to see in darkness."
] = (
    "Orkowie wywodzą swe pochodzenie od Gruumsha, potężnego boga, który przemierzał rozległe przestrzenie Sfery "
    "Materialnej. Gruumsh obdarzył swoje dzieci darami pozwalającymi im wędrować po wielkich równinach, rozległych "
    "jaskiniach i wzburzonych morzach oraz stawiać czoła czającym się tam potworom. Nawet jeśli zaczynają czcić "
    "innych bogów, orkowie zachowują dary Gruumsha: wytrzymałość, determinację i zdolność widzenia w ciemności."
)

UID_OVERRIDES["h62e16743gcb72g9068gb2d0gb1a62ea9d321"] = (
    "Nauczyłeś się czerpać moc ze Sfery Cieni, dzięki czemu zyskujesz następujące korzyści.\n\n"
    "Ciemność. Możesz wydać 1 punkt skupienia, aby rzucić czar Ciemność bez komponentów. Gdy rzucasz go za pomocą "
    "tej cechy, widzisz w jego obszarze. Dopóki czar trwa, na początku każdej swojej tury możesz przenieść obszar "
    "Ciemności na wybrane pole w promieniu [1] od siebie.\n"
    "Widzenie w ciemności. Zyskujesz Widzenie w ciemności o zasięgu [1]. Jeśli już je masz, jego zasięg zwiększa "
    "się o 18 m.\n\n"
    "Cieniste mamidła. Znasz "
    '<LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">Pomniejszą iluzję</LSTag>. Mądrość jest twoją '
    "cechą bazową do tego czaru."
)
UID_OVERRIDES["hae8c9a5cgf06dg6b71gb093ge2e25716f7d2"] = (
    "Twoja wrodzona magia wywodzi się z najbardziej mglistych i nieprzeniknionych mocy Sfery Cieni albo z innych "
    "krain nadprzyrodzonego mroku. Być może pochodzisz od istoty z takiego miejsca albo przemieniła cię złowroga "
    "energia smoka cienia, z którą zetknąłeś się w przeszłości. Twoja mroczna magia pozwala ci władać ciemnością, "
    "nieumarłością i niedolą."
)

HEALING_LIGHT_TEXT = (
    "Zyskujesz zdolność kierowania niebiańską energią, aby leczyć rany. Dysponujesz pulą kości k6, które zasilają "
    "to leczenie. Liczba kości w puli wynosi 1 plus twój poziom czarownika.\n\n"
    "W ramach akcji dodatkowej możesz uleczyć siebie albo jedną istotę, którą widzisz w promieniu 18 m od siebie, "
    "zużywając kości z puli. Maksymalna liczba kości, które możesz zużyć naraz, jest równa twojemu modyfikatorowi "
    "Charyzmy (co najmniej jedna kość). Rzuć zużytymi kośćmi i przywróć punkty wytrzymałości w liczbie równej sumie "
    "wyników. Wszystkie zużyte kości wracają do puli po ukończeniu długiego odpoczynku."
)
for duplicate_uid in (
    "hdaeea362gfb80g3de3gfc7bgaaff6ca3e93f",
    "h13ee529eg2e3ag6b49ge487g5564265ef86c",
):
    UID_OVERRIDES[duplicate_uid] = HEALING_LIGHT_TEXT

CHARGER_TEXT = (
    "Ulepszony sprint. Gdy wykonujesz akcję Sprintu, twoja Szybkość wzrasta o 3 m na czas tej akcji.\n\n"
    "Atak szarżą. Jeśli bezpośrednio przed trafieniem celu atakiem wręcz wykonywanym w ramach akcji Ataku "
    "przemieścisz się co najmniej 3 m w linii prostej w jego stronę, wybierz jeden z następujących efektów: dodaj "
    "1k8 do rzutu obrażeń tego ataku albo odepchnij cel na maksymalnie 3 m, jeśli jest nie więcej niż o jeden "
    "rozmiar większy od ciebie. Z tej korzyści możesz skorzystać tylko raz na turę."
)
UID_OVERRIDES["h9ed109c6ga680g6d73gce1ag6e136e676cb2"] = CHARGER_TEXT
UID_OVERRIDES["h4e972de5g72bbgc7d9gfda3g1c89f2af41d0"] = CHARGER_TEXT.replace(
    "Ulepszony sprint", 'Ulepszony <LSTag Type="Spell" Tooltip="Shout_Dash">Sprint</LSTag>', 1
)

UID_OVERRIDES["hdbb54662gd707gd172gbdfdgd57e57e3b819"] = (
    "W każdej swojej turze rumak może wykonać jedną z następujących akcji: Sprint, Odstąpienie, Unik albo Atak."
)
UID_OVERRIDES["h06128f4dg8b4fg7ee1gbb06gbcef6e2bdfac"] = (
    "W ramach akcji Ataku wykonaj jeden atak wręcz. Jeśli trafisz, możesz w ramach akcji dodatkowej wykonać akcję "
    '<LSTag Type="Spell" Tooltip="Shout_Dash">Sprintu</LSTag>. Ruch uzyskany dzięki temu Sprintowi nie prowokuje '
    "ataków okazyjnych."
)
UID_OVERRIDES["h2ff7efe3g2f98g2386g3e31g16cac67905a4"] = (
    "W ramach akcji dodatkowej możesz wykonać akcję "
    '<LSTag Type="Spell" Tooltip="Shout_Dash">Sprintu</LSTag>. Ruch uzyskany dzięki temu Sprintowi nie prowokuje '
    "ataków okazyjnych."
)

UID_OVERRIDES["h9e1946a3g463agb8b7g75e7gd94f9c36f9f7"] = (
    "Gdy używasz czarów Porażenia, zyskujesz "
    '<LSTag Tooltip="TemporaryHitPoints">tymczasowe punkty wytrzymałości</LSTag> w liczbie równej twojemu '
    '<LSTag Tooltip="AbilityModifier">modyfikatorowi</LSTag> Charyzmy.'
)
UID_OVERRIDES["hd984038eg2324g666bg83degd9c1722e9df2"] = (
    "Kości obrażeń Ataku z ukrycia zwiększają się dodatkowo o [1]."
)
UID_OVERRIDES["hf357f8d7g161dg5711g5d18gf26bc2d2273f"] = (
    "W pierwszej rundzie każdej walki masz Ułatwienie w testach ataku przeciwko każdej istocie, która nie wykonała "
    "jeszcze tury. Jeśli w tej rundzie trafisz dowolny cel Atakiem z ukrycia, otrzymuje on dodatkowe obrażenia typu "
    "zadawanego przez broń w liczbie równej twojemu poziomowi łotrzyka."
)

UID_OVERRIDES["hb015b8bcg9783ge81ag0118gaa1388097f11"] = (
    "Gdy nie zdasz rzutu obronnego, możesz uznać go za udany. Po skorzystaniu z tej cechy nie możesz zrobić tego "
    "ponownie, dopóki nie ukończysz długiego odpoczynku."
)
UID_OVERRIDES["h852a89d3g128fga1e5g2fedg98ddac129936"] = (
    "Gdy nie zdasz rzutu obronnego, możesz uznać go za udany."
)
UID_OVERRIDES["hd944c877g9f95g1749ge647gfe18b6b31562"] = (
    "Gdy nie zdasz rzutu obronnego na Inteligencję, Mądrość albo Charyzmę, możesz zamiast tego uznać go za udany. "
    "Po skorzystaniu z tej korzyści nie możesz zrobić tego ponownie, dopóki nie ukończysz krótkiego albo długiego "
    "odpoczynku."
)

SPEEDY_TEXT = (
    "Zwiększenie szybkości. Twoja Szybkość wzrasta o 3 m.\n\n"
    'Sprint przez <LSTag Type="Status" Tooltip="DIFFICULT_TERRAIN">trudny teren</LSTag>. Gdy w swojej turze '
    "wykonujesz akcję Sprintu, trudny teren nie wymaga od ciebie dodatkowego ruchu do końca tej tury.\n\n"
    "Zwinny ruch. Ataki okazyjne przeciwko tobie są wykonywane z Utrudnieniem."
)
UID_OVERRIDES["h9aba9e0ag4af1g9f8fg922ag7e65e5b8a86b"] = SPEEDY_TEXT
UID_OVERRIDES["h1ea9a52fg1499gbdd8g9ab4g8e8ff63c7f3f"] = SPEEDY_TEXT.replace(
    "Sprint przez", '<LSTag Type="Spell" Tooltip="Shout_Dash">Sprint</LSTag> przez', 1
)

FAVORED_ENEMY_TEXT = (
    "Zawsze masz przygotowany czar Znak łowcy. Możesz rzucić go dwukrotnie bez zużywania komórki czaru, a wszystkie "
    "użycia odzyskujesz po ukończeniu długiego odpoczynku.\n\n"
    "Liczba rzuceń czaru bez zużywania komórki zwiększa się na określonych poziomach łowcy, zgodnie z kolumną "
    "Ulubiony wróg w tabeli cech łowcy."
)
for duplicate_uid in (
    "hcd8000b2gdb8aga27dg0c5agb3cd6b125346",
    "h306c6ef1gb334gc9d9g3199g2f6fed258ca6",
):
    UID_OVERRIDES[duplicate_uid] = FAVORED_ENEMY_TEXT

UID_OVERRIDES["haa5e73d8ga7e5ge281g8b67gae695bb23d75"] = (
    "Zawsze masz przygotowany czar Księżycowy promień.\n\n"
    "Gdy rzucasz Księżycowy promień, wybrana widoczna istota w promieniu 18 m od ciebie odzyskuje 2k4 punkty "
    "wytrzymałości.\n\n"
    "Po użyciu tej cechy do zmodyfikowania Księżycowego promienia nie możesz zrobić tego ponownie, dopóki nie "
    "ukończysz długiego odpoczynku."
)

FIND_STEED_FEATURE_TEXT = (
    "Zawsze masz przygotowany czar Znalezienie wierzchowca. Za pomocą tej cechy możesz rzucić go bez zużywania "
    "komórki czaru ani komponentów, a Inteligencja jest twoją cechą bazową do tego czaru.\n\n"
    "Po rzuceniu czaru za pomocą tej cechy nie możesz zrobić tego ponownie, dopóki nie ukończysz krótkiego "
    "odpoczynku."
)
for duplicate_uid in (
    "h4bf647c4g9622g1b59gd3ccg7614d1ac3969",
    "h92ac32f2gae16g6effgdffege7984a067a57",
):
    UID_OVERRIDES[duplicate_uid] = FIND_STEED_FEATURE_TEXT
EXACT_OVERRIDES["Find Steed"] = "Znalezienie wierzchowca"
EXACT_OVERRIDES["Scroll of Find Steed"] = "Zwój znalezienia wierzchowca"
UID_OVERRIDES["h0aaffea6g03a3g6185g2b3eg67a082d34700"] = (
    "Możesz raz rzucić Znalezienie wierzchowca bez zużywania komórki czaru. Możliwość tę odzyskujesz po ukończeniu "
    "długiego odpoczynku."
)

FIND_STEED_DESCRIPTION = (
    "Przywołujesz nieziemskiego wierzchowca i natychmiast go dosiadasz.\n\n"
    "W każdej swojej turze rumak może wykonać jedną z następujących akcji: "
    '<LSTag Type="Spell" Tooltip="Shout_Dash">Sprint</LSTag>, Odstąpienie, Unik albo Atak.\n\n'
    "Gdy dosiadasz wierzchowca i otrzymasz obrażenia o wartości co najmniej 4, musisz wykonać rzut obronny na "
    "Zręczność o ST 8. Przy niepowodzeniu spadasz z rumaka i otrzymujesz stan Powalenia na 1 turę."
)
UID_OVERRIDES["h2e3d13a5gdd90g80a4g970dg3282a7a7bfa9"] = FIND_STEED_DESCRIPTION
UID_OVERRIDES["hca271062g4f0eg4316gc46ag52e3d54b2851"] = (
    FIND_STEED_DESCRIPTION + "\n\nTylko gracz o czystym sercu może zobaczyć rumaka."
)

UID_OVERRIDES["h15e226b3g215bge214g85e0gbbc2eafde5c5"] = (
    "Zawsze masz przygotowany czar Krok przez mgłę. Możesz rzucić go, zużywając użycie Aktu wiary zamiast komórki "
    "czaru. Gdy rzucasz go w ten sposób, możesz wybrać zajęte przez istotę pole w promieniu 9 m od siebie. Jeśli "
    "istota jest chętna, oboje teleportujecie się i zamieniacie miejscami. Efekt się nie powiedzie, jeśli na miejscu "
    "docelowym nie ma dość miejsca dla ciebie albo tej istoty."
)
UID_OVERRIDES["hf409717bg5c28g26d8gd2b4g68055dc739d0"] = (
    "Możesz rzucić Krok przez mgłę bez zużywania komórki czaru. Możesz zrobić to tyle razy, ile wynosi twój "
    "modyfikator Mądrości (co najmniej raz), a wszystkie użycia odzyskujesz po ukończeniu długiego odpoczynku."
)

UID_OVERRIDES["h2cf47fc4g37cfg4d26ga580g3908890371fb"] = (
    "Twoja zdolność kierowania duchami rozwija się. Zyskujesz następujące korzyści.\n\n"
    "Moc z zaświatów. Raz na turę, gdy za pomocą komórki czaru rzucasz czar barda, który zadaje obrażenia albo przywraca "
    "punkty wytrzymałości, rzuć 1k6. Dodaj wynik do jednego rzutu obrażeń czaru albo do łącznej liczby przywracanych "
    "przez niego punktów wytrzymałości.\n\n"
    "Duchowe objawienie. Zawsze masz przygotowany czar Duchowi strażnicy. Ponadto zyskujesz jedną komórkę czaru 3. "
    "poziomu, której możesz użyć wyłącznie do rzucenia Duchowych strażników. Odzyskujesz tę komórkę po ukończeniu "
    "długiego odpoczynku."
)

SPELL_SLOT_BUNDLE_TEXT = "Zyskujesz dwie komórki czaru 1. poziomu i jedną komórkę czaru 2. poziomu."
for duplicate_uid in (
    "h0ef080f7gca72g7669g8b06g981e2feedb49",
    "h55dcc998g2b80g48f8g46ddg8233ec32e4b0",
):
    UID_OVERRIDES[duplicate_uid] = SPELL_SLOT_BUNDLE_TEXT
UID_OVERRIDES["h7c14769cg0f8ag7968g4156g1272fd5b7850"] = (
    "Zużyj komórkę czaru, aby odzyskać jedno użycie bardowskiej inspiracji."
)

UID_OVERRIDES["h13f755b1gb20cg69d9g98a6g40d319bcab11"] = (
    "Gdy rzucasz Księżycowy promień, wybrana widoczna istota w promieniu 18 m od ciebie odzyskuje 2k4 punkty "
    "wytrzymałości."
)
UID_OVERRIDES["ha5f5579fg9ce6ge4abg474ag9e80c16acfae"] = (
    "Przywołujesz i wypuszczasz stado śmiercionośnych kruków. Każda wybrana przez ciebie istota w stożku o długości "
    "9 m, którego źródłem jesteś, wykonuje rzut obronny na Zręczność. Przy niepowodzeniu otrzymuje 5k6 obrażeń od "
    'mocy i stan <LSTag Type="Status" Tooltip="BLINDED">Oślepienia</LSTag>. Przy powodzeniu otrzymuje połowę tych '
    "obrażeń. Oślepiona istota ponawia rzut obronny na koniec każdej swojej tury i w razie powodzenia kończy ten "
    "efekt na sobie."
)

ALERTNESS_AURA_TEXT = (
    "Dopóki nie masz stanu Obezwładnienia, emanujesz aurą czujności. Gdy ty oraz wybrane przez ciebie istoty w "
    "promieniu 3 m rzucacie na inicjatywę, wszyscy otrzymujecie premię do inicjatywy równą twojej premii z biegłości."
)
for duplicate_uid in (
    "ha8e6db56ge4ddgc57dgdfdbg53d7f82bba08",
    "h41b477e4g3e5cg4162gb3dbga2e44d7f9e08",
):
    UID_OVERRIDES[duplicate_uid] = ALERTNESS_AURA_TEXT

UID_OVERRIDES["h15504b2agf3a9gc7f3g51e1g6775163e7006"] = (
    "Gdy za pomocą komórki co najmniej 2. poziomu rzucasz czar ze szkoły Wieszczenia, odzyskujesz jedną zużytą "
    "komórkę czaru o jeden poziom niższą od użytej do rzucenia tego czaru. Za pomocą tej cechy nie możesz odzyskać "
    "komórki wyższej niż 5. poziomu."
)

FORMATION_MOVEMENT_TEXT = (
    "Możesz rozkazać sojusznikom podążać za twoją formacją (bez użycia akcji). Wybierz słyszące cię istoty w "
    "promieniu 18 m w liczbie nieprzekraczającej twojej premii z biegłości. Każdy cel może natychmiast przemieścić "
    "się maksymalnie o swoją Szybkość bez prowokowania ataków okazyjnych."
)
for duplicate_uid in (
    "hcac28d23geb38gd19fge1c7gd81fdc6dc09b",
    "h820d0d49g5c04gb627g8857g7f344163dd3d",
):
    UID_OVERRIDES[duplicate_uid] = FORMATION_MOVEMENT_TEXT

CELESTIAL_RESILIENCE_TEXT = (
    "Ty oraz każdy sojusznik w promieniu 9 m od ciebie zyskujecie tymczasowe punkty wytrzymałości w liczbie równej "
    "sumie twojego poziomu czarownika i modyfikatora Charyzmy. Po użyciu tej cechy nie możesz zrobić tego ponownie, "
    "dopóki nie ukończysz krótkiego odpoczynku."
)
for duplicate_uid in (
    "hcdda7ab4ge734g2112g0666gf41d8d14e579",
    "h1b6e4734gfe4cg6127g1562gd33af4d185ba",
    "h1a05b56aga724gdcdbge2deg4a389d5eeb0b",
):
    UID_OVERRIDES[duplicate_uid] = CELESTIAL_RESILIENCE_TEXT

ARCANE_WARD_DAMAGE_TEXT = (
    "Gdy otrzymujesz obrażenia, zamiast ciebie otrzymuje je magiczna powłoka. Jeśli masz Odporność albo Podatność "
    "na te obrażenia, zastosuj ją przed zmniejszeniem punktów wytrzymałości powłoki. Jeśli obrażenia zmniejszą jej "
    "punkty wytrzymałości do 0, otrzymujesz pozostałe obrażenia. Powłoka o 0 punktach wytrzymałości nie może "
    "pochłaniać obrażeń, lecz jej magia pozostaje aktywna."
)
UID_OVERRIDES["h2a374b86g81f6g7146ga72ag43246ef53813"] = ARCANE_WARD_DAMAGE_TEXT
UID_OVERRIDES["h211b59f7g914aga7a2gaf0eg6d3b97922133"] = (
    "Potrafisz splatać wokół siebie ochronną magię. Gdy za pomocą komórki rzucasz czar odpychania, możesz "
    "jednocześnie wykorzystać część jego magii, aby utworzyć na sobie magiczną powłokę trwającą do ukończenia "
    "długiego odpoczynku. Maksymalna liczba punktów wytrzymałości powłoki jest równa dwukrotności twojego poziomu "
    "maga plus twój modyfikator Inteligencji. "
    + ARCANE_WARD_DAMAGE_TEXT
    + "\n\nGdy za pomocą komórki rzucasz czar odpychania, powłoka odzyskuje punkty wytrzymałości w liczbie równej "
    "dwukrotności poziomu tej komórki. W ramach akcji dodatkowej możesz również zużyć komórkę czaru, aby powłoka "
    "odzyskała punkty wytrzymałości w liczbie równej dwukrotności poziomu zużytej komórki."
)
ARCANE_WARD_RECHARGE_TEXT = (
    "Możesz zużyć komórkę czaru, aby magiczna powłoka odzyskała punkty wytrzymałości w liczbie równej dwukrotności "
    "poziomu zużytej komórki."
)
for duplicate_uid in (
    "hf4e3045fg19c3gb683gfdccgf602f9c972bc",
    "h441c9c45ge8e7g3d2cg79e6g8a57eab6e20d",
):
    UID_OVERRIDES[duplicate_uid] = ARCANE_WARD_RECHARGE_TEXT
EXACT_OVERRIDES["Recharge Arcane Ward"] = "Odnów magiczną powłokę"
EXACT_OVERRIDES["Arcane Ward: 2"] = "Magiczna powłoka: 2"
EXACT_OVERRIDES["Arcane Ward: 5"] = "Magiczna powłoka: 5"
for ward_points in (10, 15, 20, 25):
    EXACT_OVERRIDES[f"Arcane Ward: {ward_points}"] = f"Magiczna powłoka: {ward_points}"
for ward_points in (2, 5, 10, 15, 20, 25):
    EXACT_OVERRIDES[f"Projected Ward: {ward_points}"] = f"Przekazanie osłony: {ward_points}"
EXACT_OVERRIDES["Level 6: Entropic Ward"] = "Poziom 6: Entropiczna ochrona"
EXACT_OVERRIDES["You gain the effects of the Death Ward spell until you finish a Long Rest."] = (
    "Pozostajesz pod wpływem czaru Osłona przed śmiercią do ukończenia długiego odpoczynku."
)
EXACT_OVERRIDES[
    "Whenever you take damage, the ward takes the damage instead, and if you have any Resistances or Vulnerabilities, "
    "apply them before reducing the ward’s Hit Points. If the damage reduces the ward to 0 Hit Points, you take any "
    "remaining damage. While the ward has 0 Hit Points, it can’t absorb damage, but its magic remains."
] = (
    "Za każdym razem, gdy otrzymujesz obrażenia, pochłania je powłoka. Jeśli masz jakiekolwiek odporności lub "
    "podatności, zastosuj je przed odjęciem obrażeń od punktów wytrzymałości powłoki. Jeśli obrażenia zmniejszą jej "
    "punkty wytrzymałości do 0, otrzymujesz pozostałe obrażenia. Gdy powłoka ma 0 punktów wytrzymałości, nie może "
    "pochłaniać obrażeń, lecz jej magia pozostaje aktywna."
)
EXACT_OVERRIDES["Activate Enervation"] = "Aktywuj Wyczerpanie"
EXACT_OVERRIDES["Enervation Target"] = "Cel Wyczerpania"
EXACT_OVERRIDES["Scroll of Enervation"] = "Zwój wyczerpania"

# Spell-scroll names need the genitive form of the Polish spell title.  They
# cannot be produced safely by translating "Scroll of" and the title as two
# independent segments, so keep the complete, reviewed set here.  Vanilla
# spell names follow the shipped Polish BG3 localization; spells absent from
# vanilla follow the Polish D&D 2024 corpus used by the community pass.
SCROLL_TITLE_OVERRIDES = {
    "Scroll of Acid Splash": "Zwój kwasowego rozprysku",
    "Scroll of Aganazzar's Scorcher": "Zwój spopielacza Aganazzara",
    "Scroll of Arcane Gate": "Zwój magicznych wrót",
    "Scroll of Armor of Agathys": "Zwój zbroi Agathys",
    "Scroll of Arms of Hadar": "Zwój ramion Hadara",
    "Scroll of Ashardalon's Stride": "Zwój kroku Ashardalona",
    "Scroll of Astral Flood": "Zwój astralnej powodzi",
    "Scroll of Aura of Vitality": "Zwój aury witalności",
    "Scroll of Awaken": "Zwój przebudzenia",
    "Scroll of Ballistic Smite": "Zwój balistycznego ugodzenia",
    "Scroll of Bane": "Zwój zguby",
    "Scroll of Barkskin": "Zwój korowej skóry",
    "Scroll of Beacon of Hope": "Zwój promienia nadziei",
    "Scroll of Blade Barrier": "Zwój bariery ostrzy",
    "Scroll of Blade Ward": "Zwój osłony przed orężem",
    "Scroll of Bless": "Zwój błogosławieństwa",
    "Scroll of Blinding Smite": "Zwój oślepiającego ugodzenia",
    "Scroll of Blood Bolt": "Zwój krwawego pocisku",
    "Scroll of Body Warping of Gorgoroth": "Zwój wypaczenia ciała Gorgorotha",
    "Scroll of Booming Blade": "Zwój grzmiącego ostrza",
    "Scroll of Branding Smite": "Zwój piętnującego ugodzenia",
    "Scroll of Bursting Sinew": "Zwój pękającego ścięgna",
    "Scroll of Cacophonic Shield": "Zwój kakofonicznej tarczy",
    "Scroll of Call Lightning": "Zwój wezwania błyskawicy",
    "Scroll of Calm Emotions": "Zwój wyciszenia emocji",
    "Scroll of Catapult": "Zwój katapulty",
    "Scroll of Circle of Power": "Zwój kręgu mocy",
    "Scroll of Cloak of Shadow": "Zwój płaszcza cienia",
    "Scroll of Command": "Zwój rozkazu",
    "Scroll of Compelled Duel": "Zwój prowokacji",
    "Scroll of Conjure Barrage": "Zwój przywołania ognia zaporowego",
    "Scroll of Conjure Woodland Beings": "Zwój wyczarowania leśnych istot",
    "Scroll of Contagion": "Zwój zarazy",
    "Scroll of Create Destroy Water": "Zwój stworzenia lub zniszczenia wody",
    "Scroll of Create Undead": "Zwój stworzenia nieumarłego",
    "Scroll of Crusaders Mantle": "Zwój płaszcza krzyżowca",
    "Scroll of Cure Wounds": "Zwój leczenia ran",
    "Scroll of Dancing Lights": "Zwój tańczących świateł",
    "Scroll of Danse Macabre": "Zwój makabrycznego tańca",
    "Scroll of Darkbolt": "Zwój mrocznego pocisku",
    "Scroll of Dawn": "Zwój świtu",
    "Scroll of Daylight": "Zwój światła dnia",
    "Scroll of Dazing Blast": "Zwój oszałamiającego wybuchu",
    "Scroll of Death Armor": "Zwój zbroi śmierci",
    "Scroll of Death Ward": "Zwój osłony przed śmiercią",
    "Scroll of Dispel Evil and Good": "Zwój rozproszenia dobra i zła",
    "Scroll of Dissonant Whispers": "Zwój fałszywych podszeptów",
    "Scroll of Divine Favor": "Zwój boskiej łaski",
    "Scroll of Dominate Beast": "Zwój dominacji nad bestią",
    "Scroll of Dragon's Breath": "Zwój smoczego zionięcia",
    "Scroll of Dream": "Zwój snu",
    "Scroll of Eldritch Blast": "Zwój nieziemskiego uderzenia",
    "Scroll of Elemental Exhalation": "Zwój zionięcia żywiołu",
    "Scroll of Elemental Weapon": "Zwój broni żywiołu",
    "Scroll of Elminster's Elusion": "Zwój nieuchwytności Elminstera",
    "Scroll of Enervation": "Zwój wyczerpania",
    "Scroll of Enhance Ability": "Zwój wzmocnienia cechy",
    "Scroll of Ensnaring Strike": "Zwój pętającego uderzenia",
    "Scroll of Entangle": "Zwój oplątania",
    "Scroll of Enthrall": "Zwój fascynacji",
    "Scroll of Faerie Fire": "Zwój blasku faerie",
    "Scroll of Find Steed": "Zwój znalezienia wierzchowca",
    "Scroll of Finger Guns": "Zwój pistoletów z palców",
    "Scroll of Fire Dance": "Zwój tańca ognia",
    "Scroll of Fire Rune": "Zwój runy ognia",
    "Scroll of Flame Strike": "Zwój słupa ognia",
    "Scroll of Fount of Moonlight": "Zwój źródła blasku księżyca",
    "Scroll of Freedom of Movement": "Zwój swobody ruchu",
    "Scroll of Friends": "Zwój przyjaźni",
    "Scroll of Frightful Start": "Zwój przerażającego początku",
    "Scroll of Frostbite": "Zwój odmrożenia",
    "Scroll of Grasping Vine": "Zwój chwytnego pnącza",
    "Scroll of Greater Restoration": "Zwój większego przywrócenia",
    "Scroll of Green-Flame Blade": "Zwój ostrza zielonego płomienia",
    "Scroll of Guardian of Faith": "Zwój strażnika wiary",
    "Scroll of Guidance": "Zwój wskazówek",
    "Scroll of Guiding Bolt": "Zwój pocisku wiodącego",
    "Scroll of Hail of Thorns": "Zwój gradu cierni",
    "Scroll of Harm": "Zwój krzywdy",
    "Scroll of Heal": "Zwój uleczenia",
    "Scroll of Healing Word": "Zwój kojącego słowa",
    "Scroll of Heat Metal": "Zwój rozgrzania metalu",
    "Scroll of Hell's Lash": "Zwój piekielnego bicza",
    "Scroll of Hellfire": "Zwój ognia piekielnego",
    "Scroll of Heroes Feast": "Zwój uczty bohaterów",
    "Scroll of Heroism": "Zwój heroizmu",
    "Scroll of Hex": "Zwój uroku",
    "Scroll of Holy Weapon": "Zwój świętej broni",
    "Scroll of Holy Word": "Zwój świętego słowa",
    "Scroll of Hunger of Hadar": "Zwój głodu Hadara",
    "Scroll of Hungering Blade": "Zwój głodnego ostrza",
    "Scroll of Hunter's Mark": "Zwój znaku łowcy",
    "Scroll of Inflict Wounds": "Zwój zadawania ran",
    "Scroll of Insect Plague": "Zwój plagi owadów",
    "Scroll of Laeral's Silver Lance": "Zwój srebrnej lancy Laeral",
    "Scroll of Lesser Restoration": "Zwój mniejszego przywrócenia",
    "Scroll of Light": "Zwój światła",
    "Scroll of Lightning Arrow": "Zwój piorunostrzału",
    "Scroll of Mage Hand": "Zwój magicznej dłoni",
    "Scroll of Mass Cure Wounds": "Zwój masowego leczenia ran",
    "Scroll of Mass Healing Word": "Zwój masowego kojącego słowa",
    "Scroll of Mind Sliver": "Zwój myślowego odłamka",
    "Scroll of Mind Spike": "Zwój myślowego ciernia",
    "Scroll of Minor Illusion": "Zwój pomniejszej iluzji",
    "Scroll of Moonbeam": "Zwój księżycowego promienia",
    "Scroll of Murder of Crows": "Zwój stada kruków",
    "Scroll of Murmurs of Doom": "Zwój pomruków zagłady",
    "Scroll of Pass Without Trace": "Zwój przejścia bez śladu",
    "Scroll of Phantom Steed": "Zwój widmowego wierzchowca",
    "Scroll of Planar Ally": "Zwój sferalnego sojusznika",
    "Scroll of Plant Growth": "Zwój rozrostu roślin",
    "Scroll of Poison Spray": "Zwój trującego rozprysku",
    "Scroll of Prayer of Healing": "Zwój uzdrawiającej modlitwy",
    "Scroll of Produce Flame": "Zwój wywołania płomienia",
    "Scroll of Protection from Poison": "Zwój ochrony przed trucizną",
    "Scroll of Resistance": "Zwój odporności",
    "Scroll of Rime's Binding Ice": "Zwój wiążącego lodu Rime'a",
    "Scroll of Sacred Flame": "Zwój świętego płomienia",
    "Scroll of Sanctuary": "Zwój sanktuarium",
    "Scroll of Searing Orb": "Zwój płonącej kuli",
    "Scroll of Searing Smite": "Zwój palącego ugodzenia",
    "Scroll of Shadow Blade": "Zwój ostrza cienia",
    "Scroll of Shield of Faith": "Zwój tarczy wiary",
    "Scroll of Shillelagh": "Zwój Shillelagh",
    "Scroll of Silence": "Zwój ciszy",
    "Scroll of Snilloc's Snowball Swarm": "Zwój roju śnieżek Snilloca",
    "Scroll of Sorcerous Burst": "Zwój wybuchu mocy",
    "Scroll of Spare the Dying": "Zwój powstrzymania śmierci",
    "Scroll of Speak With Animals": "Zwój rozmawiania ze zwierzętami",
    "Scroll of Spectral Slash": "Zwój widmowego cięcia",
    "Scroll of Spellfire Flare": "Zwój rozbłysku magicznego ognia",
    "Scroll of Spellfire Storm": "Zwój burzy magicznego ognia",
    "Scroll of Spike Growth": "Zwój wzrostu kolców",
    "Scroll of Spirit Guardians": "Zwój duchowych strażników",
    "Scroll of Spiritual Weapon": "Zwój duchowej broni",
    "Scroll of Starry Wisp": "Zwój gwiezdnego ognika",
    "Scroll of Steel Wind Strike": "Zwój uderzenia stalowego wichru",
    "Scroll of Summon Beast": "Zwój przyzwania bestii",
    "Scroll of Summon Celestial": "Zwój przyzwania niebianina",
    "Scroll of Summon Dragon": "Zwój przyzwania smoka",
    "Scroll of Summon Fey": "Zwój przyzwania Fey",
    "Scroll of Sword Burst": "Zwój wybuchu miecza",
    "Scroll of Synaptic Static": "Zwój szumu synaptycznego",
    "Scroll of Tasha's Mind Whip": "Zwój bicza umysłu Tashy",
    "Scroll of Thaumaturgy": "Zwój taumaturgii",
    "Scroll of Thorn Armor": "Zwój cierniowej zbroi",
    "Scroll of Thorn Whip": "Zwój cierniowego bicza",
    "Scroll of Thunderclap": "Zwój grzmotu",
    "Scroll of Thunderous Smite": "Zwój grzmiącego ugodzenia",
    "Scroll of Tidal Wave": "Zwój fali przypływowej",
    "Scroll of Tide of Darkness": "Zwój przypływu ciemności",
    "Scroll of Toll the Dead": "Zwój żałobnego dzwonu",
    "Scroll of Trollblood Infusion": "Zwój nasycenia krwią trolla",
    "Scroll of True Strike": "Zwój prawdziwego uderzenia",
    "Scroll of Umbral Tendril": "Zwój cienistej macki",
    "Scroll of Vengeful Blade": "Zwój mściwego ostrza",
    "Scroll of Vicious Mockery": "Zwój zjadliwego szyderstwa",
    "Scroll of Vitriolic Sphere": "Zwój żrącej kuli",
    "Scroll of Void Strike": "Zwój uderzenia pustki",
    "Scroll of Wall of Thorns": "Zwój ściany cierni",
    "Scroll of Wardaway": "Zwój odpędzenia",
    "Scroll of Warding Bond": "Zwój ochronnej więzi",
    "Scroll of Wind Walk": "Zwój spaceru na wietrze",
    "Scroll of Word of Radiance": "Zwój słowa blasku",
    "Scroll of Wrathful Smite": "Zwój gniewnego ugodzenia",
}
EXACT_OVERRIDES.update(SCROLL_TITLE_OVERRIDES)

# The mod exposes one localized selector label per Magic Initiate spell.  The
# source repeats these labels across several lists, and translating each whole
# phrase independently produced four competing Polish prefixes and many stale
# spell-name calques.  BG3's Polish UI uses "Wtajemniczony: …" for this family.
MAGIC_INITIATE_TITLES = {
    "Absorb Elements": "Wchłanianie żywiołów",
    "Acid Splash": "Kwasowy rozprysk",
    "Animal Friendship": "Przyjaciel zwierząt",
    "Bane": "Zguba",
    "Blade Ward": "Osłona przed orężem",
    "Bless": "Błogosławieństwo",
    "Blood Bolt": "Krwawy pocisk",
    "Body Warping of Gorgoroth": "Wypaczenie ciała Gorgorotha",
    "Booming Blade": "Grzmiące ostrze",
    "Burning Hands": "Płonące dłonie",
    "Bursting Sinew": "Pękające ścięgno",
    "Catapult": "Katapulta",
    "Charm Person": "Zauroczenie osoby",
    "Chill Touch": "Przeszywający dotyk",
    "Chromatic Orb": "Barwna kula",
    "Cleric": "Kleryk",
    "Cloak of Shadow": "Płaszcz cienia",
    "Colour Spray": "Kolorowy rozprysk",
    "Command": "Rozkaz",
    "Create or Destroy Water": "Stworzenie lub zniszczenie wody",
    "Cure Wounds": "Leczenie ran",
    "Dancing Lights": "Tańczące światła",
    "Disguise Self": "Przebranie siebie",
    "Druid": "Druid",
    "Eldritch Blast": "Nieziemskie uderzenie",
    "Enhance Leap": "Dłuższy skok",
    "Entangle": "Oplątanie",
    "Expeditious Retreat": "Błyskawiczny odwrót",
    "Faerie Fire": "Blask faerie",
    "False Life": "Fałszywe życie",
    "Feather Fall": "Piórkospadanie",
    "Find Familiar": "Znalezienie chowańca",
    "Finger Guns": "Pistolety z palców",
    "Fire Bolt": "Ognisty pocisk",
    "Fog Cloud": "Chmura mgły",
    "Friends": "Przyjaźń",
    "Frightful Start": "Przerażający początek",
    "Frostbite": "Odmrożenie",
    "Goodberry": "Dobre jagody",
    "Grease": "Tłuszcz",
    "Green-Flame Blade": "Ostrze zielonego płomienia",
    "Guidance": "Wskazówki",
    "Guiding Bolt": "Pocisk wiodący",
    "Healing Word": "Kojące słowo",
    "Hellfire": "Ogień piekielny",
    "Hell’s Lash": "Piekielny bicz",
    "Hideous Laughter": "Ohydny śmiech",
    "Holy Word": "Święte słowo",
    "Ice Knife": "Lodowy nóż",
    "Inflict Wounds": "Zadawanie ran",
    "Jump": "Skok",
    "Light": "Światło",
    "Longstrider": "Szybkonogi",
    "Mage Armor": "Zbroja maga",
    "Mage Armour": "Zbroja maga",
    "Mage Hand": "Magiczna dłoń",
    "Magic Missile": "Magiczny pocisk",
    "Mind Sliver": "Myślowy odłamek",
    "Minor Illusion": "Pomniejsza iluzja",
    "Poison Spray": "Trujący rozprysk",
    "Prestidigitation": "Kuglarstwo",
    "Produce Flame": "Wywołanie płomienia",
    "Protection from Evil and Good": "Ochrona przed dobrem i złem",
    "Ray of Frost": "Promień mrozu",
    "Ray of Sickness": "Promień zatrucia",
    "Resistance": "Odporność",
    "Sacred Flame": "Święty płomień",
    "Sanctuary": "Sanktuarium",
    "Shield": "Tarcza",
    "Shield of Faith": "Tarcza wiary",
    "Shillelagh": "Shillelagh",
    "Shocking Grasp": "Porażający uścisk",
    "Sleep": "Uśpienie",
    "Sorcerous Burst": "Wybuch mocy",
    "Spare the Dying": "Powstrzymanie śmierci",
    "Speak with Animals": "Rozmawianie ze zwierzętami",
    "Spellfire Flare": "Rozbłysk magicznego ognia",
    "Starry Wisp": "Gwiezdny ognik",
    "Sword Burst": "Wybuch miecza",
    "Tasha's Hideous Laughter": "Ohydny śmiech Tashy",
    "Thaumaturgy": "Taumaturgia",
    "Thorn Armor": "Cierniowa zbroja",
    "Thorn Whip": "Cierniowy bicz",
    "Thunderclap": "Grzmot",
    "Thunderwave": "Fala gromu",
    "Tide of Darkness": "Przypływ ciemności",
    "Toll the Dead": "Żałobny dzwon",
    "True Strike": "Prawdziwe uderzenie",
    "Umbral Tendril": "Cienista macka",
    "Vengeful Blade": "Mściwe ostrze",
    "Vicious Mockery": "Zjadliwe szyderstwo",
    "Wardaway": "Odpędzenie",
    "Witch Bolt": "Wiedźmowy pocisk",
    "Wizard": "Mag",
    "Word of Radiance": "Słowo blasku",
}
EXACT_OVERRIDES.update(
    {f"Magic Initiate: {english}": f"Wtajemniczony: {polish}" for english, polish in MAGIC_INITIATE_TITLES.items()}
)

FEY_SELECTOR_TITLES = {
    "Animal Friendship": "Przyjaciel zwierząt",
    "Bane": "Zguba",
    "Bless": "Błogosławieństwo",
    "Charm Person": "Zauroczenie osoby",
    "Command": "Rozkaz",
    "Compelled Duel": "Prowokacja",
    "Dissonant Whispers": "Fałszywe podszepty",
    "Heroism": "Heroizm",
    "Hex": "Urok",
    "Tasha's Hideous Laughter": "Ohydny śmiech Tashy",
    "Hunter's Mark": "Znak łowcy",
    "Sleep": "Uśpienie",
    "Speak with Animals": "Rozmawianie ze zwierzętami",
}
for english, polish in FEY_SELECTOR_TITLES.items():
    EXACT_OVERRIDES[f"Fey Touched: {english}"] = f"Dotknięty przez fey: {polish}"
    EXACT_OVERRIDES[f"Fey Magic: {english}"] = f"Magia fey: {polish}"
EXACT_OVERRIDES['Fey Magic: <LSTag Type="Spell" Tooltip="Target_Bane">Bane</LSTag>'] = (
    'Magia fey: <LSTag Type="Spell" Tooltip="Target_Bane">Zguba</LSTag>'
)

SHADOW_SELECTOR_TITLES = {
    "Cloak of Shadow": "Płaszcz cienia",
    "Colour Spray": "Kolorowy rozprysk",
    "Disguise Self": "Przebranie siebie",
    "False Life": "Fałszywe życie",
    "Hungering Blade": "Głodne ostrze",
    "Inflict Wounds": "Zadawanie ran",
    "Ray of Sickness": "Promień zatrucia",
    "Wrathful Smite": "Gniewne ugodzenie",
}
for english, polish in SHADOW_SELECTOR_TITLES.items():
    EXACT_OVERRIDES[f"Shadow Touched: {english}"] = f"Dotknięty przez cień: {polish}"
    EXACT_OVERRIDES[f"Shadow Magic: {english}"] = f"Cienista magia: {polish}"

RUNE_SHAPER_TITLES = {
    "Cloud": "Chmura",
    "Death": "Śmierć",
    "Dragon": "Smok",
    "Enemy": "Wróg",
    "Fire": "Ogień",
    "Friend": "Przyjaciel",
    "Frost": "Mróz",
    "Hill": "Wzgórze",
    "Journey": "Podróż",
    "King": "Król",
    "Mountain": "Góra",
    "Stone": "Kamień",
    "Storm": "Burza",
}
EXACT_OVERRIDES.update(
    {f"Rune Shaper: {english}": f"Kształtujący runy: {polish}" for english, polish in RUNE_SHAPER_TITLES.items()}
)

RUNE_MAGIC_TITLES = {
    "Fog cloud": "Chmura mgły",
    "Inflict wounds": "Zadawanie ran",
    "Chromatic orb": "Barwna kula",
    "Disguise self": "Przebranie siebie",
    "Burning hands": "Płonące dłonie",
    "Speak with animals": "Rozmawianie ze zwierzętami",
    "Armor of Agathys": "Zbroja Agathys",
    "Goodberry": "Dobre jagody",
    "Longstrider": "Szybkonogi",
    "Command": "Rozkaz",
    "Entangle": "Oplątanie",
    "Sanctuary": "Sanktuarium",
    "Thunderwave": "Fala gromu",
}
EXACT_OVERRIDES.update(
    {f"Rune Magic: {english}": f"Magia runiczna: {polish}" for english, polish in RUNE_MAGIC_TITLES.items()}
)

for surge_result in range(1, 101):
    EXACT_OVERRIDES[f"Wild Magic Surge: {surge_result}"] = f"Przypływ dzikiej magii: {surge_result}"
EXACT_OVERRIDES.update({
    "Wild Magic Surge: Turn": "Przypływ dzikiej magii: tura",
    "Wild Magic Surge: Heal": "Przypływ dzikiej magii: uleczenie",
    "Wild Magic Surge: Heightened Spell": "Przypływ dzikiej magii: Przebijające zaklęcie",
    "Wild Magic Surge: Subtle Spell": "Przypływ dzikiej magii: Dyskretne zaklęcie",
    "Wild Magic Surge: Empowered Spell": "Przypływ dzikiej magii: Wzmocnione zaklęcie",
    "Wild Magic Surge: Resistance": "Przypływ dzikiej magii: odporność",
    "Wild Magic Surge: Shield": "Przypływ dzikiej magii: Tarcza",
    "Wild Magic Surge: Quickened Spell": "Przypływ dzikiej magii: Przyspieszone zaklęcie",
})

# Keep the Way of the Elements action family aligned with the Polish D&D 2024
# community terminology. Damage-type labels follow the official Polish BG3 UI.
EXACT_OVERRIDES.update({
    "Elemental Attunement: Acid": "Harmonia żywiołów: Kwas",
    "Elemental Attunement: Cold": "Harmonia żywiołów: Zimno",
    "Elemental Attunement: Fire": "Harmonia żywiołów: Ogień",
    "Elemental Attunement: Lightning": "Harmonia żywiołów: Elektryczność",
    "Elemental Attunement: Thunder": "Harmonia żywiołów: Dźwięk",
    "Elemental Attunement: Reach": "Harmonia żywiołów: Zasięg",
    "Elemental Strikes: Pull": "Uderzenia żywiołów: Przyciągnięcie",
    "Elemental Strikes: Push": "Uderzenia żywiołów: Odepchnięcie",
    "Elemental Strikes: Acid": "Uderzenia żywiołów: Kwas",
    "Elemental Strikes: Cold": "Uderzenia żywiołów: Zimno",
    "Elemental Strikes: Fire": "Uderzenia żywiołów: Ogień",
    "Elemental Strikes: Lightning": "Uderzenia żywiołów: Elektryczność",
    "Elemental Strikes: Thunder": "Uderzenia żywiołów: Dźwięk",
    "Elemental Burst: Acid": "Wybuch żywiołów: Kwas",
    "Elemental Burst: Cold": "Wybuch żywiołów: Zimno",
    "Elemental Burst: Fire": "Wybuch żywiołów: Ogień",
    "Elemental Burst: Lightning": "Wybuch żywiołów: Elektryczność",
    "Elemental Burst: Thunder": "Wybuch żywiołów: Dźwięk",
})

CLASS_NAMES = {
    "Artificer": "Wynalazca",
    "Barbarian": "Barbarzyńca",
    "Bard": "Bard",
    "Cleric": "Kleryk",
    "Druid": "Druid",
    "Fighter": "Wojownik",
    "Monk": "Mnich",
    "Paladin": "Paladyn",
    "Ranger": "Łowca",
    "Rogue": "Łotrzyk",
    "Sorcerer": "Zaklinacz",
    "Warlock": "Czarownik",
    "Wizard": "Mag",
}


def translate_usable_classes(source: str) -> str | None:
    prefix = "Usable Classes: "
    if not source.startswith(prefix):
        return None
    classes = [part.strip() for part in source[len(prefix):].split(",")]
    if any(class_name not in CLASS_NAMES for class_name in classes):
        return None
    return "Dostępne klasy: " + ", ".join(CLASS_NAMES[class_name] for class_name in classes)


ORIGIN_FEAT_TITLES = {
    "Alert": "Czujność",
    "Cult of the Dragon Initiate": "Nowicjusz Kultu Smoka",
    "Emerald Enclave Fledgling": "Pisklę Szmaragdowej Enklawy",
    "Harper Agent": "Agent Harfiarzy",
    "Healer": "Uzdrowiciel",
    "Lords’ Alliance Agent": "Agent Sojuszu Lordów",
    "Lucky": "Szczęściarz",
    "Magic Initiate (Cleric)": "Wtajemniczony (kleryk)",
    "Magic Initiate (Druid)": "Wtajemniczony (druid)",
    "Magic Initiate (Wizard)": "Wtajemniczony (mag)",
    "Musician": "Muzyk",
    "Purple Dragon Rook": "Rekrut Purpurowego Smoka",
    "Savage Attacker": "Brutalny napastnik",
    "Skilled": "Uzdolniony",
    "Spellfire Spark": "Iskra magicznego ognia",
    "Strike of the Giants": "Uderzenie olbrzymów",
    "Tavern Brawler": "Zabijaka",
    "Tough": "Twardziel",
    "Tyro of the Gauntlet": "Nowicjusz Rękawicy",
    "Zhentarim Ruffian": "Oprych Zhentarimów",
}
EXACT_OVERRIDES.update({
    f"Origin Feat: {english}": f"Atut pochodzenia: {polish}"
    for english, polish in ORIGIN_FEAT_TITLES.items()
})

SKILLED_TITLES = {
    "Acrobatics": "Akrobatyka",
    "Animal Handling": "Opieka nad zwierzętami",
    "Arcana": "Wiedza Tajemna",
    "Athletics": "Atletyka",
    "Deception": "Oszustwo",
    "History": "Historia",
    "Insight": "Intuicja",
    "Intimidation": "Zastraszanie",
    "Investigation": "Śledztwo",
    "Medicine": "Medycyna",
    "Nature": "Przyroda",
    "Perception": "Percepcja",
    "Performance": "Występy",
    "Persuasion": "Perswazja",
    "Religion": "Religia",
    "Sleight of Hand": "Zwinne dłonie",
    "Stealth": "Skradanie się",
    "Survival": "Sztuka przetrwania",
}
EXACT_OVERRIDES.update({
    f"Skilled: {english}": f"Uzdolniony: {polish}"
    for english, polish in SKILLED_TITLES.items()
})
EXACT_OVERRIDES.update({
    "Skilled: You have gained proficiency in the selected skill.": (
        "Uzdolniony: Zyskujesz biegłość w wybranej umiejętności."
    ),
    "Skilled: You have gained proficiency in three skills. Well chosen.": (
        "Uzdolniony: Zyskujesz biegłość w trzech umiejętnościach. Dobry wybór."
    ),
    "Wild Shape: Deep Rothé": "Dzika postać: Głębinowy roth",
    "Wild Shape: Sea": "Dzika postać: Morze",
    "Level 2: Wild Shape": "Poziom 2: Dzika postać",
})

SPIRIT_TITLES = {
    "Arsonist": "Podpalacz",
    "Avenger": "Mściciel",
    "Beloved": "Ukochany",
    "Coward": "Tchórz",
    "Fortune Teller": "Wróżbita",
    "Renegade": "Renegat",
    "Shade": "Cień",
    "Sharpshooter": "Strzelec wyborowy",
    "Trickster": "Oszust",
    "Wayfarer": "Wędrowiec",
}
EXACT_OVERRIDES.update({
    "Spirits From Beyond": "Duchy z zaświatów",
    "Controlled Channeling": "Kontrolowane przywołanie",
    "Unleashing a Spirit": "Uwolnienie ducha",
    "Level 6: Empowered Channeling": "Poziom 6: Wzmocnione przywołanie",
})
for english, polish in SPIRIT_TITLES.items():
    EXACT_OVERRIDES[f"Spirits From Beyond: {english}"] = f"Duchy z zaświatów: {polish}"
    EXACT_OVERRIDES[f"Controlled Channeling: {english}"] = f"Kontrolowane przywołanie: {polish}"
    EXACT_OVERRIDES[f"Unleashing a Spirit: {english}"] = f"Uwolnienie ducha: {polish}"

for ability_en, ability_pl in {
    "Charisma": "Charyzma",
    "Dexterity": "Zręczność",
    "Intelligence": "Inteligencja",
    "Strength": "Siła",
    "Wisdom": "Mądrość",
}.items():
    EXACT_OVERRIDES[f"Severed from Dreams: {ability_en}"] = f"Odcięty od snów: {ability_pl}"
EXACT_OVERRIDES["Severed from Dreams"] = "Odcięty od snów"

for giant_en, giant_pl in {
    "Cloud Giant": "Olbrzym chmurowy",
    "Fire Giant": "Olbrzym ognisty",
    "Frost Giant": "Olbrzym mroźny",
    "Hill Giant": "Olbrzym wzgórzowy",
    "Stone Giant": "Olbrzym kamienny",
    "Storm Giant": "Olbrzym burzowy",
}.items():
    EXACT_OVERRIDES[f"Giant Ancestry: {giant_en}"] = f"Rodowód olbrzymów: {giant_pl}"
EXACT_OVERRIDES["Giant Ancestry"] = "Rodowód olbrzymów"

EXACT_OVERRIDES.update({
    "Dread Allegiance": "Złowrogie oddanie",
    "Dread Allegiance: Bane": "Złowrogie oddanie: Bane",
    "Dread Allegiance: Bhaal": "Złowrogie oddanie: Bhaal",
    "Dread Allegiance: Myrkul": "Złowrogie oddanie: Myrkul",
    "Cunning Strike": "Chytre uderzenie",
    "Level 5: Cunning Strike": "Poziom 5: Chytre uderzenie",
    "Cunning Strike: Poison": "Chytre uderzenie: Trucizna",
    "Cunning Strike: Terrify": "Chytre uderzenie: Przerażenie",
    "Cunning Strike: Trip": "Chytre uderzenie: Podcięcie",
    "Cunning Strike: Withdraw": "Chytre uderzenie: Odwrót",
    "Conjure Minor Elementals": "Wyczarowanie mniejszych żywiołaków",
    "Conjure Minor Elementals: Acid": "Wyczarowanie mniejszych żywiołaków: Kwas",
    "Conjure Minor Elementals: Cold": "Wyczarowanie mniejszych żywiołaków: Zimno",
    "Conjure Minor Elementals: Fire": "Wyczarowanie mniejszych żywiołaków: Ogień",
    "Conjure Minor Elementals: Lightning": "Wyczarowanie mniejszych żywiołaków: Elektryczność",
    "Unleash Hell": "Rozpętanie piekła",
    "Unleash Hell: Fire": "Rozpętanie piekła: Ogień",
    "Unleash Hell: Necrotic": "Rozpętanie piekła: Nekrotyczne",
    "Infused": "Nasycenie",
    "Infused: Acid": "Nasycenie: Kwas",
    "Infused: Cold": "Nasycenie: Zimno",
    "Infused: Fire": "Nasycenie: Ogień",
    "Infused: Lightning": "Nasycenie: Elektryczność",
    "Infused: Poison": "Nasycenie: Trucizna",
    "Infused: Thunder": "Nasycenie: Dźwięk",
    "Level 5: Eldritch Smite": "Poziom 5: Mistyczne ugodzenie",
    "Level 6: Bastion of Law": "Poziom 6: Bastion prawa",
    "Eldritch Smite: Reaction": "Mistyczne ugodzenie: reakcja",
    "Eldritch Smite (Melee)": "Mistyczne ugodzenie (wręcz)",
    "Eldritch Smite on Critical Hit (Melee)": "Mistyczne ugodzenie przy trafieniu krytycznym (wręcz)",
    "Eldritch Smite (Ranged)": "Mistyczne ugodzenie (dystansowe)",
    "Eldritch Smite on Critical Hit (Ranged)": (
        "Mistyczne ugodzenie przy trafieniu krytycznym (dystansowe)"
    ),
    "Use Poisoner’s Kit: Poison": "Użyj zestawu truciciela: Trucizna",
    "Use Poisoner’s Kit: Toxin": "Użyj zestawu truciciela: Toksyna",
    "Burning Seals: Fire": "Płonące pieczęcie: Ogień",
    "Burning Seals: Necrotic": "Płonące pieczęcie: Nekrotyczne",
})
for bastion_dice in range(1, 6):
    EXACT_OVERRIDES[f"Bastion of Law: {bastion_dice}"] = f"Bastion prawa: {bastion_dice}"
for hit_die in (6, 8, 10, 12):
    EXACT_OVERRIDES[f"Hit Point Dice: D{hit_die}"] = f"Kość Wytrzymałości: k{hit_die}"
    EXACT_OVERRIDES[f"Use Hit Point Dice: D{hit_die}"] = f"Użyj Kości Wytrzymałości: k{hit_die}"

for initiate_class_en, initiate_class_pl in {
    "Cleric": "kleryk",
    "Druid": "druid",
    "Wizard": "mag",
}.items():
    initiate_prefix = f"Magic Initiate ({initiate_class_en})"
    target_prefix = f"Wtajemniczony ({initiate_class_pl})"
    EXACT_OVERRIDES[f"{initiate_prefix}: Cantrip"] = f"{target_prefix}: sztuczka"
    EXACT_OVERRIDES[f"{initiate_prefix}: Cantrip 2"] = f"{target_prefix}: druga sztuczka"
    EXACT_OVERRIDES[f"{initiate_prefix}: Spell"] = f"{target_prefix}: czar"
    EXACT_OVERRIDES[f"{initiate_prefix}: You have learned two cantrips. Well chosen."] = (
        f"{target_prefix}: Poznajesz dwie sztuczki. Dobry wybór."
    )
    EXACT_OVERRIDES[f"{initiate_prefix}: You have learned the selected cantrip."] = (
        f"{target_prefix}: Poznajesz wybraną sztuczkę."
    )
    EXACT_OVERRIDES[f"{initiate_prefix}: You have learned the selected spell."] = (
        f"{target_prefix}: Poznajesz wybrany czar."
    )

EXACT_OVERRIDES[
    'Protect a creature from attacks: increase its <LSTag Tooltip="ArmourClass">Armour Class</LSTag> up to 17.'
] = (
    'Ochroń cel przed atakami: zwiększ <LSTag Tooltip="ArmourClass">Klasę Pancerza</LSTag> istoty, '
    "maksymalnie do 17."
)
UID_OVERRIDES["h2eddaae5gd399g869eg1cdag9e9a178e24d8"] = "Nasycenie"

UID_OVERRIDES["h90c565bfgdc8eg1fc2gde60ga457cc60135b"] = (
    'Dopóki twoja <LSTag Type="Spell" Tooltip="Shout_HarmonyOfFireAndWater">Harmonia żywiołów</LSTag> '
    "jest aktywna, zyskujesz Szybkość lotu i Szybkość pływania równe twojej Szybkości."
)
UID_OVERRIDES["h13aa2cdag2fb5g8660ga803g42449d529329"] = (
    "Wybierz obrażenia od kwasu, zimna, ognia, elektryczności, trucizny albo dźwięku. Cel trafiony atakiem "
    "otrzymuje dodatkowe obrażenia wybranego typu."
)
for infused_description_uid in (
    "h2c602649g9292g91d9g709bg07327682e721",
    "h14e14dcbg4d74gcb77g5954gf0d23d010934",
):
    UID_OVERRIDES[infused_description_uid] = (
        "Wybierz jeden z następujących typów obrażeń: kwas, zimno, ogień, elektryczność, trucizna albo dźwięk. "
        "Przez 10 minut za każdym razem, gdy trafisz atakiem bronią, możesz sprawić, że zada on obrażenia wybranego "
        "typu zamiast swojego zwykłego typu obrażeń."
    )
UID_OVERRIDES["h4c3e9164gb5c2g35d0g405dgb887921e3e3a"] = (
    "Opracowujesz chytre sposoby wykorzystania Ataku z ukrycia. Gdy zadajesz obrażenia Atakiem z ukrycia, możesz "
    "dodać jeden z poniższych efektów Chytrego uderzenia.\n\nJeśli efekt Chytrego uderzenia wymaga rzutu "
    "obronnego, jego ST wynosi 8 + twój modyfikator Zręczności + Premia z biegłości."
)
UID_OVERRIDES["h0343e6b8g3fecg85eag5ab7gd8f289bd951a"] = (
    "Zyskujesz wariant Przerażenie Chytrego uderzenia. Dopóki cel jest przerażony, masz ułatwienie w testach "
    "ataku przeciwko niemu."
)
UID_OVERRIDES["h834d7e4cg19fdgd3acg2b88g50ab0030af80"] = (
    "Doskonalisz odporność na moce wpływające na umysł. Zyskujesz biegłość w rzutach obronnych na Mądrość."
)
STEADY_AIM_TEXT = (
    "W ramach akcji dodatkowej zapewniasz sobie ułatwienie w następnym teście ataku w tej turze. Możesz skorzystać "
    "z tej cechy tylko przed wykonaniem ruchu w tej turze. Po jej użyciu twoja Szybkość wynosi 0 do końca tury."
)
for steady_aim_uid in (
    "h8b43db08gaf12gc02agb86cge29d6c39df7f",
    "haf3b75e3g8f42g8af5ge959ga8ee656088f7",
    "h49585eb0g7c75g3df5g4aacg38e6e664edb2",
):
    UID_OVERRIDES[steady_aim_uid] = STEADY_AIM_TEXT
UID_OVERRIDES["h32ed567egee36g91e1g2accgb992c0f4d730"] = (
    'Podczas nauki magii zdobywasz również specjalizację w innej dziedzinie. Wybierz jedną z poniższych '
    'umiejętności, w której masz biegłość: <LSTag Type="Skills" Tooltip="Arcana">Wiedza Tajemna</LSTag>, '
    '<LSTag Type="Skills" Tooltip="History">Historia</LSTag>, Śledztwo, '
    '<LSTag Type="Skills" Tooltip="Medicine">Medycyna</LSTag>, '
    '<LSTag Type="Skills" Tooltip="Nature">Przyroda</LSTag> albo '
    '<LSTag Type="Skills" Tooltip="Religion">Religia</LSTag>. Zyskujesz Znawstwo w wybranej umiejętności.'
)
UID_OVERRIDES["h5ec953edgae89gbe4fgbc37g46d66f973083"] = "Zyskujesz biegłość w tej umiejętności."
UID_OVERRIDES["h81682b22g3da3g86c5g11f5gbebe41d25951"] = (
    'Poznajesz trzy wybrane <LSTag Tooltip="RitualSpell">czary rytualne</LSTag>.'
)
UID_OVERRIDES["h60b4a6b6g2c59g4b4cgb657g5872fb1a68d4"] = (
    "Otacza cię tajemnicza aura fey — dar arcyfey albo skutek przemiany w jednym z miejsc Feywild. Niezależnie od "
    "źródła tej magii jesteś teraz Wędrowcem Fey. Twój radosny śmiech podnosi na duchu uciśnionych, a biegłość w "
    "walce napełnia wrogów grozą. Wesołość fey jest bowiem wielka, a ich gniew straszliwy."
)
UID_OVERRIDES["h9d72f0d7g2c0egb1bbgde11g3864f11ceed2"] = (
    "Duszostrze atakuje umysłem, przecinając zarówno fizyczne, jak i psychiczne bariery. Łotrzykowie tej podklasy "
    "odkrywają w sobie moc psioniczną i wykorzystują ją w swoim fachu. Zdolności te mogły prześladować cię od "
    "dzieciństwa, ujawniając pełnię potencjału dopiero pod wpływem trudów życia poszukiwacza przygód. Możliwe też, "
    "że należysz do zakonu adeptów psioniki i przez lata uczysz się przejawiać swoją moc."
)
UID_OVERRIDES["h05d7703fg52a0gdeefgd5b6g6d58a2ca1db4"] = (
    "Warunek: Gnom\n\nTwój lud słynie ze sprytu i talentu do magii iluzji. Znasz magiczną sztuczkę pozwalającą "
    "zniknąć, gdy spotka cię krzywda.\n\nNatychmiast po otrzymaniu obrażeń możesz użyć reakcji, aby magicznie "
    "zyskać niewidzialność do końca swojej następnej tury albo do chwili, gdy zaatakujesz, zadasz obrażenia lub "
    "zmusisz kogoś do wykonania rzutu obronnego. Po użyciu tej zdolności nie możesz zrobić tego ponownie, dopóki "
    "nie ukończysz krótkiego albo długiego odpoczynku."
)
SPELLFIRE_FLAME_TEXT = (
    "Absorpcja magii. Raz na turę, gdy otrzymujesz obrażenia od czaru albo efektu magicznego, zmniejszasz ich "
    "łączną wartość o 1k4.\n\nPłomień magicznego ognia. Poznajesz sztuczkę Święty płomień. Możesz również "
    "rzucać ją w ramach akcji dodatkowej tyle razy, ile wynosi twoja Premia z biegłości. Wszystkie użycia "
    "odzyskujesz po ukończeniu długiego odpoczynku."
)
for spellfire_uid in (
    "hdefd07e9gac32g3227g03d6g27116876f808",
    "h5b07f997g2114g17b3gd384gcaa505b50750",
):
    UID_OVERRIDES[spellfire_uid] = SPELLFIRE_FLAME_TEXT

RANGED_STEADY_AIM_TEXT = (
    "W ramach akcji dodatkowej możesz zapewnić sobie ułatwienie w teście ataku bronią dystansową w tej turze. "
    "Możesz skorzystać z tej akcji dodatkowej tylko przed wykonaniem ruchu w tej turze. Po jej użyciu twoja "
    "Szybkość wynosi 0 do końca tury."
)
for ranged_steady_uid in (
    "hc67a4df3gcd8bgf957g4d35gee2424c14472",
    "hd4674709g7d30gba4fgad6cg17adc9b95a51",
    "h76568432gfb37gc67cgcb8egf3cebfdfa094",
):
    UID_OVERRIDES[ranged_steady_uid] = RANGED_STEADY_AIM_TEXT
UID_OVERRIDES["h0f8ca247g66e5g6260ga870g3e352f39fa6e"] = (
    "Elfy mają naturalny talent do celnego strzelania z łuku. Dzięki niemal doskonałemu opanowaniu tej sztuki "
    "twoje strzały trafiają z nadzwyczajną precyzją.\n\n" + RANGED_STEADY_AIM_TEXT
)
UID_OVERRIDES["h4e3d30b7g2c20gf8a7gd14eg44eb335e86b5"] = (
    "Szczególnie dobrze walczysz z wrogami naznaczonymi przez ciebie śmiercią. Masz ułatwienie w testach ataku "
    "przeciwko istotom objętym interdyktem."
)
UID_OVERRIDES["h45df701cg39aag071cg66aag602b1d91c8a1"] = (
    "Znasz tajemne schematy służące do tworzenia magicznych przedmiotów.\n\nTworzenie przedmiotu. Po ukończeniu "
    "długiego odpoczynku możesz stworzyć jeden albo dwa różne magiczne przedmioty.\n\nNa 6. i 10. poziomie tej "
    "klasy liczba magicznych przedmiotów, które możesz stworzyć po długim odpoczynku, wzrasta odpowiednio do "
    "trzech i czterech."
)
UID_OVERRIDES["h8fe28200g46b7g051cga5b0ga6bd5b6a5b73"] = (
    "Twój pakt łączy cię z istotą, która przeciwstawia się cyklowi życia i śmierci: potężnym liczem, wampirem albo "
    "inną nieumarłą istotą. Ci pradawni patroni sami byli kiedyś śmiertelnikami, dlatego dobrze znają ścieżki "
    "ambicji i drogi prowadzące przez wrota śmierci. Chętnie dzielą się bluźnierczą wiedzą i innymi tajemnicami z "
    "tymi, którzy wypełniają ich wolę wśród żywych."
)
UID_OVERRIDES["h76260c1cg2fd0ga2b1gf453g7108d2706083"] = (
    "Twój pakt łączy cię ze świadomą magiczną bronią i przeklętymi siłami uwięzionymi w jej ostrzu. Może to być "
    "miecz noszony u boku czarownika albo osławiona broń przechowywana w odległym miejscu, która przenosi swoją moc "
    "przez wieloświat, by realizować przebiegłe plany. Tym, którzy godzą się spełniać jej kaprysy, ten nieodgadniony "
    "patron zapewnia moc nakładania złowrogich klątw, zadawania druzgocących ciosów i wzmacniania swoich dzierżycieli."
)
UID_OVERRIDES["h3504f51eg1ac0gd563g881eg515b53b1f37b"] = (
    "Wybierając tę podklasę, możesz związać się z niewysłowionym bytem z Odległej Dziedziny albo z pradawnym "
    "bogiem — istotą taką jak Tharizdun, Skuty Bóg; Zargon, Powracający; Hadar, Mroczny Głód; lub Wielki Cthulhu. "
    "Możesz też przyzywać moc kilku bytów, nie wiążąc się z żadnym z nich. Motywy tych istot są niepojęte, a Wielki "
    "Przedwieczny może być obojętny wobec twojego istnienia. Poznane sekrety pozwalają ci jednak czerpać od niego "
    "dziwną magię."
)
GIANT_MAGIC_TEXT = (
    "Noszona w tobie pierwotna magia niesie echo potęgi olbrzymów. Raz na turę, gdy trafiasz cel atakiem wręcz "
    "bronią albo atakiem dystansowym bronią miotaną, możesz nasycić atak dodatkowym efektem zależnym od wybranej "
    "korzyści. Możesz użyć tego atutu tyle razy, ile wynosi twoja Premia z biegłości, a wszystkie użycia odzyskujesz "
    "po ukończeniu długiego odpoczynku."
)
UID_OVERRIDES["h603f364eg76f2g4896gd3eeg723e7e1e85a7"] = GIANT_MAGIC_TEXT
UID_OVERRIDES["h928f5df7ga251g34dbg0162g20a1a67d1a84"] = (
    "Noszona w tobie pierwotna magia niesie echo potęgi olbrzymów. Wybierając ten atut, wybierz jedną z poniższych "
    "korzyści. Raz na turę, gdy trafiasz cel atakiem wręcz bronią albo atakiem dystansowym bronią miotaną, możesz "
    "nasycić atak dodatkowym efektem zależnym od wybranej korzyści:"
)
UID_OVERRIDES["hae8c9a5cgf06dg6b71gb093ge2e25716f7d2"] = (
    "Twoja wrodzona magia wywodzi się z najbardziej mglistych i nieprzeniknionych mocy Sfery Cieni albo z innych "
    "krain nadprzyrodzonego mroku. Być może pochodzisz od istoty z takiego miejsca albo przemienia cię złowroga "
    "energia smoka cienia. Twoja cienista magia pozwala ci władać ciemnością, nieumarłością i niedolą."
)
BLINK_SURGE_TEXT = (
    "Do końca swojej następnej tury trafiasz na Plan Eteryczny jak pod wpływem czaru Mrugnięcie. Następnie wracasz "
    "na poprzednio zajmowane pole albo, jeśli jest ono zajęte, na najbliższe wolne pole."
)
for blink_uid in (
    "haecbe11fg6d60g47e2gb1a2g08f0d2c311f2",
    "hbaae27bag3d21g4b92g824egab934089bcc0",
    "hfd23c057g13d1g4881g84e9g8f3ccd39b79e",
    "hb601c55dgad62g404eg95eeg2d21a1b38165",
):
    UID_OVERRIDES[blink_uid] = BLINK_SURGE_TEXT
UID_OVERRIDES["h112fb3e9g734ag7e2dg4366g1a44c9038a26"] = (
    "W tej turze darmowy atak drugą ręką wynikający z Nacięcia został już wykorzystany i nie możesz wykonać kolejnego."
)
UID_OVERRIDES["ha614b061ga252gec97g0245gecd6aee49796"] = (
    "Gdy rzucasz czar o czasie rzucania równym akcji, możesz wydać 2 punkty zaklinania, aby przy tym użyciu zmienić "
    "czas rzucania na akcję dodatkową. Nie możesz w ten sposób zmodyfikować czaru po rzuceniu w tej turze czaru "
    "poziomu 1 lub wyższego. Po takiej modyfikacji nie możesz też rzucić w tej turze czaru poziomu 1 lub wyższego."
)
SEEKING_SPELL_TEXT = (
    "Jeśli wykonujesz test ataku czarem i chybiasz, możesz wydać 1 punkt zaklinania, aby przerzucić k20; musisz "
    "wykorzystać nowy wynik.\n\nMożesz użyć Naprowadzanego czaru nawet wtedy, gdy podczas rzucania tego czaru "
    "wykorzystujesz już inną opcję metamagii."
)
for seeking_uid in (
    "h4350095ege773ga624g7919g62f04bb30b95",
    "h28f9a741ga446ga31eg8889g3b0e1ddcb286",
):
    UID_OVERRIDES[seeking_uid] = SEEKING_SPELL_TEXT
UID_OVERRIDES["hf2c58c13g34f2g4e5eg89a5gf8e830952d02"] = (
    "Pakt Księgi: Poznajesz wybraną sztuczkę."
)
UID_OVERRIDES["hd12a19f5g37feg4c67g90c2g675801f2f329"] = (
    "Pakt Księgi: Poznajesz trzy sztuczki. Dobry wybór."
)
UID_OVERRIDES["h62e16743gcb72g9068gb2d0gb1a62ea9d321"] = (
    "Potrafisz czerpać moc ze Sfery Cieni, dzięki czemu zyskujesz następujące korzyści.\n\nCiemność. Możesz wydać "
    "1 punkt skupienia, aby rzucić czar Ciemność bez komponentów. Gdy rzucasz go za pomocą tej cechy, widzisz w "
    "jego obszarze. Dopóki czar trwa, na początku każdej swojej tury możesz przenieść jego obszar na wybrane pole "
    "w promieniu [1] od siebie.\nWidzenie w ciemności. Zyskujesz widzenie w ciemności o zasięgu [1]. Jeśli już je "
    "masz, jego zasięg zwiększa się o 18 m.\n\nCieniste mamidła. Znasz czar "
    '<LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">Pomniejsza iluzja</LSTag>. Mądrość jest twoją '
    "cechą bazową do tego czaru."
)
UID_OVERRIDES["h761a2d1bgfaa4g6c2fgbda3g198675b6a886"] = (
    "Mistrzostwo w sztuce zastawiania przerażających zasadzek zapewnia ci następujące korzyści.\n\nZryw z "
    "zasadzki. Na początku pierwszej tury każdej walki twoja Szybkość zwiększa się o [1] do końca tej tury.\n\n"
    "Przerażające uderzenie. Gdy trafiasz istotę atakiem bronią, możesz zadać jej dodatkowe [2]. Z tej korzyści "
    "możesz skorzystać tylko raz na turę i tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz). "
    "Wszystkie użycia odzyskujesz po ukończeniu długiego odpoczynku.\n\nPremia do inicjatywy. Gdy wykonujesz rzut "
    "na inicjatywę, możesz dodać do niego swój modyfikator Mądrości."
)
UID_OVERRIDES["hd5715a4dge184g890agee7ag4f904fb90c6b"] = (
    "Znasz sekrety rozmaitych tradycji magicznych. Za każdym razem, gdy osiągasz poziom barda — w tym również ten "
    "poziom — i zwiększa się wartość w kolumnie Przygotowane czary w tabeli cech barda, możesz wybrać dowolne nowe "
    "przygotowane czary z list czarów barda, kleryka, druida i maga. Wybrane czary są dla ciebie czarami barda "
    "(listę czarów każdej klasy znajdziesz w jej opisie). Ponadto za każdym razem, gdy zastępujesz czar przygotowany "
    "dla tej klasy, możesz zastąpić go czarem z jednej z tych list."
)
TWO_WEAPON_FIGHTING_TEXT = (
    'Możesz korzystać z walki dwiema broniami, nawet jeśli twoje bronie nie mają właściwości '
    '<LSTag Tooltip="Light">Lekka</LSTag>. Nie możesz walczyć dwiema '
    'broniami <LSTag Tooltip="TwoHanded">Dwuręcznymi</LSTag>.<br><br>Gdy w swojej turze wykonujesz akcję Ataku i '
    "atakujesz bronią do walki wręcz, możesz później w tej samej turze wykonać jeden atak drugą ręką w ramach "
    "akcji dodatkowej. Jeśli masz mistrzostwo we właściwości Nacięcie i trzymasz w drugiej ręce broń z tą "
    "właściwością, możesz wykonać do dwóch ataków drugą ręką na turę."
)
for two_weapon_uid in (
    "h2d809685g28ffge26ag3e6ag5fa20f63c9e3",
    "h91a9a031gbb78g3004g2f6cg6dcdb8f2cea3",
):
    UID_OVERRIDES[two_weapon_uid] = TWO_WEAPON_FIGHTING_TEXT
UID_OVERRIDES["hdcc3a388gb292gacb2gf7d4gedf14ac8aeed"] = (
    "Obca siła oplotła twój umysł swoimi mackami, obdarzając cię mocą psioniczną. Teraz możesz dotykać innych "
    "umysłów tą mocą i kształtować świat wokół siebie. Czy ta moc rozbłyśnie w tobie jako latarnia nadziei dla "
    "innych? A może staniesz się postrachem tych, którzy poczują ukłucie twojego umysłu?\n\nByć może psychiczny "
    "wiatr z Planu Astralnego przyniósł ci energię psioniczną albo dotknął cię wypaczający wpływ Odległej "
    "Dziedziny. Możliwe też, że w twoim ciele umieszczono kijankę łupieżcy umysłów, lecz przemiana nigdy się nie "
    "dokonała — teraz jej moc psioniczna należy do ciebie. Niezależnie od źródła tej mocy twój umysł nią płonie."
)
UID_OVERRIDES["h0e929a83g6124gede3gd6d6g810f31fc91bf"] = (
    "Rycerze runiczni rozwijają swoje umiejętności bojowe za pomocą nadprzyrodzonej mocy run — pradawnej praktyki "
    "zapoczątkowanej przez olbrzymy. Rytowników run można spotkać wśród wszystkich rodów olbrzymów, a twoje metody "
    "najpewniej pochodzą bezpośrednio albo pośrednio od takiego mistycznego rzemieślnika. Być może odnajdujesz "
    "dzieło olbrzyma wyryte na wzgórzu lub w jaskini, poznajesz runy dzięki mędrcowi albo spotykasz olbrzyma "
    "osobiście. Niezależnie od drogi zgłębiasz rzemiosło olbrzymów i uczysz się nakładać magiczne runy, aby "
    "wzmacniać swój ekwipunek."
)
UID_OVERRIDES["ha8eaee0fg754dg1d66g293cgf44cc84312b0"] = (
    "Zyskujesz zdolność karania istot mocą Piekła. Raz w swojej turze możesz nałożyć magiczną pieczęć na istotę w "
    "promieniu 9 m od siebie. Możesz zrobić to po trafieniu celu atakiem bronią (bez wydawania akcji) albo w ramach "
    "akcji dodatkowej nałożyć pieczęć na widoczny cel w zasięgu. Pieczęć trwa do chwili spalenia. Istotę noszącą "
    "co najmniej jedną twoją pieczęć nazywa się istotą objętą interdyktem.\n\nPrzed odpoczynkiem możesz nałożyć "
    "ograniczoną liczbę pieczęci, a wszystkie zużyte pieczęcie odzyskujesz po ukończeniu krótkiego albo długiego "
    "odpoczynku. Możesz mieć maksymalnie trzy pieczęcie na 1. poziomie, cztery na 3. poziomie i pięć na 7. "
    "poziomie.\n\nJeśli istota objęta interdyktem ginie, odzyskujesz wszystkie nałożone na nią pieczęcie. Możesz "
    "ponownie nakładać je na nowe cele, pojedynczo i na zwykłych zasadach."
)
SHAPECHANGER_TEXT = (
    "W ramach akcji możesz zmienić postać, modyfikując swój wygląd i głos. Samodzielnie określasz szczegóły zmian, "
    "w tym ubarwienie, długość włosów i płeć. Możesz także dostosować wzrost i wagę oraz zmieniać rozmiar między "
    "Średnim a Małym. Możesz upodobnić się do przedstawiciela innego grywalnego gatunku, lecz żadne twoje "
    "parametry gry się nie zmieniają. Nie możesz odtworzyć wyglądu osoby, której wyglądu nie znasz, i musisz "
    "przyjąć formę o tym samym podstawowym układzie kończyn. Cecha nie zmienia twojego ubioru ani "
    "wyposażenia.\n\nPodczas tej przemiany masz ułatwienie w testach Charyzmy.\n\nNowa forma utrzymuje się, dopóki "
    "w ramach akcji nie powrócisz do swojej prawdziwej postaci."
)
for shapechanger_uid in (
    "h842fd89bg0642gf761gc3e7ga95824e9c738",
    "haddbec72gf9c4g510bg8c8cgba4bcfd87301",
):
    UID_OVERRIDES[shapechanger_uid] = SHAPECHANGER_TEXT
UID_OVERRIDES["hd51ae331gb1a0gb3bfg9c3bg17441135a4c2"] = (
    "Wybierz jedną z poniższych opcji cechy. Po każdym krótkim albo długim odpoczynku możesz zastąpić wybraną "
    "opcję drugą.\n\nPogromca kolosów\nTwoja wytrwałość może osłabić nawet najbardziej odpornych wrogów. Gdy "
    "trafiasz istotę bronią, zadajesz jej dodatkowe 1k8 obrażeń, jeśli utraciła choć 1 punkt wytrzymałości. Te "
    "dodatkowe obrażenia możesz zadać tylko raz na turę.\n\nŁamacz hordy\nRaz w każdej swojej turze, gdy wykonujesz "
    "atak bronią, możesz wykonać jeszcze jeden atak tą samą bronią przeciwko innej istocie, która znajduje się "
    "w promieniu 1,5 m od pierwotnego celu i w zasięgu broni oraz nie była jeszcze celem twojego ataku w tej turze."
)
UID_OVERRIDES["h5039598cg6db2g2d04g6e52gb5d4956c7773"] = (
    "Atut: Twardziel\n\nDzicz jest twoim domem, a przetrwanie z dala od wygód cywilizacji — codziennością. "
    "Pokonywanie niezwykłych zagrożeń dzikich ostępów zwiększa twoją sprawność i poszerza wiedzę."
)
UID_OVERRIDES["h15dc29ceg8c9cg6290g5aa9gcfb5242e5617"] = (
    "Atut: Twardziel\n\nBliskość ziemi kształtuje cię od najmłodszych lat. Opieka nad zwierzętami i uprawa "
    "roli dają ci cierpliwość oraz dobre zdrowie. Doceniasz hojność natury, ale darzysz też zdrowym szacunkiem jej "
    "gniew."
)
UID_OVERRIDES["h49166a1eg4322g9138gf1d7g4a5a791dc1d6"] = (
    "Atut: Wtajemniczony (druid)\n\nDojrzewasz pod gołym niebem, z dala od osiadłych krain. Domem jest dla ciebie "
    "każde miejsce, w którym da się rozłożyć posłanie. Dzicz kryje cuda — osobliwe potwory, nieskalane lasy i "
    "strumienie oraz porośnięte ruiny wielkich sal, po których niegdyś stąpały olbrzymy. Podczas ich odkrywania "
    "uczysz się samodzielności. Od czasu do czasu służysz za przewodnika przyjaznym kapłanom natury, którzy "
    "przekazują ci podstawy posługiwania się magią dziczy."
)
UID_OVERRIDES["ha5ec425bg430dg6de7ge56ag7b5f719afc8e"] = (
    "Atut: Uzdrowiciel\n\nWczesne lata upływają ci w odosobnionej chatce albo klasztorze, daleko poza "
    "obrzeżami najbliższej osady. Towarzyszą ci głównie leśne istoty oraz nieliczni goście przynoszący zapasy i "
    "wieści ze świata. Samotność daje wiele czasu na rozważanie tajemnic stworzenia."
)
UID_OVERRIDES["h1de6d67bgeb49gcb85gfb65g06babeedf8df"] = (
    "Atut: Szczęściarz\n\nNauka u handlarza, mistrza karawany albo sklepikarza pozwala ci poznać podstawy "
    "handlu. Podróżujesz szeroko i zarabiasz na kupnie oraz sprzedaży surowców potrzebnych rzemieślnikom lub "
    "gotowych wyrobów. Być może przewozisz towary statkiem, wozem albo karawaną, a może kupujesz je od wędrownych "
    "kupców i sprzedajesz we własnym sklepie."
)
UID_OVERRIDES["h7187b090g05a9g4c6fgefa0g22b1e8de0294"] = (
    "Atut: Zabijaka\n\nMorze jest twoim żywiołem — wiatr wieje w plecy, a pokład kołysze się pod stopami. "
    "Znasz stołki barowe w niezliczonych portach, potężne sztormy i opowieści wymieniane z ludem mieszkającym pod "
    "falami."
)
UID_OVERRIDES["h196d3642g2b8eg0c5ag525dg06fde33550c2"] = (
    "Atut: Uzdolniony\n\nLata kształcenia w skryptorium, klasztorze strzegącym wiedzy albo urzędzie uczą cię "
    "wyraźnego pisma i starannego tworzenia tekstów. Być może sporządzasz dokumenty państwowe lub przepisujesz "
    "dzieła literackie. Możesz też mieć talent do poezji, prozy albo pracy naukowej. Przede wszystkim cechuje cię "
    "dbałość o szczegóły, dzięki której unikasz błędów w przepisywanych i tworzonych dokumentach."
)
UID_OVERRIDES["h906ec4f3gc82ag542bgde14g6bc7078122ad"] = (
    "Atut: Szczęściarz\n\nUlica jest twoim domem, a otaczają cię równie nieszczęśni wyrzutkowie — jedni są "
    "przyjaciółmi, inni rywalami. Śpisz, gdzie się da, i podejmujesz dorywcze prace za jedzenie. Gdy głód staje się "
    "nie do zniesienia, czasem uciekasz się do kradzieży. Mimo to zachowujesz dumę i nadzieję. Los jeszcze z tobą "
    "nie skończył."
)
UID_OVERRIDES["he504b2a7g6a08gdabfgb8a9g1df72a68f86c"] = (
    "Atut: Uzdolniony\n\nChoć większość młodzieży w Chondath odbywa czteroletnią obowiązkową służbę "
    "wojskową, sprzeciwiasz się tej autorytarnej próbie kontroli nad twoim życiem. Odrzucasz obywatelstwo i nadane "
    "imię, po czym dołączasz jako korsarz do pierwszego statku, który przyjmuje cię na pokład. Od tamtej pory "
    "przemierzasz Przesmyk Vilhon. Rzadko oddalasz się od lądu o więcej niż kilkadziesiąt lig, lecz nadrabiasz to "
    "rozległymi miejscowymi kontaktami i bogactwem doświadczeń."
)
UID_OVERRIDES["h0026be6dg10c9g0f95gcab2g7474991939fb"] = (
    "Atut: Uzdrowiciel\n\nStrefy martwej magii na pustyni Anauroch są przekleństwem dla czarujących i "
    "potworów zależnych od magii — właśnie dlatego Anauroch staje się twoim domem. Być może uciekasz przed "
    "Czerwonymi Magami albo popadasz w konflikt z potężnym dżinnem w Calimshanie. Niezależnie od przyczyny życie "
    "na pustyni okazuje się najlepszym wyjściem. Po wielu miesiącach lub latach masz więcej siły i mądrości oraz "
    "ciężko zdobytą wiedzę o pustynnej medycynie i przetrwaniu na pustkowiach."
)
UID_OVERRIDES["h9ce67cb6ga5b0ga13bg7785g0b5aae8510f3"] = (
    "Atut: Nowicjusz Kultu Smoka\n\nNależysz do nowicjuszy Kultu Smoka. Trafiasz do komórki kultu i wykazujesz "
    "cenione przez smoczych kultystów cechy: dwulicowość, dyskrecję i determinację. W zamian za przysięgę służby "
    "kult zapewnia ci towarzystwo innych czcicieli smoków oraz dostęp do zasobów pomocnych w zgłębianiu wiedzy "
    "tajemnej i okultyzmu.\n\nSmocza groza. W ramach akcji Magii możesz napełnić grozą widoczną istotę w promieniu "
    "9 m od siebie. Cel musi wykonać udany rzut obronny na Mądrość albo otrzymuje stan Przerażenia do końca twojej "
    "następnej tury.\n\nNatchnienie strachem. Gdy sprawiasz, że istota otrzymuje stan Przerażenia, a ty jesteś "
    "źródłem jej strachu, zyskujesz heroiczną inspirację. Po użyciu tej korzyści nie możesz zrobić tego ponownie, "
    "dopóki nie ukończysz krótkiego albo długiego odpoczynku."
)
UID_OVERRIDES["h3ab69a8agd42agbda7g29dbgb432d976003a"] = (
    "Atut: Pisklę Szmaragdowej Enklawy\n\nW Szmaragdowej Enklawie troszczysz się o tych, którzy dbają o "
    "świat. Wraz z innymi członkami Enklawy albo na własną rękę zdobywasz umiejętności niezbędne do życia w zgodzie "
    "z naturą: tropienie zwierzyny, odnajdywanie przydatnych ziół, a nawet przewidywanie pogody. Wykorzystujesz te "
    "talenty, aby zachować równowagę między cywilizacją a dziczą oraz oczyszczać świat z wynaturzonych "
    "istot.\n\nRozmawianie ze zwierzętami. Zawsze masz przygotowany czar Rozmawianie ze zwierzętami i możesz "
    "rzucać go, zużywając dowolną posiadaną komórkę czaru.\n\nZgrany zespół. Gdy wykonujesz akcję Pomocy, możesz w "
    "ramach tej samej akcji zamienić się miejscami z chętnym sojusznikiem w promieniu 1,5 m od siebie. Ten ruch nie "
    "prowokuje ataków okazyjnych."
)
UID_OVERRIDES["he09a0c77g31aeg7362g892bg7bdd827aa73e"] = (
    "Atut: Twardziel\n\nGłówną formacją strzegącą prawa we Wrotach Baldura jest Płonąca Pięść — potężna "
    "gildia najemników dowodzona przez wielkiego księcia miasta. Masz za sobą służbę w jej szeregach, która uczy "
    "cię uprzedzać kłopoty groźnym spojrzeniem, a w razie potrzeby przyjmować śmiertelne ciosy. Czynni i emerytowani "
    "najemnicy Płonącej Pięści uchodzą za jednych z najtwardszych i najbardziej wytrzymałych wojowników Wybrzeża "
    "Mieczy, a ty zamierzasz podtrzymać tę reputację."
)
UID_OVERRIDES["h44bec492ga13fg76e5gfab8g3f1ba78481ca"] = (
    "Atut: Wtajemniczony (mag)\n\nChoć dżiny nie rządzą już Calimshanem, ich magia nadal jest powszechna w "
    "twojej ojczyźnie. Być może przypadkowo przywołujesz dżinna z magicznej lampy albo trafiasz do oazy strzeżonej "
    "przez marida. Dao może ocalić cię przed osuwiskiem, a efreeti — zaoferować ulotne bogactwo w zamian za układ. "
    "Niezależnie od tego, jak twój los splata się z losem dżina, doświadczenie obdarza cię bystrym okiem, srebrnym "
    "językiem i niemałą dozą magii."
)
UID_OVERRIDES["he00a4a5dg14ebg9a5cg87e7ga940f48f405e"] = (
    "Atut: Agent Harfiarzy\n\nDołączasz do Harfiarzy i składasz przysięgę przestrzegania ich kodeksu oraz "
    "służby wspólnemu dobru. Jak wszyscy Harfiarze rozumiesz wartość pracy zespołowej, ale wiesz też, kiedy lepiej "
    "działać w pojedynkę. Weterani przekazują ci sekrety bractwa — magiczne melodie, specjalne hasła i sztuczki "
    "zręcznych dłoni — oraz powierzają tę wiedzę, aby za jej pomocą śledzić i osłabiać siły zła.\n\nSzkolenie z "
    "instrumentów. Zyskujesz biegłość w posługiwaniu się instrumentami muzycznymi.\n\nRozpraszająca melodia. Gdy "
    "wykonujesz akcję Rozproszenia, aby wspomóc test ataku sojusznika, rozpraszany wróg może znajdować się w "
    "promieniu 9 m zamiast 1,5 m od ciebie, pod warunkiem że cię widzi albo słyszy."
)
UID_OVERRIDES["h0326e7b1g8c73g586agce87gedf968fe63ea"] = (
    "Atut: Czujność\n\nPochodzisz z dumnego rodu rybaków łowiących pod lodem w Dziesięciu Miastach Doliny "
    "Lodowego Wichru. Połów pstrąga pięściogłowego nie należy do najbardziej chwalebnych zajęć Północy, ale "
    "zapewnia uczciwe życie. Twoje zmysły są wyczulone na najlżejsze szarpnięcie żyłki, ramiona — zahartowane "
    "zmaganiami z wielkimi pstrągami pod lodem, a wprawa w patroszeniu wystarcza, by wielokrotnie wykarmić całą "
    "wioskę. Te doświadczenia przygotowują twoje ciało i umysł do życia pełnego przygód.\n\nRamię w ramię. Gdy "
    "sojusznik w promieniu 1,5 m od ciebie podlega efektowi, który miałby go odepchnąć albo przyciągnąć, możesz w "
    "ramach reakcji temu zapobiec. Sojusznik nie może mieć stanu Obezwładnienia."
)
UID_OVERRIDES["hfabda183g7436g881egc8e9gf6ec8a6a8cb3"] = (
    "Atut: Agent Sojuszu Lordów\n\nTwoja wierność należy do jednego z miast Sojuszu Lordów. Jako agent Sojuszu "
    "musisz przestrzegać jego zasad oraz działać na rzecz bezpieczeństwa i dobrobytu Wybrzeża Mieczy. Masz "
    "przynosić honor i chwałę rodowi swego pana — czy to zabezpieczając szlaki handlowe dla kupieckiego lorda z "
    "Waterdeep, czy zgładzając potwory grasujące w górnym biegu rzeki od Daggerfordu. Szkolenie w walce mieczem i "
    "sztuce rządzenia sprawia, że równie sprawnie posługujesz się ostrzem, co piórem.\n\nInspirujące uderzenie. Raz "
    "na turę, gdy zadajesz istocie trafienie krytyczne, zyskujesz heroiczną inspirację.\n\nPrzywrócenie honoru. "
    "Gdy widoczny wróg zadaje ci obrażenia, masz ułatwienie w następnym teście ataku przeciwko niemu wykonanym przed "
    "końcem swojej następnej tury."
)
UID_OVERRIDES["h38b188b6g2fc2g8138g725agd0f6fbca254c"] = (
    "Atut: Wtajemniczony (druid)\n\nJak wielu mieszkańców Wysp Moonshae, od najmłodszych lat czcisz "
    "błogosławioną ziemię, jej wyjątkowe bóstwa i tajemnicze sanktuaria zwane księżycowymi studniami. Jako pielgrzym "
    "podejmujesz wyprawę, by odwiedzić każdą z nich — zarówno zaznaczoną na mapie, jak i nieznaną kartografom — i "
    "nawiązać z nią duchową więź. Podczas sielankowych wędrówek gromadzisz repertuar ludowych pieśni Moonshae, "
    "malujesz urzekające krajobrazy i uczysz się władać odrobiną pierwotnej magii."
)
UID_OVERRIDES["h96aa51dag6fb2gf3a9g321fged3d699fde79"] = (
    "Atut: Szczęściarz\n\nDorastasz w krainie żyjących boskich królów, słuchając niezliczonych opowieści o "
    "starożytnych imperiach i pogrzebanych miastach. Według nich Mulhorand przepełniają zapomniane bogactwa — "
    "bezcenne skarby czekające na każdego, kto ma dość sprytu i odwagi, by ich szukać. Podejmujesz się eksploracji "
    "krypt, grobowców i piramid swojej ojczyzny, aby odzyskać relikty własnego ludu."
)
UID_OVERRIDES["h07cec1a0g7220ge9ebg9676gffd755fa50d0"] = (
    "Atut: Rekrut Purpurowego Smoka\n\nPoświęcasz życie bezpieczeństwu Cormyru i starasz się o przyjęcie do "
    "elitarnego zakonu wojowników tego królestwa — Rycerzy Purpurowego Smoka. Zanim jednak oficjalnie dołączysz do "
    "ich szeregów, musisz służyć jako giermek. Udaje ci się znaleźć seniora gotowego przyjąć cię na służbę i "
    "nauczyć zwyczajów zakonu. Czy dochowasz ideałów Rycerzy Purpurowego Smoka — chwały, honoru i siły — oraz "
    "dowiedziesz, że zasługujesz na pasowanie?\n\nProśba. Zyskujesz biegłość w "
    '<LSTag Type="Skills" Tooltip="Persuasion">Perswazji</LSTag>.\n\nOkrzyk bojowy. Możesz wybrać tyle '
    "widocznych istot w promieniu 9 m od siebie, ile wynosi twoja Premia z biegłości. Wybrane istoty zyskują "
    "heroiczną inspirację. Po użyciu tej korzyści nie możesz zrobić tego ponownie, dopóki nie ukończysz długiego "
    "odpoczynku."
)
UID_OVERRIDES["h75277cafgfc31g7483g2ad8gfd91011a85cc"] = (
    "Atut: Twardziel\n\nLata wędrówki po wyżynach Rashemenu hartują cię na niebezpiecznych, smaganych "
    "wiatrem wrzosowiskach. Stoją tam starożytne obeliski zaklęte tak, by więzić czarty, a okolicę zamieszkują smoki, "
    "gnolle i inne śmiercionośne istoty. W tak odizolowanej krainie trudno o przyjaźń, dlatego uczysz się trzymać "
    "obcych na dystans."
)
UID_OVERRIDES["he15395feg34cbgfdbbgc738g75da56bca5d6"] = (
    "Atut: Brutalny napastnik\n\nCałe życie poświęcasz przygotowaniom do wstąpienia w szeregi Mistrzów Cienia — "
    "tajemniczej gildii złodziei, która zza kulis kontroluje Thesk. Skradanie się i szybki refleks stanowią jedynie "
    "początek szkolenia; musisz również wyostrzyć swoją bezwzględność, by chronić sekrety gildii. Jeden błędny ruch "
    "prowadzi jednak do wygnania z zakonu. Teraz musisz podążać własną ścieżką."
)
UID_OVERRIDES["he8c36bc0g70c8g1d48g6d88g25469ebb3fda"] = (
    "Atut: Iskra magicznego ognia\n\nNosisz dar magicznego ognia — rzadkiej formy magii, która przewodzi surową "
    "moc Splotu. Władanie nim mocno obciąża ciało, dlatego hartujesz zarówno umysł, jak i ciało, aby skutecznie "
    "posługiwać się tą świętą mocą.\n\nAbsorpcja magii. Raz na turę, gdy otrzymujesz obrażenia od czaru albo efektu "
    "magicznego, zmniejszasz ich łączną wartość o 1k4.\n\nPłomień magicznego ognia. Poznajesz sztuczkę Święty "
    "płomień. Możesz również rzucać ją w ramach akcji dodatkowej tyle razy, ile wynosi twoja Premia z biegłości. "
    "Wszystkie użycia odzyskujesz po ukończeniu długiego odpoczynku."
)
UID_OVERRIDES["hdeab958dge913gf95bg123dg27338a365d6d"] = (
    "Atut: Oprych Zhentarimów\n\nMoże chodzi o pieniądze. Może o tęsknotę za rodziną, choćby najbardziej "
    "podejrzaną. A może po prostu potrafisz doprowadzić robotę do końca wszelkimi niezbędnymi środkami. Bez względu "
    "na powód dołączasz do Zhentarimów, najbardziej osławionej gildii najemników w Krainach. Choć jej przywódcy "
    "twierdzą, że organizacja bardziej przypomina rodzinę niż tajny syndykat, niewiele rodzin dorównuje jej pod "
    "względem nieuczciwości, nepotyzmu i korupcji. Doskonalisz spryt, refleks i władanie ostrzem, aby piąć się w "
    "szeregach gildii.\n\nWykorzystanie luki. Gdy wykonujesz rzut obrażeń ataku okazyjnego, możesz rzucić kośćmi "
    "obrażeń dwukrotnie i wybrać jeden z wyników.\n\nRodzina przede wszystkim. Raz na długi odpoczynek zapewniasz "
    "sobie i sojusznikom w promieniu 9 m ułatwienie w rzutach na inicjatywę."
)
UID_OVERRIDES["h7d405f4ag1770gee29gfd7egc0479b1be286"] = (
    "Atut: Strażnik grobu\n\nW miejscu położonym bliżej krainy umarłych niż żywych, osoby dbające o wieczny "
    "spoczynek zmarłych budzą zarówno głęboki szacunek, jak i niepokój. Znasz fach grabarza, przedsiębiorcy "
    "pogrzebowego i balsamisty. Niekiedy tylko ty znajdujesz życzliwe słowo, aby uczcić pamięć zmarłych. Dobrze "
    "znasz spustoszenie czynione przez nieumarłych i nie pozwalasz im zakłócać spoczynku powierzonych ci "
    "ciał.\n\nStrażnik grobu. Zyskujesz jedno użycie zdolności Akt wiary klasy kleryka i możesz za jego pomocą "
    "wywołać efekt Odpędzanie nieumarłych. Jeśli masz już Akt wiary, dodajesz to użycie do tej zdolności z jednej "
    "wybranej klasy."
)
UID_OVERRIDES["h0089c30fg8c4dg346dg41fag7df171fac04f"] = (
    "Atut: Uderzenie olbrzymów\n\nNie należysz do olbrzymów, lecz dorastasz pośród nich. Być może jako sierotę "
    "przygarnia cię życzliwa rodzina kamiennych olbrzymów i wychowuje jak własne dziecko. Możliwe też, że żyjesz w "
    "odciętej od świata prehistorycznej krainie pełnej olbrzymów, przerażających kolosów i potężnych "
    "dinozaurów.\n\nCoś w twoim otoczeniu — pożywienie, woda, magia żywiołów przenikająca dom albo bujne "
    "błogosławieństwo wzrostu — sprawia, że osiągasz niezwykłe rozmiary jak na przedstawiciela swojego gatunku. Ta "
    "magia uczy cię ucieleśniać potęgę olbrzymów. Życie w świecie znacznie większym od ciebie kształtuje twoje "
    "umiejętności, nastawienie i spojrzenie na życie.\n\nUderzenie olbrzymów. Raz na turę, gdy trafiasz cel atakiem "
    "wręcz bronią albo atakiem dystansowym bronią miotaną, możesz nasycić atak dodatkowym efektem zależnym od "
    "wybranej korzyści: chmur, ognia, mrozu, wzgórz, kamienia albo burzy."
)
UID_OVERRIDES["hc84e5f2cg37c3g238bgb1b6g73db07b36581"] = (
    "Obycie z kołysaniem pokładów statków i innych pojazdów zapewnia ci ułatwienie w rzutach obronnych na Siłę i "
    "Zręczność oraz testach tych cech wykonywanych, aby uniknąć odepchnięcia, Powalenia albo innego przemieszczenia "
    "wbrew twojej woli."
)
UID_OVERRIDES["h318d1b8eg0580g3d5cgacf3g81c76726bcd3"] = (
    "Surowe warunki i groźne potwory Północy są ci dobrze znane. Masz odporność na obrażenia od zimna oraz "
    "ułatwienie w testach ataku przeciwko smokom, olbrzymom i istotom Dużym lub większym."
)
UID_OVERRIDES["h97dd1bbcg1ca7g6953g67d7g155182b6526b"] = (
    "Potrafisz zręcznie unikać niektórych niebezpieczeństw. Gdy podlegasz efektowi, który pozwala wykonać rzut "
    "obronny na Zręczność, aby otrzymać tylko połowę obrażeń, przy powodzeniu nie otrzymujesz żadnych obrażeń, a "
    "przy niepowodzeniu — tylko połowę. Nie możesz użyć tej zdolności, jeśli masz stan Obezwładnienia."
)
UID_OVERRIDES["h672e82feg2734g7895ga227gd76ffbfded41"] = (
    'Przyjmij postać olbrzymiego borsuka, który może '
    '<LSTag Type="Spell" Tooltip="Target_Burrow_GiantBadger">zagrzebać się</LSTag> w ziemi.'
)
UID_OVERRIDES["h9f0fbf45g41d6gb607g5104g558e4732b4de"] = (
    'Przyjmij postać olbrzymiego pająka, który może '
    '<LSTag Type="Spell" Tooltip="Target_Web_Spider">usidlać</LSTag> wrogów.'
)
EXACT_OVERRIDES["Giant Stature"] = "Olbrzymia postura"
EXACT_OVERRIDES["Giant Foundling"] = "Wychowanek olbrzymów"
SANCTIFIED_BLADE_TEXT = (
    "Po każdym krótkim odpoczynku możesz odprawić rytuał nad bronią do walki wręcz, w której masz biegłość i która "
    "zadaje obrażenia kłute albo cięte, uświęcając ją. Broń staje się twoim uświęconym ostrzem; jednocześnie możesz "
    "mieć tylko jedno takie ostrze. Zyskuje ono dla ciebie właściwość Finezja, a wykonywane nim ataki przeciwko "
    "aberracjom, czartom i nieumarłym ignorują odporność na obrażenia."
)
UID_OVERRIDES["h1449cbcfg1e78g7153g5e0dg53362829c1a3"] = (
    "Intensywny trening przynosi owoce. Zyskujesz biegłość w broni bojowej i średnim pancerzu.\n\n"
    + SANCTIFIED_BLADE_TEXT
)
UID_OVERRIDES["hb8fdcfc4ga498g2b1cg07dfg1712e7560d44"] = SANCTIFIED_BLADE_TEXT

HUMAN_LORE_TEXT = (
    "Ludzi można spotkać w całym wieloświecie. Są równie różnorodni, co liczni, i starają się osiągnąć jak "
    "najwięcej w ciągu danych im lat. Ich ambicja i zaradność budzą w wielu światach uznanie, szacunek, a czasem "
    "także strach.\n\nLudzie są równie zróżnicowani pod względem wyglądu jak mieszkańcy Ziemi i czczą wielu bogów. "
    "Uczeni spierają się o pochodzenie ludzkości, lecz podobno jedno z najwcześniejszych znanych skupisk ludzi "
    "powstało w Sigil — torusowatym mieście w centrum wieloświata, w którym narodził się język Wspólny. Stamtąd "
    "ludzie mogli rozprzestrzenić się po całym wieloświecie, zabierając ze sobą kosmopolityczny charakter Miasta "
    "Drzwi."
)
for human_lore_uid in (
    "hc3405af3g4811g97c2gc534g546e8726cc0d",
    "hf3d6ddebg352bg36d4g9fbbg9ac02f78c004",
):
    UID_OVERRIDES[human_lore_uid] = HUMAN_LORE_TEXT

UID_OVERRIDES["h23814ae4g55bbg25cbg61a4gcf6756b9d02f"] = (
    "Diabelstwa o chtonicznym dziedzictwie odczuwają nie tylko zew Carceri, lecz także chciwość Gehenny i mrok "
    "Hadesu. Niektóre z nich mają trupią aparycję. Inne odznaczają się nieziemskim pięknem sukkuba albo cechami "
    "fizycznymi nocnej wiedźmy, yugolotha lub innego czarciego przodka o charakterze neutralnym złym."
)
UID_OVERRIDES["h7620f19ag43c9g05a4g36acg0cd45d849578"] = (
    "Krąg Niezłomnych to zakon druidów, którzy odrzucili cierpliwe nauki swoich poprzedników i chwycili za broń "
    "w obronie dziczy. Ci wojowniczy druidzi tworzą oddziały i wykorzystują gniew samej natury, aby siłą "
    "wykorzeniać wszelkie nadciągające zło zagrażające ich świętym krainom.\n\nChoć druidzi ci noszą w sobie "
    "chaos natury, trening i dyscyplina pozwalają im panować nad ciałem i odruchami. Nauki tego kręgu, wywodzącego "
    "się z bezlitosnego Festerwood, są równie surowe jak sam las. Łączą atak z obroną, przygotowując druidów na "
    "wszelkie wyzwania świata."
)
UID_OVERRIDES["he9c252edgc46cg4450gfb88g57508151df65"] = "Poziom 3: Czary Kręgu Niezłomnych"
UID_OVERRIDES["head50b7eg3179gbc89g1334gbee0de9d925c"] = (
    'Więź z Kręgiem Niezłomnych sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu poziomu '
    'druida wskazanego w tabeli Czarów Kręgu Niezłomnych zawsze masz przygotowane wymienione w niej czary: na 3. '
    'poziomie — Pętające uderzenie, Shillelagh, Lśniące ugodzenie i Prawdziwe uderzenie; na 5. poziomie — '
    '<LSTag Type="Spell" Tooltip="Target_Haste">Przyspieszenie</LSTag>; na 7. poziomie — Tarcza ognia; a na 9. '
    'poziomie — Słup ognia.'
)

DRACONIC_FLIGHT_TEXT = (
    "Po osiągnięciu 5. poziomu postaci możesz skupić smoczą magię, aby tymczasowo zyskać zdolność lotu. W ramach "
    "akcji dodatkowej z twoich pleców wyrastają widmowe skrzydła. Utrzymują się przez 10 minut, dopóki ich nie "
    "schowasz (nie wymaga to akcji) albo dopóki nie uzyskasz stanu Obezwładnienia. W tym czasie twoja szybkość lotu "
    "jest równa twojej szybkości. Skrzydła wyglądają, jakby były stworzone z tej samej energii co twoje zionięcie. "
    "Po użyciu tej cechy nie możesz jej użyć ponownie do następnego długiego odpoczynku."
)
for draconic_flight_uid in (
    "h1ad7e3a3g7b2fg4393g4b53g5a1bc9137cbd",
    "ha4935cd2g4e6dg156ag2742g4ff317774e14",
    "h792db4a7g911aga472g7377ge4c0224fc65a",
):
    UID_OVERRIDES[draconic_flight_uid] = DRACONIC_FLIGHT_TEXT

ARMOUR_OF_HEXES_TEXT = (
    "Gdy otrzymujesz obrażenia od celu objętego twoim Urokiem, możesz w ramach reakcji zmniejszyć je o 2k8 plus swój "
    "modyfikator Charyzmy. Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator Charyzmy, a wszystkie "
    "użycia odzyskujesz po długim odpoczynku."
)
for armour_of_hexes_uid in (
    "h49e72c1cg2d7bgc3fbg7e56gdbf9203830ad",
    "h16aa8ef8g9057g8804g10e3g6c754af3589d",
    "hf03aeb95g5dbbg3147g324cg388502cbfe2e",
):
    UID_OVERRIDES[armour_of_hexes_uid] = ARMOUR_OF_HEXES_TEXT

ARCANE_WARD_DAMAGE_TEXT = (
    "Gdy otrzymujesz obrażenia, pochłania je magiczna powłoka. Jeśli masz odporność albo podatność na te obrażenia, "
    "zastosuj ją przed odjęciem obrażeń od punktów wytrzymałości powłoki. Jeśli obrażenia zmniejszą jej punkty "
    "wytrzymałości do 0, otrzymujesz pozostałe obrażenia. Powłoka o 0 punktach wytrzymałości nie może pochłaniać "
    "obrażeń, lecz jej magia pozostaje aktywna."
)
for arcane_ward_damage_uid in (
    "h2a374b86g81f6g7146ga72ag43246ef53813",
    "h9cb11bc4g520dg35a2g4731g7635211c5e76",
    "h9ecd6711g2397g780fgf43bg3fef96b7272b",
):
    UID_OVERRIDES[arcane_ward_damage_uid] = ARCANE_WARD_DAMAGE_TEXT

BATTLE_MEDIC_TEXT = (
    "Medyk bojowy. Możesz przywrócić istocie 1k8 punktów wytrzymałości. Z tej zdolności możesz skorzystać tyle razy, "
    "ile wynosi twoja premia z biegłości, a wszystkie użycia odzyskujesz po długim odpoczynku.\n\nLeczenie. Za "
    "każdym razem, gdy przywracasz istocie punkty wytrzymałości, odzyskuje ona dodatkowe punkty wytrzymałości w "
    "liczbie równej twojej premii z biegłości."
)
for battle_medic_uid in (
    "hb5fed628gc7a2g2040gd0adgb152d0d9aa4a",
    "hf4670cedg622ag16adgd7fbgf472400d198b",
):
    UID_OVERRIDES[battle_medic_uid] = BATTLE_MEDIC_TEXT

ENCOURAGE_ALLY_TEXT = (
    "Pokrzepienie sojusznika. W ramach akcji dodatkowej dodajesz otuchy jednemu widocznemu sojusznikowi w promieniu "
    "9 m. Zyskuje on tymczasowe punkty wytrzymałości w liczbie równej 2k6 plus twoja premia z biegłości. Możesz użyć "
    "tej akcji dodatkowej tyle razy, ile wynosi twoja premia z biegłości, a wszystkie użycia odzyskujesz po długim "
    "odpoczynku.\n\nOstatni bastion. Gdy jesteś Zakrwawiony, masz ułatwienie w testach ataku."
)
for encourage_ally_uid in (
    "hf790b35fg5b7ege376ge7e5gfdcf78fcbf35",
    "h4f5ef875gef6dg93aag6e38g370f1fde0a68",
):
    UID_OVERRIDES[encourage_ally_uid] = ENCOURAGE_ALLY_TEXT

EXACT_OVERRIDES.update({
    "Level 10: Magic Item Adept": "Poziom 10: Znawca magicznych przedmiotów",
    "Ritual Adept": "Adept rytuałów",
    "Level 2: Ritual Adept": "Poziom 2: Adept rytuałów",
    "Eldritch Adept": "Mistyczny adept",
    "Metamagic Adept": "Adept metamagii",
    "Spellfire Adept": "Adept magicznego ognia",
    "Feat: Spellfire Adept": "Atut: Adept magicznego ognia",
    "Feat: Martial Adept": "Atut: Adept sztuk walki",
})

UID_OVERRIDES["h4ad37d2fg7e63g64e1g0db3g45844045ca7d"] = (
    "Użycie Stabilnego celowania nie zmniejsza twojej szybkości do 0."
)
RAGE_TEMPORARY_HIT_POINTS_TEXT = (
    'Gdy aktywujesz <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, zyskujesz tymczasowe punkty '
    'wytrzymałości w liczbie równej twojemu poziomowi barbarzyńcy.'
)
for rage_temporary_hit_points_uid in (
    "hcc3ad546g16bcgfa68g23a7g1b2b0bcd4801",
    "hde63b209g1d1dg2fb9gf3abg0f84f42a69f8",
):
    UID_OVERRIDES[rage_temporary_hit_points_uid] = RAGE_TEMPORARY_HIT_POINTS_TEXT

RAGE_SAVING_THROW_BONUS_TEXT = (
    'Gdy trwa twój <LSTag Type="Status" Tooltip="RAGE">szał</LSTag>, do rzutów obronnych dodajesz premię równą '
    'premii do obrażeń od <LSTag Type="Status" Tooltip="RAGE">szału</LSTag>.'
)
for rage_saving_throw_bonus_uid in (
    "h9416ea15g9b17g07abg6c06gd6905fe706ed",
    "he4612c48gfd84gd95cg77b9g94667cfad8a4",
):
    UID_OVERRIDES[rage_saving_throw_bonus_uid] = RAGE_SAVING_THROW_BONUS_TEXT

UID_OVERRIDES["h624efb18g8179g6ce0gbe0fg03d310683b76"] = (
    "Twoje bitewne umiejętności (a może po prostu szczęście?) rosną wraz z doświadczeniem.\n\nZyskujesz premię "
    "+1 do KP. Tracisz ją, jeśli masz stan Obezwładnienia albo dzierżysz tarczę."
)
UID_OVERRIDES["h74ec9648ga223g71b5g6f79gcbbc5f6ca2bb"] = (
    "Rosnące mistrzostwo w nasycaniu przedmiotów i magicznym rzemiośle powiększa twój zasób magicznej mocy. "
    "Zyskujesz po jednej dodatkowej komórce czaru 1., 2. i 3. poziomu. Te dodatkowe komórki odzwierciedlają większą "
    "wydajność i stabilność, z jaką przekazujesz magię swoim dziełom."
)
UID_OVERRIDES["hcf7da3ddg6f1bg143bg1d62g96bcb0b5bf29"] = (
    "Testy ataku bronią i ataku bez broni kończą się trafieniem krytycznym przy wyniku 19 albo 20 na k20."
)
UID_OVERRIDES["h4d2eb6abgde1bg02e5g7229g271d5c3cc35b"] = (
    "Twoja skóra nabiera delikatnego, lodowego, krystalicznego blasku. Maksymalna liczba twoich punktów wytrzymałości "
    "zwiększa się o 3 oraz o kolejne 1 za każdym razem, gdy zyskujesz poziom zaklinacza. Ponadto trudny teren z lodu "
    "albo śniegu nie wymaga od ciebie dodatkowego ruchu, a podczas chodzenia po lodzie przemieszczasz się dwukrotnie "
    "dalej przy tym samym wydatku ruchu."
)
UID_OVERRIDES["hf664a7b1g2fffg549cgf62dgbca83b181e57"] = (
    "Możesz pożerać szczątki potworów, wywołując w swoim ciele potężne i przerażające mutacje. Możesz spożyć tyle "
    "porcji, ile wynosi 1 plus twój modyfikator Inteligencji (co najmniej jedną). Wszystkie użycia tej zdolności "
    "odzyskujesz po długim odpoczynku. Możesz jednocześnie czerpać korzyści z kilku porcji, ale nie możesz uzyskać "
    "tej samej mutacji więcej niż raz w tym samym czasie."
)

LIFE_GIVING_FORCE_TEXT = (
    'Na początku każdej swojej tury podczas <LSTag Type="Status" Tooltip="RAGE">szału</LSTag> możesz wybrać inną '
    'istotę w promieniu 3 m od siebie, aby zyskała tymczasowe punkty wytrzymałości. Rzuć tyloma k6, ile wynosi twoja '
    'premia do obrażeń od <LSTag Type="Status" Tooltip="RAGE">szału</LSTag>, i zsumuj wyniki, aby określić ich '
    'liczbę. Niewykorzystane tymczasowe punkty wytrzymałości znikają po zakończeniu szału.'
)
UID_OVERRIDES["h17806188g48eag72daga9fag423961387d39"] = (
    'Twój <LSTag Type="Status" Tooltip="RAGE">szał</LSTag> czerpie z siły życiowej Drzewa Świata. Zyskujesz '
    'następujące korzyści.\n\nPrzypływ witalności. Gdy aktywujesz szał, zyskujesz tymczasowe punkty wytrzymałości '
    'w liczbie równej twojemu poziomowi barbarzyńcy.\n\nŻyciodajna siła. Na początku każdej swojej tury podczas '
    'szału możesz wybrać inną istotę w promieniu 3 m od siebie, aby zyskała tymczasowe punkty wytrzymałości. Rzuć '
    'tyloma k6, ile wynosi twoja premia do obrażeń od <LSTag Type="Status" Tooltip="RAGE">szału</LSTag>, i zsumuj '
    'wyniki, aby określić ich liczbę. Niewykorzystane tymczasowe punkty wytrzymałości znikają po zakończeniu szału.'
)
UID_OVERRIDES["h21000e09gdda6g7a5fg404eg1458b9ccd985"] = LIFE_GIVING_FORCE_TEXT
UID_OVERRIDES["hd109b0dbg19e8ga1d2g4826gc3978e7b2e7f"] = "Obuchowe korzenie: Obalenie"

UID_OVERRIDES["h61388cf8g2c44ge32ege2c8gd43ed94d46c8"] = (
    "Masz talent do taktyki na polu bitwy i poza nim. Możesz zużyć jedno użycie Drugiego oddechu, aby zwiększyć "
    "szanse powodzenia testu cechy. Rzuć 1k10 i dodaj wynik do testu, co może zmienić niepowodzenie w powodzenie."
)
UID_OVERRIDES["h25de2a50g4c8dg2b55gea44gd2074336ba6a"] = "Użycie Drugiego oddechu"
UID_OVERRIDES["h1ef6a3c5gfadagaff9gd6e8gf62d1e802c10"] = (
    "Liczba użyć Drugiego oddechu lub Umysłu taktycznego."
)
SECOND_WIND_MOVEMENT_TEXT = (
    "Gdy w ramach akcji dodatkowej używasz Drugiego oddechu, możesz przemieścić się o maksymalnie połowę swojej "
    "szybkości bez prowokowania ataków okazyjnych."
)
for second_wind_movement_uid in (
    "h34197e5dgf2d4g066fgdb45gb041adb38595",
    "hfd6115a2g072eg747bg10e1gc93f7616eafe",
):
    UID_OVERRIDES[second_wind_movement_uid] = SECOND_WIND_MOVEMENT_TEXT

UID_OVERRIDES["ha8111f35ge4bag28bcg4d99g339262b0a595"] = (
    "Gdy używasz Drugiego oddechu, aby odzyskać punkty wytrzymałości, możesz wybrać w emanacji o promieniu 9 m, "
    "której źródłem jesteś, maksymalnie tylu sojuszników, ile wynosi twój modyfikator Charyzmy. Każdy z nich "
    "odzyskuje punkty wytrzymałości w liczbie równej sumie 1k10 i twojego poziomu wojownika."
)
UID_OVERRIDES["h9e1cff8dg946cga7ccgaeddg5ee4b899b6c6"] = (
    "Gdy używasz Przypływu sił, możesz wybrać w emanacji o promieniu 9 m, której źródłem jesteś, maksymalnie tylu "
    "sojuszników, ile wynosi twój modyfikator Charyzmy. Każdy z nich również zyskuje korzyść z Przypływu sił."
)
UID_OVERRIDES["h6bfa7986g7edeg322fgd99egace84461fcf5"] = (
    "Wybierz w emanacji o promieniu 9 m, której źródłem jesteś, maksymalnie tylu sojuszników, ile wynosi twój "
    "modyfikator Charyzmy. Każdy z nich odzyskuje punkty wytrzymałości w liczbie równej sumie 1k10 i twojego "
    "poziomu wojownika."
)
UID_OVERRIDES["h02149e62gbafbgc9c5g274fg20af94229331"] = (
    "Wybierz w emanacji o promieniu 9 m, której źródłem jesteś, maksymalnie tylu sojuszników, ile wynosi twój "
    "modyfikator Charyzmy. Każdy z nich zyskuje korzyść z twojego Przypływu sił."
)
UID_OVERRIDES["h03df3855gb482gdaf5g11f0gbf6d6d9fbb62"] = (
    "Gdy zmniejszysz punkty wytrzymałości wroga do 0, zyskujesz tymczasowe punkty wytrzymałości w liczbie równej "
    "sumie twojego modyfikatora Charyzmy i poziomu czarownika (co najmniej 1). Zyskujesz tę korzyść również wtedy, "
    "gdy ktoś inny zmniejszy do 0 punkty wytrzymałości wroga znajdującego się w promieniu 3 m od ciebie."
)

UID_OVERRIDES["he20dfbbag75a3gc426g332eg26d5f5687c72"] = (
    "W ramach akcji dodatkowej wybierz jedną widoczną istotę w promieniu 18 m od siebie i zużyj maksymalnie tyle "
    "tych kości, ile wynosi połowa twojego poziomu druida. Rzuć zużytymi kośćmi i zsumuj wyniki. Cel odzyskuje "
    "punkty wytrzymałości w liczbie równej tej sumie. Ponadto za każdą zużytą kość zyskuje 1 tymczasowy punkt "
    "wytrzymałości."
)
RAVENOUS_NEGATIVE_ENERGY_TEXT = (
    "Nasycasz żarłoczną negatywną energią trzymaną broń albo swoje ataki bez broni. Przez czas trwania efektu, gdy "
    "po raz pierwszy w turze trafisz istotę atakiem nasyconą bronią albo atakiem bez broni, cel otrzymuje obrażenia "
    "nekrotyczne równe twojemu modyfikatorowi cechy bazowej czarów. Zyskujesz wtedy tymczasowe punkty wytrzymałości "
    "w liczbie równej zadanym obrażeniom nekrotycznym."
)
for ravenous_negative_energy_uid in (
    "h0f617ea9g5fc5gff42gae8ag41a6861d59c0",
    "h353f6fe0g981eg9ab6gd5b9g0148d8001530",
):
    UID_OVERRIDES[ravenous_negative_energy_uid] = RAVENOUS_NEGATIVE_ENERGY_TEXT

UID_OVERRIDES["h261201bdgf3e1gc0a9g001bg9f21c4b6eb0b"] = (
    'Mag. Znasz jedną dodatkową sztuczkę z listy czarów druida. Ponadto twoja mistyczna więź z naturą zapewnia ci '
    'premię do testów Inteligencji (<LSTag Type="Skills" Tooltip="Arcana">Wiedza Tajemna</LSTag> albo '
    '<LSTag Type="Skills" Tooltip="Nature">Natura</LSTag>). Premia jest równa twojemu modyfikatorowi Mądrości '
    '(co najmniej +1).'
)
UID_OVERRIDES["ha334fba5ge039gfb31g1b15g55b8f07d80f4"] = (
    'Poświęć połowę swoich pozostałych <LSTag Tooltip="HitPoints">punktów wytrzymałości</LSTag>, aby przywrócić '
    'celowi taką samą ich ilość.'
)
UID_OVERRIDES["h6b46b470gc898g44d3g2c4ag944728a674a0"] = (
    "Tworzysz miksturę leczenia. Liczba przywracanych przez nią punktów wytrzymałości zwiększa się po osiągnięciu "
    "5. i 9. poziomu tej klasy."
)
UID_OVERRIDES["h26a9d040g90ffg7098gc158g401ddd420d2e"] = (
    'Podczas swojej tury masz zasięg większy o 3 m, gdy używasz broni do walki wręcz z właściwością Ciężka albo '
    'Wszechstronna, ponieważ wyrastają z ciebie pnącza Drzewa Świata. Gdy w swojej turze trafisz taką bronią, '
    'oprócz używanej właściwości mistrzostwa możesz aktywować również <LSTag Type="Passive" '
    'Tooltip="WeaponMasteryPush">Popchnięcie</LSTag> albo Obalenie.'
)
UID_OVERRIDES["h8756f6c6ga536g0a7agc01agf500547496f2"] = (
    "Dotykasz broni do walki wręcz i nasycasz ją magicznym efektem, tworząc na niej widoczną runę. Trafienie "
    "atakiem nasyconą bronią zadaje dodatkowe 1k8 obrażeń od ognia."
)

CHANGELING_LORE_TEXT = (
    "Odmieńcy o wiecznie zmiennym wyglądzie żyją niezauważeni w wielu społecznościach. Każdy odmieniec może w "
    "nadprzyrodzony sposób przybrać dowolną twarz. Dla niektórych nowa twarz ujawnia aspekt ich duszy.\n\nPierwsi "
    "odmieńcy w wieloświecie pojawili się w Feywild, a cudowna, zmienna esencja tej sfery wciąż jest w nich obecna — "
    "nawet w tych, którzy nigdy nie postawili stopy w krainie fey.\n\nW prawdziwej postaci odmieńcy wyglądają "
    "blado, a ich rysy są niemal pozbawione szczegółów. Rzadko można ich jednak zobaczyć w tej postaci, ponieważ "
    "typowy odmieniec zmienia kształt tak, jak inni zmieniają ubranie. Wielu odmieńców tworzy również głębsze "
    "tożsamości, opracowując dla każdej postaci personę z własną historią i przekonaniami. Odmieniec poszukiwacz "
    "przygód może mieć persony przeznaczone do różnych sytuacji, takich jak negocjacje, śledztwo czy walka.\n\nKilku "
    "odmieńców może dzielić tę samą personę. Persony mogą być nawet przekazywane w rodzinie, dzięki czemu młodszy "
    "odmieniec korzysta z kontaktów nawiązanych przez poprzednich użytkowników danej persony."
)
for changeling_lore_uid in (
    "h5844527eg5bc7g6d08gb8bdg836fe861ad65",
    "h00779e8dg1144g5eecg3f98g33292e8dea42",
):
    UID_OVERRIDES[changeling_lore_uid] = CHANGELING_LORE_TEXT

UID_OVERRIDES["he05ad460g276fg1990g8fccg4bd00b5d035a"] = (
    'Silna trucizna. Rzucane przez ciebie czary i wykonywane ataki ignorują <LSTag '
    'Tooltip="Resistant">odporność</LSTag> na obrażenia od trucizny. Ponadto, gdy zadajesz czarem obrażenia od '
    'trucizny, każdy wynik 1 na kości obrażeń traktujesz jak 2.\n\nWarzenie trucizny. Otrzymujesz zestaw '
    'truciciela i zyskujesz biegłość w posługiwaniu się nim. Gdy zadasz istocie obrażenia od trucizny, musi ona '
    'wykonać udany rzut obronny na Kondycję albo otrzymuje stan Zatrucia.'
)
UID_OVERRIDES["h95ef44fegf44dg26b7g490bg4d2254baeba6"] = (
    "Gdy podlegasz efektowi, który pozwala ci wykonać rzut obronny na Zręczność, aby otrzymać tylko połowę obrażeń, "
    "przy powodzeniu nie otrzymujesz żadnych obrażeń, a przy niepowodzeniu — tylko połowę. Nie korzystasz z tej "
    "zdolności, jeśli masz stan Obezwładnienia."
)

UID_OVERRIDES["ha5ec425bg430dg6de7ge56ag7b5f719afc8e"] = (
    "Atut: Uzdrowiciel\n\nWczesne lata upływają ci w odosobnionej chatce albo klasztorze, daleko poza obrzeżami "
    "najbliższej osady. Towarzyszą ci głównie leśne istoty oraz nieliczni goście przynoszący zapasy i wieści ze "
    "świata. Samotność daje wiele czasu na rozważanie tajemnic stworzenia."
)
STAND_AS_ONE_TEXT = (
    "Ramię w ramię. Gdy sojusznik w promieniu 1,5 m od ciebie podlega efektowi, który miałby go odepchnąć albo "
    "przyciągnąć, możesz w ramach reakcji temu zapobiec. Aby skorzystać z tej ochrony, sojusznik nie może mieć stanu "
    "Obezwładnienia."
)
for stand_as_one_uid in (
    "hfde09985geec3g307ag4015ga087801eec7f",
    "hae5d214ag6792g7325g5146gf48dfd5f7239",
):
    UID_OVERRIDES[stand_as_one_uid] = STAND_AS_ONE_TEXT

UID_OVERRIDES["hdfb7e043ga3ecgc3afg13c5g96138794e52b"] = (
    'Poznajesz uniwersalny język tańca. W ramach akcji dodatkowej możesz zużyć jedno użycie <LSTag '
    'Type="ActionResource" Tooltip="BardicInspiration">bardowskiej inspiracji</LSTag>, aby zatańczyć i pokrzepić '
    'inną wybraną istotę, która cię widzi.\n\nRzuć kością bardowskiej inspiracji. Istota zyskuje tymczasowe punkty '
    'wytrzymałości w liczbie równej sumie wyniku rzutu i twojego modyfikatora Charyzmy (co najmniej 2). Następnie '
    'może natychmiast w ramach reakcji przemieścić się na odległość do swojej szybkości bez prowokowania ataków '
    'okazyjnych albo wykonać akcję Uniku.'
)
UID_OVERRIDES["hd517f270gefc4g3302ge7ecge9468f84b00a"] = (
    "Jesteś wcieleniem legendarnego bohatera, który wsławił się pokonaniem wielu przerażających wrogów, a twoja "
    "magia czerpie z tej owianej legendą przeszłości. Powrót do życia za sprawą bogów, niezwykle potężnego maga albo "
    "cyklu reinkarnacji obudził w tobie źródło magii i pradawne instynkty bojowe."
)
UID_OVERRIDES["h02367640g69e6gdb06g9a72g6354c8a4ccb6"] = (
    'Ręka krzywdy. Gdy używasz Ręki krzywdy na istocie, możesz również nałożyć na nią stan Zatrucia do końca swojej '
    'następnej tury.\n\n<LSTag Type="Spell" Tooltip="Target_HandOfHealing">Ręka uzdrawiania</LSTag>. Gdy używasz '
    'Ręki uzdrawiania, możesz również usunąć z leczonej istoty następujące stany: <LSTag Type="Status" '
    'Tooltip="BLINDED">Oślepienie</LSTag>, Choroba, Paraliż albo Zatrucie.'
)
UID_OVERRIDES["h6bf206d3ga5dag2afag19eegf2c35e7a534e"] = (
    "Zawsze masz przygotowany Znak łowcy. Możesz rzucić go bez zużywania komórki czaru tyle razy, ile wskazuje "
    "wartość w kolumnie Ulubiony wróg w tabeli cech łowcy. Wszystkie użycia odzyskujesz po długim odpoczynku."
)
UID_OVERRIDES.update({
    "h097afcaegbffcg54c6g7e95g39e866fdaad8": "Siłowy niszczyciel: Pchnij",
    "hc997bdabg8c5dg07ceg15dfgb0f9460ee068": "Siłowy niszczyciel: Pociągnij",
    "h64fa93dage730gf474gfa7agc5a1466cbb77": "Siłowy niszczyciel",
    "h95594e96g7134g5267g0351g720116b03ad5": "Ulepszony siłowy niszczyciel",
    "h4fbaa426ge15cg76e8g135bg063e1212f51b": (
        "Jeśli trafisz Siłowym niszczycielem istotę mniejszą od ciebie o co najmniej jedną kategorię rozmiaru, "
        "możesz odepchnąć ją prosto od siebie na odległość do 3 m."
    ),
    "h885fc7c4ga223g5fe2g45e3gcecbe30e37ae": (
        "Jeśli trafisz Siłowym niszczycielem istotę mniejszą od ciebie o co najmniej jedną kategorię rozmiaru, "
        "możesz przyciągnąć ją do siebie na odległość do 3 m."
    ),
    "hf7e85ad5gadc6g23b3ge9bdgb92b56e72159": (
        "W ramach akcji dodatkowej ukazujesz swój Święty Symbol i zużywasz jedno użycie Aktu wiary, aby przekląć "
        "jedną widoczną istotę w promieniu 9 m od siebie do początku swojej następnej tury. Przeklęta istota ma "
        "utrudnienie w testach ataku i rzutach obronnych.\n\nGdy przeklęty cel zostanie trafiony atakiem przez "
        "ciebie albo widocznego przez ciebie sojusznika, możesz przedwcześnie zakończyć klątwę (bez użycia akcji), "
        "aby zadać mu dodatkowe obrażenia nekrotyczne albo od światłości (wedle twojego wyboru) równe twojemu "
        "poziomowi kleryka."
    ),
    "h348d60dcgba3eg7259gaac2g9675ec8837a8": (
        "W ramach akcji dodatkowej ukazujesz swój Święty Symbol i zużywasz jedno użycie Aktu wiary, aby przekląć "
        "jedną widoczną istotę w promieniu 9 m od siebie do początku swojej następnej tury. Przeklęta istota ma "
        "utrudnienie w testach ataku i rzutach obronnych.\n\nGdy przeklęty cel zostanie trafiony atakiem przez "
        "ciebie albo widocznego przez ciebie sojusznika, możesz przedwcześnie zakończyć klątwę (bez użycia akcji), "
        "aby zadać mu dodatkowe obrażenia nekrotyczne albo od światłości (wedle twojego wyboru) równe twojemu "
        "poziomowi kleryka."
    ),
    "h99fc91bfg4ca1g9784g96bege336a9f9cf88": (
        "W ramach akcji Magii możesz uwolnić jednego z przywołanych duchów. Wybierz na jego cel jedną widoczną "
        "istotę w promieniu 9 m od siebie. Duch wywołuje wówczas swój efekt. Jeśli wymaga on rzutu obronnego, jego "
        "ST jest równy twojemu ST obrony przed czarami Barda. Ta akcja pozwala rzeczywiście skorzystać z mocy ducha."
    ),
    "h88dd0cdfgc1deg9209g9c35g14ede2f5ccbb": "Poziom 3: Ręka uzdrawiania",
    "hb103cff4g6592ga38bge61dgc57ab7419d1f": (
        "Przeklęta istota ma utrudnienie w testach ataku i rzutach obronnych."
    ),
    "hf0b95e32g4ebbg93cdgf26eg83a31fd8654e": (
        "Bardowie z Kolegium Tańca wiedzą, że Słów Stworzenia nie da się zamknąć w mowie ani pieśni; wypowiadają "
        "je ruchy ciał niebieskich i płyną one w ruchach nawet najmniejszych istot. Bardowie ci ćwiczą pozostawanie "
        "w harmonii z wirującym kosmosem, kładąc nacisk na zwinność, szybkość i grację."
    ),
    "h82e9547dg2a57g3068g6744g22536b77a26f": "Poziom 10: Mistyczne uderzenie",
    "hf94f288fge015g4a15g6c34g367d15c45d89": "Poziom 2: Mistyczna włócznia",
    "h12be78fcg4014gf53egdd87g0988b8262c10": (
        "Zgłębiając wiedzę okultystyczną, poznajesz jedną wybraną Mistyczną inwokację z klasy czarownika. Jeśli "
        "inwokacja ma jakikolwiek wymóg, możesz ją wybrać tylko wtedy, gdy jesteś czarownikiem spełniającym ten wymóg."
    ),
    "h8972d6f1gb973gb24eg4f39ga448bf22f9f4": "Poziom 3: Mistyczne działo",
    "hee38cff0g9a4fg5a8dgfbf6g69eae04525e5": (
        "Możesz stworzyć na swojej dłoni Malutkie Mistyczne działo. Ty decydujesz o jego wyglądzie i o tym, czy je "
        "nosisz; może na przykład mieć nogi albo koła."
    ),
    "hb63bc4e3g2375g28c1gc6f9g87176ffa864b": (
        "Tworzone przez ciebie Mistyczne działo staje się bardziej niszczycielskie i zapewnia następujące korzyści."
        "\n\nDetonacja. Gdy otrzymujesz obrażenia, możesz w ramach reakcji rozkazać działu dokonać detonacji. Każda "
        "wroga istota w promieniu 6 m od ciebie wykonuje rzut obronny na Zręczność przeciwko twojemu ST obrony "
        "przed czarami. Przy niepowodzeniu otrzymuje 3k10 obrażeń od mocy, a przy powodzeniu — połowę tych obrażeń. "
        "Z tej zdolności możesz skorzystać raz na krótki odpoczynek.\n\nSiła ognia. Rzuty obrażeń działa oraz liczba "
        "tymczasowych punktów wytrzymałości zapewnianych przez Obrońcę zwiększają się o 1k8."
    ),
    "he30a14f7gb323g888eg2ff5g04b0a7374497": "Urzekająca magia: Zauroczenie",
    "hd31cacc2g7f81g20c3gc487gec7d06e97e53": (
        "Tryb nauki sztuczek jest aktywny. Wszystkie sztuczki maga zostają dodane do twojej listy czarów.\n\n"
        "Wybranie sztuczki do rzucenia natychmiast uczy cię jej na stałe — nie potrzebujesz prawidłowego celu ani "
        "nie musisz kończyć jej rzucania.\n\nPo wybraniu dwóch różnych sztuczek tryb się kończy."
    ),
    "h86fbc975g75b4gcf4cg3416geb64d948c1e4": (
        "Chorąży. Masz niewrażliwość na stany Powalenia, Zauroczenia i Przerażenia."
    ),
    "hca4c73c6g5ff9g1e2dg6288g9bd5466da9c1": (
        "Chorąży. Masz niewrażliwość na stany Powalenia, Zauroczenia i Przerażenia."
    ),
    "h49b1f4ebg0b80g1cbbg3266g01728d057db5": "Atut: Szybkie czarowanie",
    "haac5a803g73dfg5282g175eg12c90e9a77cd": "Urzekająca magia: Przerażenie",
    "h55c4eaaag12b5gf38cg05acg5df6c318f96c": (
        'Masz niewrażliwość na <LSTag Type="Status" Tooltip="BLINDED">stan Oślepienia</LSTag>.'
    ),
    "hb3aa275bga6abgc81agd39bg3d1c211dcc20": (
        "Ziemia wznosi się wokół celu. Cel otrzymuje stan Unieruchomienia."
    ),
    "hea98e86cg6f0eg6fa9gd366g94bd7a432ec2": (
        "Możesz w ramach akcji dodatkowej zużyć jedno użycie Dzikiej postaci, aby przybrać wyjątkową formę smoka. "
        "W tej postaci twój rozmiar zmienia się na Średni, poruszasz się na czterech łapach, ale zachowujesz zwykłe "
        "statystyki i zmysły postaci.\n\nW formie smoka możesz atakować pazurami i używać broni oddechowej. Zyskujesz "
        "szybkość latania równą dwukrotności swojej szybkości oraz odporność na obrażenia od kwasu, zimna, ognia, "
        "elektryczności i trucizny."
    ),
    "hffd4abcage782g546dgaeacgc8fe055bd42e": (
        "W ramach akcji dodatkowej zyskujesz na 1 minutę moc olbrzyma. Twój rozmiar zmienia się na Duży, masz "
        "ułatwienie w testach Siły i rzutach obronnych na Siłę, a twoje ataki bronią i ataki bez broni przy "
        "trafieniu zadają dodatkowe 1k6 obrażeń."
    ),
    "h0346ca00g9886g1f41g905dge46c1a82136e": (
        "Raz podczas każdej swojej tury, gdy trafisz istotę Wyrzutnią błyskawic, możesz zadać temu celowi dodatkowe "
        "1k6 obrażeń od elektryczności."
    ),
    "h0ca5e8d6gb9fdgdf73g977bgf17f49b479f7": (
        "Raz podczas każdej swojej tury, gdy trafisz istotę Wyrzutnią błyskawic, możesz zadać temu celowi dodatkowe "
        "1k6 obrażeń od elektryczności."
    ),
    "hff8f8621g9bc7gd484g306bg3d323ffef343": (
        "Gdy trafisz istotę atakiem zadającym obrażenia cięte, możesz zmniejszyć jej szybkość o 3 m do początku "
        "swojej następnej tury."
    ),
    "h913cbdacgf9e4g58feg0296g889e13ab49d9": (
        'Gdy trafisz istotę atakiem wręcz, możesz zużyć <LSTag Type="ActionResource" '
        'Tooltip="ChannelDivinity">Akt wiary</LSTag>, aby zadać dodatkowe obrażenia od ognia.'
    ),
    "hf4556a98g94c2g16ddg4fe9g5fa3c35a3652": (
        'Gdy trafisz istotę atakiem wręcz, możesz zużyć <LSTag Type="ActionResource" '
        'Tooltip="ChannelDivinity">Akt wiary</LSTag>, aby zadać dodatkowe obrażenia od ognia.'
    ),
    "hcc3c36c6gd341g9ef3g75a6gd57375a199cd": (
        "Atut: Uzdolniony\n\nSpecjalizujesz się w manipulacji, masz skłonność do koloryzowania i chętnie "
        "wykorzystujesz to dla własnych korzyści. Naginanie prawdy i nastawianie sojuszników przeciwko sobie "
        "może z czasem przynieść jeszcze większe sukcesy."
    ),
    "h1594d7ffge703g7b01g1f9bg2776670f8c1f": (
        "Fortuna bywa kapryśna — chyba że należysz do Hazardzistów. Ci rewolwerowcy mistrzowsko grają w karty i "
        "kości, łącząc zamiłowanie do ryzyka z talentem strzeleckim. Wyciskają ze szczęścia ostatnią kroplę, a gdy "
        "go zabraknie, podbijają stawkę jeszcze wyżej. Po co zadowalać się zwycięstwem, skoro można postawić "
        "wszystko i zgarnąć główną wygraną?"
    ),
    "h99e9e197g55f2g72f5g3b37g75a3f15b60bc": (
        "Biegle posługujesz się bronią palną. Możesz dodawać swój modyfikator cechy do rzutów obrażeń ataków "
        "wykonywanych bronią palną."
    ),
    "h86b389a9gfe27g7353g9f20g12d9431a57fa": (
        "Biegle posługujesz się bronią palną. Możesz dodawać swój modyfikator cechy do rzutów obrażeń ataków "
        "wykonywanych bronią palną."
    ),
    "h4580d441g9dc0gbc53g7a59g25cce7bd8ba2": (
        'Nie można się poruszać. Stan Unieruchomienia wywołany <LSTag '
        'Tooltip="OpportunityAttack">atakiem okazyjnym</LSTag> Nieugiętego mściciela.'
    ),
    "hf85d24eegb746gb3e4g54ddg00cde5bd922f": "Uderzenie tarczą: Powalenie",
    "h890ef36dga451ge5acgb49dg6c441e309f11": "Poziom 7: Telekinetyczne pchnięcie (Powalenie)",
    "h4bf93b9cg7a63g5e2bgf86ag8868c3da02b1": (
        "Gdy ta zdolność jest włączona, nie możesz wykonywać reakcji. W zamian sojusznicy w promieniu 1,5 m od "
        "ciebie nie mogą być odpychani ani przyciągani przez efekty, chyba że mają stan Obezwładnienia."
    ),
    "h6adc649fgbd08g1d76g0aecg4e5c0ef03271": (
        "Gdy wykonujesz atak bronią przeciwko istocie ze stanem Zauroczenia, możesz zyskać ułatwienie w teście "
        "ataku (bez użycia akcji). Jeśli atak trafi, staje się trafieniem krytycznym."
    ),
    "hc39bb1c4g3c5bg1b8fga689g2acf69286fc7": (
        "Gdy wykonujesz atak bronią przeciwko istocie ze stanem Zauroczenia, możesz zyskać ułatwienie w teście "
        "ataku (bez użycia akcji). Jeśli atak trafi, staje się trafieniem krytycznym."
    ),
    "h363f8861g503bg174cgc576g28e60841fa32": (
        "Gdy atak trafia cię i zadaje obrażenia obuchowe, kłute albo cięte, możesz w ramach reakcji zmniejszyć "
        "łączną wartość otrzymywanych obrażeń o 1k10 + twój modyfikator Zręczności + twój poziom mnicha.\n\n"
        "Jeśli zmniejszy to obrażenia do 0, możesz wydać 1 punkt ki, aby użyć Przekierowania ataku."
    ),
    "h96997b05g813bg4cedge308g8b97a39ea6cc": (
        'Zmniejsz otrzymywane obrażenia obuchowe, kłute albo cięte o 1k10 + twój <LSTag '
        'Tooltip="AbilityModifier">modyfikator</LSTag> Zręczności + twój poziom mnicha.\n\nJeśli zmniejszy to '
        'obrażenia do 0, możesz wydać 1 punkt ki, aby użyć Przekierowania ataku.'
    ),
    "h5873afb5ga1a1gb7ddgaea4gaf5ab082ffd4": (
        "Możesz w ramach akcji dodatkowej aktywować runę, zyskując na 1 minutę odporność na obrażenia obuchowe, "
        "kłute i cięte."
    ),
    "hf478fc95g9735gc147g5553g233bdcac6a42": (
        "Posiadacz zyskuje odporność na obrażenia obuchowe, kłute i cięte pochodzące zarówno z ataków "
        "niemagicznych, jak i magicznych."
    ),
    "h8697b53cg246dg4397g9db8gc35b4035bc5b": "Związanie broni paktu (obrażenia od światłości)",
    "h42e7e44fge041g864egc55fgbbdba0e4da67": (
        "Za każdym razem, gdy otrzymujesz obrażenia od światłości, napastnik otrzymuje obrażenia od mocy równe "
        "jego premii z biegłości."
    ),
    "h5f178becg3db2geb81g5414g5c6e0287715f": (
        "Masz odporność na obrażenia nekrotyczne i od światłości."
    ),
    "h1e811cadgb62eg0b4cgf227g305228f83fc7": (
        "Za każdym razem, gdy trafisz atakiem bez broni, możesz sprawić, że zamiast zwykłego typu obrażeń zada "
        "on wybrane przez ciebie obrażenia od kwasu, zimna, ognia, elektryczności albo dźwięku."
    ),
    "h7a33c7b9g8cc0g6c2bg348fg50d1aa50e0f5": (
        "Gdy trafisz cel magiczną bronią, możesz skierować przez uderzenie magiczną energię i wyzwolić "
        "Niszczycielską energię. Cel otrzymuje dodatkowe 2k6 obrażeń od mocy."
    ),
    "h2a2d4c40ge64cg5bd8gb073g4424cebf9004": (
        'Gdy twój <LSTag Type="Spell" Tooltip="Target_SteelDefender">Stalowy obrońca</LSTag> trafi cel, możesz '
        "skierować przez uderzenie magiczną energię i wyzwolić Niszczycielską energię. Cel otrzymuje dodatkowe "
        "2k6 obrażeń od mocy."
    ),
    "hf1072944g3718g45edgace3ga7e816803e30": (
        'Sięgnij do kieszeni celu i spróbuj ukraść przedmiot. W tym teście Zręczności (<LSTag Type="Skills" '
        'Tooltip="SleightOfHand">Zręczność dłoni</LSTag>) jako Mistyczny oszust wykorzystujesz własny modyfikator.'
    ),
    "hf03822e2g7af0g67edg9165g36461a798fbc": (
        "Twoja magiczna zbroja zyskuje dodatkowe korzyści zależne od modelu.\n\nDrednot. Kość obrażeń "
        "Siłowego niszczyciela zwiększa się do 2k6 obrażeń od mocy, a twój zasięg zwiększa się o 3 m.\n\n"
        "Strażnik. Kość obrażeń Gromowego impulsu zwiększa się do 1k10 obrażeń od dźwięku. Ponadto za każdym "
        "razem, gdy widoczna istota zbliży się na odległość 1,5 m od ciebie, możesz wykonać przeciwko niej atak "
        "okazyjny.\n\nInfiltrator. Kość obrażeń Wyrzutni błyskawic zwiększa się do 2k6 obrażeń od elektryczności. "
        "Każda istota, która otrzyma od niej obrażenia od elektryczności, zostaje porażona."
    ),
    "hc78c376dg616ag7239gb066ga93738880899": "Widmowy atak bronią sieczną",
    "heb8ccc52g26b4gf1c4g7dfbge1ff8af766c2": (
        "Możesz wezwać siły natury, aby poznać mocne i słabe strony swojej ofiary. Dopóki istota jest oznaczona "
        "twoim Znakiem łowcy, twoje ataki bronią ignorują jej odporność na obrażenia obuchowe, kłute i cięte."
    ),
    "h9bcb3486gd911g3c9fgace0g779c9bda1aa7": (
        'Ma <LSTag Tooltip="Resistant">odporność</LSTag> na obrażenia obuchowe, kłute i cięte.'
    ),
    "hb35a01acgce21gf8a8gc7b6g225fbd67b408": (
        'Ma <LSTag Tooltip="Resistant">odporność</LSTag> na obrażenia obuchowe, kłute i cięte.'
    ),
    "ha9065fa0gda11g9fbag0a9fgd56f197c42ac": (
        "Przez 1 minutę masz odporność na obrażenia obuchowe, kłute i cięte."
    ),
})

STONE_FLESH_TEXT = (
    'Spraw, by ciało istoty stało się twarde jak kamień. Istota zyskuje <LSTag '
    'Tooltip="Resistant">odporność</LSTag> na obrażenia obuchowe, kłute i cięte.'
)
for stone_flesh_uid in (
    "h36a49c70g93aeg56fag31d6g861694b3eca0",
    "hbd15ec06ga1begd062g730ega5c6e100ec6f",
    "h901059e2g5cefg4bbbg2e95g491ea1dbb812",
    "h138ad957g4e4cgf396gebd4g8ad15a605ba6",
):
    UID_OVERRIDES[stone_flesh_uid] = STONE_FLESH_TEXT

SHIELD_MASTER_TEXT = (
    "Uderzenie tarczą. Jeśli w ramach akcji Ataku zaatakujesz istotę w promieniu 1,5 m od siebie i trafisz ją "
    "bronią do walki wręcz, możesz natychmiast uderzyć cel wyposażoną tarczą. Cel wykonuje rzut obronny na Siłę "
    "(ST 8 + twój modyfikator Siły + premia z biegłości). Przy niepowodzeniu odpychasz go o 1,5 m albo nadajesz "
    "mu stan Powalenia (wedle twojego wyboru). Z tej korzyści możesz skorzystać tylko raz podczas każdej swojej "
    "tury.\n\nOsłona tarczą. Gdy podlegasz efektowi, który pozwala ci wykonać rzut obronny na Zręczność, aby otrzymać "
    "tylko połowę obrażeń, możesz w ramach reakcji nie otrzymać żadnych obrażeń przy powodzeniu, o ile trzymasz tarczę."
)
for shield_master_uid in (
    "he75553c3gd15ag322eg1dcega59ac6593319",
    "h5752835cge17egb9e8g58cdgb5e2500ab72d",
):
    UID_OVERRIDES[shield_master_uid] = SHIELD_MASTER_TEXT
UID_OVERRIDES["he6b03eaeg69d3geb4cgfcafg07e44f75a6d9"] = SHIELD_MASTER_TEXT.split("\n\n", 1)[0]

SENTINEL_LOCKDOWN_TEXT = (
    "Doskonalisz się w powstrzymywaniu wrogów. Istoty prowokują od ciebie atak okazyjny, gdy przemieszczą się o "
    "co najmniej 1,5 m w obrębie twojego zasięgu, a gdy trafisz istotę atakiem okazyjnym, jej szybkość zmniejsza "
    "się do 0 do końca bieżącej tury."
)
for sentinel_uid in (
    "h96dd1a79g41bfg7310gfaedg7ce04dd1acf3",
    "h6d3bae27g9034g8149g3867g484287a79d30",
):
    UID_OVERRIDES[sentinel_uid] = SENTINEL_LOCKDOWN_TEXT

GIANT_DESCENDANT_TEXT = (
    "Wywodzisz się od olbrzymów. Wybierz jedną z poniższych korzyści — nadprzyrodzony dar wynikający z twojego "
    "dziedzictwa. Możesz użyć wybranej korzyści tyle razy, ile wynosi twoja premia z biegłości, a wszystkie użycia "
    "odzyskujesz po ukończeniu długiego odpoczynku:"
)
for giant_descendant_uid in (
    "h3f95591ag3b57ge6b7g67dag6b78011d07e5",
    "hbfc7d66dgd649g2d81g9f50ga79cce5da957",
):
    UID_OVERRIDES[giant_descendant_uid] = GIANT_DESCENDANT_TEXT

BULWARK_TEXT = (
    "Przedmurze. Gdy podlegasz efektowi, który nadałby ci stan Powalenia, możesz w ramach reakcji zachować "
    "równowagę i nie otrzymać tego stanu."
)
UID_OVERRIDES["h625d9005geaaagf264gd451g2b3a70bba135"] = BULWARK_TEXT.removeprefix("Przedmurze. ")
UID_OVERRIDES["ha9361cceg5dd0g35ecg1949g313ca2768512"] = (
    BULWARK_TEXT
    + "\n\nŻelazny żołądek. Za każdym razem, gdy przywracasz sobie punkty wytrzymałości, odzyskujesz dodatkowe "
    "punkty w liczbie równej swojemu modyfikatorowi Kondycji."
)
UID_OVERRIDES["h0397fcaag1719g76a6g53f7g803d71e9392d"] = (
    "Przejawiasz wytrzymałość właściwą olbrzymom wzgórzowym, co zapewnia ci następujące korzyści:\n\n"
    + UID_OVERRIDES["ha9361cceg5dd0g35ecg1949g313ca2768512"]
)

# The exact English word also occurs as a status, where the official Polish
# adjective "Przebudzony" is correct.  Only the spell-title handle is the noun.
UID_OVERRIDES["hfefb5384gcdb9g70a3g4fd3g5796fed23526"] = "Przebudzenie"
UID_OVERRIDES["h969e79f8ga241g4f3eg904ag8f4858d7c146"] = "Zwój Shillelagh"
UID_OVERRIDES.update({
    "hd0c364a3g050eg598bgd2fdg4c1b525be149": "Poziom 1: Pierwotny porządek: Shillelagh",
    "hdd5d9c2cg059eg4e76gb6b6g01e4d851171d": "Wtajemniczony: Shillelagh",
    "h6b046ff8ga327gdc59g8f4fgebc351482d81": "Poziom 3: Ulepszenie Shillelagh",
    "h7fe6e3e8gb94ag15c5g406eg227fcfa3c807": "Poziom 6: Mistrzostwo Shillelagh",
    "h33d907d8gd0a0gaee7g061fg578448183f33": "Ulepszenie Shillelagh",
    "h3bb1c07ag3913g5b74g9454gdcebc7737556": "Tarcza wiary: błogosławieństwo boga wojny",
    "hcaeae1ebgf2c5gb598g6716gb1b7c699916c": "Duchowa broń: błogosławieństwo boga wojny",
})
UID_OVERRIDES["hd5322297g3c9agc288gf0d2g3bf720ba3cbf"] = (
    "Charyzmatyczni i wyrachowani Piekielni Mówcy służą Molochowi, przemierzając pole bitwy i czyniąc z wrogów "
    "mimowolnych sojuszników.\n\n"
    "Moloch włada Styksem, Miastem Kłamstw, lecz jego wpływy sięgają znacznie dalej. Najwybitniejsi piekielni "
    "politycy i dyplomaci zyskują znaczenie dzięki subtelnym manipulacjom Molocha. Są mu bezgranicznie lojalni, "
    "wiedzą bowiem, że bez niego byliby nikim — dlatego jego potęga rozbrzmiewa echem w całym Piekle.\n\n"
    "Illriggerzy Molocha to elokwentni zaklinacze, którzy za pomocą czarów i podstępów usypiają czujność wrogów, "
    "aż ci odzyskują świadomość jako poddani Zakonu Spustoszenia. Piekielni Mówcy ćwiczą się w sztuce zwanej "
    "Czerwoną Pieśnią albo Piekielną Pieśnią. Rozumiejąc przeciwnika i wplatając subtelne czary w zwykłą mowę, "
    "potrafią sprawić, że wrogowie poczują, pomyślą lub zrobią niemal wszystko, co przyspieszy zwycięstwo Piekła.\n\n"
    "W całej czasoprzestrzeni Piekielni Mówcy słyną jako uśmiechnięci łotrzykowie i zawadiaccy złoczyńcy. Cenieni "
    "w każdych negocjacjach, wiedzą, że w świecie kłamstw prawda może być bronią równie potężną jak stal."
)
UID_OVERRIDES.update({
    "hd660fd06g45aeg25f4g7e9dg6fd338c66f83": "Atut pochodzenia: Wtajemniczony (kleryk)",
    "ha980b3fbg98dcgc88eg9edbg89be32a4b191": "Wtajemniczony (kleryk): sztuczka",
    "hd57d4d53gfb82gc5e5ge39eg18ccf99d11ac": "Wtajemniczony (kleryk): druga sztuczka",
    "he64b4a45gba6eg30a6g9703gb0f13f9230e8": "Wtajemniczony (kleryk): sztuczka",
    "h3522b895gaf8eg23c8ge2a5g19305a3832ce": "Atut pochodzenia: Wtajemniczony (druid)",
    "h948ef541g3485gbf64g5f3ag0b03af06a06a": "Wtajemniczony (kleryk): czar",
    "h5e27ad01ga610ga42cgc65dg1ce99d93cdf8": "Atut pochodzenia: Wtajemniczony (mag)",
    "hffac3ddcg8327g4829g8b8fgec3bb18e4a7e": (
        "Wtajemniczony (kleryk): Poznajesz dwie sztuczki. Dobry wybór."
    ),
    "h4b636d62g474cg4604ga98egff95e23fd181": "Poznajesz ten czar dzięki atutowi Wtajemniczony.",
    "hf4a140acg44b0g71b4gdc1bg5649f5dce909": "Poziom 2: Wtajemniczony (kleryk, Lekcje Pierwszych)",
    "h1e432242gf706g3505g9353g62a0e8892839": "Poziom 2: Wtajemniczony (druid, Lekcje Pierwszych)",
    "he0f08303ge368gad59g9d19gf23e26ea8152": "Poziom 2: Wtajemniczony (mag, Lekcje Pierwszych)",
})
UID_OVERRIDES["h18021532g7cf1g263eg148bg852a52db6cf5"] = (
    "Atut: Wtajemniczony (kleryk)\n\nTwoje życie upływało dotąd na posłudze w świątyni, nauce świętych "
    "rytuałów i składaniu ofiar bóstwom, którym oddajesz cześć. Służba bogom i kontemplacja dzieł ich rąk "
    "poprowadzą cię ku wielkości."
)
UID_OVERRIDES["hca28ebc2ga938g8c68g1dbag7edf639c41fc"] = (
    "Atut: Wtajemniczony (mag)\n\nOdznaczasz się erudycją i ciekawością świata oraz niezaspokojonym "
    "pragnieniem wiedzy. Poznawanie rzadkich tajemnic świata inspiruje cię, by wykorzystać tę wiedzę do "
    "wyższych celów."
)
EXACT_OVERRIDES["Abjurer"] = "Mag odpychania"
EXACT_OVERRIDES["Level 3: Arcane Ward"] = "Poziom 3: Magiczna powłoka"
EXACT_OVERRIDES["Level 6: Projected Ward"] = "Poziom 6: Przekazanie osłony"
EXACT_OVERRIDES["Level 10: Improved Abjuration"] = "Poziom 10: Ulepszone odpychanie"
UID_OVERRIDES["h9d3fbbaegc6b1gf48egd8c4gef06e95785f3"] = (
    'Za każdym razem, gdy kończysz <LSTag Tooltip="ShortRest">krótki odpoczynek</LSTag>, twoja '
    '<LSTag Type="Passive" Tooltip="ArcaneWard">magiczna powłoka</LSTag> w pełni się odnawia.'
)

UID_OVERRIDES["hd251b05fg755bge84dgf97egf45679814510"] = (
    "Gdy istota trafia cię testem ataku, możesz w ramach reakcji stworzyć między sobą a napastnikiem swojego "
    "iluzorycznego sobowtóra. Atak automatycznie chybia, po czym iluzja znika.\n\n"
    "Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie ukończysz krótkiego albo długiego odpoczynku. "
    "Możesz również odnowić jej użycie, zużywając komórkę czaru co najmniej 2. poziomu."
)
UID_OVERRIDES["h0844a944gf85ag2577g8e77g23dcd6a6e387"] = (
    "Twoje majsterkowanie zapewniło ci towarzysza: Stalowego obrońcę. Jest przyjazny tobie i twoim towarzyszom oraz "
    "wykonuje twoje polecenia. Jeśli zginął, możesz w ramach akcji użyć narzędzi kowalskich i zużyć komórkę czaru co "
    "najmniej 1. poziomu, aby go ożywić."
)
UID_OVERRIDES["h72243c73g089cge11bg923dgf4b6e05bcaf5"] = (
    "Magicznie przywołujesz pierwotną bestię, która czerpie siłę z twojej więzi z naturą. Jeśli bestia zginęła w "
    "ciągu ostatniej godziny, możesz w ramach akcji Magii dotknąć jej i zużyć komórkę czaru."
)
UID_OVERRIDES["h082d1855ga658g2a35g05a7g0252200ad020"] = (
    "Porady wieszcza zasięgają ci, którzy pragną lepiej zrozumieć przeszłość, teraźniejszość i przyszłość. Jako "
    "wieszcz starasz się uchylić zasłony przestrzeni, czasu i świadomości. Dążysz do opanowania czarów pozwalających "
    "dostrzegać to, co ukryte, widzieć odległe miejsca, zdobywać nadprzyrodzoną wiedzę i przewidywać przyszłość."
)

BARDIC_UNARMED_STRIKE_TEXT = (
    "Gdy korzystasz z bardowskiej inspiracji w ramach akcji, akcji dodatkowej albo reakcji, możesz w jej ramach "
    "wykonać jeden atak bez broni."
)
for duplicate_uid in (
    "h6d7a7de1g2c02gc8bbgcf20g79bdbdc08374",
    "h3838231fg4eb9g1855g186cg2e9b9e1e45e6",
):
    UID_OVERRIDES[duplicate_uid] = BARDIC_UNARMED_STRIKE_TEXT

# Final prose corrections found by the full-corpus language and semantic audit.
UID_OVERRIDES.update({
    # Upstream 4.12.9.5 corrected these handles from the duplicated background
    # title to the actual feature name.  Use the established Polish D&D term.
    "he4b058a0g2cdbgba7agf3cfg71fa968bbd61": "Przywrócenie honoru",
    "h9fa0d3deg53aag92d4g5ba5g0185574f2cd7": "Przywrócenie honoru",
    "h1034780age61eg388fg49d2g23bd1ca7ca75": (
        "Wyll, nazywany „Klingą Pogranicza”, używa swojej magii do walki z potworami i diabłami nękającymi "
        "Wybrzeże Mieczy. W chwili rozpaczy przyjął zaoferowaną mu moc, stając się tym samym pionkiem w "
        "piekielnej grze, w której nie radzi sobie zbyt dobrze."
    ),
    "h2f0d755egc57dga744g72aaga03c4b3365ab": (
        "Gdy rozkazujesz swojej pierwotnej bestii towarzyszącej wykonać akcję Uderzenia bestii, może ona "
        "użyć jej dwukrotnie.\n\nPonadto, gdy po raz pierwszy w danej turze trafi istotę objętą Znakiem "
        "łowcy, zadaje dodatkowe obrażenia od mocy równe dodatkowym obrażeniom tego czaru."
    ),
    "hb0efd2ceg0833g9420g8355ge424da379f9e": (
        "Wystrzeliwujesz olśniewającą gamę migających, kolorowych świateł. Każda istota w stożku o długości "
        "4,5 m, którego źródłem jesteś, wykonuje rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje stan "
        "Oślepienia do końca twojej następnej tury."
    ),
    "h853f3b07gf693g964eg9f97g97a2cfda50ef": (
        "Każda istota w emanacji [1], której źródłem jesteś, wykonuje rzut obronny na Kondycję. Przy "
        "niepowodzeniu otrzymuje obrażenia od dźwięku."
    ),
    "hbb7ccd06g2737gdcf2gc167g21f32c9615fb": (
        "Z ciebie wybucha płonący blask, tworząc emanację o promieniu [1]. Każda wybrana przez ciebie "
        "widoczna istota w jej obrębie wykonuje rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje "
        "obrażenia od światłości."
    ),
    "hfa86f65dg33d6g9ea6g0948gfbf198214a31": (
        "Gdy używasz Kroku fey, przed teleportacją wybierz jedną widoczną istotę w promieniu 1,5 m od siebie. "
        "Istota wykonuje rzut obronny na Mądrość. Przy niepowodzeniu otrzymuje do końca twojej następnej tury "
        "stan Przerażenia, którego źródłem jesteś."
    ),
    "h4642fa9fg99f2g37fcg659cg1f43f42e73ee": (
        "Jeśli cel ma rozmiar duży lub mniejszy, wykonuje rzut obronny na Zręczność. Przy niepowodzeniu "
        "otrzymuje stan Powalenia."
    ),
    "he6c26bfag496eg4545g66e5g0166e2cb0452": "Uderzenie tarczą (Powalenie)",
    "h9b9091cdg68c3ga5edgce70g3588f2071f07": "Zyskaj 1k10 tymczasowych punktów wytrzymałości.",
    "h55ff7bfdg1e2bg7f91gd91bge020cba01b4d": "Zyskaj 1k10 tymczasowych punktów wytrzymałości.",
    "h947ed943ge9abg4881g2010ge2b6da6351b6": (
        "Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz). "
        "Odzyskujesz wszystkie użycia po długim odpoczynku."
    ),
    "h40fa14d1gcd8ag4b04g332cg14f014f79df1": (
        "Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz). "
        "Odzyskujesz wszystkie użycia po długim odpoczynku."
    ),
    "h84a7d362gf65ag0f66g6103g7d1f4fc707d2": "Poziom 2: Akt wiary",
    "h8e8ebc40g6f5cg5d29gc885g2f7fb0f2899b": "Witalność Dzikiej postaci",
    "h7e67754bg739bg3c96gcd25g72c30f60a4d8": (
        'Zmuś istotę do ponownego wykonania <LSTag Tooltip="AttackRoll">testu ataku</LSTag>.'
    ),
    "h8774fb9bg4691ge891gcd62g04a6e30adc85": (
        'Odwróć uwagę wrogów iluzją. Ty i twoi sojusznicy macie <LSTag Tooltip="Advantage">ułatwienie</LSTag> '
        'w <LSTag Tooltip="AttackRoll">testach ataku</LSTag> przeciwko istotom znajdującym się w promieniu [1] '
        "od iluzji, o ile atakujący również znajduje się w promieniu [1] od iluzji."
    ),
    "hdb3ddc06g4d4eg4b4ag5673g48373fbbaa38": (
        "Zyskujesz następującą opcję Chytrego uderzenia.\n\nParaliż. Gdy zadajesz obrażenia z ukradkowego "
        "ataku, możesz zrezygnować z dodatkowych obrażeń tego ataku. Jeśli to zrobisz, cel wykonuje rzut "
        "obronny na Kondycję. Przy niepowodzeniu otrzymuje stan Paraliżu do końca twojej następnej tury."
    ),
})

CUNNING_STRIKE_PARALYZE_TEXT = (
    "Gdy zadajesz obrażenia z ukradkowego ataku, możesz zrezygnować z dodatkowych obrażeń tego ataku. Jeśli to "
    "zrobisz, cel wykonuje rzut obronny na Kondycję. Przy niepowodzeniu otrzymuje stan Paraliżu do końca twojej "
    "następnej tury."
)
for duplicate_uid in (
    "h5bbad71ag4750g78afg0c59ga5aca446dc13",
    "hf1e8a3afg2d52gf821gfb11ge37ef7d60eda",
    "hc79c3b73g4d95gf714gfb45g8a3475bc2391",
):
    UID_OVERRIDES[duplicate_uid] = CUNNING_STRIKE_PARALYZE_TEXT

# Preserve the source formula spacing so the rendered bonus reads "2k4 + 1".
UID_OVERRIDES["h22179fdag3286gcd27g7facg8e73f5c76e01"] = (
    'Zyskujesz 2k4 + [1] <LSTag Tooltip="TemporaryHitPoints">tymczasowe punkty wytrzymałości</LSTag>.'
)

# UI terminology and grammar corrections confirmed against the shipped Polish
# BG3 localization and the current Polish D&D 2024 community corpus.  The
# mastery-name handles are UID-specific because their isolated English words
# otherwise collide with unrelated official UI strings.
UID_OVERRIDES.update({
    "hb60d9b3bg491bg7056g1bd9gc752b67bfd56": "Szerokie cięcie",
    "h64e7021cg8b69g3f60gde38gd59f3cdc5846": "Popchnięcie",
    "ha395ebeag3995g70fage1d7g718229b74f9b": "Obalenie",
    "h39b48f39g9a41g2ba3g3567g7ab1cb265f82": "Poziom 3: Ochronny rozbłysk",
    "h67f1e6b2g8adcge989g555ag3cbae9d62375": "Poziom 6: Ulepszony ochronny rozbłysk",
    "h03dc1992g1d8agc3e0ga6bbg22607e81d966": "Ochronny rozbłysk (sojusznik)",
    "hcb0f1d4dg6ea8gf1eag5e72g32b56f306af2": "Ochronny rozbłysk (własna postać)",
    "hb220d543g0de9ga76cg8f82gc0f939ce0a89": "Ulepszony ochronny rozbłysk",
    "hdc4e30afg0702g20ddgf4a5g1751c8b46770": "Poziom 3: Przywołanie sobowtóra",
    "h5c1e93a7g2f48g4d6bg8e13ga7f4c2b60d95": "Czarowanie przez sobowtóra",
    "h3f8a1c72g5e94g4b21ga7c3gd8e51f0b9a46": "Czarowanie przez sobowtóra",
    "h4e92a1c7g63bdg48f0g9c25ga07f1b53de86": "Sztuczka sobowtóra",
    "h2d47b9e1g8c35g4a70gb61fg5e8d0c34a927": "Sztuczka sobowtóra",
    "hda020f21g72bagfe0cgda65g4bd7740d8934": "Przesuń sobowtóra",
    "h9a4f2b81gd37eg46c2gb058ge1d93f7a2c46": (
        "Zużyj akcję i komórkę czaru, aby skierować magię przez swojego sobowtóra. W swojej turze sobowtór "
        "może rzucić jeden z przygotowanych przez ciebie czarów, zużywając tę komórkę i korzystając z twojego "
        "ST obrony przed czarami oraz premii do ataku czarami. Dzięki temu rzucasz czar tak, jakbyś znajdował "
        "się na miejscu iluzji."
    ),
    "h7b2e4d19gc63fg41a8gb95egf2c8a3d716b0": (
        "W swojej turze sobowtór może rzucić jeden z czarów przygotowanych przez kleryka, zużywając wydaną "
        "komórkę czaru i korzystając z jego ST obrony przed czarami oraz premii do ataku czarami."
    ),
    "hb1c6082fg95a4g4e37g8d16gf3ae92c04751": (
        "Zużyj akcję, aby skierować magię przez swojego sobowtóra. W swojej turze sobowtór może rzucić jedną "
        "z twoich sztuczek, korzystając z twojego ST obrony przed czarami oraz premii do ataku czarami. "
        "Dzięki temu rzucasz sztuczkę tak, jakbyś znajdował się na miejscu iluzji."
    ),
    "h6f81c3a5g47deg4b92g8a03gd15f92c7be48": (
        "W swojej turze sobowtór może rzucić jedną ze sztuczek kleryka, korzystając z jego ST obrony przed "
        "czarami oraz premii do ataku czarami."
    ),
    "h2b54832cgd102gec1dg521dgc5239b16c5b9": "Pomoc natury",
    "h773e9cb8g4f4agad4egf609gdb85666d9d37": "Poziom 3: Pomoc natury",
    "h89713adeg01adg81acg9f46g71f0e1a5f820": "Poziom 6: Naturalna regeneracja",
    "h620c69f6g5443g20cdg6ba6g742691ee6c08": (
        "Druidzi z Kręgu Morza czerpią z burzliwych sił oceanów i burz. Niektórzy uważają się za "
        "ucieleśnienia gniewu natury i szukają zemsty na tych, którzy ją rabują. Inni poszukują mistycznej "
        "jedności z naturą, dostrajając się do rytmu przypływów i odpływów, podążając za pędem prądów i fal "
        "oraz słuchając nieprzeniknionych szeptów i ryków wiatrów."
    ),
    "ha3fdc893gcf78gc804gf587gdbeacfc06c65": "Powtórz Ciemność",
    "hadf8e795g3f57g1ec6g0288gfd8ec498c690": "Powtórz Ciemność",
    "h99ed2837g02ccg455dg2e23gad3d13fc9b06": "Powtórz Ciemność",
    "h48d3643fg9150g4323g6a3bg15e71e622720": "Powtórz Ciemność",
    "h272e8b3fg32bcg9272g86a0g32a43e6b7889": "Powtórz Ciemność",
    "hc846b26dgef48g7d56g1bb9g632994732104": "Powtórz Poryw wiatru",
    "h939b7cccgc964gc711gd6f5gecea12c2f0bf": "Powtórz Uderzenie pustki",
    "hb2dd14b4gba6bgdc59gf8f1g789a1ebe6b74": "Powtórz Uderzenie pustki",
    "h87fda05fg80fdg949dg6eb1g69542080219a": (
        "Uzyskano komórkę czaru poziomu [1]. Użyj tej komórki przed utworzeniem kolejnej na tym samym poziomie."
    ),
    "hc69907d4g8c9eg708ag8797ge1e6e4d47653": (
        'Wydaj [1] punktów zaklinania, aby odblokować <LSTag Tooltip="SpellSlot">komórkę czaru</LSTag> '
        "poziomu [2]. Utworzenie kolejnej komórki czaru tego samego poziomu nie przyniesie efektu, dopóki ta "
        "nie zostanie użyta."
    ),
    "hba2e93bcg0b57g355dg5803gd6ef0f19efec": "Ma utrudnienie w następnym teście k20, który wykonuje.",
    "h9d6713c3gcb8cgea0fg44deg1925c2bcb55d": (
        "Przywołujesz ducha smoka. Pojawia się on na widocznym, niezajętym miejscu w zasięgu i korzysta z "
        "bloku statystyk Smoczego ducha. Istota znika, gdy jej punkty wytrzymałości spadną do 0 albo gdy czar "
        "dobiegnie końca."
    ),
    "h3fc5f406g8b36gf617gf0f4ga02e99f55658": "Smoczy duch",
    "h94c82192gf055gfc18gd5bfgfcedb51b258c": "Cel wyczarowania mniejszych żywiołaków",
    "h33a18d4cgdf06g9238gf504ge24a7a01dabc": (
        "Gdy wykonujesz rzut na inicjatywę, możesz dodać do wyniku swoją premię z biegłości."
    ),
    "h3a9af277g0525g3e62g4bf1g23d2ae263ac0": (
        "Gdy wykonujesz rzut na inicjatywę, możesz dodać do wyniku swoją premię z biegłości."
    ),
    "hdca03596gcde4g4b29g8a36g81f8496c69a4": "Najemnik Płonącej Pięści",
})

# Focused gameplay-description pass.  These strings either contained a
# semantic mistranslation (for example, BG3's class-change terminology), a
# broken Polish construction, or a duplicate feature name that disagreed with
# the canonical standalone label already used elsewhere in this localization.
UID_OVERRIDES.update({
    "h1d522e3cgc9dcg916bgfa58g5cd59e1f7ebd": (
        "Gdy trafisz istotę testem ataku, możesz spróbować ją speszyć. Cel musi wykonać rzut obronny na "
        "Mądrość; w razie niepowodzenia ma utrudnienie w rzutach obronnych do końca twojej następnej tury."
    ),
    "h7f09b2d2g5ce4g617bgbbb7gae4f47ac82af": (
        "Masz niewrażliwość na stan Powalenia oraz ułatwienie w rzutach obronnych na Siłę."
    ),
    "h3b19c28cg80dcg38e9gc853g0c674ef3b5e5": (
        "Natychmiast po tym, jak istota w promieniu 1,5 m od ciebie trafi cię atakiem wręcz, możesz "
        "wykonać przeciwko niej atak okazyjny."
    ),
    "h3566bf7ege17bg0f56g4fbdgfac65706f1a2": (
        "Podczas tworzenia postaci lub zmiany jej klasy wybierz tylko jeden atut Początki magii. "
        "Wybranie więcej niż jednego może spowodować nieoczekiwane problemy."
    ),
    "ha77cb967ga90dgf3bagbb92g9b2af176e030": (
        "Legenda Barda Łucznika zainspirowała wielu młodych ludzi z Dale, którzy pragną dowieść swej "
        "wartości, zabijając potężnego potwora. Jak wielu przed tobą, od dawna rozmyślasz nad sposobami "
        "walki z ogromnymi istotami, licząc, że pewnego dnia zdobędziesz sławę, pokonując jedną z nich."
        "\n\nMasz ułatwienie w testach ataku przeciwko istotom rozmiaru dużego lub większego. Ponadto, gdy "
        "trafiasz taką istotę, zadajesz dodatkowe obrażenia równe swojemu modyfikatorowi Siły."
    ),
    "ha694feb3g0781gc772g6147gd804e68c64f8": (
        "Możesz dokonać przemiany w ramach akcji dodatkowej, korzystając z jednej z poniższych opcji "
        "(wybierasz ją przy każdej przemianie). Przemiana trwa 1 minutę albo do chwili, gdy ją zakończysz "
        "(bez użycia akcji). Po przemianie nie możesz dokonać kolejnej, dopóki nie ukończysz długiego "
        "odpoczynku.\n\nRaz w każdej swojej turze przed końcem przemiany możesz zadać dodatkowe obrażenia "
        "jednemu celowi, gdy zadajesz mu obrażenia atakiem albo czarem. Dodatkowe obrażenia są równe "
        "twojej premii z biegłości. Są to obrażenia nekrotyczne w przypadku Nekrotycznego całunu albo "
        "obrażenia od światłości w przypadku Niebiańskich skrzydeł i Wewnętrznego blasku."
    ),
    "hb4b6f30eg2b17g2d0dg2d38g75f0949d374e": (
        "Gdy osiągniesz 3. poziom postaci, możesz dokonać przemiany w ramach akcji dodatkowej, korzystając "
        "z jednej z dostępnych opcji. Przemiana trwa 1 minutę albo do chwili, gdy ją zakończysz (bez użycia "
        "akcji). Po przemianie nie możesz dokonać kolejnej, dopóki nie ukończysz długiego odpoczynku."
        "\n\nGdy zadajesz celowi obrażenia atakiem albo czarem, możesz zadać mu dodatkowe obrażenia równe swojej "
        "premii z biegłości. Są to obrażenia nekrotyczne w przypadku Nekrotycznego całunu albo obrażenia "
        "od światłości w przypadku Niebiańskich skrzydeł i Wewnętrznego blasku."
    ),
    "h947e63dfge856g93fdge133g7915f597706a": (
        "Palące światło chwilowo bije z twoich oczu i ust. Na czas przemiany emitujesz jasne światło w "
        "promieniu 3 m oraz słabe światło w promieniu dalszych 3 m. Na koniec każdej twojej tury każda "
        "istota w promieniu 3 m od ciebie otrzymuje obrażenia od światłości równe twojej premii z biegłości."
    ),
    "h4049a129gb079gf0dagb270g0aa72eb1171d": (
        "Palące światło chwilowo bije z twoich oczu i ust. Na czas przemiany emitujesz jasne światło w "
        "promieniu 3 m oraz słabe światło w promieniu dalszych 3 m. Na koniec każdej twojej tury każda "
        "istota w promieniu 3 m od ciebie otrzymuje obrażenia od światłości równe twojej premii z biegłości."
    ),
    "h6a146679g10b4gcab6g7371g8809ef5326f6": (
        "Twoje oczy na chwilę stają się otchłaniami ciemności, a z pleców wyrastają nielotne skrzydła. "
        "Wybrane przez ciebie istoty w promieniu 3 m muszą wykonać rzut obronny na Charyzmę; w razie "
        "niepowodzenia otrzymują stan Przerażenia na 1 minutę."
    ),
    "h3a16b87eg8dd3g9578gd609gbf2f106aa676": (
        "Twoje oczy na chwilę stają się otchłaniami ciemności, a z pleców wyrastają nielotne, widmowe "
        "skrzydła. Wszystkie istoty poza twoimi sojusznikami w promieniu 3 m muszą wykonać rzut obronny na "
        "Charyzmę; w razie niepowodzenia otrzymują stan Przerażenia do końca twojej następnej tury."
    ),
    "h9223661bgace2gba01g10dcgfc1ea09add5a": "Poziom 3: Inspiracja księżyca",
    "haca3aef8ga626gc323g22acg746bfa4a9426": "Poziom 3: Pierwotna wiedza",
    "h3911c437g16cagdddcgede4gaa0c643aec8c": "Poziom 6: Błogosławieństwa światła księżyca",
    "h3f223b42g605egefc2g504ag6ef36cc460ed": "Poziom 3: Grupowa regeneracja",
    "h3cc7fa69g03fdgb1f5g1a26g3dbd2b575ce8": (
        "Gdy korzystasz z Grupowej regeneracji, każdy wybrany sojusznik ma ułatwienie w testach k20 do "
        "początku twojej następnej tury."
    ),
    "h4def2360g5a4cgbe2fge70fgbe9d99d7fa1f": "Poziom 10: Mobilizujący zryw",
    "ha112c9d1gc29dg2a81g78e9g5ee83dc15b44": "Poziom 3: Lodowy odkrywca",
    "hf2ce8883g7e85g48fcgfb85geaec662b97b7": "Poziom 3: Szron łowcy",
    "h7d1048f2gc9feg4128g633ag3409fc6ecdc6": "Nie może wykonać akcji Odstąpienia.",
})

# Official Polish BG3 uses "znawstwo" for the Expertise rules term.  This
# pass removes several community/MT variants and cleans up the adjoining
# species and subclass prose without changing any handles or markup.
UID_OVERRIDES.update({
    "h32ed567egee36g91e1g2accgb992c0f4d730": (
        "Podczas nauki magii wybierasz również inną dziedzinę specjalizacji. Wybierz jedną z poniższych "
        "umiejętności, w której masz biegłość: <LSTag Type=\"Skills\" Tooltip=\"Arcana\">Wiedza "
        "tajemna</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"History\">Historia</LSTag>, Śledztwo, "
        "<LSTag Type=\"Skills\" Tooltip=\"Medicine\">Medycyna</LSTag>, <LSTag Type=\"Skills\" "
        "Tooltip=\"Nature\">Przyroda</LSTag> albo <LSTag Type=\"Skills\" Tooltip=\"Religion\">"
        "Religia</LSTag>. Zyskujesz znawstwo w wybranej umiejętności."
    ),
    "h2f5671feg10a3g6221g9db1gcd1af3a88f5b": "Poziom 2: Znawstwo",
    "h9e315a90g0705gb2c6g1a8eg13de362924de": (
        "Zyskujesz znawstwo (patrz słownik zasad) w dwóch wybranych umiejętnościach, w których masz "
        "biegłość. <LSTag Type=\"Skills\" Tooltip=\"Performance\">Występy</LSTag> i <LSTag Type=\"Skills\" "
        "Tooltip=\"Persuasion\">Perswazja</LSTag> są zalecane, jeśli masz w nich biegłość.\n\n"
        "Na 9. poziomie barda zyskujesz znawstwo w dwóch kolejnych wybranych umiejętnościach, w których "
        "masz biegłość."
    ),
    "hc9341211ge6c1g1fd9gddbeg13315817fedb": (
        "Zyskujesz biegłość w dwóch wybranych umiejętnościach spośród następujących: "
        "<LSTag Type=\"Skills\" Tooltip=\"Arcana\">Wiedza tajemna</LSTag>, <LSTag Type=\"Skills\" "
        "Tooltip=\"History\">Historia</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Nature\">Przyroda</LSTag> "
        "albo <LSTag Type=\"Skills\" Tooltip=\"Religion\">Religia</LSTag>. Zyskujesz znawstwo w obu "
        "wybranych umiejętnościach."
    ),
    "ha8b64524g7467g0f1eg9214gbd3da8ce6302": "Poziom 1: Znawstwo",
    "h75d54fe5g6285g141fgd2b8gca722e196ecc": (
        "Zyskujesz znawstwo w dwóch wybranych umiejętnościach, w których masz biegłość. "
        "<LSTag Type=\"Skills\" Tooltip=\"SleightOfHand\">Zwinne dłonie</LSTag> i <LSTag Type=\"Skills\" "
        "Tooltip=\"Stealth\">Skradanie się</LSTag> są zalecane, jeśli masz w nich biegłość.\n\n"
        "Na 6. poziomie łotra zyskujesz znawstwo w dwóch kolejnych wybranych umiejętnościach, w których "
        "masz biegłość."
    ),
    "h06b8380ag7f73g106agdf63g8dabbadb964c": (
        "Odwet. Natychmiast po tym, jak istota w promieniu 1,5 m od ciebie trafi cię atakiem wręcz, "
        "możesz wykonać przeciwko niej atak okazyjny.\n\nWszechstronny najemnik. Wybierz umiejętność, "
        "w której masz biegłość. Zyskujesz w niej znawstwo."
    ),
    "he09232a3g8429ge28bga994gd171ef3f3292": (
        "Odwet. Natychmiast po tym, jak istota w promieniu 1,5 m od ciebie trafi cię atakiem wręcz, "
        "możesz wykonać przeciwko niej atak okazyjny.\n\nWszechstronny najemnik. Wybierz umiejętność, "
        "w której masz biegłość. Zyskujesz w niej znawstwo."
    ),
    "ha6aeb659gba2ag0648g1d28g8d765621e3a9": (
        "Zyskujesz znawstwo we wszystkich następujących umiejętnościach: <LSTag Type=\"Skills\" "
        "Tooltip=\"Insight\">Intuicja</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">"
        "Zastraszanie</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Perswazja</LSTag> oraz "
        "<LSTag Type=\"Skills\" Tooltip=\"Performance\">Występy</LSTag>."
    ),
    "hda6df4cdg93a3gab23g3fd8ga7f8a4585d19": (
        "Zyskujesz znawstwo w testach <LSTag Type=\"Skills\" Tooltip=\"History\">Historii</LSTag>."
    ),
    "h83b92101gfc2bg31e9gf707gf2e81d4a43fc": (
        "Zyskujesz znawstwo w posługiwaniu się bronią palną. Ponadto w pierwszej turze walki możesz "
        "wykonać jeden atak bronią bez użycia akcji."
    ),
    "hb052fe34g86bfg992cg2672g146c445e9dc4": (
        "Gdy Moloch przyjmie cię jako swojego illriggera, zyskujesz <LSTag Tooltip=\"Expertise\">"
        "znawstwo</LSTag> w <LSTag Tooltip=\"AbilityCheck\">testach</LSTag> <LSTag Type=\"Skills\" "
        "Tooltip=\"Persuasion\">Perswazji</LSTag> i <LSTag Type=\"Skills\" Tooltip=\"Deception\">"
        "Oszustwa</LSTag>."
    ),
    "h4b29ebdegfa87g42bege4a2g3b10f7973640": (
        "Gdy Moloch przyjmie cię jako swojego illriggera, zyskujesz <LSTag Tooltip=\"Expertise\">"
        "znawstwo</LSTag> w <LSTag Tooltip=\"AbilityCheck\">testach</LSTag> <LSTag Type=\"Skills\" "
        "Tooltip=\"Persuasion\">Perswazji</LSTag> i <LSTag Type=\"Skills\" Tooltip=\"Deception\">"
        "Oszustwa</LSTag>."
    ),
    "h6e348a1aga0b0g9788gb85dgeba21fa79668": "Pogromca Smoków",
    "ha574dfdfgf055g69c1g9889gce2fffa674e6": (
        "Czarna Strzała, która powaliła smoka Smauga, mogła być do tego przeznaczona, lecz ręka, która "
        "posłała ją z taką siłą, była niezwykle mocna. Gdy rzucasz włócznią albo napinasz łuk, dbasz o "
        "pewny chwyt i celny strzał.\n\nPodczas ataku bronią dystansową używasz modyfikatora Siły zarówno "
        "do testu ataku, jak i rzutu na obrażenia; do obu musisz użyć tego samego modyfikatora. Jeśli w tej "
        "samej turze przemieścisz się najwyżej o połowę swojej szybkości i trafisz istotę atakiem bronią "
        "dystansową, możesz w ramach akcji dodatkowej sprawić, że atak zada dodatkowe 1k4 obrażeń typu "
        "zadawanego przez broń."
    ),
    "h80c3bb0dgd84cg63b6g9b47g339cb3415da6": (
        "Z twoich pleców na chwilę wyrastają dwa widmowe skrzydła. Do końca przemiany masz szybkość "
        "lotu równą swojej szybkości."
    ),
    "hbcd3d36fgdc84gb744gaaf6ge51968dbc88e": (
        "Z twoich pleców na chwilę wyrastają dwa widmowe skrzydła. Do końca przemiany masz szybkość "
        "lotu równą swojej szybkości."
    ),
    "h759d592bgce3eg0689gb28cgb0e2182d4aba": (
        "Kolegium Księżyca wywodzi się z prastarych kręgów druidycznych Wysp Moonshae, które powierzyły "
        "pierwszym bardom tej tradycji spisywanie dziejów wysp i ich mieszkańców. Bardowie tego kolegium "
        "wykorzystują magię fey wysp oraz pierwotną moc księżycowych studni, by wspierać sojuszników, "
        "chronić świat natury i znajdować natchnienie dla swej bardowskiej twórczości."
    ),
    "h16bfd443g2ac4gcdcegaa91gcadfccb20761": (
        "Poznajesz język druidzki i jedną sztuczkę z listy czarów druida. Sztuczka ta jest dla ciebie "
        "czarem barda, ale nie wlicza się do liczby znanych przez ciebie sztuczek.\n\nPonadto wybierz jedną "
        "z następujących umiejętności: <LSTag Type=\"Skills\" Tooltip=\"AnimalHandling\">Opieka nad "
        "zwierzętami</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Insight\">Intuicja</LSTag>, <LSTag "
        "Type=\"Skills\" Tooltip=\"Medicine\">Medycyna</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Nature\">"
        "Przyroda</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Perception\">Percepcja</LSTag> albo <LSTag "
        "Type=\"Skills\" Tooltip=\"Survival\">Sztuka przetrwania</LSTag>. Zyskujesz biegłość w wybranej "
        "umiejętności."
    ),
    "hdf72a045g6802g6864g7289gb8715a4c18b6": (
        "Przenikliwe zimno. Obrażenia zadawane przez twoje ataki bronią, czary łowcy i cechy łowcy ignorują "
        "odporność na obrażenia od zimna.\n\nOdporność na mróz. Masz odporność na obrażenia od zimna.\n\n"
        "Polarne uderzenia. Gdy trafiasz istotę testem ataku bronią, możesz zadać celowi dodatkowe 1k4 "
        "obrażeń od zimna. Cel może otrzymać te dodatkowe obrażenia tylko raz na turę. Gdy osiągasz 11. "
        "poziom łowcy, dodatkowe obrażenia wzrastają do 1k6."
    ),
    "hf17390fdg279dg4294gb86ag4e1049c6b097": (
        "Szron pokrywa cię i twoją zdobycz, chroniąc cię i krępując jej ruchy. Gdy rzucasz Znak łowcy, "
        "zyskujesz tymczasowe punkty wytrzymałości w liczbie równej sumie 1k10 i twojego poziomu łowcy."
        "\n\nPonadto istota oznaczona twoim Znakiem łowcy nie może wykonywać akcji Odstąpienia."
    ),
    "h319bdef0g52b5g7c9dg095eg8fdb31fd0953": (
        "Zyskujesz tymczasowe punkty wytrzymałości w liczbie równej sumie 1k10 i twojego poziomu łowcy."
    ),
})

# Follow-up audit of status and core-rule tags.  These entries either contained
# broken Polish grammar, untranslated 2024 mastery names, or a clear semantic
# error inherited from the shipped Polish BG3 string (Attack Rolls translated
# as Saving Throws).  Tooltip identifiers and placeholders stay unchanged.
UID_OVERRIDES.update({
    # Preserve title capitalization after the running-text resistance cleanup.
    "heda822d9g6ca8g4d69g862cg8e593ceb6f22": "Wtajemniczony: Odporność",
    "h8279b78cg9f64gf40egab20gf3b5ab80bc72": "Atut: Odporność (Charyzma)",
    "h264cac24g55adg2b42g5689g9ac57b287ff0": "Atut: Odporność (Kondycja)",
    "h4d896d4bg38ffgb852ge9c4g321634de4a1d": "Atut: Odporność (Zręczność)",
    "h28f453f2gecbagbf36g9580ga18155f4ed7c": "Atut: Odporność (Inteligencja)",
    "ha5d92735g8afdga8f3ge1c5g5b06d62a50e6": "Atut: Odporność (Siła)",
    "he4365c80ga72cgc5ebg1ae0g6a84db454a82": "Atut: Odporność (Mądrość)",
    "hfc97be68g0890g2eb4g60ceg4fcde289a6f3": "Poziom 3: Smocza Odporność",
    "h3860f913g1f6fg4b18g9ecfgabcab0169949": "Atut: Odporność Zakonu",
    "h10dbbaa0g2b5fg5521gc9cag50d5d54e8706": "Poziom 10: Odporność na czary",
    "hfd45d1c1g9dd3g206agfb7eg456c6af02ac0": (
        "Raz na <LSTag Tooltip=\"ShortRest\">krótki odpoczynek</LSTag>, jeśli liczba twoich "
        "<LSTag Tooltip=\"HitPoints\">punktów wytrzymałości</LSTag> spadnie do [1] podczas "
        "<LSTag Type=\"Status\" Tooltip=\"RAGE\">szału</LSTag>, zamiast <LSTag Type=\"Status\" "
        "Tooltip=\"DOWNED\">stracić przytomność</LSTag>, odzyskujesz punkty wytrzymałości w liczbie "
        "równej dwukrotności twojego poziomu barbarzyńcy."
    ),
    "hae6c4966g7a68ga1edg4bc6gae39ac7aeb6b": (
        "Ty i wszyscy pobliscy sojusznicy macie odporność na obrażenia nekrotyczne, psychiczne i od "
        "światłości. Aura znika, jeśli <LSTag Type=\"Status\" Tooltip=\"DOWNED\">stracisz "
        "przytomność</LSTag>."
    ),
    "he44a89e4gd251g9a1dg6abagca1e9807a226": (
        "Istota emituje słabe światło w promieniu [1] i nie może korzystać ze stanu "
        "<LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">niewidzialności</LSTag>."
    ),
    "he571e586gc384gf9bbg0231g7c7be2144adc": (
        "Rozpłyń się w mroku i zyskaj <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">"
        "niewidzialność</LSTag>."
    ),
    "h03f4e692g56c6g5001g17adg72f182951516": (
        "Nałóż klątwę dotykiem. Istota pod jej wpływem ma <LSTag Tooltip=\"Disadvantage\">"
        "utrudnienie</LSTag> w <LSTag Tooltip=\"AttackRoll\">testach ataku</LSTag> przeciwko tobie."
    ),
    "hc0faf0e3g6b1bgefbbge13cg61d3cdca920b": (
        "Nałóż klątwę dotykiem. Istota pod jej wpływem ma <LSTag Tooltip=\"Disadvantage\">"
        "utrudnienie</LSTag> w <LSTag Tooltip=\"AttackRoll\">testach ataku</LSTag> przeciwko tobie."
    ),
    "h2f5f424bg14ceg447ag33b9g312025e7738d": (
        "Zadaje dodatkowe [1] obrażeń bronią do walki wręcz, bronią improwizowaną i rzucanymi "
        "przedmiotami. <br><br>Sojusznicy mają <LSTag Tooltip=\"Advantage\">ułatwienie</LSTag> w "
        "<LSTag Tooltip=\"AttackRoll\">testach ataku</LSTag> przeciwko przeciwnikom w obrębie [2]."
        "<br><br>Ma również odporność na obrażenia fizyczne oraz ułatwienie w <LSTag "
        "Tooltip=\"AbilityCheck\">testach cechy</LSTag> i <LSTag Tooltip=\"SavingThrow\">rzutach "
        "obronnych</LSTag> na Siłę.<br><br>Nie może rzucać czarów ani utrzymywać koncentracji."
    ),
    "h708146b3g1fd7g7ca1g06e9g815f4a5e342b": (
        "Zadaje dodatkowe [1] obrażeń bronią do walki wręcz, bronią improwizowaną i rzucanymi "
        "przedmiotami. <br><br>Sojusznicy mają <LSTag Tooltip=\"Advantage\">ułatwienie</LSTag> w "
        "<LSTag Tooltip=\"AttackRoll\">testach ataku</LSTag> przeciwko przeciwnikom w obrębie [2]."
        "<br><br>Ma również odporność na obrażenia fizyczne oraz ułatwienie w <LSTag "
        "Tooltip=\"AbilityCheck\">testach cechy</LSTag> i <LSTag Tooltip=\"SavingThrow\">rzutach "
        "obronnych</LSTag> na Siłę.<br><br>Nie może rzucać czarów ani utrzymywać koncentracji."
    ),
    "h33a83d2bg7e97g9bebg4b1ag640c88459c92": (
        "Zadajesz dodatkowe obrażenia od kwasu w liczbie równej twojej <LSTag "
        "Tooltip=\"ProficiencyBonus\">premii z biegłości</LSTag>. Przy trafieniu tworzysz wokół celu "
        "kałużę kwasu, która zmniejsza jego <LSTag Tooltip=\"ArmourClass\">Klasę Pancerza</LSTag> o [1]."
    ),
    "h2c05bd1dg9548g9d0ag66dbgd31ce3af6dab": (
        "Gdy trafisz wroga <LSTag Tooltip=\"OpportunityAttack\">atakiem okazyjnym</LSTag>, możesz "
        "zmniejszyć jego szybkość do 0 do końca bieżącej tury. W swojej następnej turze twoja "
        "<LSTag Tooltip=\"MovementSpeed\">szybkość ruchu</LSTag> zwiększa się o [1]."
    ),
    "h2c920020g431dge64eg8e26g01537cb63450": (
        "Gdy wykonujesz atak bronią, możesz dodatkowo zastosować do niego jedną z następujących "
        "właściwości mistrzostwa: Popchnięcie, <LSTag Type=\"Passive\" "
        "Tooltip=\"Fighter_9_TacticalMaster_Sap\">Osłabienie</LSTag> albo Spowolnienie."
    ),
    "h858b33e5g3b62g9b7fg692fg50cb883ac903": "Mistrz taktyki: Popchnięcie",
    "h53c4a6c9g7930g55a2ga6d9g74f864e922d2": "Mistrz taktyki: Osłabienie",
    "h1bcf613agff33gdd61g8288g83128f467505": "Mistrz taktyki: Spowolnienie",
    "h0558e9e5gd74bg0f9fg2820gc589e678173e": (
        "Możesz dodatkowo zastosować do tego ataku właściwość mistrzostwa Osłabienie."
    ),
    "hfd56201dg7690g59deg5771g7c00df6810c1": (
        "Możesz dodatkowo zastosować do tego ataku właściwość mistrzostwa Spowolnienie."
    ),
    "h1261d64eg6ff9gfcfcg691agbb4378c7bc02": (
        "Do sprawnego poruszania się w ciężkiej zbroi wymagana jest Siła 13."
    ),
    "h1b6d335fg71e3g921bg96efgd3563a3e9d4b": (
        "Paladyn i pobliscy sojusznicy mają odporność na obrażenia nekrotyczne, psychiczne i od światłości."
    ),
    "he4565ab2g2625gaeb8g694eg929ab02e448c": (
        "Paladyn i pobliscy sojusznicy mają odporność na obrażenia nekrotyczne, psychiczne i od światłości."
    ),
    "hcd9d1097ga19dg7c70g4d29gc5f6d7f4a948": (
        "Twój Gniew morza zapewnia ci dwa dodatkowe efekty, gdy jest aktywny, jak opisano poniżej.\n\n"
        "Lot. Zyskujesz szybkość lotu równą swojej szybkości ruchu.\n\n"
        "Odporność. Masz odporność na obrażenia od zimna, elektryczności i dźwięku."
    ),
    "hc5a84737g0024g47c9g1052gdf0e4350d3ec": (
        "Niebiańskie skrzydła. Z twoich pleców tymczasowo wyrastają widmowe skrzydła. Dopóki "
        "transformacja trwa, masz szybkość lotu równą swojej szybkości ruchu.\n\n"
        "Wewnętrzny blask. Z twoich oczu i ust tymczasowo bije palące światło. Podczas trwania "
        "efektu emitujesz jasne światło w promieniu 3 m oraz słabe światło na dalsze 3 m. Ponadto "
        "na koniec każdej ze swoich tur każda istota w promieniu 3 m od ciebie otrzymuje obrażenia "
        "od światłości w liczbie równej twojej premii z biegłości.\n\n"
        "Nekrotyczny całun. Twoje oczy na krótko stają się otchłaniami ciemności, a z twoich pleców "
        "tymczasowo wyrastają nielotne skrzydła. Wszystkie istoty poza twoimi sojusznikami w promieniu "
        "3 m od ciebie muszą zdać rzut obronny na Charyzmę (ST wynosi 8 + twój modyfikator Charyzmy "
        "+ twoja premia z biegłości) albo zyskują stan przerażenia do końca twojej następnej tury."
    ),
    "h76a22005g0fd5g7e8bgedc0g71ee16b02cd7": (
        "Ostrze jest dla ciebie bronią finezyjną, a wykonane nim ataki przeciwko wynaturzeniom, "
        "czartom i nieumarłym ignorują odporność na obrażenia."
    ),
    "h0e363cf3g0162gc215g7872g2aa8512bdbd6": (
        "Barbarzyńcy kroczący Ścieżką Zeloty otrzymują łaski od boga lub panteonu. Przeżywają swój "
        "<LSTag Type=\"Status\" Tooltip=\"RAGE\">szał</LSTag> jako ekstatyczny stan boskiego "
        "zjednoczenia, który napełnia ich mocą. Często są sojusznikami kapłanów i innych wyznawców "
        "swojego boga lub panteonu."
    ),
    "h054c34e8gf7acg1ce5g9297g2f198a57cc90": (
        "Barbarzyńcy kroczący Ścieżką Berserkera kierują swój <LSTag Type=\"Status\" "
        "Tooltip=\"RAGE\">szał</LSTag> przede wszystkim ku przemocy. Ich ścieżkę wyznacza nieokiełznana "
        "furia; rozkoszują się chaosem bitwy, pozwalając, by <LSTag Type=\"Status\" Tooltip=\"RAGE\">"
        "szał</LSTag> nimi zawładnął i napełnił ich mocą."
    ),
    "hb18d7e9eg37d4g8642g14a4g092815e31296": (
        "Dotknięta istota jest duszona garotą, <LSTag Type=\"Status\" Tooltip=\"SILENCED\">"
        "uciszona</LSTag> i otrzymuje [1] na turę."
    ),
    "h8f70346agdae6g92b8gc487gb1bbc53e7cbd": (
        "<LSTag Type=\"Status\" Tooltip=\"TURNED\">Odpędź</LSTag> wynaturzenia, niebian, "
        "żywiołaki, fey albo czarty w pobliżu. Muszą uciekać i nie mogą się do ciebie zbliżyć."
    ),
    "h409cb932g8ed1gc110g3616g0fa1bc73cc21": (
        "Nakaż istocie, by natychmiast <LSTag Type=\"Status\" Tooltip=\"PRONE\">padła</LSTag> na ziemię."
    ),
    "ha798ee23gc1b7gfd05g86c0ga477ff4d0a9d": (
        "Masz ułatwienie w rzutach obronnych przeciwko czarom oraz odporność na obrażenia od czarów."
    ),
})

# Follow-up audit of condition casing, deity names, movement rules, and several
# descriptions whose earlier wording changed the mechanic or broke Polish
# grammar. Running-text condition names follow the lowercase convention used
# by the shipped Polish BG3 localization.
ORC_ORIGIN_TEXT = (
    "Orkowie wierzą, że stworzył ich Gruumsh, potężny bóg, który przemierzał rozległe przestrzenie "
    "Sfery Materialnej. Gruumsh obdarzył swoje dzieci darami, które pomagają im przemierzać wielkie "
    "równiny, rozległe jaskinie i wzburzone morza oraz stawiać czoła czającym się tam potworom. Nawet "
    "gdy zaczynają czcić innych bogów, orkowie zachowują dary Gruumsha: wytrzymałość, determinację i "
    "zdolność widzenia w ciemności."
)
for duplicate_uid in (
    "h449084fbgb69ag0519ge52dg161d6d97eae4",
    "hefd844a2gf6d5g1299g89e1ge8acaed81bb9",
):
    UID_OVERRIDES[duplicate_uid] = ORC_ORIGIN_TEXT

CONJURE_MINOR_ELEMENTALS_TEXT = (
    "Przywołujesz duchy z Planów Żywiołów, które przez czas trwania czaru krążą wokół ciebie w "
    "emanacji o promieniu 4,5 m. Dopóki czar trwa, każdy twój atak zadaje dodatkowe obrażenia, gdy "
    "trafiasz istotę w obrębie emanacji. Podczas wykonywania ataku wybierasz typ tych obrażeń: od "
    "kwasu, zimna, ognia albo elektryczności.\n\nPonadto obszar emanacji jest trudnym terenem dla "
    "twoich wrogów."
)
CONJURE_MINOR_ELEMENTALS_SCALING_TEXT = (
    "Przywołujesz duchy z Planów Żywiołów, które przez czas trwania czaru krążą wokół ciebie w "
    "emanacji o promieniu 4,5 m. Dopóki czar trwa, każdy twój atak zadaje dodatkowe [1] obrażeń, gdy "
    "trafiasz istotę w obrębie emanacji. Podczas wykonywania ataku wybierasz typ tych obrażeń: od "
    "kwasu, zimna, ognia albo elektryczności.\n\nPonadto obszar emanacji jest trudnym terenem dla "
    "twoich wrogów."
)
UID_OVERRIDES["hb170c461g64a8ga1b1g8e92g84265039c932"] = CONJURE_MINOR_ELEMENTALS_TEXT
for duplicate_uid in (
    "hd5c12bafga9aagfb28g8efbg6a56a1770bd5",
    "h11cbe00dg7613g77ebgcbf6g82af126dc834",
    "hf72ba7eeg74aeg8025g8d10g383f2aab6a51",
):
    UID_OVERRIDES[duplicate_uid] = CONJURE_MINOR_ELEMENTALS_SCALING_TEXT

UID_OVERRIDES.update({
    "hcd10eb1fgc367ga39egd371g5e071e079549": (
        "Możesz przemieścić się prosto w stronę celu na odległość nie większą niż połowa swojej "
        "szybkości ruchu, nie prowokując ataków okazyjnych."
    ),
    "h035b29c1g51d0ge9f8gb63fgc75cd5045b0c": (
        "Zawsze masz przygotowane czary Zauroczenie osoby i Lustrzane odbicia.\n\nPonadto "
        "bezpośrednio po rzuceniu czaru ze szkoły uroków lub iluzji z użyciem komórki czaru możesz "
        "zmusić istotę, którą widzisz w odległości do [1] od siebie, do wykonania rzutu obronnego na "
        "Mądrość przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu cel otrzymuje wybrany "
        "przez ciebie stan zauroczenia albo przerażenia na 1 minutę."
    ),
    "h374216bbgf985gc96cg64b3g959b101fd376": (
        "Obrażenia psychiczne zadawane przez twoje Straszliwe uderzenie wzrastają do 2k8. Cel musi "
        "wykonać rzut obronny na Mądrość przeciwko twojemu ST obrony przed czarami. Przy "
        "niepowodzeniu otrzymuje stan przerażenia do początku twojej następnej tury.\n\nDziałasz dość "
        "szybko, by zamienić chybienie w kolejne uderzenie. Gdy chybisz atakiem bronią, możesz bez "
        "dodatkowych kosztów wykonać jeszcze jeden atak bronią."
    ),
    "h1db10ba1g91aagc5a2g2acbg5853ba104450": (
        "Warunek wstępny: Drakon\n\nGdy wpadasz w gniew, możesz emanować grozą.\n\nZyskujesz "
        "jedno dodatkowe użycie zionięcia.\n\nMożesz zużyć jedno użycie zionięcia, aby ryknąć i "
        "zmusić każdą wybraną istotę w promieniu 9 m do wykonania rzutu obronnego na Mądrość. Przy "
        "niepowodzeniu cel otrzymuje na 1 minutę stan przerażenia, którego źródłem jesteś."
    ),
    "hfcbd3784g4436g3a40g1260g63eb8006c7fa": (
        "Twoje oddanie dzikim, nadnaturalnym istotom zmienia cię jeszcze bardziej. Po przemianie za "
        "pomocą <LSTag Type=\"Passive\" Tooltip=\"HollowWarden_3_WrathOfTheWild\">Gniewu "
        "dziczy</LSTag> zyskujesz następujące dodatkowe korzyści.\n\nGroźna aura. Gdy istocie nie "
        "powiedzie się rzut obronny przeciwko twojej <LSTag Type=\"Status\" "
        "Tooltip=\"UNNERVING_AURA\">Niepokojącej aurze</LSTag>, nie może ona odzyskiwać punktów "
        "wytrzymałości ani wykonywać reakcji do początku twojej następnej tury.\n\nZłowieszcze "
        "ciosy. Gdy trafisz testem ataku istotę, która ma stan przerażenia, atak zadaje dodatkowe "
        "obrażenia w liczbie równej twojemu modyfikatorowi Mądrości."
    ),
    "h08797ed7gc753g8f41gd903g4ec54ed567d1": (
        "Kierujesz energię Morza Astralnego, uwalniając z siebie potok magii. Wybierz zimno albo "
        "światłość jako typ przekazywanej energii. Każda istota w stożku o długości 9 m wykonuje rzut "
        "obronny na Zręczność. Przy niepowodzeniu otrzymuje obrażenia wybranego typu oraz dodatkowy "
        "efekt zależny od tego typu:\n\nZimno. Cel ma utrudnienie w następnym teście k20 wykonanym "
        "przed końcem twojej następnej tury.\nŚwiatłość. Cel otrzymuje stan oślepienia do końca twojej "
        "następnej tury.\n\nPrzy powodzeniu cel otrzymuje tylko połowę obrażeń."
    ),
    "ha031b042gd64ag0b74g62b9g7aa92b2a2119": (
        "Potomek Trójki czerpie moc ze złowrogich bogów znanych we Wrotach Baldura jako Martwa "
        "Trójka: Bane'a, boga tyranii; Bhaala, boga przemocy i mordu; oraz Myrkula, boga śmierci. "
        "Niektórzy łotrzykowie tej podklasy gorliwie oddają się tym trzem makabrycznym bóstwom, "
        "innych zaś sprowadza na tę ścieżkę klątwa. W obu przypadkach moc potomka przejawia się w "
        "rozmaitych okultystycznych darach oraz niezwykłym talencie do zadawania ciosów i wzbudzania "
        "trwogi.\n\nPotomkowie Trójki najczęściej występują we Wrotach Baldura, gdzie członkowie "
        "Martwej Trójki żyli jako śmiertelnicy, zanim osiągnęli boskość. Tajne kulty Bane'a, Bhaala i "
        "Myrkula często zaliczają ich do swoich najcenniejszych agentów. Poza Wrotami Baldura świeckie "
        "gildie złodziei — takie jak Złodzieje Cienia z Amn czy Gildia Xanathara w Waterdeep — mogą "
        "powierzyć Potomkowi Trójki wyjątkowo krwawe zlecenie."
    ),
    "h717c2effgcfefg6531g04eeg3d6a10c88329": (
        "Zawierasz złowrogie przymierze, wybierając jednego z członków Martwej Trójki: Bane'a, "
        "Bhaala albo Myrkula. Twój wybór zapewnia ci odporność na określony typ obrażeń oraz możliwość "
        "rzucania powiązanej sztuczki, przy czym Inteligencja jest twoją cechą bazową rzucania "
        "czarów.\n\nJeśli wybierzesz Bane'a, zyskujesz odporność na obrażenia psychiczne i możesz "
        "rzucać <LSTag Type=\"Spell\" Tooltip=\"Target_ImprovedMinorIllusion\">Pomniejszą "
        "iluzję</LSTag>.\n\nJeśli wybierzesz Bhaala, zyskujesz odporność na obrażenia od trucizny i "
        "możesz rzucać <LSTag Type=\"Spell\" Tooltip=\"Shout_BladeWard\">Osłonę przed "
        "orężem</LSTag>.\n\nJeśli wybierzesz Myrkula, zyskujesz odporność na obrażenia nekrotyczne "
        "i możesz rzucać Przeszywający dotyk.\n\nWybrane bóstwo możesz zmienić po każdym długim "
        "odpoczynku."
    ),
    "hed1840dbga25bga18bg158cg2e3656728e43": (
        "Zawierasz złowrogie przymierze, wybierając jednego z członków Martwej Trójki: Bane'a, "
        "Bhaala albo Myrkula. Twój wybór zapewnia ci odporność na określony typ obrażeń oraz możliwość "
        "rzucania powiązanej sztuczki, przy czym Inteligencja jest twoją cechą bazową rzucania czarów."
    ),
    "h6d6ec091g6782g7736g3633g063bf2cee187": "Złowrogie oddanie: Bane",
    "h7601f4ccg5ecfg89a8gf4d4gc425820bf2a2": (
        "Jeśli wybierzesz Bane'a, zyskujesz odporność na obrażenia psychiczne i możesz rzucać "
        "<LSTag Type=\"Spell\" Tooltip=\"Target_ImprovedMinorIllusion\">Pomniejszą iluzję</LSTag>."
    ),
    "h9a96305agf2f9g7267gdc69g37c278977066": "Złowrogie oddanie: Bane",
    "h8caea2f7gd7feg90a5gc318g2cfb95c6f90b": (
        "Szepczesz pod nosem boskie słowo, uważając, by nie wypowiedzieć go zbyt głośno, ponieważ "
        "taka niebiańska moc nie jest przeznaczona dla niegodnych. Wykonaj dystansowy atak czarem "
        "przeciwko celowi w zasięgu. Przy trafieniu cel otrzymuje obrażenia od światłości. Jeśli cel "
        "jest istotą fey, czartem albo nieumarłym, jego szybkość ruchu zmniejsza się o 3 m i nie może "
        "wykonywać reakcji do końca swojej następnej tury."
    ),
    "h4fb83fe3g593ag7f0cg6424g2a7ebbb50df8": (
        "Jeśli cel jest istotą fey, czartem albo nieumarłym, jego szybkość ruchu zmniejsza się o 3 m "
        "i nie może wykonywać reakcji do końca swojej następnej tury."
    ),
    "h520a3350gab70g330fge64fgd34f7914b820": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie Aktu wiary, aby otworzyć planarną "
        "szczelinę w widocznym punkcie w promieniu 18 m. Szczelina tworzy potężną próżnię w kuli o "
        "promieniu 4,5 m wokół tego punktu. Każda istota na tym obszarze wykonuje rzut obronny na "
        "Zręczność. Przy niepowodzeniu otrzymuje obrażenia od mocy w liczbie równej 1k8 + twój poziom "
        "kleryka i zostaje przyciągnięta o maksymalnie 4,5 m w stronę szczeliny. Przy powodzeniu "
        "otrzymuje tylko połowę tych obrażeń. Następnie szczelina znika."
    ),
    "h62513dd3g7a62g4659g151cg25df749019af": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie Aktu wiary, aby otworzyć planarną "
        "szczelinę w widocznym punkcie w promieniu 18 m. Szczelina tworzy potężną próżnię w kuli o "
        "promieniu 4,5 m wokół tego punktu. Każda istota na tym obszarze wykonuje rzut obronny na "
        "Zręczność. Przy niepowodzeniu otrzymuje obrażenia od mocy w liczbie równej 1k8 + twój poziom "
        "kleryka i zostaje przyciągnięta o maksymalnie 4,5 m w stronę szczeliny. Przy powodzeniu "
        "otrzymuje tylko połowę tych obrażeń. Następnie szczelina znika."
    ),
    "h5fe7400ag82f7g6073g3bcbgd343cec9bd16": (
        "Ta broń zapewnia premię +[1] do testów ataku, obrażeń, <LSTag "
        "Tooltip=\"SpellDifficultyClass\">ST rzutów przeciwko swoim czarom</LSTag> oraz <LSTag "
        "Tooltip=\"AttackRoll\">testów ataku</LSTag> czarami."
    ),
    "h99e76e2eg9ad8ge1c9g7478g77f49aa7113e": (
        "Ta broń zapewnia premię +[1] do testów ataku, obrażeń, <LSTag "
        "Tooltip=\"SpellDifficultyClass\">ST rzutów przeciwko swoim czarom</LSTag> oraz <LSTag "
        "Tooltip=\"AttackRoll\">testów ataku</LSTag> czarami."
    ),
    "h64a85505gb9ccg347eg37efg4472a54e2380": (
        "Otrzymuje 2k4+[1] <LSTag Tooltip=\"TemporaryHitPoints\">tymczasowych punktów "
        "wytrzymałości</LSTag>."
    ),
})

# Follow-up audit of composite feature and spell names. These handles had
# independently translated prefixes/suffixes which drifted away from the
# canonical Polish title used elsewhere in the same localization (and, where
# available, from the terminology shipped by Polish BG3).
UID_OVERRIDES.update({
    "h6002075bg4feegb25ag03b5g8e88a4351c0f": "Poziom 5: Źródło inspiracji",
    "h0dd0eba8g9b93g7909g9d9cg2a09e01a4c46": "Poziom 1: Boski porządek: Obrońca",
    "hc0f7da49g83b0g2364gd22fg0e72e6d0f671": "Poziom 1: Boski porządek: Słowo blasku",
    "h4d5b8b7cg1eddg15a0g6e0cgb4e68f50ee06": "Poziom 1: Boski porządek: Wskazówki",
    "h865f785bge303g1b8ag2f0egee91191a55fd": "Poziom 1: Boski porządek: Światło",
    "h0bfe486dga99eg5aefg818agacd35ff6e130": "Poziom 1: Boski porządek: Pękające ścięgno",
    "hd5ac78c8g2d8cg02bag6ebbg2f9ccd67bc36": "Poziom 1: Boski porządek: Odporność",
    "h63c03147gca42g60bdgfa7ag47ceb695bc38": "Poziom 1: Boski porządek: Święty płomień",
    "hf2f5e5c4g141ag2b8egb90cg9ff6727b6910": "Poziom 1: Boski porządek: Powstrzymanie śmierci",
    "h50136471gff21g505fg888cgf856fc01281a": "Poziom 1: Boski porządek: Taumaturgia",
    "h9b0eeaeeg6a13gc99dg6669gc97c57ec0db5": "Poziom 1: Boski porządek: Żałobny dzwon",
    "h1193aa13ge0d7ge702g2f85ga0c0527d229d": "Poziom 1: Pierwotny porządek: Strażnik",
    "hdc66e2feg6dc9g8e0dg69c3g1ac135e77240": "Poziom 1: Pierwotny porządek: Wskazówki",
    "h4e0c0b74gabceg8644g0a67g8c877d23dd83": "Poziom 1: Pierwotny porządek: Trujący rozprysk",
    "h5307ff13g4736g2ce2ga66fg11f20a990de2": "Poziom 1: Pierwotny porządek: Wywołanie płomienia",
    "h55c47b09ga380g8cf2g15b8g2bedd46fe8e9": "Poziom 1: Pierwotny porządek: Odporność",
    "hd0c364a3g050eg598bgd2fdg4c1b525be149": "Poziom 1: Pierwotny porządek: Shillelagh",
    "hab8ea7d9g7419g79d4ge012g86380a295a02": "Poziom 1: Pierwotny porządek: Powstrzymanie śmierci",
    "hd5bb58c8g9203g4533gc615ga31bea2a2187": "Poziom 1: Pierwotny porządek: Gwiezdny ognik",
    "hc7a0905fg5836g8050gb036gd435c6a53ffd": "Poziom 1: Pierwotny porządek: Cierniowy bicz",
    "h566f5dd1g1db3g0d0age62cg0ff1909892ef": "Poziom 1: Pierwotny porządek: Grzmot",
    "h86990efage02cg7a58gc14dgac02e5274f97": "Poziom 5: Dzikie odrodzenie",
    "h7f91f61fg551cg9fe6g9a0cg340e7bc48a41": "Poziom 10: Krok w blasku księżyca",
    "hcf67e29ag6032g30cfgf7dbg0fb20210f91d": "Użycie Kroku w blasku księżyca",
    "hcd5cf1b2gd583gccb7gb15cg0cd8f525eccb": "Liczba użyć Kroku w blasku księżyca.",
    "h3a4d5e28gabe3g3168ge119g17a00c4aa941": "Przywołaj Runę ognia",
    "hcb4e031eg6175g6174g6466gcc87b839601d": (
        "Gdy trafisz cel atakiem Pistoletów z palców, możesz zużyć jedną kość ryzyka i dodać "
        "jej wynik do rzutu na obrażenia."
    ),
    "h4087e43dg1626g7141gb492g08612b1d6f08": "Poziom 7: Płomienny kanał",
    "h5632b4f6g50degba74g0caaga04a7e569f75": "Obrażenia Mściwego ostrza",
    "h144805ebgf1c3gf55bg8676gdc4af6ca5ea9": "Obrażenia Mściwego ostrza",
    "h3078333fg393bg6e2agaff6gd37adce9760c": "Obrażenia Mściwego ostrza",
    "hd2d76fb0g487cg3ab3g3908g9f58ed8e7217": (
        "Po osiągnięciu określonych poziomów Zaklinacza wskazanych w tabeli Czarów psionicznych "
        "zawsze masz przygotowane wymienione w niej czary.\n\nNa 3. poziomie są to Ramiona Hadara, "
        "Wyciszenie emocji, Wykrycie myśli, Fałszywe podszepty i Myślowy odłamek; na 5. poziomie "
        "dodatkowo — Głód Hadara; na 7. poziomie — Czarne macki Evarda; a na 9. poziomie — Telekineza."
    ),
    "h463f00d2g43d4g6387ga3e8g5af46bc31369": "Myślowy odłamek (utrzymujący się)",
    "h41d2ff5cgefb3g4750gfbbfg9ce76cd22456": "Poziom 3: Stalowy obrońca",
    "he182f30fgc762gfc22g6adegda911d4ae8ea": (
        "Twoje majsterkowanie dało ci towarzysza — stalowego obrońcę."
    ),
    "h6d2cfddegb7bag99e2g6ffbg6a101cdf219d": "Poziom 9: Tajemny wstrząs",
    "hcbe0e0aeg4adbgf201g248cg78fdbe7712a4": "Tajemny wstrząs (stalowy obrońca)",
    "h02a16612g51dege910g582fg8824be4f2aee": (
        "Po osiągnięciu poziomu Łowcy wskazanego w tabeli Czarów Strażnika Pustki zawsze masz "
        "przygotowane wymienione w niej czary: na 3. poziomie — Gniewne ugodzenie, na 5. poziomie — "
        "Zbroja śmierci, a na 9. poziomie — Widmowy wierzchowiec."
    ),
    "hd23192ffgdf59ga725g1c97g7e364650fe0c": (
        "Na 3. poziomie zawsze masz przygotowane Gniewne ugodzenie, na 5. poziomie — Zbroję śmierci, "
        "a na 9. poziomie — Widmowego wierzchowca."
    ),
    "h4ed71b8cg3ed3gd84eg3c79gb92ad8cf0e94": (
        "Po osiągnięciu określonych poziomów Zaklinacza zawsze masz przygotowane następujące czary: "
        "na 3. poziomie — Ostrze zielonego płomienia, Prawdziwe uderzenie, Heroizm, Magiczna broń, "
        "Lustrzane odbicia i Tarcza; na 5. poziomie — <LSTag Type=\"Spell\" Tooltip=\"Target_Haste\">"
        "Przyspieszenie</LSTag> i Widmowy wierzchowiec; na 7. poziomie — Osłona przed śmiercią i "
        "Kamienna skóra; a na 9. poziomie — Unieruchomienie potwora. Czary te nie wliczają się do "
        "liczby czarów, które możesz przygotować."
    ),
    "h4336900ag6e5egc73bgadb8g0a8300eeb536": (
        "Magia twojego patrona sprawia, że zawsze masz przygotowane określone czary. Gdy osiągasz "
        "poziom Czarownika wskazany w tabeli Czarów Hexblade’a, od tej pory zawsze masz przygotowane "
        "wymienione w niej czary. Na 3. poziomie są to <LSTag Type=\"Spell\" "
        "Tooltip=\"Shout_ArcaneVigor\">Magiczna krzepa</LSTag>, Urok, Magiczna broń, Tarcza i "
        "Gniewne ugodzenie; na 5. poziomie — Nałożenie klątwy i Przywołanie ognia zaporowego; na "
        "7. poziomie — Swoboda ruchu i Wstrząsające ugodzenie; na 9. poziomie — Uderzenie stalowego "
        "wichru."
    ),
    "h6b8ec4b1g6350g0a0ag1d7dgc74d66ad8dd7": (
        "Na 3. poziomie zyskujesz Magiczną krzepę, Urok, Magiczną broń, Tarczę i Gniewne ugodzenie; "
        "na 5. poziomie — Nałożenie klątwy i Przywołanie ognia zaporowego; na 7. poziomie — Swobodę "
        "ruchu i Wstrząsające ugodzenie; na 9. poziomie — Uderzenie stalowego wichru."
    ),
    "had6cf5adg8eb1gc683g7f11gab246e2b6b44": (
        "Wędrówka chmur (olbrzym chmurowy). W ramach akcji dodatkowej magicznie teleportujesz się "
        "na odległość do 9 m na widoczne, niezajęte miejsce."
    ),
    "hf91e618bg7cfcg3668g95bbg4b7e8eb659d9": "Burza magicznego ognia: Zakłócenie czarów",
    "h2d7fc4afgebcbg804ag8764g1902de76e587": "Burza magicznego ognia: Obrażenia od światłości",
    "h81c2ba2bgde76gcf4dgb0feg9c1e82f5c048": "Przesuń Chmurę sztyletów",
    "h933efb07gb6d9g6ac3g1616gcb30169f9ef8": "Przesuń Chmurę sztyletów",
    "hf9903a34g76c3gfdf1g4be2g6ded0a0cde47": "Przesuń Chmurę sztyletów",
    "h91d412b9gc3c1g03ddg9d69g14b5660c1d16": "Przesuń Chmurę sztyletów",
    "haaf05dcegc1c7g957cg76bagbacf907adfb7": "Przesuń Chmurę sztyletów",
    "h39f64ea5gb60eg3361ga734gb5f1af066885": "Aura Tańca ognia",
    "hc78c376dg616ag7239gb066ga93738880899": "Atak bronią: Widmowe cięcie",
    "h63ced89eg89ebg0483ga272g25ce1e27bec3": "Cel Widmowego cięcia",
    "h95052719gb237gac57g92e1g14b60980710f": "Atak Widmowym cięciem",
    "h5f04addfg41ecgbc72gedadga5ba2a2eea90": "Aura Kręgu mocy",
    "hbf3f7449g1ed3gab0dgc670g9f81ada8e42a": (
        "Paladyni, którzy złożą Przysięgę Podboju, uzyskują dostęp do Zbroi Agathys i Rozkazu na "
        "3. poziomie, Unieruchomienia osoby i Duchowej broni na 5. poziomie oraz Nałożenia klątwy "
        "i Strachu na 9. poziomie."
    ),
    "h7731d2eag11ffg44e4g8569ga5e35e0e6de9": (
        "Paladyni, którzy złożą Przysięgę Obserwatorów, uzyskują dostęp do Ochrony przed dobrem i "
        "złem oraz Tarczy na 3. poziomie, Księżycowego promienia i Widzenia niewidzialnego na "
        "5. poziomie oraz Przeciwzaklęcia i Duchowych strażników na 9. poziomie."
    ),
    "h434df1f3gdadag1149g4c36g6bfc2c7a1bec": (
        "Po osiągnięciu określonych poziomów kleryka zawsze masz przygotowane następujące czary: "
        "na 3. poziomie — Blask faerie, Uśpienie, Księżycowy promień i Widzenie niewidzialnego; na "
        "5. poziomie — Aura witalności i Uderzenie pustki; na 7. poziomie — Swoboda ruchu i "
        "<LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">Większa niewidzialność</LSTag>; "
        "a na 9. poziomie — Krąg mocy i Świt. Czary te nie wliczają się do liczby czarów, które "
        "możesz przygotować."
    ),
})

POST_REFINEMENT_UID_OVERRIDES = {
    # Keep the official BG3 term lowercase in ordinary running text. Linked
    # spell/action-resource labels retain the capitalization shipped by BG3.
    "h5d1b01ffgd776g8ca4gd2edgb4e5e0068ad7": (
        "Ponadto możesz zużyć komórkę czaru (bez konieczności użycia akcji), aby odzyskać jedno zużyte "
        "użycie bardowskiej inspiracji."
    ),
    # In source-aware terminology, Bane normally means the spell Zguba. These
    # six handles refer to the deity instead, so their proper name must survive
    # that otherwise-correct replacement.
    "ha031b042gd64ag0b74g62b9g7aa92b2a2119": UID_OVERRIDES[
        "ha031b042gd64ag0b74g62b9g7aa92b2a2119"
    ],
    "h717c2effgcfefg6531g04eeg3d6a10c88329": UID_OVERRIDES[
        "h717c2effgcfefg6531g04eeg3d6a10c88329"
    ],
    "hed1840dbga25bga18bg158cg2e3656728e43": UID_OVERRIDES[
        "hed1840dbga25bga18bg158cg2e3656728e43"
    ],
    "h6d6ec091g6782g7736g3633g063bf2cee187": UID_OVERRIDES[
        "h6d6ec091g6782g7736g3633g063bf2cee187"
    ],
    "h7601f4ccg5ecfg89a8gf4d4gc425820bf2a2": UID_OVERRIDES[
        "h7601f4ccg5ecfg89a8gf4d4gc425820bf2a2"
    ],
    "h9a96305agf2f9g7267gdc69g37c278977066": UID_OVERRIDES[
        "h9a96305agf2f9g7267gdc69g37c278977066"
    ],
    "h22179fdag3286gcd27g7facg8e73f5c76e01": UID_OVERRIDES[
        "h22179fdag3286gcd27g7facg8e73f5c76e01"
    ],
    "hf106deb5gfb07g4bdeg0a01g623dd85de6b9": (
        "Pieśniarze klingi opanowują tradycję magii, która łączy fechtunek i taniec. "
        "W walce Pieśniarz klingi wykonuje złożone, eleganckie manewry, które odpierają "
        "zagrożenia i pozwalają mu kierować magię w niszczycielskie ataki oraz przebiegłą "
        "obronę. Wielu, którzy widzieli Pieśniarza klingi w akcji, wspomina ten pokaz jako "
        "jedno z najpiękniejszych doświadczeń w swoim życiu — wspaniały taniec, któremu "
        "towarzyszy śpiewająca klinga.\n\n"
        "Pieśń klingi wiąże się ze starożytnymi elfimi społecznościami, które jako pierwsze "
        "opanowały tę sztukę i ukuły to określenie. Nawet dziś większość Pieśniarzy klingi "
        "wywodzi się ze starych elfich krain, takich jak Myth Drannor, albo ze społeczności "
        "nieelfich, które dzielą ziemię i historię z elfami, takich jak Srebrne Marchie. "
        "Niezależnie od pochodzenia, Pieśniarze klingi niosą swe talenty po całych Krainach, "
        "by pomagać zwykłym ludziom i dokonywać bohaterskich czynów. Większość społeczności "
        "wita przybycie Pieśniarza klingi jako dobrą wróżbę."
    ),
}

# Follow-up terminology and semantic corrections. These are applied after the
# generic refinement passes so that the class-feature vocabulary remains
# consistent with the shipped Polish BG3 localization and the established
# Polish D&D 2024 community translation where BG3 has no equivalent.
POST_REFINEMENT_UID_OVERRIDES.update({
    # Arcane Armor: the Polish D&D 2024 community term is "Magiczny pancerz".
    "h5e04a4b5g175bgdd37g3e7dgce0dab6d5f40": "Poziom 3: Magiczny pancerz",
    "h2d1fac5ag5486g7185gac07g348c2ae033ff": (
        "Jeśli pancerz zwykle wymaga określonej wartości Siły, magiczny pancerz nie nakłada na ciebie tego "
        "wymogu."
    ),
    "h3757893egada1gdcfdgf81egfaecbf54b4e4": (
        "Możesz dostosować swój magiczny pancerz. Wybierz jeden z następujących modeli pancerza: Drednot, "
        "Strażnik albo Infiltrator. Wybrany model zapewnia ci szczególne korzyści, gdy nosisz magiczny "
        "pancerz.\n\nKażdy model obejmuje specjalną broń. Gdy atakujesz za pomocą tej broni, możesz używać "
        "modyfikatora Inteligencji zamiast modyfikatora Siły lub Zręczności w testach ataku i rzutach obrażeń."
    ),
    "hcc906553g972bg8298gd9cfga6a42e0fdb7c": (
        "Możesz dostosować swój magiczny pancerz. Wybierz jeden z następujących modeli pancerza: Drednot, "
        "Strażnik albo Infiltrator. Wybrany model zapewnia ci szczególne korzyści, gdy nosisz magiczny "
        "pancerz. Każdy model obejmuje specjalną broń. Gdy atakujesz za pomocą tej broni, możesz używać "
        "modyfikatora Inteligencji zamiast modyfikatora Siły lub Zręczności w testach ataku i rzutach obrażeń."
    ),
    "hf03822e2g7af0g67edg9165g36461a798fbc": (
        "Twój magiczny pancerz zyskuje dodatkowe korzyści zależne od modelu.\n\nDrednot. Kość obrażeń "
        "Siłowego niszczyciela zwiększa się do 2k6 obrażeń od mocy, a twój zasięg zwiększa się o 3 m.\n\n"
        "Strażnik. Kość obrażeń Gromowego impulsu zwiększa się do 1k10 obrażeń od dźwięku. Ponadto za każdym "
        "razem, gdy widoczna istota zbliży się na odległość 1,5 m od ciebie, możesz wykonać przeciwko niej atak "
        "okazyjny.\n\nInfiltrator. Kość obrażeń Wyrzutni błyskawic zwiększa się do 2k6 obrażeń od elektryczności. "
        "Każda istota, która otrzyma od niej obrażenia od elektryczności, zostaje porażona."
    ),
    # Durable/Survivor wording and the complete Hit Die/Hit Dice terminology family.
    "hf12dc8a9g3079g890agb1ffgdf7b91f3c03d": (
        "Oporny na śmierć. Masz ułatwienie w rzutach obronnych przeciwko śmierci.\n\n"
        "Szybka regeneracja. Po wyleczeniu odzyskujesz maksymalną możliwą liczbę "
        '<LSTag Tooltip="HitPoints">punktów wytrzymałości</LSTag>.'
    ),
    "h6299a92eg8049g117bga5b7g17d26b0619d6": (
        "Oporny na śmierć. Masz ułatwienie w rzutach obronnych przeciwko śmierci.\n\n"
        "Szybka regeneracja. Po wyleczeniu odzyskujesz maksymalną możliwą liczbę "
        '<LSTag Tooltip="HitPoints">punktów wytrzymałości</LSTag>.'
    ),
    "hfd791ef7g7534g8fdcgba6ag9741c29e31d4": (
        "Opis klasy określa rodzaj kości punktów wytrzymałości twojej postaci (w skrócie: kości "
        "wytrzymałości). Na 1. poziomie postać ma 1 taką kość. Możesz wydawać kości wytrzymałości, aby "
        "odzyskiwać punkty wytrzymałości."
    ),
    "haa8d3917gd15fg261dg5b19g07a62de6a88f": (
        "Za każdym razem, gdy w walce wykonasz akcję Uniku, możesz wydać jedną kość wytrzymałości, aby się "
        "wyleczyć. Rzuć kością, dodaj swój modyfikator Kondycji i odzyskaj punkty wytrzymałości w liczbie "
        "równej sumie (co najmniej 1)."
    ),
    "h5d6d057fg00c7g16f2g3e29g4815f812225a": (
        "Warunek: Krasnolud\n\nW twoich żyłach płynie krew krasnoludzkich bohaterów.\n\nZa każdym razem, "
        "gdy w walce wykonasz akcję Uniku, możesz wydać jedną kość wytrzymałości, aby się wyleczyć. Rzuć "
        "kością, dodaj swój modyfikator Kondycji i odzyskaj punkty wytrzymałości w liczbie równej sumie "
        "(co najmniej 1)."
    ),
    "h6bdae4c0g3fcdg259fgefa5g636614568bc0": (
        "Możesz wzmocnić swoją obronę kosztem żywotności. Za każdym razem, gdy nie powiedzie ci się rzut "
        "obronny, możesz wydać jedną ze swoich kości wytrzymałości, rzucić nią i dodać wynik do tego rzutu "
        "obronnego."
    ),
    "h6975a894g14d4g0b4dga8ecg80a20b85ad85": (
        "Możesz wzmocnić swoją obronę kosztem żywotności. Za każdym razem, gdy nie powiedzie ci się rzut "
        "obronny, możesz wydać jedną ze swoich kości wytrzymałości, rzucić nią i dodać wynik do tego rzutu "
        "obronnego."
    ),
    "h28992689gab7eg0bcega955gb5ee06d7deaf": (
        "Możesz wydawać kości wytrzymałości podczas krótkiego odpoczynku, aby odzyskiwać punkty wytrzymałości."
    ),
    "h2826d606g7d49g321cg9686gfc615a4ba31d": (
        "Liczba niewykorzystanych kości wytrzymałości, którymi możesz rzucić, zwiększa się o jeden za każdy "
        "poziom komórki czaru powyżej 2."
    ),
    # Official BG3 spell and feature names in ordinary running text.
    "h0c6d3ec2g7683g7e9fg7d62g08a6874b3c5f": (
        "Możesz zużyć jedno użycie Aktu wiary, aby rzucić Tarczę wiary albo Duchową broń bez zużywania "
        "komórki czaru. Czar rzucony w ten sposób nie wymaga koncentracji i trwa 1 minutę, ale kończy się "
        "wcześniej, jeśli rzucisz ten czar ponownie, otrzymasz stan obezwładnienia albo zginiesz."
    ),
    "h9e1946a3g463agb8b7g75e7gd94f9c36f9f7": (
        "Gdy używasz czarów ugodzenia, zyskujesz "
        '<LSTag Tooltip="TemporaryHitPoints">tymczasowe punkty wytrzymałości</LSTag> w liczbie równej twojemu '
        '<LSTag Tooltip="AbilityModifier">modyfikatorowi</LSTag> Charyzmy.'
    ),
    "hbaabf179g575bg3c69g6b39ge57aa643ebf4": (
        "Za każdym razem, gdy otrzymujesz obrażenia od światłości, atakująca cię istota otrzymuje obrażenia "
        "od ognia równe dwukrotności swojej premii z biegłości."
    ),
    # Wild Shape uses the exact casing and inflection established by Polish BG3.
    "hc6dea6aag9290gf3cegeb8ag0351bd8d0fc5": (
        "W ramach akcji dodatkowej możesz użyć dzikiej postaci, aby przemienić się w znaną postać bestii. "
        "Przemianę możesz zakończyć wcześniej w ramach akcji dodatkowej. Dzikiej postaci możesz użyć "
        "dwukrotnie. Jedno użycie odzyskujesz po krótkim odpoczynku, a wszystkie po długim odpoczynku. Gdy "
        "przyjmujesz dziką postać, zyskujesz tymczasowe punkty wytrzymałości w liczbie równej swojemu "
        "poziomowi druida. Nie możesz rzucać czarów, ale przemiana nie przerywa koncentracji ani w żaden inny "
        "sposób nie zakłóca działania wcześniej rzuconego czaru."
    ),
    "h8e8ebc40g6f5cg5d29gc885g2f7fb0f2899b": "Witalność dzikiej postaci",
    "h2e1bf345gb5fcg3bbag17c4g7ac514e8455e": (
        "Gdy przyjmujesz dziką postać, zyskujesz tymczasowe punkty wytrzymałości w liczbie równej swojemu "
        "poziomowi druida."
    ),
    "h69bf3828g083cg1e10g408egf0f2ee4c7fe8": (
        "Możesz wykorzystać księżycową magię, gdy przybierasz dziką postać, zyskując poniższe korzyści.\n\n"
        "Klasa pancerza: Dopóki pozostajesz w tej postaci, twoja KP wynosi 13 plus twój modyfikator Mądrości, "
        "jeśli ta wartość jest wyższa niż KP bestii.\n\nTymczasowe punkty wytrzymałości: Zyskujesz tymczasowe "
        "punkty wytrzymałości w liczbie równej trzykrotności swojego poziomu druida."
    ),
    "h1cfad235g00bdg10bfgf085g60ac289d2534": (
        "Pierwotne uderzenie. Raz na turę, gdy trafisz istotę testem ataku bronią albo atakiem postaci bestii "
        "podczas dzikiej postaci, możesz zadać celowi dodatkowo [1]."
    ),
    "hb6ef2813g5893gbc58ga19aga900b5ff9a74": (
        "Możesz odzyskać jedno użycie dzikiej postaci, zużywając komórkę czaru (nie wymaga to akcji)."
    ),
    "h70ae88b1gd34eg0e8ag5b7bga526ea0cf7a6": (
        "Możesz odzyskać jedno użycie dzikiej postaci, zużywając komórkę czaru (nie wymaga to akcji)."
    ),
    "h97d1904cg83d1gdb83ge2b8gfb2e45881c92": (
        "Podczas dzikiej postaci możesz rzucać czary Kręgu Księżyca."
    ),
    "h7d366d57g2abcg334egec99gd574e5abbc31": (
        "W ramach akcji Magii możesz zużyć jedno użycie dzikiej postaci i wybrać punkt w promieniu 18 m od "
        "siebie. W sferze o promieniu 3 m, której środkiem jest ten punkt, pojawiają się na chwilę życiodajne "
        "kwiaty i ciernie wysysające życie. Wrogie istoty w sferze otrzymują 2k6 obrażeń nekrotycznych. "
        "Pozostałe istoty na tym obszarze odzyskują 2k6 punktów wytrzymałości.\n\nObrażenia i leczenie "
        "zwiększają się o 1k6 na 5. poziomie druida (3k6) i ponownie na 10. poziomie (4k6)."
    ),
    "he83b406cg6857g3e88gd60dg2ef8a8d31d88": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie dzikiej postaci, aby przejawić otaczającą cię "
        "emanację morskiej bryzy o promieniu 1,5 m. Emanacja kończy się wcześniej, jeśli ją zakończysz (bez "
        "użycia akcji), przejawisz ponownie albo otrzymasz stan obezwładnienia.\n\nGdy przejawiasz emanację, "
        "a także w ramach akcji dodatkowej w kolejnych turach, możesz wybrać inną widoczną istotę w jej "
        "obrębie. Cel musi wykonać rzut obronny na Kondycję przeciwko twojemu ST obrony przed czarami; w "
        "razie niepowodzenia otrzymuje obrażenia od zimna, a jeśli ma rozmiar duży lub mniejszy, zostaje "
        "odepchnięty do 4,5 m od ciebie. Aby określić obrażenia, rzuć tyloma k6, ile wynosi twój modyfikator "
        "Mądrości."
    ),
    "h57810054gfe7fgd3feg857agf79b5362dc6c": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie dzikiej postaci, aby przejawić otaczającą cię "
        "emanację morskiej bryzy o promieniu 1,5 m. Emanacja kończy się wcześniej, jeśli ją zakończysz (bez "
        "użycia akcji), przejawisz ponownie albo otrzymasz stan obezwładnienia."
    ),
    "hf8470c53gc4a7gf584g96f0g33c340603191": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie dzikiej postaci, aby przejawić otaczającą cię "
        "emanację morskiej bryzy o promieniu 1,5 m. Emanacja kończy się wcześniej, jeśli ją zakończysz (bez "
        "użycia akcji), przejawisz ponownie albo otrzymasz stan obezwładnienia."
    ),
    "h334bd2c8g7709g2b93g78b1g773fe3b8ebf1": (
        "Każdy twój atak w dzikiej postaci może zadawać obrażenia zwykłego typu albo obrażenia od światłości. "
        "Wybierasz typ obrażeń za każdym razem, gdy trafiasz takim atakiem."
    ),
    "heb2a7f7ag521bg6a02g5dffg52cdf49a9788": (
        "Uczysz się regenerować dzięki dzikiej, zwierzęcej magii płynącej w twoich żyłach. W ramach akcji "
        "dodatkowej możesz zużyć jedno użycie dzikiej postaci, aby odzyskać punkty wytrzymałości w liczbie "
        "równej sumie 2k6 i twojego poziomu druida. Leczenie zwiększa się o 1k6 na 5. poziomie druida (3k6 plus "
        "poziom druida) i ponownie na 10. poziomie (4k6 plus poziom druida)."
    ),
    "hc24409fagede8g0aaag1ad3g32c2949bb667": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie dzikiej postaci, aby odzyskać punkty wytrzymałości "
        "w liczbie równej sumie 2k6 i twojego poziomu druida. Leczenie zwiększa się o 1k6 na 5. poziomie druida "
        "(3k6 plus poziom druida) i ponownie na 10. poziomie (4k6 plus poziom druida)."
    ),
    # Circle of Dragons and Dragon Shape, including the official BG3 term "Zionięcie".
    "h6d46b975ga195gac49gab4cg2ff48ea0ff54": (
        "Twoje zionięcie staje się potężniejsze na określonych poziomach. Na 6. poziomie zadaje 3k6 obrażeń, "
        "a na 10. poziomie — 4k6 obrażeń."
    ),
    "hea98e86cg6f0eg6fa9gd366g94bd7a432ec2": (
        "Możesz w ramach akcji dodatkowej zużyć jedno użycie dzikiej postaci, aby przybrać wyjątkową formę — "
        "kształt smoka. W tej formie stajesz się smokiem rozmiaru średniego poruszającym się na czterech "
        "łapach, ale zachowujesz zwykłe statystyki i zmysły swojej postaci.\n\nW kształcie smoka możesz atakować "
        "pazurami i używać zionięcia. Zyskujesz szybkość lotu równą dwukrotności swojej szybkości oraz "
        "odporność na obrażenia od kwasu, zimna, ognia, elektryczności i trucizny."
    ),
    "hc56adb28g1c39g4a79g84bbgc0a1b6238a22": (
        "Na 6. i 10. poziomie druida twój kształt smoka staje się potężniejszy."
    ),
    "h8a2a463cg9e0fg4e84gefd3g2307577a9b84": "Krąg smoków",
    "h4dcc12fag7d0cgb63ag23cfg441ee129b6df": (
        "Krąg smoków to stary zakon druidów o sztywnych tradycjach. Ci związani honorem strażnicy natury i "
        "smoczego dziedzictwa należą do tajnego stowarzyszenia, które wpływało na rządy, wojny i kulturę na "
        "całym świecie. Wysoko postawieni członkowie tego kręgu mają związki z rodami królewskimi sięgające "
        "wielu pokoleń wstecz, czego subtelnym świadectwem są herby i insygnia rodzin królewskich.\n\nDruidzi z tego "
        "kręgu wiedzą, że smoki i smocza magia są tak samo związane ze światem jak rośliny czy bestie, i "
        "wykorzystują tę więź, aby przybrać własną, wyjątkową i potężną smoczą postać."
    ),
    "hea0350ecg3563gf151g3949ge2a04d0eb3da": "Poziom 3: Smocza wiedza",
    "h8ea85d5eg5bc3gd5aagf3e6g7179f506b3ef": "Poziom 3: Kształt smoka",
    "hc9360440gfe54g46f9gbb9dge1b352d710ba": (
        "W ramach akcji dodatkowej możesz zużyć jedno użycie dzikiej postaci, aby przybrać wyjątkową formę — "
        "kształt smoka. W tej formie stajesz się smokiem rozmiaru średniego poruszającym się na czterech "
        "łapach, ale zachowujesz zwykłe statystyki i zmysły.\n\nGdy przybierasz kształt smoka, zyskujesz "
        "tymczasowe punkty wytrzymałości w liczbie równej trzykrotności swojego poziomu druida. W kształcie "
        "smoka możesz atakować pazurami i używać zionięcia. Zyskujesz szybkość lotu równą dwukrotności "
        "swojej szybkości oraz odporność na obrażenia od kwasu, zimna, ognia, elektryczności i trucizny."
    ),
    "hcb4664e4g5158g21d8ga6dcgb912ed163b0d": (
        "Na 6. i 10. poziomie druida twój kształt smoka staje się potężniejszy."
    ),
    "h188fcbccg032fg827cg4fc8g0526eb475df0": (
        "W kształcie smoka twoje ataki są uznawane za magiczne na potrzeby przełamywania "
        '<LSTag Tooltip="Resistant">odporności</LSTag> i '
        '<LSTag Tooltip="Immune">niepodatności</LSTag> na obrażenia niemagiczne, a twoja KP zwiększa się o 1.'
    ),
    "h8a430f87g813dg7f42g06f9gd34f0e6f79f3": (
        "W kształcie smoka możesz rzucać przygotowane czary druida, a twoja KP zwiększa się o 2."
    ),
})

# Follow-up 17: the official corpus contains an unrelated Submit button
# translated as "Wyślij". Here Submit is the Architect of Ruin's imperative
# command that weakens a sealed creature's resistance to a spell.
POST_REFINEMENT_UID_OVERRIDES.update({
    "h528f5094gf88ag08d3ge649gc14b423059e7": "Poziom 11: Ulegnij",
})

for kalashtar_title_uid in (
    "h877ab541g5ce7g7a78g2577g02cab9025520",
    "h0a563e02g95f0gd9e3g039ag98f3b4346158",
    "ha860cb95g7c9ag10c1g85f5gc9e5b708f2a5",
    "hfa61106eg95adg47fbg8362gcbea543e7ea6",
):
    UID_OVERRIDES[kalashtar_title_uid] = "Kalashtar"


# Corrections toward the shipped Polish BG3 terminology. These operate only on
# visible text, never inside LSTag attributes or other markup.
VISIBLE_REPLACEMENTS = [
    # Polish titles capitalize only the first word; fey is a common creature
    # type, not a proper name. Apply the same casing in inflected prose.
    (r"\bKrok Fey\b", "Krok fey"),
    (r"\bKroku Fey\b", "Kroku fey"),
    (r"\bGłodne Ostrze\b", "Głodne ostrze"),
    (r"\bMasz Odporność\b", "Masz odporność"),
    (r"\bmasz Odporność\b", "masz odporność"),
    (r"\bmają Odporność\b", "mają odporność"),
    (r"\bignorują Odporność\b", "ignorują odporność"),
    (r"\bJeśli masz odporność albo Podatność\b", "Jeśli masz odporność albo podatność"),
    (r"\b[Nn]ie jesteś obezwładniony\b", "nie masz stanu Obezwładnienia"),
    (r"\bJesteś obezwładniony\b", "Masz stan Obezwładnienia"),
    (r"\bjesteś obezwładniony\b", "masz stan Obezwładnienia"),
    (r"\bJesteś Powalony\b", "Masz stan Powalenia"),
    (r"\bjesteś Powalony\b", "masz stan Powalenia"),
    (r"\bZostajesz Powalony\b", "Otrzymujesz stan Powalenia"),
    (r"\bzostajesz Powalony\b", "otrzymujesz stan Powalenia"),
    (r"\bstać się niewidzialnym\b", "zyskać niewidzialność"),
    (r"\bjesteś nieuzbrojony\b", "nie używasz broni"),
    (r"\bjesteś narażony na\b", "podlegasz"),
    (r"\bJesteś odporny na\b", "Masz odporność na"),
    (r"\bjesteś odporny na\b", "masz odporność na"),
    (r"\bJesteś biegły w\b", "Masz biegłość w"),
    (r"\bjesteś biegły w\b", "masz biegłość w"),
    (r"\bBaldur(?:'|’)s Gate\b", "Wrota Baldura"),
    (r"\bShadowfell\b", "Sfera Cieni"),
    (r"\bMglisty Krok\b", "Krok przez mgłę"),
    (r"\bMglisty krok\b", "Krok przez mgłę"),
    (r"\b(\d+(?:[,.]\d+)?)\s+metr(?:a|y|ów)\b", r"\1 m"),
    (r"\bAkcji Atak\b", "akcji Ataku"),
    (r"\bAkcję Atak\b", "akcję Ataku"),
    (r"\bAkcja Atak\b", "akcja Ataku"),
    (r"\bPremii Biegłości\b", "premii z biegłości"),
    (r"\bPremię Biegłości\b", "premię z biegłości"),
    (r"\bpremii biegłości\b", "premii z biegłości"),
    (r"\bAtaku z [Uu]krycia\b", "ukradkowego ataku"),
    (r"\bataku z ukrycia\b", "ukradkowego ataku"),
    (r"\bAtakiem z [Uu]krycia\b", "ukradkowym atakiem"),
    (r"\batakiem z ukrycia\b", "ukradkowym atakiem"),
    (r"\bAtak z [Uu]krycia\b", "Ukradkowy atak"),
    (r"\batak z ukrycia\b", "ukradkowy atak"),
    (r"\bBohaterską [Ii]nspirację\b", "heroiczną inspirację"),
    (r"\btej dodatkowej akcji\b", "tej akcji dodatkowej"),
    (r"\bpo zadaniu Trafienia Krytycznego\b", "po uzyskaniu trafienia krytycznego"),
    (
        r"\bgdy zadasz Trafienie Krytyczne dużemu lub mniejszemu istocie\b",
        "gdy uzyskasz trafienie krytyczne przeciwko istocie rozmiaru dużego lub mniejszego",
    ),
    (
        r"\bgdy zadasz Trafienie Krytyczne istocie\b",
        "gdy uzyskasz trafienie krytyczne przeciwko istocie",
    ),
    (
        r"\bgdy zadasz trafienie krytyczne celowi\b",
        "gdy uzyskasz trafienie krytyczne przeciwko celowi",
    ),
    (
        r"\bgdy zadasz istocie trafienie krytyczne\b",
        "gdy uzyskasz trafienie krytyczne przeciwko istocie",
    ),
    (
        r"\bGdy zadasz istocie trafienie krytyczne\b",
        "Gdy uzyskasz trafienie krytyczne przeciwko istocie",
    ),
    (
        r"\bgdy zadajesz istocie trafienie krytyczne\b",
        "gdy uzyskujesz trafienie krytyczne przeciwko istocie",
    ),
    (
        r"\bmusi wykonać udany rzut obronny ([^.\n]+?) albo otrzymuje\b",
        r"musi wykonać rzut obronny \1; w razie niepowodzenia otrzymuje",
    ),
    (
        r"\bmusi wykonać udany rzut obronny ([^.\n]+?) albo zostaje\b",
        r"musi wykonać rzut obronny \1; w razie niepowodzenia zostaje",
    ),
    (
        r"\bmusi wykonać udany rzut obronny ([^.\n]+?) albo nie może\b",
        r"musi wykonać rzut obronny \1; w razie niepowodzenia nie może",
    ),
    (r"\bstan Leżenie\b", "stan Powalenia"),
    (r"\bW ramach akcji dodatkowej,\s+(?!którą\b)", "W ramach akcji dodatkowej "),
    (r"\bJako akcję dodatkową\b", "W ramach akcji dodatkowej"),
    (r"\bmożesz akcją dodatkową\b", "możesz w ramach akcji dodatkowej"),
    (r"(?m)(^|\n\n)Akcją dodatkową\b", r"\1W ramach akcji dodatkowej"),
    (r"\bStwór\b", "Istota"),
    (r"\bstwór\b", "istota"),
    (r"\bPrędkość\b", "Szybkość"),
    (r"\bprędkość\b", "szybkość"),
    (r"\bwszystkie zużyte użycia odzyskujesz\b", "odzyskujesz wszystkie użycia"),
    (r"\bWszystkie zużyte użycia odzyskujesz\b", "Odzyskujesz wszystkie użycia"),
    (r"\bOdzyskujesz wszystkie zużyte użycia\b", "Odzyskujesz wszystkie użycia"),
    (r"\bodzyskujesz wszystkie zużyte użycia\b", "odzyskujesz wszystkie użycia"),
    (r"\bST obronności przed zaklęciami\b", "ST obrony przed czarami"),
    (r"\bST obronności na zaklęcia\b", "ST obrony przed czarami"),
    (r"\bST obronności przed czarami\b", "ST obrony przed czarami"),
    (r"\bpremia do ataku zaklęć\b", "premia do ataku czarami"),
    (r"\bpremii do ataku zaklęć\b", "premii do ataku czarami"),
    (r"\bW przypadku nieudanego zapisu\b", "Przy niepowodzeniu"),
    (r"\bW przypadku udanego zapisu\b", "Przy powodzeniu"),
    (r"\bUderzeniem [Bb]ez [Bb]roni\b", "atakiem bez broni"),
    (r"\bUderzenia [Bb]ez [Bb]roni\b", "ataku bez broni"),
    (r"\bUderzenie [Bb]ez [Bb]roni\b", "atak bez broni"),
    (r"\bAtak bez Broni\b", "atak bez broni"),
    (r"\bAtaku bez Broni\b", "ataku bez broni"),
    (r"\bAtaki bez Broni\b", "ataki bez broni"),
    (r"\batakiem wręcz bronią\b", "atakiem bronią do walki wręcz"),
    (r"\batak wręcz bronią\b", "atak bronią do walki wręcz"),
    (r"\batakami wręcz bronią\b", "atakami bronią do walki wręcz"),
    (r"\bataków wręcz bronią\b", "ataków bronią do walki wręcz"),
    (r"\bobiera ciebie albo\b", "obiera cię albo"),
    (r"\bAtaków Okazyjnych\b", "ataków okazyjnych"),
    (r"\bAtaki Okazyjne\b", "ataki okazyjne"),
    (r"\bRzutów ataku\b", "Testów ataku"),
    (r"\brzutów ataku\b", "testów ataku"),
    (r"\bRzuty ataku\b", "Testy ataku"),
    (r"\brzuty ataku\b", "testy ataku"),
    (r"\bRzutem ataku\b", "Testem ataku"),
    (r"\brzutem ataku\b", "testem ataku"),
    (r"\bRzucie ataku\b", "Teście ataku"),
    (r"\brzucie ataku\b", "teście ataku"),
    (r"\bRzutu ataku\b", "Testu ataku"),
    (r"\brzutu ataku\b", "testu ataku"),
    (r"\bRzut ataku\b", "Test ataku"),
    (r"\brzut ataku\b", "test ataku"),
    (r"\bTestów zdolności\b", "Testów cech"),
    (r"\btestów zdolności\b", "testów cech"),
    (r"\bTesty zdolności\b", "Testy cech"),
    (r"\btesty zdolności\b", "testy cech"),
    (r"\bTestem zdolności\b", "Testem cechy"),
    (r"\btestem zdolności\b", "testem cechy"),
    (r"\bTeście zdolności\b", "Teście cechy"),
    (r"\bteście zdolności\b", "teście cechy"),
    (r"\bTestu zdolności\b", "Testu cechy"),
    (r"\btestu zdolności\b", "testu cechy"),
    (r"\bTest zdolności\b", "Test cechy"),
    (r"\btest zdolności\b", "test cechy"),
    (r"\bBardowska Inspiracja\b", "bardowska inspiracja"),
    (r"\bBardowskiej Inspiracji\b", "bardowskiej inspiracji"),
    (r"\bInspiracja Barda\b", "bardowska inspiracja"),
    (r"\bInspiracji Barda\b", "bardowskiej inspiracji"),
    (r"\bzadać temu celowi dodatkowe\b", "zadać mu dodatkowe"),
    (r"\bZaklęciem\b", "Czarem"),
    (r"\bzaklęciem\b", "czarem"),
    (r"\bZaklęciu\b", "Czarze"),
    (r"\bzaklęciu\b", "czarze"),
    (r"\bZaklęciami\b", "Czarami"),
    (r"\bzaklęciami\b", "czarami"),
    (r"\bZaklęciach\b", "Czarach"),
    (r"\bzaklęciach\b", "czarach"),
    (r"\bZaklęć\b", "Czarów"),
    (r"\bzaklęć\b", "czarów"),
    (r"\bZaklęciom\b", "Czarom"),
    (r"\bzaklęciom\b", "czarom"),
    (r"\bZaklęcie\b", "Czar"),
    (r"\bzaklęcie\b", "czar"),
    (
        r"\b(tego|twojego|każdego|jednego|wybranego|następnego|rzuconego|rzucanego|danego) zaklęcia\b",
        r"\1 czaru",
    ),
    (r"\b(od|do|z|ze|bez|dla|wobec|przeciwko|podczas|po|przy) zaklęcia\b", r"\1 czaru"),
    (r"\bza pomocą zaklęcia\b", "za pomocą czaru"),
    (
        r"\b(rzucenia|rzucaniu|rzuceniu|działania|zakończenia|trwania|poziom|poziomu|efekt|efektu|"
        r"obrażenia|zasięg|zasięgu|cel|celu|opis|opisu|moc|mocy|ST) zaklęcia\b",
        r"\1 czaru",
    ),
    (r"\bzaklęcia poziomu\b", "czaru poziomu"),
    (r"\bZaklęcia\b", "Czary"),
    (r"\bzaklęcia\b", "czary"),
    (
        r"\bmodyfikator z (Siły|Zręczności|Kondycji|Inteligencji|Mądrości|Charyzmy)\b",
        r"modyfikator \1",
    ),
    (r"\bdodatkowe obrażenia (\d+k\d+)\b", r"dodatkowe \1 obrażeń"),
    (r"\bobrażenia (od [a-ząćęłńóśźż-]+) (\d+k\d+)\b", r"\2 obrażeń \1"),
    (r"\bobrażenia (\d+k\d+)\b", r"\1 obrażeń"),
    (r"\b(\d+k\d+) obrażenia\b", r"\1 obrażeń"),
    (r"\btesty obrażeń\b", "rzuty na obrażenia"),
    (r"\btestów obrażeń\b", "rzutów na obrażenia"),
    (r"\btestu obrażeń\b", "rzutu na obrażenia"),
    (r"\btest obrażeń\b", "rzut na obrażenia"),
    (r"\btesty ataku i obrażeń\b", "testy ataku i rzuty na obrażenia"),
    (r"\btestów ataku i obrażeń\b", "testów ataku i rzutów na obrażenia"),
    (r"\btestach ataku i obrażeniach\b", "testach ataku i rzutach na obrażenia"),
    (r"\btestach ataku i obrażeń\b", "testach ataku i rzutach na obrażenia"),
    (r"\btestu ataku i obrażeń\b", "testu ataku i rzutu na obrażenia"),
    (r"\bzdolności rzucania zaklęć\b", "cechy bazowej zaklęć"),
    (r"\bZdolność rzucania zaklęć\b", "Cecha bazowa zaklęć"),
    (r"\bAtut: Trudny\b", "Atut: Twardziel"),
    (r"\bPremia od Biegłości\b", "Premia z biegłości"),
    (r"\bPremii od Biegłości\b", "Premii z biegłości"),
    (r"\bpremia od biegłości\b", "premia z biegłości"),
    (r"\bpremii od biegłości\b", "premii z biegłości"),
    (r"\b([Nn]a) (\d+)(?!\.) poziomie\b", r"\1 \2. poziomie"),
    (r"\b([Nn]a) poziomie (\d+)\b", r"\1 \2. poziomie"),
    (r"\bJako akcja dodatkowa\b", "W ramach akcji dodatkowej"),
    (r"\bJako dodatkową akcję\b", "W ramach akcji dodatkowej"),
    (r"\bJako akcję Magii\b", "W ramach akcji Magii"),
    (r"(?m)(^|\n\n)akcja dodatkowa\b", r"\1Akcja dodatkowa"),
    (r"(?m)(^|\n\n)akcją dodatkową\b", r"\1Akcją dodatkową"),
    (r"(?m)(^|\n\n)akcję dodatkową\b", r"\1Akcję dodatkową"),
    (r"(?m)(^|\n\n)akcji dodatkowej\b", r"\1Akcji dodatkowej"),
    (r"\bistocie, które\b", "istocie, która"),
    (r"\bistocie, którego\b", "istocie, której"),
    (r"\bistocie znajdującemu\b", "istocie znajdującej"),
    (r"\bistota, które\b", "istota, która"),
    (r"\bistota, któremu\b", "istota, której"),
    (r"\bistota znajdujące\b", "istota znajdująca"),
    (r"\binnej istocie, które\b", "innej istocie, która"),
    (r"\binnemu istocie\b", "innej istocie"),
    (r"\bpod tym istotą\b", "pod tą istotą"),
    (r"\bkażda istota złapane\b", "każdą istotę złapaną"),
    (r"\bparząc każda istota\b", "parząc każdą istotę"),
    (r"\bKażda inna istota znajdujące\b", "Każda inna istota znajdująca"),
    (r"\bkażda inna istota znajdujące\b", "każda inna istota znajdująca"),
    (r"\bKażde z tych istot\b", "Każda z tych istot"),
    (r"\bkażde z tych istot\b", "każda z tych istot"),
    (r"\bkażdą wybraną przez ciebie istota\b", "każdą wybraną przez ciebie istotę"),
    (r"\bSłowa Istoty\b", "Słowa Stworzenia"),
    (r"\bSłów Istoty\b", "Słów Stworzenia"),
    (r"\btajemnic istoty\b", "tajemnic stworzenia"),
    (r"\btrafisz istota\b", "trafisz istotę"),
    (r"\bstan Leżenia\b", "stan Powalenia"),
    (r"\bGdy jesteś Zakrwawiony\b", "Gdy masz stan Zakrwawienia"),
    (r"\bo ile w chwili trafienia jesteś Zakrwawiony\b", "o ile w chwili trafienia masz stan Zakrwawienia"),
    (r"\bJeśli podczas przemiany jesteś Przerażony\b", "Jeśli podczas przemiany masz stan Przerażenia"),
    (r"\bistota, który\b", "istota, która"),
    (r"(\bKażda istota[^.\n]{0,180}\bzostaje) odepchnięte\b", r"\1 odepchnięta"),
    (r"(\bKażda istota[^.\n]{0,180}\bzostaje) pochłonięte\b", r"\1 pochłonięta"),
    (r"\bKażde wybrane przez ciebie stworzenie\b", "Każda wybrana przez ciebie istota"),
    (r"\bkażde wybrane przez ciebie stworzenie\b", "każda wybrana przez ciebie istota"),
    (r"\bKażde inne stworzenie\b", "Każda inna istota"),
    (r"\bkażde inne stworzenie\b", "każda inna istota"),
    (r"\bKażde wrogie stworzenie\b", "Każda wroga istota"),
    (r"\bkażde wrogie stworzenie\b", "każda wroga istota"),
    (r"\bminimum jedno istota\b", "co najmniej jedna istota"),
    (r"\bminimum\b", "co najmniej"),
    (r"\bjedno istota, która\b", "jedną istotę, którą"),
    (r"\bjedno istota\b", "jedną istotę"),
    (r"\bwybrać istota\b", "wybrać istotę"),
    (r"\bwybierz istota\b", "wybierz istotę"),
    (r"\bprzyciągnąć istota\b", "przyciągnąć istotę"),
    (r"\bprzestraszyć istota\b", "przestraszyć istotę"),
    (r"\bchętnego istoty\b", "chętnej istoty"),
    (r"\bjednego chętnej istoty\b", "jednej chętnej istoty"),
    (r"\bprzeklętego istoty\b", "przeklętej istoty"),
    (r"\bdotkniętego istoty\b", "dotkniętej istoty"),
    (r"\binnego istoty\b", "innej istoty"),
    (r"\bpierwszego istoty\b", "pierwszej istoty"),
    (r"\btego istoty\b", "tej istoty"),
    (r"\bdrugiemu istocie\b", "drugiej istocie"),
    (r"\btemu istocie\b", "tej istocie"),
    (r"\bprzeklętym istocie\b", "przeklętej istocie"),
    (r"\bdotkniętym istocie\b", "dotkniętej istocie"),
    (r"\bchętnym istocie\b", "chętnej istocie"),
    (r"\bna dużym lub mniejszym istocie\b", "na istocie rozmiaru dużego lub mniejszego"),
    (r"\bstworowi\b", "istocie"),
    (r"\bTo stworzenie(?=\s+(?:otrzymuje|odzyskuje|ma|może|musi|zostaje|jest|wykonuje))", "Ta istota"),
    (r"\bto stworzenie(?=\s+(?:otrzymuje|odzyskuje|ma|może|musi|zostaje|jest|wykonuje))", "ta istota"),
    (r"\btego stworzenia\b", "tej istoty"),
    (r"\btemu stworzeniu\b", "tej istocie"),
    (r"\btym stworzeniem\b", "tą istotą"),
    (r"\billiggerzy\b", "illriggerzy"),
    (r"\billiggera\b", "illriggera"),
    (r"\bPustani Strażnicy\b", "Strażnicy pustki"),
    (r"\bPustego Strażnika\b", "Strażnika pustki"),
    (r"\bPusty Strażnik\b", "Strażnik pustki"),
    (r"\bAtaki okazjonalne\b", "Ataki okazyjne"),
    (r"\bataki okazjonalne\b", "ataki okazyjne"),
    (r"\bAtaki okazyjne są dla (?:C|c)iebie niekorzystne\b", "Ataki okazyjne przeciwko tobie mają utrudnienie"),
    (r"\bataki okazyjne są dla (?:C|c)iebie niekorzystne\b", "ataki okazyjne przeciwko tobie mają utrudnienie"),
    (r"\bPonadto gdy\b", "Ponadto, gdy"),
    (r"\bPonadto kiedy\b", "Ponadto, kiedy"),
    (r"\bponadto gdy\b", "ponadto, gdy"),
    (r"\bponadto kiedy\b", "ponadto, kiedy"),
    (r"\bPo tym jak\b", "Po tym, jak"),
    (r"\bpo tym jak\b", "po tym, jak"),
    (r"padając na ziemię i tarzając się", "padając na ziemię i przetaczając się po niej"),
    (r"\brzuć na stół Przypływ dzikiej magii\b", "wykonaj rzut w tabeli Przypływ dzikiej magii"),
    (r"\bZdobądź\b", "Zyskaj"),
    (r"\bzdobądź\b", "zyskaj"),
    (r"\bBierze(?=\s+\[)", "Otrzymuje"),
    (r"\bwszystkie wykorzystane użycia\b", "wszystkie zużyte użycia"),
    (r"\bWszystkie wykorzystane użycia\b", "Wszystkie zużyte użycia"),
    (r"\bwszystkie użyte użycia\b", "wszystkie zużyte użycia"),
    (r"\bWszystkie użyte użycia\b", "Wszystkie zużyte użycia"),
    (r"\bwszystkie wykorzystane zastosowania\b", "wszystkie zużyte użycia"),
    (r"\bWszystkie wykorzystane zastosowania\b", "Wszystkie zużyte użycia"),
    (r"\bod od światłości\b", "od światłości"),
    (r"\bmożesz podjąć Reakcję, aby\b", "możesz w ramach reakcji"),
    (r"\bmożesz podjąć reakcję, aby\b", "możesz w ramach reakcji"),
    (r"\bmożesz wykorzystać swoją reakcję, aby\b", "możesz w ramach reakcji"),
    (r"\bmożesz użyć swojej Reakcji, aby\b", "możesz w ramach reakcji"),
    (r"\bstan Obezwładnienie\b", "stan Obezwładnienia"),
    (r"\bstan Niezdolności\b", "stan Obezwładnienia"),
    (r"\bstanie Niezdolności\b", "stanie Obezwładnienia"),
    (r"\bza każda wroga istota\b", "za każdą wrogą istotę"),
    (r"\bST rzutu obronnego na zaklęcia\b", "ST obrony przed czarami"),
    (r"\bST rzutu obronnego na zaklęcie\b", "ST obrony przed czarami"),
    (r"\bST rzutu obronnego przeciwko czarowi\b", "ST obrony przed czarami"),
    (r"\bmodyfikator z Charyzmy\b", "modyfikator Charyzmy"),
    (r"\bmodyfikator z charyzmy\b", "modyfikator Charyzmy"),
    (r"\bbierze(?=\s+\[)", "otrzymuje"),
    (r"\bZajmuje(?=\s+\[)", "Otrzymuje"),
    (r"\bzajmuje(?=\s+\[)", "otrzymuje"),
    (r"\bZdobywa(?=\s+\[)", "Otrzymuje"),
    (r"\bzdobywa(?=\s+\[)", "otrzymuje"),
    (r"\bJako Reakcję\b", "W ramach reakcji"),
    (r"\bjako Reakcję\b", "w ramach reakcji"),
    (r"\bwykonać Reakcję\b", "wykonać reakcję"),
    (r"\bpodjąć reakcję\b", "wykonać reakcję"),
    (r"\bmusi odnieść sukces w rzucie obronnym\b", "musi wykonać udany rzut obronny"),
    (r"\bmusi zakończyć się sukcesem w rzucie obronnym\b", "musi wykonać udany rzut obronny"),
    (r"\bmusi wykonać pomyślny rzut obronny\b", "musi wykonać udany rzut obronny"),
    (r"\bposiadać stan\b", "otrzymać stan"),
    (r"\bposiada stan\b", "ma stan"),
    (r"\buzyskać stan\b", "otrzymać stan"),
    (r"\buzyskuje stan\b", "otrzymuje stan"),
    (r"\buzyskasz stan\b", "otrzymasz stan"),
    (r"\bprzechodzi w stan\b", "otrzymuje stan"),
    (r"\bzyskać stan\b", "otrzymać stan"),
    (r"\bzyskuje stan\b", "otrzymuje stan"),
    (r"\bstan Przestraszenia\b", "stan Przerażenia"),
    (r"\bstan Przestraszony\b", "stan Przerażenia"),
    (r"\bstan Padnięcia\b", "stan Powalenia"),
    (r"\bstan Leżenia\b", "stan Powalenia"),
    (r"\bstan Powalony\b", "stan Powalenia"),
    (r"\bstan Obezwładniony\b", "stan Obezwładnienia"),
    (r"\bstan Niewidzialny\b", "stan Niewidzialności"),
    (r"\bstan Niezdolności do pracy\b", "stan Obezwładnienia"),
    (r"\bstan Niezdolność do pracy\b", "stan Obezwładnienia"),
    (r"\bstan Czarodziejki\b", "stan Zauroczenia"),
    (r"\bstany Czarodziejki i Przestraszenia\b", "stany Zauroczenia i Przerażenia"),
    (r"\bstany Przestraszenia i Sparaliżowania\b", "stany Przerażenia i Paraliżu"),
    (r"\bstanom Przestraszenia i Sparaliżowania\b", "stanom Przerażenia i Paraliżu"),
    (r"\bznajduje się w stanie Przestraszenia\b", "ma stan Przerażenia"),
    (r"\bpozostaje w stanie Przestraszenia\b", "ma stan Przerażenia"),
    (r"\bpozostaje w stanie Urok\b", "ma stan Zauroczenia"),
    (r"\bstan [„\"]?podatny[”\"]?\b", "stan Powalenia"),
    (r"\bstan Podatny\b", "stan Powalenia"),
    (r"\bTymczasowe punkty wytrzymałości\b", "tymczasowe punkty wytrzymałości"),
    (r"\bTymczasowy punkt wytrzymałości\b", "tymczasowy punkt wytrzymałości"),
    (r"(?m)(^|\n\n)tymczasowe punkty wytrzymałości(?=\s*:)", r"\1Tymczasowe punkty wytrzymałości"),
    (r"\bDC\b", "ST"),
    (r"\bGojenie\s+:", "Gojenie:"),
    (r"\+\s*(?=\[)", "+"),
    (r"(?<!\.)\.\.(?!\.)", "."),
    (r"\bobrażenia od Ognia\b", "obrażenia od ognia"),
    (r"\bobrażenia od Zimna\b", "obrażenia od zimna"),
    (r"\bobrażenia od Kwasu\b", "obrażenia od kwasu"),
    (r"\bobrażenia od Trucizny\b", "obrażenia od trucizny"),
    (r"\bobrażenia od Mocy\b", "obrażenia od mocy"),
    (r"\bobrażenia Mocy\b", "obrażenia od mocy"),
    (r"\bobrażenia od Światłości\b", "obrażenia od światłości"),
    (r"\bobrażenia Nekrotyczne\b", "obrażenia nekrotyczne"),
    (r"\bobrażenia Psychiczne\b", "obrażenia psychiczne"),
    (r"\bobrażenia Promienne\b", "obrażenia od światłości"),
    (r"\bobrażenia Tłuczone\b", "obrażenia obuchowe"),
    (r"\bobrażenia Kłute\b", "obrażenia kłute"),
    (r"\bobrażenia Cięte\b", "obrażenia cięte"),
    (r"\bmagiczna magia\b", "magia"),
    (r"\bpo trafieniu celem\b", "po trafieniu celu"),
    (r"\brówne wyrzuconej liczbie\b", "w liczbie równej wynikowi"),
    (r"\brówne rzucie twoją kością\b", "w liczbie równej wynikowi rzutu kością"),
    (r"\brówne rzucie twojej kości\b", "w liczbie równej wynikowi rzutu kością"),
    (r"\brówne dwóm rzutom twojej kości\b", "w liczbie równej dwóm wynikom rzutu kością"),
    (r"\bPrzysięgą Kanału\b", "Mocą przysięgi"),
    (r"\bPrzysięgi Kanału\b", "Mocy przysięgi"),
    (r"\bPrzysięgę Kanału\b", "Moc przysięgi"),
    (r"\bPrzysięga Kanału\b", "Moc przysięgi"),
    (r"\bPrzysięga Kanałowa\b", "Moc przysięgi"),
    (r"\bprzysięgą kanału\b", "mocą przysięgi"),
    (r"\bprzysięgi kanału\b", "mocy przysięgi"),
    (r"\bprzysięgę kanału\b", "moc przysięgi"),
    (r"\bprzysięga kanału\b", "moc przysięgi"),
    (r"\bForma Strachu\b", "Postać grozy"),
    (r"\bDeath Ward\b", "Osłona przed śmiercią"),
    (r"\bChill Touch\b", "Przeszywający dotyk"),
    (r"\bBlade Ward\b", "Osłona przed orężem"),
    (r"\bPoison Spray\b", "Trujący rozprysk"),
    (r"\bColou?r Spray\b", "Kolorowy rozprysk"),
    (r"\bDanse Macabre\b", "Makabryczny taniec"),
    (r"\bDoom Song\b", "Pieśń zagłady"),
    (r"\bSteel Defender\b", "Stalowy obrońca"),
    (r"\bFey Touch\b", "Dotknięty przez Fey"),
    (r"\bHunter(?:'|’)s Mark\b", "Znak łowcy"),
    (r"\bGut Shot\b", "Strzał w brzuch"),
    (r"\bTyro (?:of the Gauntlet|Rękawicy)\b", "Nowicjusz Rękawicy"),
    (r"\bVersatile Merc\b", "Wszechstronny najemnik"),
    (r"\bWszechstronny Merc\b", "Wszechstronny najemnik"),
    (r"\bBattle Smith\b", "Kowal bitewny"),
    (r"\bBitewnego Smitha\b", "kowala bitewnego"),
    (r"\bDragonborn\b", "Drakon"),
    (r"\bPiercer\b", "Przebijacz"),
    (r"\bSlasher\b", "Siepacz"),
    (r"\bSlow\b", "Spowolnienie"),
    (r"\bstan Leżący\b", "stan Powalenia"),
    (r"\bWyczyn: Zdolny\b", "Atut: Uzdolniony"),
    (r"wyrzuceni z zakonów za ich fanatyczne przekonanie", "wyrzuceni z zakonów z powodu fanatycznej wiary"),
    (r"\bMagic Initiate\b", "Wtajemniczony"),
    (r"\bWtajemniczony Magia\b", "Wtajemniczony"),
    (r"\bMage Hand Legerdemain\b", "Kuglarstwo magicznej dłoni"),
    (r"\bRęka Maga Legerdemain\b", "Kuglarstwo magicznej dłoni"),
    (r"\blegerdemain\b", "kuglarstwa"),
    (r"\bFey[- ]Touched\b", "Dotknięty przez Fey"),
    (r"\bForgotten Realms: Heroes of Faerûn\b", "Zapomniane Krainy: Bohaterowie Faerûnu"),
    (r"\bCollege of Dance\b", "Kolegium Tańca"),
    (r"\bCollege of Choreography\b", "Kolegium Choreografii"),
    (r"\bFlurry of Healing\b", "Grad uzdrowienia"),
    (r"\bFlurry of Harm\b", "Grad krzywdy"),
    (r"\bArcane Ward\b", "Magiczna powłoka"),
    (r"\bArcane Recovery\b", "Odzyskanie mocy"),
    (r"\bArcane Vigor\b", "Magiczna krzepa"),
    (r"\bElemental Attunement\b", "Harmonia żywiołów"),
    (r"\bCall Lightning\b", "Wezwanie błyskawicy"),
    (r"\bScorching Ray\b", "Wypalający promień"),
    (r"\bShatter\b", "Trzask"),
    (r"\bIce Knife\b", "Lodowy nóż"),
    (r"\bHold Person\b", "Unieruchomienie osoby"),
    (r"\bRemove Curse\b", "Zdjęcie klątwy"),
    (r"\bMoonbeam\b", "Księżycowy promień"),
    (r"\bSleep\b", "Uśpienie"),
    (r"\bRevivify\b", "Ożywianie"),
    (r"\bSynaptic Static\b", "Szum synaptyczny"),
    (r"\bBarkskin\b", "Korowa skóra"),
    (r"\bVitriolic Sphere\b", "Żrąca kula"),
    (r"\bElminster(?:'|’)s Elusion\b", "Nieuchwytność Elminstera"),
    (r"\bDancing Lights\b", "Tańczące światła"),
    (r"\bFinger Guns\b", "Pistolety z palców"),
    (r"\bInfernal Conduit\b", "Piekielne przewodzenie"),
    (r"\bSteady Aim\b", "Stabilne celowanie"),
    (r"\bStymying Mark\b", "Hamujące piętno"),
    (r"\bStyming Mark\b", "Hamujące piętno"),
    (r"\bBedevil\b", "Dręczenie"),
    (r"\bBeak\b", "Dziób"),
    (r"\bClaws\b", "Pazury"),
    (r"\bHigh Ground Rules\b", "Zasada przewagi wysokości"),
    (r"\bHill Giant\b", "olbrzym wzgórzowy"),
    (r"\bArchfey\b", "Arcyfey"),
    (r"\bZhentarim Ruffian\b", "Oprych Zhentarimów"),
    (r"\bBanneret\b", "Chorąży"),
    (r"\bGunslinger\b", "Rewolwerowiec"),
    (r"\bDevastator\b", "Niszczyciel"),
    (r"\bGuiding Bolt\b", "Pocisk wiodący"),
    (r"\bStarry Wisp\b", "Gwiezdny ognik"),
    (r"\bGwiaździsty Wisp\b", "Gwiezdny ognik"),
    (r"\bGwiezdnego Wisp\b", "Gwiezdnego ognika"),
    (r"\bRestore Vitality\b", "Przywrócenie witalności"),
    (r"\bBranding Smite\b", "Piętnujące ugodzenie"),
    (r"\bWrathful Smite\b", "Gniewne ugodzenie"),
    (r"\bShining Smite\b", "Lśniące ugodzenie"),
    (r"\bPhantasmal Force\b", "Urojona siła"),
    (r"\bPhantasmal Killer\b", "Urojony zabójca"),
    (r"\bDispel Evil and Good\b", "Rozproszenie dobra i zła"),
    (r"\bSee Invisibility\b", "Widzenie niewidzialnego"),
    (r"\bFaerie Fire\b", "Blask faerie"),
    (r"\bInsect Plague\b", "Plaga owadów"),
    (r"\bDeath Armor\b", "Zbroja śmierci"),
    (r"\bPhantom Steed\b", "Widmowy rumak"),
    (r"\bEnsnaring Strike\b", "Pętające uderzenie"),
    (r"\bSteel Wind Strike\b", "Uderzenie stalowego wichru"),
    (r"\bWarding Bond\b", "Ochronna więź"),
    (r"\bWitch Bolt\b", "Wiedźmowy pocisk"),
    (r"\bGoodberry\b", "Dobre jagody"),
    (r"\bSpike Growth\b", "Wzrost kolców"),
    (r"\bWardaway\b", "Odpędzenie"),
    (r"\bTopple\b", "Obalenie"),
    (r"\bPush\b", "Popchnięcie"),
    (r"\bTasha's Hideous Laughter\b", "Ohydny śmiech Tashy"),
    (r"\bCompelled Duel\b", "Prowokacja"),
    (r"\bAnimal Friendship\b", "Przyjaciel zwierząt"),
    (r"\bColor Spray\b", "Kolorowy rozprysk"),
    (r"\bCreate or Destroy Water\b", "Stworzenie lub zniszczenie wody"),
    (r"\bLongstrider\b", "Szybkonogi"),
    (r"\bInvisibility\b", "Niewidzialność"),
    (r"\bBlindness\b", "Ślepota"),
    (r"\bCloudkill\b", "Zabójcza chmura"),
    (r"\bContagion\b", "Zaraza"),
    (r"\bBlink\b", "Mignięcie"),
    (r"\bBlur\b", "Rozmycie"),
    (r"\bBane\b", "Zguba"),
    (r"\bTrue Strike\b", "Prawdziwe uderzenie"),
    (r"\bRaniący Bolt\b", "Raniący bełt"),
    (r"\bObdania Klątwy\b", "Zdjęcia klątwy"),
    (r"\bstan Niezdolności\b", "stan Obezwładnienia"),
    (r"\bobrażenia tłuczące\b", "obrażenia obuchowe"),
    (r"\bobrażenia Tłuczące\b", "obrażenia obuchowe"),
    (r"\bTłuczące Korzenie\b", "Obuchowe korzenie"),
    (r"\bTłuczące korzenie\b", "Obuchowe korzenie"),
    (r"\bEladrin Seasons\b", "Pory roku eladrinów"),
    (r"\bRycerze Sanguine\b", "Rycerze Krwi"),
    (r"\bZaklęcia Spellfire\b", "Czary magicznego ognia"),
    (r"\bSpellfire Storm\b", "Burza magicznego ognia"),
    (r"\bSpellfire Flare\b", "Rozbłysk magicznego ognia"),
    (r"\bSpellfire\b", "magiczny ogień"),
    (r"\bAktualizacja Cantripa\b", "Ulepszenie sztuczki"),
    (r"\bAcrobatics\b", "Akrobatyka"),
    (r"\bAthletics\b", "Atletyka"),
    (r"\bAnimal Handling\b", "Opieka nad zwierzętami"),
    (r"\bArcana\b", "Wiedza Tajemna"),
    (r"\bHistory\b", "Historia"),
    (r"\bNature\b", "Natura"),
    (r"\bReligion\b", "Religia"),
    (r"\bDeception\b", "Oszustwo"),
    (r"\bPerception\b", "Percepcja"),
    (r"\bWydajność\b", "Występy"),
    (r"\bpunktów sorcery\b", "punktów zaklinania"),
    (r"\bpunkt sorcery\b", "punkt zaklinania"),
    (r"\bscores\b", ""),
    (r"\bAkcj(a|ą|ę|i) Bonusow(a|ą|ą|ej)\b", None),
    (r"\bAkcja Bonusowa\b", "Akcja dodatkowa"),
    (r"\bAkcji Bonusowej\b", "Akcji dodatkowej"),
    (r"\bAkcję Bonusową\b", "Akcję dodatkową"),
    (r"\bAkcją Bonusową\b", "Akcją dodatkową"),
    (r"\bakcja bonusowa\b", "akcja dodatkowa"),
    (r"\bakcji bonusowej\b", "akcji dodatkowej"),
    (r"\bakcję bonusową\b", "akcję dodatkową"),
    (r"\bakcją bonusową\b", "akcją dodatkową"),
    (r"\bPunkty Życia\b", "Punkty wytrzymałości"),
    (r"\bPunktów Życia\b", "Punktów wytrzymałości"),
    (r"\bPunktami Życia\b", "Punktami wytrzymałości"),
    (r"\bPunktach Życia\b", "Punktach wytrzymałości"),
    (r"\bPunktu Życia\b", "Punktu wytrzymałości"),
    (r"\bPunktem Życia\b", "Punktem wytrzymałości"),
    (r"\bPunkcie Życia\b", "Punkcie wytrzymałości"),
    (r"\bPunkt Życia\b", "Punkt wytrzymałości"),
    (r"\bpunktów życia\b", "punktów wytrzymałości"),
    (r"\bpunkty życia\b", "punkty wytrzymałości"),
    (r"\bpunkt życia\b", "punkt wytrzymałości"),
    (r"\bDługi Odpoczynek\b", "Długi odpoczynek"),
    (r"\bDługiego Odpoczynku\b", "Długiego odpoczynku"),
    (r"\bDługim Odpoczynku\b", "Długim odpoczynku"),
    (r"\bKrótki Odpoczynek\b", "Krótki odpoczynek"),
    (r"\bKrótkiego Odpoczynku\b", "Krótkiego odpoczynku"),
    (r"\bKrótkim Odpoczynku\b", "Krótkim odpoczynku"),
    (r"\bTemporary Hit Points\b", "tymczasowe punkty wytrzymałości"),
    (r"\bHit Points\b", "punkty wytrzymałości"),
    (r"\bHit Point\b", "punkt wytrzymałości"),
    (r"\bBonus Action\b", "akcja dodatkowa"),
    (r"\bSaving Throws\b", "rzuty obronne"),
    (r"\bSaving Throw\b", "rzut obronny"),
    (r"\bAttack Rolls\b", "testy ataku"),
    (r"\bAttack Roll\b", "test ataku"),
    (r"\bSpell Slots\b", "komórki czarów"),
    (r"\bSpell Slot\b", "komórka czaru"),
    (r"\bProficiency Bonus\b", "premia z biegłości"),
    (r"\bLong Rest\b", "długi odpoczynek"),
    (r"\bShort Rest\b", "krótki odpoczynek"),
    (r"\bDisadvantage\b", "utrudnienie"),
    (r"\bAdvantage\b", "ułatwienie"),
    (r"\bReckless Attack\b", "Szaleńczy atak"),
    (r"\bUnarmed Strike\b", "atak bez broni"),
    (r"\bRaging\b", "w szale"),
    (r"\bRage\b", "Szał"),
    (r"\bStrength\b", "Siła"),
    (r"\bDexterity\b", "Zręczność"),
    (r"\bConstitution\b", "Kondycja"),
    (r"\bIntelligence\b", "Inteligencja"),
    (r"\bWisdom\b", "Mądrość"),
    (r"\bCharisma\b", "Charyzma"),
    (r"\bInsight\b", "Intuicja"),
    (r"\bMedicine\b", "Medycyna"),
    (r"\bDash\b", "Sprint"),
    (r"\bDisengage\b", "Odstąpienie"),
    (r"\bProne\b", "Powalenie"),
    (r"\bUnconscious\b", "Nieprzytomność"),
    (r"\bTurn Undead\b", "Odpędzanie nieumarłych"),
    (r"\bChannel Divinity\b", "Akt wiary"),
    (r"\bBreath Weapon\b", "zionięcie"),
    (r"\bWrath of the Sea\b", "Gniew morza"),
    (r"\bWrath of the Wild\b", "Gniew dziczy"),
    (r"\bToll the Dead\b", "Żałobny dzwon"),
    (r"\bPotęga Giganta\b", "Potęga olbrzyma"),
    (r"\bRycerze Ruhnów\b", "Rycerze runiczni"),
    (r"\bMaverick Spirit\b", "Duch indywidualisty"),
    (r"\bSkin of Your Teeth\b", "O włos"),
    (r"\bCantrips\b", "sztuczki"),
    (r"\bCantripy\b", "Sztuczki"),
    (r"\bCantrip\b", "sztuczka"),
    (r"\bArcane Trickster\b", "Mistyczny oszust"),
    (r"\bArtificers\b", "Wynalazcy"),
    (r"\bArtificera\b", "Wynalazcy"),
    (r"\bArtificer\b", "Wynalazca"),
    (r"\bSorcerer\b", "Zaklinacz"),
    (r"\bWarlock\b", "Czarownik"),
    (r"\bWizard\b", "Mag"),
    (r"\bRanger\b", "Łowca"),
    (r"\bPerformance\b", "Występy"),
    (r"\bPersuasion\b", "Perswazja"),
    (r"\bStealth\b", "Skradanie się"),
    (r"\bSleight of Hand\b", "Zwinne dłonie"),
    (r"\bIntimidation\b", "Zastraszanie"),
    (r"\bSurvival\b", "Sztuka przetrwania"),
    (r"\bBardic Inspiration\b", "bardowska inspiracja"),
    (r"\bHeroic Inspiration\b", "heroiczną inspirację"),
    (r"\bobrażenia Radiant\b", "obrażenia od światłości"),
    (r"\bHell's Lash\b", "Piekielny bicz"),
    (r"\bNick\b", "Nacięcie"),
    (r"\bVex\b", "Nękanie"),
    (r"\bCollege of Spirits\b", "Kolegium Duchów"),
    (r"\bDomena Grave\b", "Domena Grobu"),
    (r"\bDomeny Grave\b", "Domeny Grobu"),
    (r"\bTropical Land\b", "Kraina tropikalna"),
    (r"\bAcid Splash\b", "Kwasowy rozprysk"),
    (r"\bRay of Sickness\b", "Promień zatrucia"),
    (r"\bWeb\b", "Pajęczyna"),
    (r"\bDivine Spark\b", "Boska iskra"),
    (r"\bPrestidigitacja\b", "Kuglarstwo"),
    (r"\bGromowcowe Uderzenie\b", "Grzmiące ugodzenie"),
    (r"\bBardyckiej Inspiracji\b", "bardowskiej inspiracji"),
    (r"\binspirację bardyczną\b", "bardowską inspirację"),
    (r"\bDzikej postaci\b", "Dzikiej postaci"),
    (r"\bspowią\b", "spowiją"),
    (r"\bbezlitosni\b", "bezlitośni"),
    (r"\brozproszena\b", "rozproszona"),
    (r"\bobrażeniam\b", "obrażeniom"),
    (r"\bnie-elfickich\b", "nieelfickich"),
    (r"\barcywróżkiem\b", "arcyfey"),
    (r"\bposiadają wampiryczne zdolności\b", "mają wampiryczne zdolności"),
    (r"\bposiadają cechy zdradzające\b", "mają cechy zdradzające"),
    (r"\bJeśli nie posiadasz właściwości\b", "Jeśli nie masz właściwości"),
    (r"\bDopóki posiadasz tę wiedzę\b", "Dopóki masz tę wiedzę"),
    (r"\bAtak Szarżowy\b", "Atak z szarży"),
    (r"\bW przypadku nieudanego rzutu obronnego,", "W przypadku nieudanego rzutu obronnego"),
    (r"\bW przypadku udanego rzutu obronnego,", "W przypadku udanego rzutu obronnego"),
    (r"\bPremia jest równy\b", "Premia jest równa"),
    (r"\bTryb uczenia sztuczka jest aktywny\.", "Tryb nauki sztuczek jest aktywny."),
    (
        r"\bWybranie sztuczki do rzucenia na stałe uczy cię tego od razu\b",
        "Wybranie sztuczki powoduje, że od razu poznajesz ją na stałe",
    ),
    (r"\bPo wybraniu dwóch różnych sztuczek tryb ten kończy się\.", "Tryb ten wyłącza się po wybraniu dwóch różnych sztuczek."),
    (r"\bPo wybraniu trzech różnych sztuczek tryb ten kończy się\.", "Tryb ten wyłącza się po wybraniu trzech różnych sztuczek."),
    (r"\bTryb nauki pisowni jest aktywny\.", "Tryb nauki czarów jest aktywny."),
    (
        r"\bWybierając zaklęcie do rzucenia na stałe, nauczysz się go od razu — nie potrzebujesz ważnego celu ani zakończenia jego rzucania\.",
        "Po wybraniu czaru od razu poznajesz go na stałe — nie potrzebujesz prawidłowego celu ani nie musisz kończyć rzucania.",
    ),
    (r"\bPo wybraniu zaklęcia tryb ten kończy się\.", "Tryb ten wyłącza się po wybraniu czaru."),
    (r"\batrybuty swojej bestii - z wyjątkiem\b", "atrybuty swojej bestii — z wyjątkiem"),
    (r"\bbroń paktu - wybraną\b", "broń paktu — wybraną"),
    (r"\bmagii tropiciela - przesuwając\b", "magii tropiciela — przesuwając"),
    (r"\bstarszym bogiem - istotą\b", "starszym bogiem — istotą"),
    (r"\bz zdolności\b", "ze zdolności"),
    (r"\bpowyżej 3-go\b", "powyżej 3."),
    (r"\bpod warunkiem, że\b", "pod warunkiem że"),
    (r"\bDodatkowo,", "Ponadto"),
    (r"\bDodatkowo\b", "Ponadto"),
    (r"\bhide\b", "ukryć się"),
    (r"\bWild Magic Surge\b", "Przypływ dzikiej magii"),
    (r"\bWrath z Wild\b", "Gniew dziczy"),
    (r"\bUnnerving Aura\b", "Niepokojąca aura"),
    (r"\bmodifier\b", "modyfikator"),
    (r"\bModifier\b", "Modyfikator"),
    (r"\bBonus jest\b", "Premia jest"),
    (r"\bBonus ten\b", "Premia ta"),
    (r"\bminimalny bonus\b", "minimalna premia"),
    (r"\bminimum bonus\b", "minimalna premia"),
    (r"\bPunkty Sorcery\b", "Punkty zaklinania"),
    (r"\bpunkty sorcery\b", "punkty zaklinania"),
    (r"\bpunkty czarnoksięskie\b", "punkty zaklinania"),
    (r"\bPunkt Sorcery\b", "Punkt zaklinania"),
    (r"\bPunktów Sorcery\b", "Punktów zaklinania"),
    (r"\bPremia Biegłości\b", "premia z biegłości"),
    (r"\bDzikiego Przypływu Magii\b", "Przypływu dzikiej magii"),
    # Official BG3 uses komórka czaru. These cover all inflected literal
    # machine translations while preserving surrounding sentence grammar.
    (r"\bmiejscach na zaklęcia\b", "komórkach czarów"),
    (r"\bmiejscami na zaklęcia\b", "komórkami czarów"),
    (r"\bmiejscem na zaklęcie\b", "komórką czaru"),
    (r"\bmiejscu na zaklęcia\b", "komórce czaru"),
    (r"\bmiejscu na zaklęcie\b", "komórce czaru"),
    (r"\bmiejsc na zaklęcia\b", "komórek czarów"),
    (r"\bmiejsca na zaklęcia\b", "komórki czarów"),
    (r"\bmiejsca na zaklęcie\b", "komórki czaru"),
    (r"\bbez miejsca na zaklęcia\b", "bez komórki czaru"),
    (r"\bikonę miejsca na zaklęcia\b", "ikonę komórki czaru"),
    (r"\bmiejsce na zaklęcia\b", "komórkę czaru"),
    (r"\bmiejsce na zaklęcie\b", "komórkę czaru"),
    (r"\bmiejsca na czar\b", "komórki czaru"),
    (r"\bmiejsce na czar\b", "komórkę czaru"),
    (r"\bjedno komórkę czaru\b", "jedną komórkę czaru"),
    (r"\bto komórkę czaru\b", "tę komórkę czaru"),
    (r"\bkażde komórkę czaru\b", "każdą komórkę czaru"),
    (r"\bwydane komórkę czaru\b", "wydaną komórkę czaru"),
    (r"\bwykorzystane komórkę czaru\b", "wykorzystaną komórkę czaru"),
    (r"\bGigantów\b", "Olbrzymów"),
    (r"\bgigantów\b", "olbrzymów"),
    (r"\bGiganta\b", "Olbrzyma"),
    (r"\bgiganta\b", "olbrzyma"),
    (r"\bGigantem\b", "Olbrzymem"),
    (r"\bgigantem\b", "olbrzymem"),
    (r"\bGiganci\b", "Olbrzymy"),
    (r"\bgiganci\b", "olbrzymy"),
    (r"\bGigant\b", "Olbrzym"),
    (r"\bgigant\b", "olbrzym"),
    # Official Polish BG3 keeps condition names lowercase in running prose.
    (
        r"\b(Stan|stan|stanu|stanem|stanie|stany|stanów|stanom|stanami|stanach) "
        r"((?:Powalenia|Przerażenia|Obezwładnienia|Oślepienia|Nieprzytomności|Zauroczenia|"
        r"Unieruchomienia|Niewidzialności|Paraliżu|Zakrwawienia|Ogłuszenia|Zatrucia|"
        r"Pochwycenia|Płonięcia)(?:(?:,\s*|\s+(?:lub|albo|i|oraz)\s+)(?:Powalenia|"
        r"Przerażenia|Obezwładnienia|Oślepienia|Nieprzytomności|Zauroczenia|Unieruchomienia|"
        r"Niewidzialności|Paraliżu|Zakrwawienia|Ogłuszenia|Zatrucia|Pochwycenia|Płonięcia))*)\b",
        lambda match: f"{match.group(1)} {match.group(2).lower()}",
    ),
    (
        r"\b(efekt|efektu|efektem|efekcie) "
        r"((?:Powalenia|Przerażenia|Obezwładnienia|Oślepienia|Nieprzytomności|Zauroczenia|"
        r"Unieruchomienia|Niewidzialności|Paraliżu|Zakrwawienia|Ogłuszenia|Zatrucia|"
        r"Pochwycenia|Płonięcia)(?:(?:,\s*|\s+(?:lub|albo|i|oraz)\s+)(?:Powalenia|"
        r"Przerażenia|Obezwładnienia|Oślepienia|Nieprzytomności|Zauroczenia|Unieruchomienia|"
        r"Niewidzialności|Paraliżu|Zakrwawienia|Ogłuszenia|Zatrucia|Pochwycenia|Płonięcia))*)\b",
        lambda match: f"{match.group(1)} {match.group(2).lower()}",
    ),
    (
        r"\b(do chwili|do momentu) "
        r"(Powalenia|Przerażenia|Obezwładnienia|Oślepienia|Nieprzytomności|Zauroczenia|"
        r"Unieruchomienia|Niewidzialności|Paraliżu|Zakrwawienia|Ogłuszenia|Zatrucia|"
        r"Pochwycenia|Płonięcia)\b",
        lambda match: f"{match.group(1)} {match.group(2).lower()}",
    ),
    (r", Powalenia albo innego przemieszczenia", ", powalenia albo innego przemieszczenia"),
    (
        r"\b(stan|stanu|stanem|stanie) Wyciszony\b",
        lambda match: f"{match.group(1)} wyciszenia",
    ),
    (r"\brówne twojej [Ss]zybkości\.", "równe twojej szybkości ruchu."),
    (r"\brówna twojej [Ss]zybkości\.", "równa twojej szybkości ruchu."),
    (r"\brówną swojej [Ss]zybkości\.", "równą swojej szybkości ruchu."),
    (r"\bTrudnym Terenem\b", "trudnym terenem"),
    (r"\bjest Unieruchomiony\b", "jest unieruchomiony"),
    (r"\bjest Unieruchomiona\b", "jest unieruchomiona"),
    (r"\bjest Przerażony\b", "jest przerażony"),
    (r"\bjest Przerażona\b", "jest przerażona"),
    (r"\bjest Przerażone\b", "jest przerażone"),
    (r"\bzostaje Przerażony\b", "zostaje przerażony"),
    (r"\bzostaje Przerażona\b", "zostaje przerażona"),
    (r"\bzostaje Przerażone\b", "zostaje przerażone"),
    (r"\bzostaje Oślepiony\b", "zostaje oślepiony"),
    (r"\bzostaje Oślepiona\b", "zostaje oślepiona"),
    (r"\bzostaje Powalony\b", "zostaje powalony"),
    (r"\bzostaje Powalona\b", "zostaje powalona"),
    (r"\bzostaje Uwiązany\b", "zostaje uwiązany"),
]


SOURCE_AWARE_CLASS_REPLACEMENTS = {
    "Artificer": [
        (r"\bRzemieślnicy\b", "Wynalazcy"),
        (r"\brzemieślnicy\b", "wynalazcy"),
        (r"\bRzemieślnika\b", "Wynalazcy"),
        (r"\brzemieślnika\b", "wynalazcy"),
        (r"\bRzemieślnikiem\b", "Wynalazcą"),
        (r"\brzemieślnikiem\b", "wynalazcą"),
        (r"\bRzemieślnikowi\b", "Wynalazcy"),
        (r"\brzemieślnikowi\b", "wynalazcy"),
        (r"\bRzemieślników\b", "Wynalazców"),
        (r"\brzemieślników\b", "wynalazców"),
        (r"\bRzemieślnikom\b", "Wynalazcom"),
        (r"\brzemieślnikom\b", "wynalazcom"),
        (r"\bRzemieślnik\b", "Wynalazca"),
        (r"\brzemieślnik\b", "wynalazca"),
    ],
    "Sorcerer": [
        (r"\bCzarnoksiężnicy\b", "Zaklinacze"),
        (r"\bczarnoksiężnicy\b", "zaklinacze"),
        (r"\bCzarnoksiężnika\b", "Zaklinacza"),
        (r"\bczarnoksiężnika\b", "zaklinacza"),
        (r"\bCzarnoksiężnikiem\b", "Zaklinaczem"),
        (r"\bczarnoksiężnikiem\b", "zaklinaczem"),
        (r"\bCzarnoksiężnikowi\b", "Zaklinaczowi"),
        (r"\bczarnoksiężnikowi\b", "zaklinaczowi"),
        (r"\bCzarnoksiężnik\b", "Zaklinacz"),
        (r"\bczarnoksiężnik\b", "zaklinacz"),
    ],
    "Warlock": [
        (r"\bCzarnoksiężnicy\b", "Czarownicy"),
        (r"\bczarnoksiężnicy\b", "czarownicy"),
        (r"\bCzarnoksiężnika\b", "Czarownika"),
        (r"\bczarnoksiężnika\b", "czarownika"),
        (r"\bCzarnoksiężnik\b", "Czarownik"),
        (r"\bczarnoksiężnik\b", "czarownik"),
        (r"\bCzarnoksiężnikiem\b", "Czarownikiem"),
        (r"\bczarnoksiężnikiem\b", "czarownikiem"),
    ],
    "Wizard": [
        (r"\bCzarodzieje\b", "Magowie"),
        (r"\bczarodzieje\b", "magowie"),
        (r"\bCzarodzieja\b", "Maga"),
        (r"\bczarodzieja\b", "maga"),
        (r"\bCzarodziejem\b", "Magiem"),
        (r"\bczarodziejem\b", "magiem"),
        (r"\bCzarodziej\b", "Mag"),
        (r"\bczarodziej\b", "mag"),
        (r"\bCzarodziejów\b", "Magów"),
        (r"\bczarodziejów\b", "magów"),
    ],
    "Ranger": [
        (r"\bRangerzy\b", "Łowcy"),
        (r"\brangerzy\b", "łowcy"),
        (r"\bRangera\b", "Łowcy"),
        (r"\brangera\b", "łowcy"),
        (r"\bRangerem\b", "Łowcą"),
        (r"\brangerem\b", "łowcą"),
        (r"\bRanger\b", "Łowca"),
        (r"\branger\b", "łowca"),
    ],
}


SOURCE_AWARE_TERM_REPLACEMENTS = {
    "Withering Wordplay": [
        (r"\bWiędnąca gra słów\b", "Cięta gra słów"),
    ],
    "Sentinel": [
        (r"\batutu Strażnik\b", "atutu Wartownik"),
        (r"\batutu strażnik\b", "atutu Wartownik"),
    ],
    "Creature": [
        (r"\bStworzenie\b", "Istota"),
        (r"\bstworzenie\b", "istota"),
        (r"\bKażde stworzenie\b", "Każda istota"),
        (r"\bkażde stworzenie\b", "każda istota"),
        (r"\bStworzenie, które\b", "Istota, która"),
        (r"\bstworzenie, które\b", "istota, która"),
        (r"\bStworzeniami\b", "Istotami"),
        (r"\bstworzeniami\b", "istotami"),
        (r"\bStworzeniom\b", "Istotom"),
        (r"\bstworzeniom\b", "istotom"),
        (r"\bStworzeniem\b", "Istotą"),
        (r"\bstworzeniem\b", "istotą"),
        (r"\bStworzeniu\b", "Istocie"),
        (r"\bstworzeniu\b", "istocie"),
        (r"\bStworzeń\b", "Istot"),
        (r"\bstworzeń\b", "istot"),
        (r"\bStworzenia\b", "Istoty"),
        (r"\bstworzenia\b", "istoty"),
    ],
    "Long Rest": [
        (r"\bDługim Odpoczynku\b", "długim odpoczynku"),
        (r"\bDługim odpoczynku\b", "długim odpoczynku"),
        (r"\bDługiego Odpoczynku\b", "długiego odpoczynku"),
        (r"\bDługiego odpoczynku\b", "długiego odpoczynku"),
        (r"\bDługi Odpoczynek\b", "długi odpoczynek"),
        (r"\bDługi odpoczynek\b", "długi odpoczynek"),
    ],
    "Short Rest": [
        (r"\bKrótkim Odpoczynku\b", "krótkim odpoczynku"),
        (r"\bKrótkim odpoczynku\b", "krótkim odpoczynku"),
        (r"\bKrótkiego Odpoczynku\b", "krótkiego odpoczynku"),
        (r"\bKrótkiego odpoczynku\b", "krótkiego odpoczynku"),
        (r"\bKrótki Odpoczynek\b", "krótki odpoczynek"),
        (r"\bKrótki odpoczynek\b", "krótki odpoczynek"),
    ],
    "Bonus Action": [
        (r"\bAkcjami Dodatkowymi\b", "akcjami dodatkowymi"),
        (r"\bAkcjach Dodatkowych\b", "akcjach dodatkowych"),
        (r"\bAkcji Dodatkowej\b", "akcji dodatkowej"),
        (r"\bAkcji dodatkowej\b", "akcji dodatkowej"),
        (r"\bAkcją Dodatkową\b", "akcją dodatkową"),
        (r"\bAkcją dodatkową\b", "akcją dodatkową"),
        (r"\bAkcję Dodatkową\b", "akcję dodatkową"),
        (r"\bAkcję dodatkową\b", "akcję dodatkową"),
        (r"\bAkcja Dodatkowa\b", "akcja dodatkowa"),
        (r"\bAkcja dodatkowa\b", "akcja dodatkowa"),
    ],
    "Sorcery Point": [
        (r"\bPunktami Magii\b", "punktami zaklinania"),
        (r"\bpunktami Magii\b", "punktami zaklinania"),
        (r"\bPunktach Magii\b", "punktach zaklinania"),
        (r"\bpunktach Magii\b", "punktach zaklinania"),
        (r"\bPunktów Magii\b", "punktów zaklinania"),
        (r"\bpunktów Magii\b", "punktów zaklinania"),
        (r"\bPunktem Magii\b", "punktem zaklinania"),
        (r"\bpunktem Magii\b", "punktem zaklinania"),
        (r"\bPunktu Magii\b", "punktu zaklinania"),
        (r"\bpunktu Magii\b", "punktu zaklinania"),
        (r"\bPunkty Magii\b", "punkty zaklinania"),
        (r"\bpunkty Magii\b", "punkty zaklinania"),
        (r"\bPunkt Magii\b", "punkt zaklinania"),
        (r"\bpunkt Magii\b", "punkt zaklinania"),
        (r"\bpunktami magii\b", "punktami zaklinania"),
        (r"\bpunktach magii\b", "punktach zaklinania"),
        (r"\bpunktów magii\b", "punktów zaklinania"),
        (r"\bpunktem magii\b", "punktem zaklinania"),
        (r"\bpunktu magii\b", "punktu zaklinania"),
        (r"\bpunkty magii\b", "punkty zaklinania"),
        (r"\bpunkt magii\b", "punkt zaklinania"),
        (r"\bPunktami Zaklinania\b", "punktami zaklinania"),
        (r"\bPunktach Zaklinania\b", "punktach zaklinania"),
        (r"\bPunktów Zaklinania\b", "punktów zaklinania"),
        (r"\bPunktem Zaklinania\b", "punktem zaklinania"),
        (r"\bPunktu Zaklinania\b", "punktu zaklinania"),
        (r"\bPunkty Zaklinania\b", "punkty zaklinania"),
        (r"\bPunkt Zaklinania\b", "punkt zaklinania"),
    ],
    "Proficiency Bonus": [
        (r"\bpremią za Biegłość\b", "premią z biegłości"),
        (r"\bpremią za biegłość\b", "premią z biegłości"),
        (r"\bpremii za Biegłość\b", "premii z biegłości"),
        (r"\bpremii za biegłość\b", "premii z biegłości"),
        (r"\bpremię za Biegłość\b", "premię z biegłości"),
        (r"\bpremię za biegłość\b", "premię z biegłości"),
        (r"\bpremia za Biegłość\b", "premia z biegłości"),
        (r"\bpremia za biegłość\b", "premia z biegłości"),
        (r"\bpremią do Biegłości\b", "premią z biegłości"),
        (r"\bpremią do biegłości\b", "premią z biegłości"),
        (r"\bpremii do Biegłości\b", "premii z biegłości"),
        (r"\bpremii do biegłości\b", "premii z biegłości"),
        (r"\bpremię do Biegłości\b", "premię z biegłości"),
        (r"\bpremię do biegłości\b", "premię z biegłości"),
        (r"\bpremia do Biegłości\b", "premia z biegłości"),
        (r"\bpremia do biegłości\b", "premia z biegłości"),
    ],
    "Advantage": [
        (r"\bPrzewagą\b", "Ułatwieniem"),
        (r"\bprzewagą\b", "ułatwieniem"),
        (r"\bPrzewadze\b", "Ułatwieniu"),
        (r"\bprzewadze\b", "ułatwieniu"),
        (r"\bPrzewagi\b", "Ułatwienia"),
        (r"\bprzewagi\b", "ułatwienia"),
        (r"\bPrzewagę\b", "Ułatwienie"),
        (r"\bprzewagę\b", "ułatwienie"),
        (r"\bPrzewaga\b", "Ułatwienie"),
        (r"\bprzewaga\b", "ułatwienie"),
    ],
    "Disadvantage": [
        (r"\bNiekorzystnością\b", "Utrudnieniem"),
        (r"\bniekorzystnością\b", "utrudnieniem"),
        (r"\bNiekorzyścią\b", "Utrudnieniem"),
        (r"\bniekorzyścią\b", "utrudnieniem"),
        (r"\bNiekorzystności\b", "Utrudnienia"),
        (r"\bniekorzystności\b", "utrudnienia"),
        (r"\bNiekorzyści\b", "Utrudnienia"),
        (r"\bniekorzyści\b", "utrudnienia"),
        (r"\bNiekorzystność\b", "Utrudnienie"),
        (r"\bniekorzystność\b", "utrudnienie"),
        (r"\bNiekorzyść\b", "Utrudnienie"),
        (r"\bniekorzyść\b", "utrudnienie"),
        (r"\bWadą\b", "Utrudnieniem"),
        (r"\bwadą\b", "utrudnieniem"),
        (r"\bWadzie\b", "Utrudnieniu"),
        (r"\bwadzie\b", "utrudnieniu"),
        (r"\bWady\b", "Utrudnienia"),
        (r"\bwady\b", "utrudnienia"),
        (r"\bWadę\b", "Utrudnienie"),
        (r"\bwadę\b", "utrudnienie"),
        (r"\bWada\b", "Utrudnienie"),
        (r"\bwada\b", "utrudnienie"),
    ],
    "Feat": [
        (r"\bWyczynami\b", "Atutami"),
        (r"\bwyczynami\b", "atutami"),
        (r"\bWyczynach\b", "Atutach"),
        (r"\bwyczynach\b", "atutach"),
        (r"\bWyczynów\b", "Atutów"),
        (r"\bwyczynów\b", "atutów"),
        (r"\bWyczynem\b", "Atutem"),
        (r"\bwyczynem\b", "atutem"),
        (r"\bWyczynu\b", "Atutu"),
        (r"\bwyczynu\b", "atutu"),
        (r"\bWyczyny\b", "Atuty"),
        (r"\bwyczyny\b", "atuty"),
        (r"\bWyczyn\b", "Atut"),
        (r"\bwyczyn\b", "atut"),
    ],
    "Attack Roll": [
        (r"\bRzutami ataku\b", "Testami ataku"),
        (r"\bRzutach ataku\b", "Testach ataku"),
        (r"\bRzutów ataku\b", "Testów ataku"),
        (r"\bRzutem ataku\b", "Testem ataku"),
        (r"\bRzutu ataku\b", "Testu ataku"),
        (r"\bRzuty ataku\b", "Testy ataku"),
        (r"\bRzut ataku\b", "Test ataku"),
        (r"\bRzutami Ataku\b", "Testami ataku"),
        (r"\brzutami ataku\b", "testami ataku"),
        (r"\bRzutach Ataku\b", "Testach ataku"),
        (r"\brzutach ataku\b", "testach ataku"),
        (r"\bRzutów Ataku\b", "Testów ataku"),
        (r"\brzutów ataku\b", "testów ataku"),
        (r"\bRzutem Ataku\b", "Testem ataku"),
        (r"\brzutem ataku\b", "testem ataku"),
        (r"\bRzutu Ataku\b", "Testu ataku"),
        (r"\brzutu ataku\b", "testu ataku"),
        (r"\bRzuty Ataku\b", "Testy ataku"),
        (r"\brzuty ataku\b", "testy ataku"),
        (r"\bRzut Ataku\b", "Test ataku"),
        (r"\brzut ataku\b", "test ataku"),
        (r"\bRzutami na atak\b", "Testami ataku"),
        (r"\brzutami na atak\b", "testami ataku"),
        (r"\bRzutach na atak\b", "Testach ataku"),
        (r"\brzutach na atak\b", "testach ataku"),
        (r"\bRzutów na atak\b", "Testów ataku"),
        (r"\brzutów na atak\b", "testów ataku"),
        (r"\bRzutem na atak\b", "Testem ataku"),
        (r"\brzutem na atak\b", "testem ataku"),
        (r"\bRzutu na atak\b", "Testu ataku"),
        (r"\brzutu na atak\b", "testu ataku"),
        (r"\bRzucie na atak\b", "Teście ataku"),
        (r"\brzucie na atak\b", "teście ataku"),
        (r"\bRzuty na atak\b", "Testy ataku"),
        (r"\brzuty na atak\b", "testy ataku"),
        (r"\bRzut na atak\b", "Test ataku"),
        (r"\brzut na atak\b", "test ataku"),
    ],
    "Magic action": [
        (r"\bAkcjami magicznymi\b", "Akcjami Magii"),
        (r"\bakcjami magicznymi\b", "akcjami Magii"),
        (r"\bAkcjach magicznych\b", "Akcjach Magii"),
        (r"\bakcjach magicznych\b", "akcjach Magii"),
        (r"\bAkcji magicznej\b", "Akcji Magii"),
        (r"\bakcji magicznej\b", "akcji Magii"),
        (r"\bAkcją magiczną\b", "Akcją Magii"),
        (r"\bakcją magiczną\b", "akcją Magii"),
        (r"\bAkcję magiczną\b", "Akcję Magii"),
        (r"\bakcję magiczną\b", "akcję Magii"),
        (r"\bAkcja magiczna\b", "Akcja Magii"),
        (r"\bakcja magiczna\b", "akcja Magii"),
        (r"\bAkcji Magicznej\b", "Akcji Magii"),
        (r"\bakcji Magicznej\b", "akcji Magii"),
        (r"\bAkcją Magiczną\b", "Akcją Magii"),
        (r"\bakcją Magiczną\b", "akcją Magii"),
        (r"\bAkcję Magiczną\b", "Akcję Magii"),
        (r"\bakcję Magiczną\b", "akcję Magii"),
        (r"\bAkcja Magiczna\b", "Akcja Magii"),
        (r"\bakcja Magiczna\b", "akcja Magii"),
        (r"\bAkcja Magia\b", "Akcja Magii"),
        (r"\bakcja Magia\b", "akcja Magii"),
    ],
    "Lightning damage": [
        (r"\bObrażenia od Pioruna\b", "Obrażenia od elektryczności"),
        (r"\bobrażenia od Pioruna\b", "obrażenia od elektryczności"),
        (r"\bobrażenia od pioruna\b", "obrażenia od elektryczności"),
        (r"\bobrażenia od Piorunów\b", "obrażenia od elektryczności"),
        (r"\bobrażenia od piorunów\b", "obrażenia od elektryczności"),
        (r"\bobrażenia od Błyskawic\b", "obrażenia od elektryczności"),
        (r"\bobrażenia od błyskawic\b", "obrażenia od elektryczności"),
    ],
    "Thunder damage": [
        (r"\bObrażenia Pioruna\b", "Obrażenia od dźwięku"),
        (r"\bobrażenia Pioruna\b", "obrażenia od dźwięku"),
        (r"\bObrażenia od Pioruna\b", "Obrażenia od dźwięku"),
        (r"\bobrażenia od Pioruna\b", "obrażenia od dźwięku"),
        (r"\bobrażenia od pioruna\b", "obrażenia od dźwięku"),
        (r"\bobrażenia od Piorunów\b", "obrażenia od dźwięku"),
        (r"\bobrażenia od piorunów\b", "obrażenia od dźwięku"),
        (r"\bobrażenia od Grzmotu\b", "obrażenia od dźwięku"),
        (r"\bobrażenia od grzmotu\b", "obrażenia od dźwięku"),
        (r"\bobrażenia od Grzmotów\b", "obrażenia od dźwięku"),
        (r"\bobrażenia od grzmotów\b", "obrażenia od dźwięku"),
    ],
    "Slashing damage": [
        (r"\bobrażenia Tnące\b", "obrażenia cięte"),
        (r"\bobrażenia tnące\b", "obrażenia cięte"),
    ],
    "Bludgeoning damage": [
        (r"\bobrażenia Tłuczone\b", "obrażenia obuchowe"),
        (r"\bobrażenia tłuczone\b", "obrażenia obuchowe"),
    ],
    "Radiant damage": [
        (r"\bobrażenia od Promieniowania\b", "obrażenia od światłości"),
        (r"\bObrażenia od Promieniowania\b", "Obrażenia od światłości"),
        (r"\bobrażenia Świetlistości\b", "obrażenia od światłości"),
        (r"\bobrażenia świetlistości\b", "obrażenia od światłości"),
        (r"\bobrażenia Promieniowania\b", "obrażenia od światłości"),
        (r"\bobrażenia promieniowania\b", "obrażenia od światłości"),
        (r"\bobrażenia Promienne\b", "obrażenia od światłości"),
        (r"\bobrażenia promienne\b", "obrażenia od światłości"),
        (r"\bObrażenia Promienne\b", "Obrażenia od światłości"),
        (r"\bPromienne\b", "od światłości"),
        (r"\bPromieniowania\b", "od światłości"),
    ],
    "Channel Divinity": [
        (r"\bswoją Boskość Kanału\b", "swój Akt wiary"),
        (r"\bswojej Boskości Kanału\b", "swojego Aktu wiary"),
        (r"\bBoskości Kanału\b", "Aktu wiary"),
        (r"\bBoskość Kanału\b", "Akt wiary"),
    ],
    "Wild Shape": [
        (r"\bDzikiego Kształtu\b", "Dzikiej postaci"),
        (r"\bdzikiego kształtu\b", "dzikiej postaci"),
        (r"\bDzikim Kształtem\b", "Dziką postacią"),
        (r"\bdzikim kształtem\b", "dziką postacią"),
        (r"\bDziki Kształt\b", "Dzika postać"),
        (r"\bdziki kształt\b", "dzika postać"),
    ],
    "feature": [
        (r"\btej funkcji\b", "tej zdolności"),
        (r"\btę funkcję\b", "tę zdolność"),
        (r"\bta funkcja\b", "ta zdolność"),
        (r"\bfunkcją\b", "zdolnością"),
        (r"\bfunkcji\b", "zdolności"),
        (r"\bfunkcję\b", "zdolność"),
        (r"\bfunkcja\b", "zdolność"),
    ],
}


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load(path: Path) -> tuple[ET.ElementTree, list[ET.Element], dict[str, str]]:
    tree = ET.parse(path)
    nodes = list(tree.getroot().findall("content"))
    return tree, nodes, {node.attrib["contentuid"]: node.text or "" for node in nodes}


def stable_map(source: dict[str, str], target: dict[str, str]) -> dict[str, str]:
    candidates: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for uid, text in source.items():
        translated = target.get(uid, "")
        if text and translated:
            candidates[normalise(text)][translated] += 1
    result: dict[str, str] = {}
    for text, options in candidates.items():
        ranked = options.most_common()
        if len(ranked) == 1 or ranked[0][1] > ranked[1][1]:
            result[text] = ranked[0][0]
    return result


def official_level_feature_title(source_text: str, official: dict[str, str]) -> str | None:
    match = LEVEL_FEATURE_RE.fullmatch(source_text.strip())
    if match is None:
        return None
    feature_name = match.group(2)
    if feature_name in OFFICIAL_LEVEL_FEATURE_BLOCKLIST:
        return None
    translated_name = official.get(normalise(feature_name))
    if translated_name is None:
        return None
    return f"Poziom {match.group(1)}: {translated_name}"


def official_tag_map(source: dict[str, str], target: dict[str, str]) -> dict[tuple[str, str], str]:
    candidates: dict[tuple[str, str], collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for uid, source_text in source.items():
        target_text = target.get(uid, "")
        source_tags = TAG_BLOCK_RE.findall(source_text)
        target_tags = TAG_BLOCK_RE.findall(target_text)
        if not source_tags or len(source_tags) != len(target_tags):
            continue
        for (source_open, source_inner, _), (target_open, target_inner, _) in zip(source_tags, target_tags):
            if source_open == target_open and source_inner and target_inner:
                candidates[(source_open, source_inner)][target_inner] += 1
    result: dict[tuple[str, str], str] = {}
    for key, options in candidates.items():
        ranked = options.most_common()
        if len(ranked) == 1 or ranked[0][1] > ranked[1][1]:
            result[key] = ranked[0][0]
    return result


def walk_pairs(source: Any, target: Any, pairs: dict[str, collections.Counter[str]]) -> None:
    if isinstance(source, str) and isinstance(target, str):
        if source.strip() and target.strip() and source != target:
            pairs[normalise(source)][target] += 1
    elif isinstance(source, dict) and isinstance(target, dict):
        for key in source.keys() & target.keys():
            walk_pairs(source[key], target[key], pairs)
    elif isinstance(source, list) and isinstance(target, list):
        for source_item, target_item in zip(source, target):
            walk_pairs(source_item, target_item, pairs)


def community_map(root: Path) -> dict[str, str]:
    pairs: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    en_root = root / "en"
    pl_root = root / "pl"
    for en_path in en_root.rglob("*.json"):
        pl_path = pl_root / en_path.relative_to(en_root)
        if not pl_path.exists():
            continue
        source = json.loads(en_path.read_text(encoding="utf-8"))
        target = json.loads(pl_path.read_text(encoding="utf-8"))
        walk_pairs(source, target, pairs)

    result: dict[str, str] = {}
    for source, options in pairs.items():
        ranked = options.most_common()
        if len(ranked) > 1 and ranked[0][1] == ranked[1][1]:
            continue
        target = ranked[0][0]
        if "@UUID" in target or "[[/" in target:
            continue
        if BRACKET_RE.findall(source) != BRACKET_RE.findall(target):
            continue
        if collections.Counter(TAG_RE.findall(source)) != collections.Counter(TAG_RE.findall(target)):
            if TAG_RE.search(source) or TAG_RE.search(target):
                continue
        result[source] = target
    return result


def html_to_text(value: str) -> str:
    value = re.sub(
        r'<section[^>]*class="secret"[^>]*>.*?</section>',
        " ",
        value,
        flags=re.IGNORECASE | re.DOTALL,
    )
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    value = re.sub(r"</(?:p|div|h[1-6]|blockquote|li)\s*>", "\n\n", value, flags=re.IGNORECASE)
    value = re.sub(r"<li[^>]*>", "• ", value, flags=re.IGNORECASE)
    value = re.sub(r"<[^>]+>", "", value)
    value = html.unescape(value)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in value.splitlines()]
    value = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", value).strip()


def community_stripped_map(root: Path) -> dict[str, str]:
    pairs: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    en_root = root / "en"
    pl_root = root / "pl"

    def collect(source: Any, target: Any) -> None:
        if isinstance(source, str) and isinstance(target, str):
            if not source.strip() or not target.strip() or source == target:
                return
            if "@UUID" in target or "[[/" in target:
                return
            source_text = html_to_text(source)
            target_text = html_to_text(target)
            if source_text and target_text and normalise(source_text) != normalise(target_text):
                if BRACKET_RE.findall(source_text) != BRACKET_RE.findall(target_text):
                    return
                pairs[normalise(source_text)][target_text] += 1
        elif isinstance(source, dict) and isinstance(target, dict):
            for key in source.keys() & target.keys():
                collect(source[key], target[key])
        elif isinstance(source, list) and isinstance(target, list):
            for source_item, target_item in zip(source, target):
                collect(source_item, target_item)

    for en_path in en_root.rglob("*.json"):
        pl_path = pl_root / en_path.relative_to(en_root)
        if not pl_path.exists():
            continue
        collect(
            json.loads(en_path.read_text(encoding="utf-8")),
            json.loads(pl_path.read_text(encoding="utf-8")),
        )

    result: dict[str, str] = {}
    for source, options in pairs.items():
        ranked = options.most_common()
        if len(ranked) == 1 or ranked[0][1] > ranked[1][1]:
            result[source] = ranked[0][0]
    return result


def add_aligned_segments(
    source_text: str,
    target_text: str,
    candidates: dict[str, collections.Counter[str]],
    *,
    strip_html: bool = False,
) -> None:
    if strip_html:
        source_text = html_to_text(source_text)
        target_text = html_to_text(target_text)
    if "@UUID" in source_text or "@UUID" in target_text or "[[/" in source_text or "[[/" in target_text:
        return
    source_parts = re.split(r"\n\s*\n", source_text.strip())
    target_parts = re.split(r"\n\s*\n", target_text.strip())
    if len(source_parts) != len(target_parts):
        return
    for source_part, target_part in zip(source_parts, target_parts):
        source_part = source_part.strip()
        target_part = target_part.strip()
        # Short labels are already handled by the whole-entry dictionaries;
        # paragraph memory is reserved for prose whose context is unambiguous.
        if len(source_part) < 35 or not target_part or normalise(source_part) == normalise(target_part):
            continue
        if BRACKET_RE.findall(source_part) != BRACKET_RE.findall(target_part):
            continue
        if collections.Counter(TAG_RE.findall(source_part)) != collections.Counter(TAG_RE.findall(target_part)):
            continue
        candidates[normalise(source_part)][target_part] += 1


def stable_segment_map(candidates: dict[str, collections.Counter[str]]) -> dict[str, str]:
    result: dict[str, str] = {}
    for source, options in candidates.items():
        ranked = options.most_common()
        if len(ranked) == 1 or ranked[0][1] > ranked[1][1]:
            result[source] = ranked[0][0]
    return result


def official_segment_map(source: dict[str, str], target: dict[str, str]) -> dict[str, str]:
    candidates: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for uid, source_text in source.items():
        target_text = target.get(uid, "")
        if source_text and target_text:
            add_aligned_segments(source_text, target_text, candidates)
    return stable_segment_map(candidates)


def community_segment_map(root: Path) -> dict[str, str]:
    candidates: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    en_root = root / "en"
    pl_root = root / "pl"

    def collect(source: Any, target: Any) -> None:
        if isinstance(source, str) and isinstance(target, str):
            if source.strip() and target.strip() and source != target:
                add_aligned_segments(source, target, candidates, strip_html=True)
        elif isinstance(source, dict) and isinstance(target, dict):
            for key in source.keys() & target.keys():
                collect(source[key], target[key])
        elif isinstance(source, list) and isinstance(target, list):
            for source_item, target_item in zip(source, target):
                collect(source_item, target_item)

    for en_path in en_root.rglob("*.json"):
        pl_path = pl_root / en_path.relative_to(en_root)
        if not pl_path.exists():
            continue
        collect(
            json.loads(en_path.read_text(encoding="utf-8")),
            json.loads(pl_path.read_text(encoding="utf-8")),
        )
    return stable_segment_map(candidates)


def apply_segment_memory(source_text: str, target_text: str, memories: list[dict[str, str]]) -> tuple[str, int]:
    source_parts = re.split(r"\n\s*\n", source_text.strip())
    target_parts = re.split(r"\n\s*\n", target_text.strip())
    if len(source_parts) != len(target_parts):
        return target_text, 0
    replacements = 0
    for index, source_part in enumerate(source_parts):
        key = normalise(source_part)
        replacement = next((memory[key] for memory in memories if key in memory), None)
        if replacement is None:
            continue
        target_parts[index] = replacement
        replacements += 1
    return "\n\n".join(target_parts), replacements


MID_SENTENCE_PRONOUN_RE = re.compile(
    r"\b(?:Ci|Cię|Ciebie|Tobie|Tobą|Ty|Twój|Twoja|Twoje|Twoi|Twojego|Twojej|Twojemu|Twoim|Twoich|Twoimi|Twoją)\b"
)
MID_SENTENCE_RULE_TERM_RE = re.compile(
    r"\b(?:Reakcja|Reakcji|Reakcję|Reakcją|Ułatwienie|Ułatwienia|Ułatwieniem|"
    r"Utrudnienie|Utrudnienia|Utrudnieniem|Szybkość|Szybkości|Szybkością|"
    r"Premia|Premii|Premię|Premią)\b"
)


def lower_mid_sentence_pronouns(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix = text[: match.start()]
        visible_prefix = TAG_RE.sub("", prefix)
        if not visible_prefix.strip() or re.search(r"(?:^|[.!?]\s+|\n\s*)$", visible_prefix):
            return match.group(0)
        value = match.group(0)
        return value[0].lower() + value[1:]

    return MID_SENTENCE_PRONOUN_RE.sub(replace, text)


def lower_mid_sentence_rule_terms(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix = text[: match.start()]
        visible_prefix = TAG_RE.sub("", prefix)
        if not visible_prefix.strip() or re.search(
            r"(?:^|[.!?]\s+|\n\s*|Poziom \d+:\s*)$",
            visible_prefix,
        ):
            return match.group(0)
        value = match.group(0)
        return value[0].lower() + value[1:]

    return MID_SENTENCE_RULE_TERM_RE.sub(replace, text)


def refine_visible(text: str) -> str:
    parts = TAG_RE.split(text)
    tags = TAG_RE.findall(text)
    output: list[str] = []
    for index, part in enumerate(parts):
        value = part
        for pattern, replacement in VISIBLE_REPLACEMENTS:
            if replacement is not None:
                value = re.sub(pattern, replacement, value)
        value = DICE_RE.sub(lambda match: f"{match.group(1)}k{match.group(2)}", value)
        value = value.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "").replace("\ufeff", "")
        output.append(value)
        if index < len(tags):
            output.append(tags[index])
    refined = "".join(output)
    refined = lower_mid_sentence_pronouns(refined)
    refined = lower_mid_sentence_rule_terms(refined)
    # D&D source material capitalises rules terms, while shipped Polish BG3
    # generally keeps them lowercase in running prose.
    refined = re.sub(
        r"(?<=[a-ząćęłńóśźż0-9,;)])(\s+)Punkt(y|ów|u|em|ami|ach|ach)? [Ww]ytrzymałości\b",
        lambda match: match.group(1) + "punkt" + (match.group(2) or "") + " wytrzymałości",
        refined,
    )
    refined = re.sub(r"[ \t]+(?=\n|$)", "", refined)
    return refined


def refine_markup_context(text: str) -> str:
    # Markup tags wrap visible words; punctuation belongs immediately after
    # the closing tag. Some community rows contained a stray space here.
    text = re.sub(r"(</LSTag>)\s+([.,;:])", r"\1\2", text)
    text = re.sub(
        r'(\b(?:Stan|stan|stanu|stanem|stanie|stany|stanów|stanom|stanami|stanach)\s+'
        r'<LSTag\b(?=[^>]*\bType="Status")[^>]*>)([A-ZĄĆĘŁŃÓŚŹŻ])',
        lambda match: match.group(1) + match.group(2).lower(),
        text,
    )
    text = re.sub(
        r'(<LSTag\b[^>]*Tooltip="POISONED"[^>]*>)(?:zatruć|Zatruć)(</LSTag>\s+cel\.)',
        r"\1Zatruwa\2",
        text,
    )
    text = re.sub(
        r'(stan\s+<LSTag\b[^>]*Tooltip="SLEEP"[^>]*>)(?:Unprzytomny|Nieprzytomny|Nieprzytomność)(</LSTag>)',
        r"\1Nieprzytomności\2",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r'(z wyjątkiem\s+<LSTag\b[^>]*Tooltip="Intelligence"[^>]*>Inteligencji</LSTag>,\s*'
        r'<LSTag\b[^>]*Tooltip="Wisdom"[^>]*>)Mądrość(</LSTag>\s+i\s+'
        r'<LSTag\b[^>]*Tooltip="Charisma"[^>]*>Charyzmy</LSTag>)',
        r"\1Mądrości\2",
        text,
    )
    text = re.sub(
        r"((?:warunek|stanu|stanem|stan)\s+<LSTag\b[^>]*Tooltip=\"INVISIBLE\"[^>]*>)niewidzialne(</LSTag>)",
        r"\1niewidzialności\2",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(stan\s+<LSTag\b[^>]*Tooltip=\"BLINDED\"[^>]*>)(?:oślepiona|oślepiony|oślepione)(</LSTag>)",
        r"\1Oślepienia\2",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(stan\s+<LSTag\b[^>]*Tooltip=\"PRONE\"[^>]*>)(?:Leżący|Powalony|Powalenie)(</LSTag>)",
        r"\1Powalenia\2",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(stan\s+<LSTag\b[^>]*Tooltip=\"STUNNED\"[^>]*>)(?:Ogłuszony|Ogłuszona|Ogłuszone|Ogłuszenie)(</LSTag>)",
        r"\1Ogłuszenia\2",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r'((?:wynikowi|wynikom) rzutu kością\s+<LSTag\b[^>]*Tooltip="BardicInspiration"[^>]*>)'
        r'(?:bardowska inspiracja|Bardowska Inspiracja)(</LSTag>)',
        r'\1bardowskiej inspiracji\2',
        text,
        flags=re.IGNORECASE,
    )
    return text


# Keep skill labels aligned with the names shipped by the official Polish BG3
# localization.  Only confirmed non-canonical nominative labels are replaced;
# contextual forms such as "Perswazji" or "Medycyny" remain inflected.
OFFICIAL_SKILL_TAG_TEXT = {
    ("AnimalHandling", "Obsługa zwierząt"): "Opieka nad zwierzętami",
    ("Investigation", "Dochodzenie"): "Śledztwo",
    ("Nature", "Natura"): "Przyroda",
    ("SleightOfHand", "Zręczność dłoni"): "Zwinne dłonie",
    ("Survival", "Przetrwanie"): "Sztuka przetrwania",
}
SKILL_TAG_RE = re.compile(
    r'(<LSTag Type="Skills" Tooltip="([^"]+)">)(.*?)(</LSTag>)'
)


def refine_official_skill_tags(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        key = (match.group(2), match.group(3))
        return match.group(1) + OFFICIAL_SKILL_TAG_TEXT.get(key, match.group(3)) + match.group(4)

    return SKILL_TAG_RE.sub(replace, text)


def refine_source_aware(source_text: str, target_text: str) -> str:
    source_first_line = source_text.split("\n", 1)[0]
    if source_first_line.startswith("Feat: "):
        feat_title = source_first_line.removeprefix("Feat: ")
        canonical_title = FEAT_PREFIX_OVERRIDES.get(feat_title)
        if canonical_title is not None:
            _, separator, remainder = target_text.partition("\n")
            target_text = f"Atut: {canonical_title}"
            if separator:
                target_text += separator + remainder
    for source_term, replacements in SOURCE_AWARE_CLASS_REPLACEMENTS.items():
        if source_term.casefold() in source_text.casefold():
            for pattern, replacement in replacements:
                target_text = re.sub(pattern, replacement, target_text)
    for source_term, replacements in SOURCE_AWARE_TERM_REPLACEMENTS.items():
        if source_term.casefold() in source_text.casefold():
            for pattern, replacement in replacements:
                target_text = re.sub(pattern, replacement, target_text)
    return target_text


def refine_measurements(source_text: str, target_text: str) -> str:
    source_values = [float(value) for value in EN_FEET_RE.findall(source_text)]
    metric_matches = list(PL_METRE_RE.finditer(target_text))
    if source_values and len(source_values) == len(metric_matches):
        replacements: list[tuple[int, int, str]] = []
        for feet, match in zip(source_values, metric_matches):
            metres = round(feet * 0.3, 4)
            if metres.is_integer():
                value = str(int(metres))
            else:
                value = str(metres).rstrip("0").rstrip(".").replace(".", ",")
            replacements.append((match.start(1), match.end(1), value))
        for start, end, value in reversed(replacements):
            target_text = target_text[:start] + value + target_text[end:]

    target_matches = list(PL_FEET_RE.finditer(target_text))
    if not target_matches:
        return target_text

    if len(source_values) == len(target_matches):
        metre_values = [feet * 0.3 for feet in source_values]
    else:
        # Some baseline rows converted only the number (10 feet -> 3 stóp)
        # or were partially refined during a previous pass. Convert the
        # remaining unmistakable grid distances directly.
        displayed_to_metres = {
            1.0: 0.3,
            2.0: 1.5,
            3.0: 3.0,
            5.0: 1.5,
            9.0: 9.0,
            10.0: 3.0,
            15.0: 4.5,
            20.0: 6.0,
            30.0: 9.0,
            40.0: 12.0,
            45.0: 13.5,
            50.0: 15.0,
            60.0: 18.0,
            90.0: 27.0,
            120.0: 36.0,
        }
        metre_values = []
        for target_match in target_matches:
            displayed = float(re.match(r"\d+(?:[,.]\d+)?", target_match.group(0)).group(0).replace(",", "."))
            metre_values.append(displayed_to_metres.get(displayed, displayed * 0.3))

    output: list[str] = []
    cursor = 0
    for metres, target_match in zip(metre_values, target_matches):
        formatted = f"{metres:.2f}".rstrip("0").rstrip(".").replace(".", ",")
        output.append(target_text[cursor : target_match.start()])
        output.append(f"{formatted} m")
        cursor = target_match.end()
    output.append(target_text[cursor:])
    return "".join(output)


def apply_official_tag_terms(source_text: str, target_text: str, terms: dict[tuple[str, str], str]) -> str:
    source_tags = TAG_BLOCK_RE.findall(source_text)
    target_matches = list(TAG_BLOCK_RE.finditer(target_text))
    if not source_tags or len(source_tags) != len(target_matches):
        return target_text
    output: list[str] = []
    cursor = 0
    for source_tag, target_match in zip(source_tags, target_matches):
        source_open, source_inner, _ = source_tag
        target_open, target_inner, target_close = target_match.groups()
        output.append(target_text[cursor : target_match.start()])
        replacement = terms.get((source_open, source_inner), target_inner) if source_open == target_open else target_inner
        output.append(target_open + replacement + target_close)
        cursor = target_match.end()
    output.append(target_text[cursor:])
    return "".join(output)


def main() -> None:
    _, _, en = load(EN_PATH)
    pl_tree, pl_nodes, _ = load(PL_PATH)
    _, _, bg_en = load(BG_EN_PATH)
    _, _, bg_pl = load(BG_PL_PATH)
    official = stable_map(bg_en, bg_pl)
    official_terms = official_tag_map(bg_en, bg_pl)
    community_maps = [community_map(root) for root in COMMUNITY_ROOTS]
    stripped_community = community_stripped_map(COMMUNITY_ROOTS[0])
    segment_memories = [
        official_segment_map(bg_en, bg_pl),
        *(community_segment_map(root) for root in COMMUNITY_ROOTS),
    ]

    stats = collections.Counter()
    for node in pl_nodes:
        uid = node.attrib["contentuid"]
        source = en[uid]
        key = normalise(source)
        official_level_title = official_level_feature_title(source, official)
        usable_classes = translate_usable_classes(source)
        used_official_exact = False
        used_uid_override = False
        used_whole_translation = False
        if uid in UID_OVERRIDES:
            node.text = UID_OVERRIDES[uid]
            stats["uid_override"] += 1
            used_uid_override = True
            used_whole_translation = True
        elif key in official:
            node.text = official[key]
            stats["official_exact"] += 1
            used_official_exact = True
            used_whole_translation = True
        elif official_level_title is not None:
            node.text = official_level_title
            stats["official_level_title"] += 1
            used_whole_translation = True
        elif usable_classes is not None:
            node.text = usable_classes
            stats["manual_family"] += 1
            used_whole_translation = True
        elif source in EXACT_OVERRIDES:
            node.text = EXACT_OVERRIDES[source]
            stats["manual_exact"] += 1
            used_whole_translation = True
        else:
            for map_index, community in enumerate(community_maps):
                if key in community:
                    node.text = community[key]
                    stats[f"community_{map_index + 1}_exact"] += 1
                    used_whole_translation = True
                    break
            else:
                if "<" not in source and "[" not in source and key in stripped_community:
                    node.text = stripped_community[key]
                    stats["community_stripped_exact"] += 1
                    used_whole_translation = True
        if not used_whole_translation:
            node.text, replaced_segments = apply_segment_memory(source, node.text or "", segment_memories)
            if replaced_segments:
                stats["segment_entries"] += 1
                stats["segments_replaced"] += replaced_segments
        if not used_official_exact:
            if not used_uid_override:
                node.text = apply_official_tag_terms(source, node.text or "", official_terms)
            node.text = refine_markup_context(node.text or "")
            node.text = refine_source_aware(source, node.text or "")
            node.text = refine_measurements(source, node.text or "")
            node.text = refine_visible(node.text or "")
        if uid in POST_REFINEMENT_UID_OVERRIDES:
            node.text = POST_REFINEMENT_UID_OVERRIDES[uid]
        node.text = refine_official_skill_tags(node.text or "")

    ET.indent(pl_tree, space="  ")
    root = pl_tree.getroot()
    root.set("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    xml_body = ET.tostring(root, encoding="unicode", short_empty_elements=False)
    with PL_PATH.open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write('<?xml version="1.0"?>\n')
        output_file.write(xml_body)
        output_file.write("\n")
    print(
        f"wrote={PL_PATH} stats={dict(stats)} official_map={len(official)} "
        f"community_maps={[len(mapping) for mapping in community_maps]} "
        f"stripped_community={len(stripped_community)} "
        f"segment_memories={[len(memory) for memory in segment_memories]} "
        f"official_tag_terms={len(official_terms)}"
    )


if __name__ == "__main__":
    main()
