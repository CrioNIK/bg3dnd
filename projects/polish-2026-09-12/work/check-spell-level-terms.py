import xml.etree.ElementTree as E
from pathlib import Path
p = Path('C:/Users/coldb/Documents/Codex/2026-08-24/new-chat/work')
pl = {x.get('contentuid'):x.text for x in E.parse(p/'official_bg3_polish_20260828/polish.loca.xml').getroot()}
for x in E.parse(p/'official_bg3_english_20260828/english.loca.xml').getroot():
    if x.text and len(x.text)<550 and ('spell slot' in x.text.lower() and any(w in x.text.lower() for w in ['level','higher'])):
        print(x.get('contentuid'),x.text,pl.get(x.get('contentuid')),sep='\t')
