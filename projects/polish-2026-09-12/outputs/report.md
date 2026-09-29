# Польская локализация DnD 5.5e All-in-One BEYOND

Готово: **109 новых записей и 2 исправленных описания Durable**. Итоговый `polish.xml` содержит **5464 записи**, полностью соответствует текущему English. В репозитории изменён только `Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization/Polish/polish.xml`; 5353 прежние записи сохранены.

Источник содержания — [main на ревизии 0f0ab55c10ce](https://github.com/Yoonmoonsik/bg3dnd/blob/0f0ab55c10ce531e8a81f66a61a2ce19fb35b21c/Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization/English/english.xml). В начале и в конце работы main совпала; повторная проверка выполнена 2026-09-12T14:50:05.166177+00:00. Английский файл за время работы не изменился. Сверка с [последней польской правкой PR #1344](https://github.com/Yoonmoonsik/bg3dnd/pull/1344) также выявила уже внесённую автором правку Improved Shillelagh: она сохранена. Оба названия Przywrócenie honoru сохранены.

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

## Публикация

**Общий исходный код обновлён; готовая игровая сборка ещё не обновлена.** При проверке после слияния на [Nexus Files](https://www.nexusmods.com/baldursgate3/mods/12727?tab=files) остаётся пакет 4.12.13.6 от 7 сентября 2026. [Workflow репозитория](https://github.com/Yoonmoonsik/bg3dnd/blob/main/.github/workflows/auto-merge-localization.yml) автоматически сливает локализации, но не собирает и не публикует игровой пакет. Новую общую сборку должен выпустить автор мода; у аккаунта пользователя нет прав публикации в основном репозитории (viewerPermission READ).

По разрешению пользователя выполнены commit и обычный push в [ветку localization/polish-2026-09-12](https://github.com/CrioNIK/bg3dnd/tree/localization/polish-2026-09-12) пользовательского форка CrioNIK/bg3dnd.

Коммит: [bd69631dfc7f57fbf2c29a982a0ac06c1b00f2ed](https://github.com/CrioNIK/bg3dnd/commit/bd69631dfc7f57fbf2c29a982a0ac06c1b00f2ed). В нём только польский XML. Удалённая ссылка, GitHub API и blob файла проверены; коммит содержит тот же XML, что сохранён в outputs. Рабочее дерево чистое. Затем открыт [PR #1446](https://github.com/Yoonmoonsik/bg3dnd/pull/1446), автоматически принятый в upstream main 2026-09-12T14:58:22Z. Коммит слияния: [787d2189094160a2e5cebafc6d448800fe80b088](https://github.com/Yoonmoonsik/bg3dnd/commit/787d2189094160a2e5cebafc6d448800fe80b088). Содержимое польского XML в upstream побайтно совпадает с готовым файлом; English не изменён. Проверка GitHub Auto Merge Localization PRs прошла успешно. Проверяемая запись публикации — `publication.json`.
