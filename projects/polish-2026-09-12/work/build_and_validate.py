import collections, csv, hashlib, json, pathlib, re, subprocess, xml.etree.ElementTree as ET
W=pathlib.Path(__file__).resolve().parent; O=W.parent/'outputs'; R=W/'bg3dnd'
REL='Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization/Polish/polish.xml'
ENREL=REL.replace('Polish/polish.xml','English/english.xml')
baseline=subprocess.check_output(['git','show','HEAD:'+REL],cwd=R)
english=(R/ENREL).read_bytes()
base=ET.fromstring(baseline); en=ET.fromstring(english)
bm={e.attrib['contentuid']:e for e in base}; em={e.attrib['contentuid']:e for e in en}
changes={}
for file in ['root-translations.json','wizard-translations.json','monk-translations.json']:
    part=json.loads((W/file).read_text(encoding='utf-8'))
    assert not changes.keys() & part.keys(), 'Overlapping translation ownership'
    changes.update(part)
required=json.loads((W/'entries-to-translate.json').read_text(encoding='utf-8'))
assert changes.keys()=={r['uid'] for r in required}
def esc(text): return text.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def node(uid): return f'<content contentuid="{uid}" version="{em[uid].attrib["version"]}">{esc(changes[uid])}</content>'
raw=baseline.decode('utf-8'); newline='\r\n' if b'\r\n' in baseline else '\n'
for uid in changes.keys() & bm.keys():
    pattern=r'<content\b[^>]*contentuid="'+re.escape(uid)+r'"[^>]*>.*?</content>'
    raw,n=re.subn(pattern,lambda m:node(uid).replace('\n',newline),raw,flags=re.S)
    assert n==1
new=''.join('  '+node(e.attrib['contentuid']).replace('\n',newline)+newline for e in en if e.attrib['contentuid'] not in bm)
raw=raw.replace('</contentList>',new+'</contentList>')
out=raw.encode('utf-8'); (R/REL).write_bytes(out); (O/'polish.xml').write_bytes(out)
pl=ET.fromstring(out); pm={e.attrib['contentuid']:e for e in pl}
problems={}
def check(name,items): problems[name]=list(items)
check('missing',em.keys()-pm.keys()); check('extra',pm.keys()-em.keys())
check('duplicates',[u for u,c in collections.Counter(e.attrib['contentuid'] for e in pl).items() if c!=1])
check('empty',[u for u,p in pm.items() if not (p.text or '').strip()])
check('version_mismatches',[u for u in em.keys() & pm.keys() if em[u].attrib!=pm[u].attrib])
check('unexpected_xml_children',[u for u,p in pm.items() if len(p)])
check('order_mismatches',[] if list(em)==list(pm) else ['English/Polish sequence differs'])
TAG=re.compile(r'</?[^>]+>'); PH=re.compile(r'\[[^\]\n]+\]')
check('tag_mismatches',[u for u in em if collections.Counter(TAG.findall(em[u].text or ''))!=collections.Counter(TAG.findall(pm[u].text or ''))])
check('placeholder_mismatches',[u for u in em if collections.Counter(PH.findall(em[u].text or ''))!=collections.Counter(PH.findall(pm[u].text or ''))])
check('changed_numeric_mismatches',[u for u in changes if re.findall(r'\d+',em[u].text or '')!=re.findall(r'\d+',pm[u].text or '')])
check('unchanged_record_mismatches',[u for u in bm if u not in changes and (bm[u].text!=pm[u].text or bm[u].attrib!=pm[u].attrib)])
check('changed_untranslated',[u for u in changes if em[u].text.strip()==pm[u].text.strip()])
tag_parse=[]
for u,p in pm.items():
    text=p.text or ''; marked=esc(text)
    for t in set(TAG.findall(text)): marked=marked.replace(esc(t),t)
    # BG3's embedded HTML-like markup accepts void <br> as well as <br/>.
    # Normalize only in the parser input; the actual output must preserve it.
    marked=re.sub(r'<br\s*>','<br/>',marked,flags=re.I)
    try: ET.fromstring('<root>'+marked+'</root>')
    except ET.ParseError as err: tag_parse.append(dict(uid=u,error=str(err)))
check('invalid_embedded_markup',tag_parse)
groups=collections.defaultdict(list)
for u,e in em.items(): groups[(e.text or '').strip()].append(u)
dupgroups={t:us for t,us in groups.items() if len(us)>1}
inconsistent=[dict(english=t,entries=[dict(uid=u,polish=pm[u].text) for u in us]) for t,us in dupgroups.items() if len({pm[u].text.strip() for u in us})>1]
check('inconsistent_duplicate_english_groups',inconsistent)
base_en=ET.fromstring(subprocess.check_output(['git','show','db749724b94d416926b7d7f9e7f1659f4f8c7bb1:'+ENREL],cwd=R))
oldem={e.attrib['contentuid']:e for e in base_en}
source_changed=[u for u,e in em.items() if u in oldem and (e.text!=oldem[u].text or e.attrib!=oldem[u].attrib)]
assert set(source_changed)=={'h6299a92eg8049g117bga5b7g17d26b0619d6','hf12dc8a9g3079g890agb1ffgdf7b91f3c03d','hb033a976g4cccgdbedg5c40ge3ee8016bca2'},source_changed
check('improved_shillelagh_preservation',[] if pm['hb033a976g4cccgdbedg5c40ge3ee8016bca2'].text==bm['hb033a976g4cccgdbedg5c40ge3ee8016bca2'].text else ['changed'])
check('reassert_honor_preservation',[u for u in ['h9fa0d3deg53aag92d4g5ba5g0185574f2cd7','he4b058a0g2cdbgba7agf3cfg71fa968bbd61'] if pm[u].text!='Przywrócenie honoru'])
patch=subprocess.check_output(['git','diff','--no-ext-diff','--binary','--',REL],cwd=R)
(O/'polish-update.patch').write_bytes(patch)
subprocess.run(['git','diff','--check'],cwd=R,check=True)
subprocess.run(['git','apply','--check','--reverse',str(O/'polish-update.patch')],cwd=R,check=True)
patchcheck=W/'patch-check'
checkfile=patchcheck/REL
checkfile.parent.mkdir(parents=True,exist_ok=True)
checkfile.write_bytes(baseline)
subprocess.run(['git','-c','core.autocrlf=false','apply','--check',str(O/'polish-update.patch')],cwd=patchcheck,check=True)
subprocess.run(['git','-c','core.autocrlf=false','apply',str(O/'polish-update.patch')],cwd=patchcheck,check=True)
check('patch_reconstructs_output',[] if checkfile.read_bytes()==out else ['Patched baseline differs from output'])
scope=subprocess.check_output(['git','diff','--name-only'],cwd=R,text=True).splitlines()
check('repository_scope',[] if scope==[REL] else scope)
result=dict(source_revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),english_entries=len(en),polish_entries=len(pl),added=len(pm.keys()-bm.keys()),updated_existing=len(changes.keys() & bm.keys()),unchanged_existing=len(bm.keys()-changes.keys()),duplicate_english_groups_checked=len(dupgroups),english_sha256=hashlib.sha256(english).hexdigest(),polish_sha256=hashlib.sha256(out).hexdigest(),patch_sha256=hashlib.sha256(patch).hexdigest(),source_changes_since_polish_pr=source_changed,checks={k:len(v) for k,v in problems.items()},findings={k:v for k,v in problems.items() if v},git_diff_check='passed',git_apply_reverse_check='passed')
result['git_apply_forward_check']='passed; output reproduced byte-for-byte with core.autocrlf=false' if not problems['patch_reconstructs_output'] else 'failed'
(O/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (O/'review.tsv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.writer(f,delimiter='\t'); writer.writerow(['contentuid','version','change','english','previous_polish','polish'])
    for e in en:
        u=e.attrib['contentuid']
        if u in changes: writer.writerow([u,e.attrib['version'],'update' if u in bm else 'add',e.text,bm[u].text if u in bm else '',pm[u].text])
print(json.dumps(result,ensure_ascii=False,indent=2))
assert not any(problems.values()),'Validation findings require review'
