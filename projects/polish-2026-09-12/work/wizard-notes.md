# Conjurer / Enchanter — источники и вычитка

Переведены все 45 новых записей с English index 5404–5448; mapping сохранён в `wizard-translations.json`. Репозиторий этот этап не изменял. Смысл и механика проверены по текущему `entries-to-translate.json`, а не по правилам оригинальной настольной редакции.

## Официальная польская BG3

Проверены пары по одному `contentuid` в локальных игровых корпусах:

- `C:/Users/coldb/Documents/Codex/2026-08-24/new-chat/work/official_bg3_english_20260828/english.loca.xml`
- `C:/Users/coldb/Documents/Codex/2026-08-24/new-chat/work/official_bg3_polish_20260828/polish.loca.xml`

| Термин EN | Принятый PL | Подтверждение BG3 |
|---|---|---|
| Conjurer | Mag przywoływania | `h05d2f547g2a6fg4b16gb1abgeb85497c7772`: Conjuration Wizard → Mag przywoływania; перенесено существующее имя специализации на краткое новое английское название |
| Enchanter | Mag uroków | `h81a51f60g1454g4d35g9142g59075b4faa94`: Enchantment Wizard → Mag uroków; тот же принцип |
| Benign Transposition | Bezpieczne przeniesienie | `h5fe29df0g88d9g4dfeg9b60g81fa93a4b183`: Benign Transposition: Teleport → Bezpieczne przeniesienie: Teleportacja; базовая часть составного названия |
| Focused Conjuration | Skupienie | `hc026d5d2ga580g4189gbdbdgd10671ad2b07`, точная пара |
| Split Enchantment | Podwójne zauroczenie | `h52e90f2bg528dg4f76g9e07gdb387013d756`, точная пара |
| Instinctive Charm | Instynktowny urok | `had78fae4g283dg4f5fgb85eg3b902f7d7eca`, также `hc08cf9b7g93d4g4618g8a2cg158f2573cafb` и `hd09d512cg8131g4e2fg9f5bgc0170814e726` |
| Charm Person | Zauroczenie osoby | `h0ee097e6g7a47g4108ga515g91d2016d86c5` |
| Conjuration | Przywoływanie | `h049b6e16g90d3g4323gaa4fg4fd11bad8118`; в прозе «szkoła przywoływania» |
| Enchantment | Uroki | `h63f1ab3bge972g40b6ga9f4gbe7a1bc842e2`; в прозе «szkoła uroków» |
| Incapacitated | Obezwładnienie | `h0663feffgbc65g47b1ga704gef8e414d6311` |
| Charmed | Zauroczenie | `h88e25a81g90f3g48adg8f25g62b54172b83a` |
| Deception / Intimidation / Persuasion | Oszustwo / Zastraszanie / Perswazja | `hcaeb4d5fg8b57g4520g912fg4fae8267b844`, `h6efd5166g9073g439fgb814gcd9186cb8e61`, `h257372d3g6f98g4450g813bg190e19aecce4` |
| Force / Necrotic / Psychic / Radiant | Moc / Nekrotyczne / Psychiczne / Światłość | `h1e927ef5g95e7g4c38g8534g39dcb3d42691`, `h09c7f407gd08fg4e4fgb21ag0863096d70eb`, `hc72a5653g5557g4bc0g9cddgb800298afaad`, `h97e5a269gf0ecg4481g9ccbge4a60aadfcaa` |

В формулах и прозе сохранены вычитанные формы текущего перевода мода: `komórka czaru`, `ST obrony przed czarami`, `akcja dodatkowa`, `akcja Magii`, `modyfikator Inteligencji`, `tymczasowe punkty wytrzymałości`, `szybkość ruchu`.

Для новых записей **spell level / spell-slot level → poziom**, в согласии с преимущественной официальной терминологией BG3: общий tooltip `h2ace8502g2abag418ag96bbgfbe3b64d60dc`, интерфейс `hcc0de24fgee83g49cdgb15fg2fa9b96203c9` (Select Spell Slot Level → Wybierz poziom komórki czaru) и Arcane Recovery `h7387ca0ag0abag4c7fgaa69ga6b41f39c7de`. В старом моде встречается настольное `krąg` (например, Twinned Spell `h3aef575agcbdfgd3e8g1850ge006a44a0100`); старые вычитанные записи не менялись. Первоначально использованное в черновике `krąg` заменено в четырёх новых записях 5411, 5413, 5438, 5441 после прямой проверки BG3.

## Польская D&D-терминология и новые решения

**Durable Summons → Wytrzymały przywołaniec**: подтверждено в первичном PDF польского издателя Rebel — [Errata do Podręcznika Gracza](https://files.rebel.pl/images/wydawnictwo/zapowiedzi/DnD/PHB_PL_errata_v1-2019.pdf), физическая стр. PDF 2 (фрагмент книжной стр. 93), раздел Szkoła przywoływania. Источник найден по ссылке издателя и непосредственно проверен; в текстовом представлении строки 432–435. Это источник польской настольной терминологии, не название из BG3. Оттуда взято только название; старые механики (14-й уровень, 30 временных PW) в перевод не переносились.

Для новых названий проверены локальные community-корпуса `community_polish_dnd_premium` ([Lioheart/DnD-Premium](https://github.com/Lioheart/DnD-Premium)) и `community_polish_dnd5_foundry`, а также веб-поиск точных английских названий с польским контекстом. Проверяемые польские эквиваленты трёх нижеследующих названий не найдены. Поэтому они обозначаются как обоснованные переводческие решения, а не официальные или общепринятые названия:

- **Distant Transposition → Dalekie przeniesienie**: сохраняет официальное `przeniesienie` из Bezpieczne przeniesienie и отражает увеличение расстояния.
- **Enchanting Conversationalist → Czarujący rozmówca**: сохраняет игру на обаятельной речи и магии ума; это именно собеседник, а не оратор.
- **Hypnotic Presence → Hipnotyzująca obecność**: отражает новое английское Presence; не подменено старой способностью Hypnotic Gaze.

## Проверка смысла и согласованности

- Benign Transposition: бонусное действие, незанятое видимое место в 30 футах либо обмен местами с согласной видимой целью среднего или меньшего размера; число использований по INT, минимум одно; восстановление после долгого отдыха.
- Distant Transposition: 60 футов; восстановление одного использования за ячейку 3-го круга или выше, без действия.
- Durable Summons: использование ячейки для заклинания школы при́зывания, которое призывает или создаёт существо; временные PW при первом появлении равны двум уровням мага; сопротивления действуют только пока сохранены именно эти временные PW; все четыре исключения сохранены.
- Enchanting Conversationalist: одна из трёх перечисленных официальных игровых умений; к проверке выбранного умения прибавляется INT, минимум +1.
- Hypnotic Presence: действие Магии, одна видимая цель в 10 футах; цель должна видеть или слышать персонажа; WIS против ST заклинаний; одна минута; прекращение при расстоянии более 10 футов, при потере одновременно зрения и слуха, либо при уроне. Зачарованная цель также обездействована и имеет скорость 0. Концентрация не добавлялась — её нет в текущем English.
- Split Enchantment: только заклинание школы уро́ков с использованием ячейки и с возможностью добавить цель повышенным кругом; повышение эффективного круга ровно на 1; число применений по INT, без отсутствующего в EN «минимум одно».
- Instinctive Charm: срабатывает на попадание видимого атакующего в 30 футах; тратится реакция; WIS против ST заклинаний; при провале атака промахивается, а при наличии иной цели в пределах атаки, кроме атакующего, перенаправляется на неё. Использование восстанавливается долгим отдыхом либо заклинанием школы уро́ков с тратой ячейки. Не добавлены старые ограничения BG3 (до броска / ближайшая цель / невосприимчивость к очарованию).
- Футы оставлены футами (`stóp`) по указанию; числа 30, 60, 3, 10, 1, +1, 0 сохранены в соответствующих строках. В этом блоке нет служебных тегов или плейсхолдеров. Повторяющиеся английские названия и описания используют одни и те же польские тексты.
