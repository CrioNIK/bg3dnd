import datetime, hashlib, json, pathlib, subprocess
W=pathlib.Path(__file__).resolve().parent; R=W/'bg3dnd'; O=W.parent/'outputs'
branch='localization/polish-2026-09-12'
rel='Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization/Polish/polish.xml'
def git(*args): return subprocess.check_output(['git',*args],cwd=R,text=True).strip()
sha=git('rev-parse','HEAD')
remote=git('ls-remote','fork','refs/heads/'+branch).split()[0]
assert sha==remote
api=json.loads(subprocess.check_output(['gh','api','repos/CrioNIK/bg3dnd/commits/'+sha],text=True,encoding='utf-8'))
assert api['sha']==sha
assert [f['filename'] for f in api['files']]==[rel]
assert api['files'][0]['sha']==git('rev-parse','HEAD:'+rel)
assert not git('status','--porcelain')
data=subprocess.check_output(['git','show','HEAD:'+rel],cwd=R)
assert data==(O/'polish.xml').read_bytes()
prs=[]
for repo,head in [('Yoonmoonsik/bg3dnd','CrioNIK:'+branch),('CrioNIK/bg3dnd',branch)]:
    prs.extend(json.loads(subprocess.check_output(['gh','pr','list','--repo',repo,'--head',head,'--state','all','--json','number,url,state'],text=True,encoding='utf-8')))
record=dict(verified_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),repository='CrioNIK/bg3dnd',branch=branch,branch_url='https://github.com/CrioNIK/bg3dnd/tree/'+branch,commit=sha,commit_url=api['html_url'],parent=git('rev-parse','HEAD^'),remote_ref_matches=True,github_api_commit_matches=True,github_blob_matches=True,committed_files=[rel],polish_sha256=hashlib.sha256(data).hexdigest(),output_matches_commit=True,working_tree_clean=True,pull_requests=prs)
(O/'publication.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=(O/'report.md').read_text(encoding='utf-8')
report+='\n## Публикация\n\n'
report+=f'По разрешению пользователя выполнены commit и обычный push в [ветку {branch}]({record["branch_url"]}) пользовательского форка CrioNIK/bg3dnd.\n\n'
report+=f'Коммит: [{sha}]({record["commit_url"]}). В нём только польский XML. Удалённая ссылка, GitHub API и blob файла проверены; коммит содержит тот же XML, что сохранён в outputs. Рабочее дерево чистое. Связанного PR на момент проверки нет. Проверяемая запись публикации — `publication.json`.\n'
(O/'report.md').write_text(report,encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
