import xml.etree.ElementTree as E
from pathlib import Path
import json
p=Path('C:/Users/coldb/Documents/Codex/2026-08-24/new-chat/work')
en=E.parse(p/'official_bg3_english_20260828/english.loca.xml').getroot()
pl={x.get('contentuid'):x.text for x in E.parse(p/'official_bg3_polish_20260828/polish.loca.xml').getroot()}
terms=['Conjur','Enchant','Benign Transposition','Focused Conjuration','Split Enchantment','Instinctive Charm','Charm Person','Conjuration','Enchantment','Incapacitated','Charmed','Deception','Intimidation','Persuasion','Wizard','Force','Necrotic','Psychic','Radiant','Resistance','Speed']
for x in en:
    if x.text in terms or (x.text and len(x.text)<150 and any(t in x.text for t in terms[:8])):
        print(x.get('contentuid'), x.text, pl.get(x.get('contentuid')), sep='\t')
print('\nCURRENT MOD:')
root=Path('work/bg3dnd/Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization')
pe={x.get('contentuid'):x.text for x in E.parse(root/'Polish/polish.xml').getroot()}
for x in E.parse(root/'English/english.xml').getroot():
    if x.text and any(t in x.text for t in terms[:8]) and len(x.text)<300:
        if pe.get(x.get('contentuid')):
            print(x.get('contentuid'),x.text,pe.get(x.get('contentuid')),sep='\t')
