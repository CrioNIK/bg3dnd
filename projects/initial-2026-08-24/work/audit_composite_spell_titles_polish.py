from __future__ import annotations

import re
import sys
from pathlib import Path


REPO = Path(sys.argv[1]).resolve()
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
TARGET = REPO / "Mods" / MOD / "Localization" / "Polish" / "polish.xml"

# audit_spells_polish reads the repository path from argv at import time.
sys.argv = [sys.argv[0], str(REPO)]
import audit_spells_polish as audit  # noqa: E402


def main() -> None:
    _, source = audit.localization(audit.SOURCE)
    _, target = audit.localization(TARGET)
    entries = audit.parse_stats()

    pairs: dict[str, str] = {}
    title_handles: set[str] = set()
    for name, entry in entries.items():
        if entry["type"] != "SpellData":
            continue
        fields = audit.resolved_fields(name, entries)
        own_fields: dict[str, str] = entry["fields"]  # type: ignore[assignment]
        flags = fields.get("SpellFlags", "")
        costs = fields.get("UseCosts", "")
        is_actual_spell = (
            "IsSpell" in flags
            or "SpellSlot" in costs
            or bool(fields.get("MemoryCost"))
            or (bool(fields.get("Level")) and bool(fields.get("SpellSchool")))
        )
        is_root = not own_fields.get("RootSpellID") and not re.search(r"_[2-9]$", name)
        uid = audit.handle(fields.get("DisplayName", ""))
        if not (is_actual_spell and is_root and uid and uid in source and uid in target):
            continue
        english = source[uid].text or ""
        polish = target[uid].text or ""
        if english and polish:
            pairs[english] = polish
            title_handles.add(uid)

    findings: list[tuple[str, str, str, str]] = []
    for uid, source_node in source.items():
        if uid in title_handles or uid not in target:
            continue
        english_text = source_node.text or ""
        polish_text = target[uid].text or ""
        for english_title, polish_title in pairs.items():
            if len(english_title) < 4:
                continue
            if not re.search(rf"(?<![A-Za-z]){re.escape(english_title)}(?![A-Za-z])", english_text):
                continue
            if polish_title not in polish_text:
                findings.append((uid, english_title, polish_title, polish_text.replace("\n", "\\n")))

    print(f"spell_title_pairs={len(pairs)} composite_findings={len(findings)}")
    for uid, english, expected, actual in findings:
        print(f"{uid}\t{english}\t{expected}\t{actual}")


if __name__ == "__main__":
    main()
