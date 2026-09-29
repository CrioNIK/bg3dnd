from pathlib import Path
import xml.etree.ElementTree as ET
import json, re, subprocess, hashlib, collections, html, csv, io
from html.parser import HTMLParser

ROOT=Path(__file__).resolve().parent
REPO=ROOT/'bg3dnd'
OUT=ROOT.parent/'outputs'
LOC=Path('Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization')
EN=LOC/'English/english.xml'
UK=LOC/'Ukrainian/ukrainian.xml'
def git(*args): return subprocess.check_output(['git','-C',str(REPO),*args])
def sha(data): return hashlib.sha256(data).hexdigest()
def records(data):
    root=ET.fromstring(data)
    assert root.tag=='contentList'
    assert all(e.tag=='content' and set(e.attrib)=={'contentuid','version'} and len(e)==0 for e in root)
    return list(root)
def byid(rows): return {e.attrib['contentuid']:e for e in rows}

source_bytes=(REPO/EN).read_bytes()
base_bytes=git('show','HEAD:'+UK.as_posix())
base=base_bytes.decode('utf-8').replace('\r\n','\n')
eng=records(source_bytes); old=records(base_bytes)
em=byid(eng); om=byid(old)
translations={}
for name in ['dragon-translations.json','wizard-translations.json','monk-translations.json']:
    t=json.loads((ROOT/name).read_text(encoding='utf-8'))
    assert not set(t)&set(translations)
    translations.update(t)
fixes={'h6299a92eg8049g117bga5b7g17d26b0619d6','hf12dc8a9g3079g890agb1ffgdf7b91f3c03d','h9fa0d3deg53aag92d4g5ba5g0185574f2cd7','he4b058a0g2cdbgba7agf3cfg71fa968bbd61'}
assert set(translations)==(set(em)-set(om))|fixes
assert len(translations)==113
pat=re.compile(r'^[ \t]*<content\b[^>]*>.*?</content>',re.M|re.S)
matches=list(pat.finditer(base))
raw={re.search(r'contentuid="([^"]+)"',m[0])[1]:m[0] for m in matches}
assert all(base[a.end():b.start()]=='\n' for a,b in zip(matches,matches[1:]))
blocks=[]
for e in eng:
    uid=e.attrib['contentuid']
    if uid in translations:
        indent=re.match(r'[ \t]*',raw.get(uid,'  '))[0]
        blocks.append(f'{indent}<content contentuid="{uid}" version="{e.attrib["version"]}">{html.escape(translations[uid],quote=False)}</content>')
    else: blocks.append(raw[uid])
text=base[:matches[0].start()]+'\n'.join(blocks)+base[matches[-1].end():]
final_bytes=text.replace('\n','\r\n').encode('utf-8')
(REPO/UK).write_bytes(final_bytes)
OUT.mkdir(exist_ok=True)
(OUT/'ukrainian.xml').write_bytes(final_bytes)

final=records(final_bytes); fm=byid(final)
assert len(final)==len(fm)==len(eng)==len(em)==5464
assert list(fm)==list(em)
assert set(fm)==set(em)
assert all(e.text and e.text.strip() for e in final)
assert all(fm[k].attrib==em[k].attrib for k in em)
assert all((fm[k].text==om[k].text and fm[k].attrib==om[k].attrib) for k in om if k not in fixes)
assert len([k for k in om if fm[k].text!=om[k].text])==4
assert fm['hb033a976g4cccgdbedg5c40ge3ee8016bca2'].text==om['hb033a976g4cccgdbedg5c40ge3ee8016bca2'].text
assert '\ufffd' not in text

def tokens(pattern,s): return collections.Counter(re.findall(pattern,s or '',re.I))
tag_mismatches=[]; variable_mismatches=[]
for k in em:
    if tokens(r'<[^>]+>',em[k].text)!=tokens(r'<[^>]+>',fm[k].text): tag_mismatches.append(k)
    if tokens(r'\[\d+\]|\{[^{}]+\}|%\d*\$?[sdif]',em[k].text)!=tokens(r'\[\d+\]|\{[^{}]+\}|%\d*\$?[sdif]',fm[k].text): variable_mismatches.append(k)
assert not tag_mismatches,tag_mismatches
assert not variable_mismatches,variable_mismatches

class TagBalance(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=False); self.stack=[]; self.errors=[]
    def handle_starttag(self,tag,attrs):
        if tag not in {'br','hr','img','input','meta','link'}: self.stack.append(tag)
    def handle_endtag(self,tag):
        if not self.stack or self.stack.pop()!=tag: self.errors.append(tag)
    def handle_startendtag(self,tag,attrs): pass

balance=[]
for e in final:
    p=TagBalance(); p.feed(e.text); p.close()
    if p.stack or p.errors: balance.append(e.attrib['contentuid'])
assert not balance,balance
numbers=[]; paragraphs=[]
for k in translations:
    if tokens(r'\d+\+?',em[k].text)!=tokens(r'\d+\+?',fm[k].text): numbers.append(k)
    if em[k].text.count('\n\n')!=fm[k].text.count('\n\n'): paragraphs.append(k)
assert not numbers,numbers
assert not paragraphs,paragraphs
for k in translations:
    assert re.search(r'[А-Яа-яІіЇїЄєҐґ]',fm[k].text),k
    assert fm[k].text!=em[k].text,k
groups=collections.defaultdict(list)
for k in translations: groups[em[k].text].append(k)
repeated=[ids for ids in groups.values() if len(ids)>1]
assert all(len({fm[k].text for k in ids})==1 for ids in repeated)

subprocess.run(['git','-C',str(REPO),'diff','--check'],check=True)
changed_paths=git('diff','--name-only').decode().splitlines()
assert changed_paths==[UK.as_posix()],changed_paths
patch=git('diff','--binary','--',UK.as_posix())
(OUT/'ukrainian.patch').write_bytes(patch)
subprocess.run(['git','-C',str(REPO),'apply','--cached','--check',str(OUT/'ukrainian.patch')],check=True)
subprocess.run(['git','-C',str(REPO),'apply','--reverse','--check',str(OUT/'ukrainian.patch')],check=True)
validation={
    'upstream':'https://github.com/Yoonmoonsik/bg3dnd',
    'base_commit':git('rev-parse','HEAD').decode().strip(),
    'source_path':EN.as_posix(), 'target_path':UK.as_posix(),
    'english_source_git_blob':git('rev-parse','HEAD:'+EN.as_posix()).decode().strip(),
    'english_source_sha256_lf':sha(source_bytes.replace(b'\r\n',b'\n')),
    'output_sha256':sha(final_bytes), 'patch_sha256':sha(patch),
    'english_records':len(eng),'original_ukrainian_records':len(old),'final_ukrainian_records':len(final),
    'added':len(set(fm)-set(om)), 'corrected':len(fixes),'unchanged_existing':len(old)-len(fixes),
    'missing':0,'extra':0,'duplicates':0,'empty':0,'version_mismatches':0,
    'english_order_matches':True,'only_target_file_changed':True,
    'inline_tag_mismatches':tag_mismatches,'unbalanced_inline_markup':balance,
    'variable_mismatches':variable_mismatches,'changed_entry_numeric_mismatches':numbers,
    'changed_entry_paragraph_mismatches':paragraphs,
    'identical_english_groups_checked':len(repeated),
    'all_changed_entries_have_ukrainian_text':True,
    'improved_shillelagh_untouched':True,
    'git_diff_check':'PASS','patch_applies_to_base_index':'PASS','patch_reverse_applies_to_worktree':'PASS',
    'updated_existing_ids':sorted(fixes),
    'limitations':['Validation covers localization XML and source meaning; no in-game playtest performed.']
}
(OUT/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (OUT/'changes.tsv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    w.writerow(['change','contentuid','version','English','previous Ukrainian','updated Ukrainian'])
    for e in eng:
        k=e.attrib['contentuid']
        if k in translations: w.writerow(['correction' if k in om else 'addition',k,e.attrib['version'],e.text,om[k].text if k in om else '',fm[k].text])
(ROOT/'all-translations.json').write_text(json.dumps(translations,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation,ensure_ascii=False,indent=2))
print(git('diff','--stat').decode())
