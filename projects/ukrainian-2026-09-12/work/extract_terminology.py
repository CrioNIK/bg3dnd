from pathlib import Path
import xml.etree.ElementTree as ET
import json, hashlib

ROOT = Path(__file__).resolve().parent
ARCHIVE = Path(r'C:\Users\coldb\Documents\Codex\2026-08-24\new-chat\work')
def read(p):
    return {n.attrib['contentuid']: n.text or '' for n in ET.parse(p).getroot()}
en = read(ROOT / 'official-bg3-en.xml')
uk = read(ROOT / 'official-bg3-uk.xml')
terms = [
 'Conjuration','Conjurer','Enchantment','Enchanter','Charm Monster','Arcane Eye',
 'Chromatic Orb','Command','Darkvision',"Dragon's Breath",'Fly','Protection from Energy',
 'Banishment','Dominate Person','Synaptic Static','Chromatic','Metallic','Gem Dragon','Tiamat','Bahamut',
 'Dragon Domain','Dragon','Breath Weapon','Channel Divinity','Hit Die','Hit Dice','Hit Point Dice',
 'Short Rest','Short Resting','Focus Point','Ki Point','Acid','Cold','Fire','Lightning','Poison','Radiant',
 'Thunder','Psychic','Force','Necrotic','Frightened','Charmed','Bonus Action','Saving Throw',
]
res={}
for term in terms:
    hits=[{'uid':uid,'english':v,'ukrainian':uk.get(uid)} for uid,v in en.items() if term.casefold() in v.casefold()]
    hits.sort(key=lambda n:(n['english'].casefold()!=term.casefold(),len(n['english'])))
    res[term]=hits[:12]
(ROOT/'official-term-matches.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
for term,hits in res.items():
    print(term)
    for h in hits[:3]: print(h)
for lang in ['en','uk']:
    fresh=read(ROOT/f'official-bg3-{lang}.xml'); old=read(ARCHIVE/f'bg3-{lang}.xml')
    print(lang,'current',len(fresh),'old',len(old),'added',len(fresh.keys()-old.keys()),'removed',len(old.keys()-fresh.keys()),'changed',sum(fresh[k]!=old[k] for k in fresh.keys()&old.keys()))
