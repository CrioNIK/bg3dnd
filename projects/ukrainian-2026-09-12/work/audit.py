from pathlib import Path
import xml.etree.ElementTree as ET
import json, subprocess, hashlib

ROOT=Path(__file__).resolve().parent
REPO=ROOT/'bg3dnd'
LOC=Path('Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization')
EN=LOC/'English/english.xml'
UK=LOC/'Ukrainian/ukrainian.xml'
def records(data):
    return [{'id': e.attrib['contentuid'], 'version':e.attrib['version'],'text':e.text or ''} for e in ET.fromstring(data)]
def git(*args):
    return subprocess.check_output(['git','-C',str(REPO),*args])

eng=records((REPO/EN).read_bytes())
uk=records((REPO/UK).read_bytes())
base=records(git('show','d15b546f420561d37ca78c9cbfe0dde1072db900:'+EN.as_posix()))
em={e['id']:e for e in eng}; um={e['id']:e for e in uk}; bm={e['id']:e for e in base}
missing=[e for e in eng if e['id'] not in um]
changed=[{'english':e,'base':bm[e['id']],'ukrainian':um.get(e['id'])} for e in eng if e['id'] in bm and (e['text']!=bm[e['id']]['text'] or e['version']!=bm[e['id']]['version'])]
(ROOT/'missing.json').write_text(json.dumps(missing,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'changed.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'context-pairs.json').write_text(json.dumps([{'en':e,'uk':um.get(e['id'])} for e in eng],ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'head':git('rev-parse','HEAD').decode().strip(),'english':len(eng),'ukrainian':len(uk),'missing':len(missing),'extra':len(set(um)-set(em)),'version_mismatch':[e['id'] for e in uk if e['id'] in em and e['version']!=em[e['id']]['version']],'source_changes_since_pr1310':len(changed)},indent=2))
for i,e in enumerate(missing): print(f"{i:03} {e['id']} v{e['version']} {e['text']}")
print('CHANGES SINCE REVIEW:')
print(json.dumps(changed,ensure_ascii=False,indent=2))
