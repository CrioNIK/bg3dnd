from __future__ import annotations

import collections
import csv
import re
import sys
from pathlib import Path


path = Path(sys.argv[1])
rows = [
    row
    for row in csv.DictReader(path.open(encoding="utf-8-sig"), delimiter="\t")
    if row["rule_id"] != "MORFOLOGIK_RULE_PL_PL"
]

print(f"non_dictionary={len(rows)} rules={collections.Counter(row['rule_id'] for row in rows)}")
for row in rows:
    text = re.sub(r"<[^>]+>", "", row["translation"].replace("\\n", " "))
    offending = row["offending"]
    index = text.find(offending)
    if index < 0:
        index = 0
    start = max(0, index - 90)
    end = min(len(text), index + len(offending) + 130)
    context = text[start:end]
    print(
        f"{row['rule_id']}\t{row['contentuid']}\t[{offending}] -> {row['suggestions']}\t{context}"
    )
