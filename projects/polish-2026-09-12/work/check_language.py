import json, pathlib, urllib.request, urllib.parse
W=pathlib.Path(__file__).resolve().parent
unique={}
for p in W.glob('*-translations.json'):
    for u,t in json.loads(p.read_text(encoding='utf-8')).items(): unique.setdefault(t,[]).append(u)
findings=[]
for t,us in unique.items():
    req=urllib.request.Request('http://127.0.0.1:8091/v2/check',data=urllib.parse.urlencode({'language':'pl-PL','text':t}).encode())
    with urllib.request.urlopen(req,timeout=30) as r: result=json.load(r)
    for m in result.get('matches',[]):
        findings.append(dict(uids=us,rule=m['rule']['id'],fragment=t[m['offset']:m['offset']+m['length']],message=m['message'],suggestions=[x['value'] for x in m['replacements'][:5]],polish=t))
(W/'language-findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Checked {sum(len(v) for v in unique.values())} entries, {len(unique)} unique texts: {len(findings)} findings')
for f in findings: print(f['rule'],repr(f['fragment']),f['message'],f['suggestions'])
