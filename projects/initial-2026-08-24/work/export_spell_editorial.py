from __future__ import annotations

import csv
from collections import defaultdict

import audit_spells as audit


def write_tsv(path, header, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(header)
        writer.writerows(rows)


def main() -> None:
    _, source = audit.localization(audit.SOURCE)
    _, target = audit.localization(audit.TARGET)
    exact = audit.official_exact()
    entries = audit.parse_stats()
    title_entries: dict[str, set[str]] = defaultdict(set)
    description_entries: dict[str, set[str]] = defaultdict(set)

    for name, entry in entries.items():
        if entry["type"] != "SpellData":
            continue
        fields = audit.resolved_fields(name, entries)
        title = audit.handle(fields.get("DisplayName", ""))
        if title and title in source:
            title_entries[title].add(name)
        for key, value in fields.items():
            if "Description" not in key:
                continue
            uid = audit.handle(value)
            if uid and uid in source:
                description_entries[uid].add(name)

    title_rows = []
    for uid, names in title_entries.items():
        english = source[uid].text or ""
        title_rows.append((
            uid,
            english,
            target[uid].text or "",
            exact.get(english, ""),
            ";".join(sorted(names)),
        ))
    title_rows.sort(key=lambda row: row[1].casefold())
    write_tsv(
        audit.ROOT / "spell_titles_editorial.tsv",
        ("uid", "english", "current_ukrainian", "official_bg3_ukrainian", "spell_entries"),
        title_rows,
    )

    description_rows = []
    for uid, names in description_entries.items():
        english = source[uid].text or ""
        description_rows.append((
            uid,
            english,
            target[uid].text or "",
            exact.get(english, ""),
            ";".join(sorted(names)),
        ))
    description_rows.sort(key=lambda row: (row[4], row[1].casefold()))
    write_tsv(
        audit.ROOT / "spell_descriptions_editorial.tsv",
        ("uid", "english", "current_ukrainian", "official_bg3_ukrainian", "spell_entries"),
        description_rows,
    )
    print(f"spell_titles={len(title_rows)} spell_descriptions={len(description_rows)}")


if __name__ == "__main__":
    main()
