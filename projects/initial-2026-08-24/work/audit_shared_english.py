from __future__ import annotations

import collections
import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve()
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
EN = REPO / "Mods" / MOD / "Localization" / "English" / "english.xml"
PL = REPO / "Mods" / MOD / "Localization" / "Polish" / "polish.xml"
OUT = ROOT / "shared_english_polish_candidates.tsv"

TAG_RE = re.compile(r"</?[^>]+>")
WORD_RE = re.compile(r"(?<![\w’'])\b[A-Za-z][A-Za-z’'-]{3,}\b(?![\w’'])")

# Words that are valid Polish, proper names, D&D product names, or intentionally
# shared international vocabulary. The report is an editorial candidate list,
# not a hard validation failure.
ALLOW = {
    "agent", "alarm", "ammunition", "archon", "armor", "astral", "aura", "baldur", "bard",
    "bhaal", "bonus", "camp", "chaos", "cleric", "critical", "cylinder", "demon", "devil",
    "diameter", "dice", "druid", "elemental", "faer", "fey", "giant", "gith", "githyanki",
    "githzerai", "gnome", "goblin", "honor", "illusion", "illrigger", "infernal", "initiative",
    "level", "magic", "metal", "model", "moment", "monster", "myrkul", "necrotic", "ogre",
    "paladin", "patron", "portal", "psychic", "radius", "reaction", "ritual", "rogue", "round",
    "shadow", "status", "symbol", "system", "talent", "teleport", "trance", "troll", "undead",
    "waterdeep", "wizard", "xanathar", "zhentarim", "aasimar", "achron", "acheron", "asmodeus",
    "dispater", "faerûn", "moloch", "maddala", "mystra", "tasha", "elminster", "aganazzar",
    "shillelagh", "hexblade", "artificer", "gunslinger", "battle", "smith", "scion",
}


def visible(text: str) -> str:
    return TAG_RE.sub("", text or "")


def main() -> None:
    en_nodes = {n.attrib["contentuid"]: n.text or "" for n in ET.parse(EN).getroot().findall("content")}
    pl_nodes = {n.attrib["contentuid"]: n.text or "" for n in ET.parse(PL).getroot().findall("content")}
    rows: list[tuple[str, str, str, str]] = []
    counts: collections.Counter[str] = collections.Counter()
    for uid, source in en_nodes.items():
        target = pl_nodes.get(uid, "")
        source_words = {word.lower() for word in WORD_RE.findall(visible(source))}
        target_words = {word.lower() for word in WORD_RE.findall(visible(target))}
        shared = sorted(word for word in source_words & target_words if word not in ALLOW)
        for word in shared:
            counts[word] += 1
            rows.append((word, uid, source.replace("\n", "\\n"), target.replace("\n", "\\n")))
    rows.sort(key=lambda row: (-counts[row[0]], row[0], row[1]))
    with OUT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(("word", "contentuid", "english", "polish"))
        writer.writerows(rows)
    print(f"candidates={len(rows)} distinct_words={len(counts)} wrote={OUT}")
    for word, count in counts.most_common(80):
        print(f"{count:4} {word}")


if __name__ == "__main__":
    main()
