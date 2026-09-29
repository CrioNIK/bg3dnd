from __future__ import annotations

import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
STRICT = "--strict" in sys.argv[1:]
repo_argument = next((argument for argument in sys.argv[1:] if not argument.startswith("-")), None)
REPO = Path(repo_argument).resolve() if repo_argument else ROOT / "bg3dnd"
MOD = "DnD2024_897914ef-5c96-053c-44af-0be823f895fe"
EN_PATH = REPO / "Mods" / MOD / "Localization" / "English" / "english.xml"
PL_PATH = REPO / "Mods" / MOD / "Localization" / "Polish" / "polish.xml"
REPORT = ROOT / ("polish_translation_coverage_strict.tsv" if STRICT else "polish_translation_coverage.tsv")

TAG_RE = re.compile(r"</?[^>]+>")
WORD_RE = re.compile(r"\b[^\W\d_]\w*\b", re.UNICODE)


def visible(text: str) -> str:
    return TAG_RE.sub("", text or "")


def paragraphs(text: str) -> int:
    return len([part for part in re.split(r"\n\s*\n", visible(text).strip()) if part.strip()])


def main() -> None:
    source = {
        node.attrib["contentuid"]: node
        for node in ET.parse(EN_PATH).getroot().findall("content")
    }
    target = {
        node.attrib["contentuid"]: node
        for node in ET.parse(PL_PATH).getroot().findall("content")
    }
    rows: list[tuple[object, ...]] = []
    for uid, source_node in source.items():
        source_text = source_node.text or ""
        target_text = target[uid].text or ""
        source_words = len(WORD_RE.findall(visible(source_text)))
        target_words = len(WORD_RE.findall(visible(target_text)))
        source_paragraphs = paragraphs(source_text)
        target_paragraphs = paragraphs(target_text)
        ratio = target_words / source_words if source_words else 1.0
        paragraph_gap = source_paragraphs - target_paragraphs
        # Polish can be somewhat shorter than English, but a translation below
        # 55% of the source or missing two or more paragraphs is very likely
        # truncated. Short UI labels are excluded because ratios are noisy.
        if STRICT:
            suspicious = source_words >= 45 and (ratio < 0.72 or paragraph_gap >= 1)
        else:
            suspicious = source_words >= 35 and (ratio < 0.55 or paragraph_gap >= 2)
        if suspicious:
            rows.append(
                (
                    uid,
                    source_words,
                    target_words,
                    f"{ratio:.3f}",
                    source_paragraphs,
                    target_paragraphs,
                    source_text.replace("\n", "\\n"),
                    target_text.replace("\n", "\\n"),
                )
            )
    rows.sort(key=lambda row: (float(row[3]), -int(row[1])))
    with REPORT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(
            (
                "contentuid",
                "source_words",
                "target_words",
                "word_ratio",
                "source_paragraphs",
                "target_paragraphs",
                "english",
                "polish",
            )
        )
        writer.writerows(rows)
    print(f"coverage_findings={len(rows)} wrote={REPORT}")


if __name__ == "__main__":
    main()
