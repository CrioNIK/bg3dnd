from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    query = " ".join(sys.argv[1:]).casefold()
    en_nodes = list(ET.parse(ROOT / "bg3-en.xml").getroot().findall("content"))
    uk = {
        node.attrib["contentuid"]: node.text or ""
        for node in ET.parse(ROOT / "bg3-uk.xml").getroot().findall("content")
    }
    found = 0
    for node in en_nodes:
        source = node.text or ""
        if query not in source.casefold():
            continue
        print(f"{source}\t{uk.get(node.attrib['contentuid'], '')}")
        found += 1
        if found >= 100:
            break
    print(f"FOUND={found}")


if __name__ == "__main__":
    main()
