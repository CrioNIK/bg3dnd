import json,pathlib
W=pathlib.Path(__file__).resolve().parent
p=W/'wizard-translations.json'; data=json.loads(p.read_text(encoding='utf-8'))
replacements={
    'trafi cię testem ataku':'trafi cię w wyniku testu ataku',
    'w jednej z następujących wybranych umiejętności':'w jednej z następujących umiejętności do wyboru',
    'aby objąć dodatkową istotę':'aby objąć działaniem dodatkową istotę',
    'poziomu Maga':'poziomu maga',
}
changed=[]
for u,t in data.items():
    edited=t
    for a,b in replacements.items(): edited=edited.replace(a,b)
    if edited!=t: changed.append(u)
    data[u]=edited
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(W/'editorial-resolution.json').write_text(json.dumps(dict(changed=changed,resolved=list(replacements.items()),meaning_changes=False),ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Applied independent reviewer suggestions in {len(changed)} new records')
