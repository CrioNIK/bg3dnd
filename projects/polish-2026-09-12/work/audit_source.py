import json, pathlib, xml.etree.ElementTree as ET, subprocess, hashlib
W=pathlib.Path(__file__).resolve().parent
R=W/'bg3dnd'
L=R/'Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization'
en=list(ET.parse(L/'English/english.xml').getroot())
pl=list(ET.parse(L/'Polish/polish.xml').getroot())
em={e.attrib['contentuid']:e for e in en}; pm={e.attrib['contentuid']:e for e in pl}
rows=[]
for i,e in enumerate(en):
    uid=e.attrib['contentuid']; p=pm.get(uid)
    if p is None or p.attrib['version']!=e.attrib['version']:
        rows.append(dict(index=i,uid=uid,version=e.attrib['version'],en=e.text,pl=p.text if p is not None else None,kind='add' if p is None else 'update'))
stats=dict(head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),english=len(en),polish=len(pl),missing=sum(x['kind']=='add' for x in rows),updates=sum(x['kind']=='update' for x in rows),extra=list(pm.keys()-em.keys()),english_sha256=hashlib.sha256((L/'English/english.xml').read_bytes()).hexdigest())
(W/'source-audit.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'entries-to-translate.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'entries-to-translate.txt').write_text('\n\n'.join(f"{i+1}. [{r['index']}] {r['uid']} v{r['version']} ({r['kind']})\n{r['en']}\nOLD PL: {r['pl']}" for i,r in enumerate(rows)),encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False,indent=2))
