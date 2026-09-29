import datetime,hashlib,json,pathlib,subprocess
W=pathlib.Path(__file__).resolve().parent; O=W.parent/'outputs'; R=W/'bg3dnd'
rel='Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization/Polish/polish.xml'
pr=json.loads(subprocess.check_output(['gh','pr','view','1446','--repo','Yoonmoonsik/bg3dnd','--json','url,state,mergedAt,mergeCommit,statusCheckRollup'],text=True,encoding='utf-8'))
assert pr['state']=='MERGED'
sha=pr['mergeCommit']['oid']
remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],cwd=R,text=True).split()[0]
main_data=subprocess.check_output(['git','show','origin/main:'+rel],cwd=R)
assert main_data==(O/'polish.xml').read_bytes()
enrel=rel.replace('Polish/polish.xml','English/english.xml')
original_en=subprocess.check_output(['git','show','0f0ab55c10ce531e8a81f66a61a2ce19fb35b21c:'+enrel],cwd=R)
current_en=subprocess.check_output(['git','show','origin/main:'+enrel],cwd=R)
assert original_en==current_en
committed_files=subprocess.check_output(['git','diff-tree','--no-commit-id','--name-only','-r',sha],cwd=R,text=True).splitlines()
assert committed_files==[rel]
pub=json.loads((O/'publication.json').read_text(encoding='utf-8'))
pub['pull_requests']=[pr]
pub['upstream_merge']={'commit':sha,'commit_url':'https://github.com/Yoonmoonsik/bg3dnd/commit/'+sha,'remote_main_at_check':remote,'polish_matches_output':True,'polish_sha256':hashlib.sha256(main_data).hexdigest(),'english_unchanged':True,'files':committed_files,'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(O/'publication.json').write_text(json.dumps(pub,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=(O/'report.md').read_text(encoding='utf-8')
report=report.replace('Связанного PR на момент проверки нет.',f'Затем открыт [PR #1446]({pr["url"]}), автоматически принятый в upstream main {pr["mergedAt"]}. Коммит слияния: [{sha}](https://github.com/Yoonmoonsik/bg3dnd/commit/{sha}). Содержимое польского XML в upstream побайтно совпадает с готовым файлом; English не изменён. Проверка GitHub Auto Merge Localization PRs прошла успешно.')
(O/'report.md').write_text(report,encoding='utf-8')
print(json.dumps(pub['upstream_merge'],ensure_ascii=False,indent=2))
