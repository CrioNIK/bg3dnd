import datetime, hashlib, json, pathlib, subprocess
W=pathlib.Path(__file__).resolve().parent; O=W.parent/'outputs'; R=W/'bg3dnd'
V=json.loads((O/'validation.json').read_text(encoding='utf-8'))
REL='Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization/English/english.xml'
remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],cwd=R,text=True).split()[0]
assert remote==V['source_revision'],'Upstream changed; refresh source before delivery'
start_blob=subprocess.check_output(['git','show',V['source_revision']+':'+REL],cwd=R)
end_blob=subprocess.check_output(['git','show','origin/main:'+REL],cwd=R)
assert start_blob==end_blob
V['freshness_check_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
V['final_remote_main']=remote
V['english_git_blob_sha256']=hashlib.sha256(end_blob).hexdigest()
V['english_source_unchanged']=True
V['proofreading']={'independent_block_reviews':3,'terminology_review':'completed; Lightning corrected to Elektryczność, spell slot level unified as poziom','language_tool':'6.5, pl-PL; 111 changed entries / 91 distinct strings; 12 false positives reviewed, no unresolved findings','in_game_test':'not performed'}
(O/'validation.json').write_text(json.dumps(V,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=f'''# Польская локализация DnD 5.5e All-in-One BEYOND

Готово: **109 новых записей и 2 исправленных описания Durable**. Итоговый `polish.xml` содержит **5464 записи**, полностью соответствует текущему English. В репозитории изменён только `Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization/Polish/polish.xml`; 5353 прежние записи сохранены.

Источник содержания — [main на ревизии {remote[:12]}](https://github.com/Yoonmoonsik/bg3dnd/blob/{remote}/{REL}). В начале и в конце работы main совпала; повторная проверка выполнена {V['freshness_check_utc']}. Английский файл за время работы не изменился. Сверка с [последней польской правкой PR #1344](https://github.com/Yoonmoonsik/bg3dnd/pull/1344) также выявила уже внесённую автором правку Improved Shillelagh: она сохранена. Оба названия Przywrócenie honoru сохранены.

## Что обновлено

Добавлены Dragon Domain, Warrior of the Mystic Arts, переработанные Conjurer/Enchanter, Charm Monster и его свиток, свиток Arcane Eye, Swift Retribution, Speedy Recovery и Short Resting. В двух описаниях Durable версия повышена с 2 до 3: бонусное действие расходует одну кость выносливости и восстанавливает выпавшее число очков. Прежнее максимальное лечение удалено. Все новые записи получили свои актуальные версии из English, в том числе версии 2 и 3.

## Термины и спорные решения

Сначала использована сохранённая выгрузка официальной польской BG3, с проверкой пар EN/PL по `contentuid`. Существующие названия Smocze zionięcie, Szum synaptyczny, Niesamowity metabolizm и Szybka regeneracja сохранены. Для отсутствующего в BG3 Charm Monster использовано подтверждённое сообществом **Zauroczenie potwora** ([карточки Hardcodex](https://hardcodex.ru/cleric/?cardcolor=2&cat=Bard&load=19-11-11-213441-bard-xge), [POLTERGEIST](https://forum.polter.pl/viewtopic.php?p=1091779)). Для Durable Summons — **Wytrzymały przywołaniec** из [официальной errata польского издателя Rebel, стр. PDF 2](https://files.rebel.pl/images/wydawnictwo/zapowiedzi/DnD/PHB_PL_errata_v1-2019.pdf). Из источников терминов не переносились старые механики.

Редакторскими решениями, для которых не найдено подтверждённого готового польского названия, остаются **Domena smoka, Chromatyczne powinowactwo, Smoczy majestat, Błogosławieństwo smoka, Dalekie przeniesienie, Czarujący rozmówca, Hipnotyzująca obecność, Wojownik sztuk mistycznych, Mistyczne skupienie, Cios skupienia, Błyskawiczna odpłata**. Для состояния Short Resting применён официальный термин действия **Krótki odpoczynek**. Эти адаптации не объявляются официальными или общепринятыми. Подробные основания, UID и происхождение корпуса — в `terminology-sources.md`.

## Проверки

- Выполнены отдельная перекрёстная вычитка всех 111 затронутых записей и проверка механик. Исправлено название типа урона Lightning на официальное Elektryczność; уровни ячеек унифицированы как poziom.
- XML и вложенная игровая разметка корректны. Нет пропусков, лишних, повторных, пустых записей, расхождений версий, тегов, плейсхолдеров или порядка. Служебные ссылки и формулы сохранены; числа новых/изменённых записей совпадают с English.
- Проверены все **758 групп** повторяющегося английского текста: несогласованных переводов нет. Диапазоны 10/30/60 футов оставлены в футах, с сохранением исходных чисел. Игровая запись костей локализована как k6/k8/k10/k12.
- Локальный LanguageTool 6.5 проверил 111 записей (91 уникальный текст); 12 срабатываний на имена, игровые сокращения и форму «maga» проверены вручную и признаны ложными. Открытых замечаний нет.
- `git diff --check` и проверка применения патча в обе стороны прошли. Применение к исходному польскому файлу воспроизводит итоговый XML побайтно. Проверка в запущенной игре не выполнялась.

## Файлы

- `polish.xml` — готовая локализация.
- `polish-update.patch` — применимый diff от указанной ревизии main (109 добавлений и 2 изменения записей; 129 добавленных и 4 удалённых физических строки).
- `review.tsv` — все изменённые записи: UID, версия, English, прежний и новый Polish.
- `validation.json` — результаты проверок, SHA-256 и финальная проверка upstream.
- `terminology-sources.md` — проверяемые свидетельства терминологии и границы подтверждения.

Для применения из корня копии репозитория: `git apply --check <путь-к-polish-update.patch>`, затем `git apply <путь-к-polish-update.patch>`.
'''
(O/'report.md').write_text(report,encoding='utf-8')
print(json.dumps({k:V[k] for k in ['final_remote_main','freshness_check_utc','english_source_unchanged','english_git_blob_sha256','polish_sha256']},indent=2))
