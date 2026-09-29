# Источники польской терминологии — проверка 12 сентября 2026

## Основной источник: официальный корпус BG3 из прошлой работы

Сначала проверены локальные материалы. Найдены парные игровые XML, сопоставленные по одному и тому же `contentuid`, а не по сходству польских слов:

- Английский корпус: `C:\Users\coldb\Documents\Codex\2026-08-24\new-chat\work\bg3-en.xml`.
- Польский корпус: `C:\Users\coldb\Documents\Codex\2026-08-24\new-chat\work\official_bg3_polish_20260828\polish.loca.xml`.
- Сохранённый исходный файл: `C:\Users\coldb\Documents\Codex\2026-08-24\new-chat\work\official_bg3_polish_20260828\extracted\Localization\Polish\polish.loca`.

Это сохранённая выгрузка из предыдущей задачи (каталог датирован 28 августа), не новая выгрузка. На текущей машине установлен BG3 в `C:/Program Files (x86)/Steam/steamapps/common/Baldurs Gate 3`; в текущем `Data/Localization` есть English.pak, но отсутствует Polish.pak. Текущая проверка не меняла игру и не переключала её язык.

SHA-256:

- `bg3-en.xml`: `E186FA9AEBE8364100E32051ECB9F9BC147170959F2E71E2E492E3931BB614FA`
- `polish.loca.xml`: `84A1B9CB3AE1147B51E9CF36892D44732609500210FEACDD72789ABAEE187AC5`
- исходный `polish.loca`: `EFDBDC67FA8E718A794098E01CAD3A12EDC85AA073E91597CF4BF45E177D8024`

### Подтверждённые названия BG3

| English | Polish в игровом корпусе | contentuid |
|---|---|---|
| Arcane Eye | Magiczne oko | `h3393012agaa37g4429gb7b1ge7f20ed88482` |
| Scroll of Arcane Eye | Zwój magicznego oka | `h213aeceag1f66g4743g82fag8a9196c72499` |
| Chromatic Orb | Barwna kula | `hd64d5d0ag20a6g4d74g8676gc34ad9ae4185` |
| Command | Rozkaz | `h5b858a78g01b2g4d06ga486g12083a002a54` |
| Darkvision | Widzenie w ciemności | `h4429287cg9154g4843g944ag9bad9d8979cc` |
| Fly | Lot | `h125be5ecg5c57g4001gadfagcb1c5ca5ee06` |
| Protection from Energy | Ochrona przed energią | `h3fc19655g97b4g496fgb23fg608be11eebc0` |
| Banishment | Wypędzenie | `h04190fa0g38fbg45bcg9444geb22d810007c` |
| Dominate Person | Dominacja nad osobą | `h26eba7c3ge9bag47e4g954eg8d34e058401a` |
| Durable | Twardziel | `h52ed0302g36beg4fb2g917fgc1f62992fbd0` |
| Short Rest | Krótki odpoczynek | `h0567d158gc840g442eg8021gef89ad3396fe` |
| Hit Dice | Kość Wytrzymałości | `hf9c0c9cbg6271g4959gb9d0g141ad19b1d6a` |
| Channel Divinity | Akt wiary | `h2830ddb0g6112g4557gb701gaaa65998837b` |
| Charmed | Zauroczenie | `h88e25a81g90f3g48adg8f25g62b54172b83a` |
| Frightened | Przerażenie | `h08166cc8g5846g432cgbdbfg289f214ce12a` |
| Incapacitated | Obezwładnienie | `h0663feffgbc65g47b1ga704gef8e414d6311` |
| Dragon | Smok | `h05c1539dg2e5cg43d5g9f9ag96d2a06f7abd` |
| Light Domain | Domena światła | `h6954b056g9dbbg492cga6fbge371a0fd9e49` |
| Tempest Domain | Domena burzy | `h3a8c5722g805ag43e0ga665g29be75b59fdb` |
| Focused Conjuration | Skupienie | `hc026d5d2ga580g4189gbdbdgd10671ad2b07` |
| Split Enchantment | Podwójne zauroczenie | `h52e90f2bg528dg4f76g9e07gdb387013d756` |
| Instinctive Charm | Instynktowny urok | `had78fae4g283dg4f5fgb85eg3b902f7d7eca` |
| Benign Transposition: Teleport | Bezpieczne przeniesienie: Teleportacja | `h5fe29df0g88d9g4dfeg9b60g81fa93a4b183` |
| Conjuration Wizard | Mag przywoływania | `h05d2f547g2a6fg4b16gb1abgeb85497c7772` |
| School of Conjuration | Szkoła przywoływania | `hb621a062gbe72g4aaag8fe3g7813a70938ee` |
| School of Enchantment | Szkoła uroków | `h2fb3dca4g6ae1g4bbeg87afg17a37e974932` |
| Draconic Resilience | Smocza odporność | `h2b56c3e6g3117g4d9dg84e3gff9843f2674f` |
| Frightful Presence | Przerażająca obecność | `h24144025ge24dg4b06g97dagc738147a3eb0` |
| Tiamat | Tiamat | `h3740ddb4gbbf6g4c93gbfc2g6767326d1e3b` |
| Bahamut | Bahamut | `h0acfe4aag5143g480fg9c45g94a07971981a` |

### Другие подтверждения в описаниях

- `hb10f8d6eg2615g47f5gb959g8c79351f19dc`: Hit Dice расходуются во время короткого отдыха на восстановление Hit Points; в PL употреблены `kość wytrzymałości` и `punktów wytrzymałości`. Для нового Hit Point Dice подходит тот же ресурс, с грамматически нужным числом (`jedną ze swoich kości wytrzymałości`). Это перенос подтверждённого игрового термина, а не перевод на «kości punktów wytrzymałości».
- `h5ac0c2deg976cg4ee6gb0e4gd3d817622fc7`: в описании драконов прямо присутствуют `Chromatyczne smoki` и `smoki metaliczne`.
- `hdefaa9bbg99a6g4665gaa04ge0a2d8722735`: `A servant of Bahamut, god of metallic dragons.` → `Sługa Bahamuta, boga metalicznych smoków`.
- `h02b86a76g0658g489dgbdf3gfae2b72445ab`: `The wyrm is fallen.` → `Smok poległ.` Поэтому `wyrm` в новых описаниях можно передавать как `smok`; это не требует придумывания новой категории существа.
- Самостоятельные названия `Conjurer` и `Enchanter` не найдены среди названий классов в BG3. Есть диалоговое `conjurer` → `przywoływacz` (`h8efac2f8gb7b9g4bb2ga71bgd1f96beb5d7c`) и `enchanter` → `adept uroków` (`h1a2ec827g6779g470dgbbacg3e04be4ebc2a`). Это только контекстная лексика, не официальные названия новых подклассов.

## Вторичный источник: польское D&D-сообщество

Для `Charm Monster` не найдено соответствующего английского названия в игровом корпусе (поиск полной строки и подстроки). Рекомендуемое `Zauroczenie potwora` подтверждено реальным употреблением:

- [Hardcodex: польские карточки bard-xge](https://hardcodex.ru/cleric/?cardcolor=2&cat=Bard&load=19-11-11-213441-bard-xge), карточка с заголовком `Zauroczenie potwora` (на открытой странице строки 343–352). В описании: один видимый объект, спасбросок Мудрости, дружественное отношение и осведомлённость после окончания — совпадает по идентичности заклинания Charm Monster. Это пользовательская карточка, не официальная локализация BG3/Wizards. Использовать как источник названия; механику переводить с текущего English мода.
- [POLTERGEIST: Trener potworów [3.5]](https://forum.polter.pl/viewtopic.php?p=1091779): `zauroczenie potwora` присутствует в перечне заклинаний. Страница открыта и проверена. Дополнительное свидетельство устойчивого употребления в польском D&D-сообществе, из другой редакции.

Предлагаемый `Zwój zauroczenia potwora` — грамматическое построение на подтверждённом названии с игровым шаблоном `Zwój ...`. Самостоятельного официального названия этого свитка в BG3 не обнаружено.

## Согласованность с вычитанным модом

Уже существующие переводы в upstream/snapshot сохраняются. Они не становятся «официальными BG3» только из-за присутствия в моде:

| English | Уже вычитанный польский мод | Пример UID |
|---|---|---|
| Dragon’s Breath | Smocze zionięcie | `he19de47agde53g5b49gd45ag019467942cb7` |
| Synaptic Static | Szum synaptyczny | `hd666f94dg1a88g5b93g7dcbgfbc951360305` |
| Speedy Recovery (в старом описании Durable) | Szybka regeneracja | `h6299a92eg8049g117bga5b7g17d26b0619d6` |
| Magic action | akcja Magii | `h397f04c0gccd3gd295ga021g620c652c55a6` |
| Emanation | Emanacja | `h8e98b937g68e2gbad3g7b1ag31a19750c163` |

Тексты Dragon’s Breath и Synaptic Static отсутствуют среди точных названий проверенного официального BG3 корпуса. Новые упоминания должны брать названия из мода, без переименования.

## Решения, для которых нет подтверждённого эквивалента

Точные новые названия `Dragon Domain`, `Chromatic Affinity`, `Draconic Majesty`, `Wyrm’s Blessing`, `Warrior of the Mystic Arts`, `Mystic Focus`, `Focused Strike`, `Swift Retribution`, `Speedy Recovery` и `Short Resting` в проверенном корпусе BG3 не обнаружены. Веб-поиск точных английских названий Dragon Domain/Warrior of the Mystic Arts вместе с польскими словами не дал подтверждённого польского названия. Новые формулировки следует честно обозначать редакторскими решениями, за исключением уже существующего в моде `Szybka regeneracja`.

Для Dragon Domain обоснован выбранный редактором `Domena smoka`: структура официальных `Domena światła`/`Domena burzy` и официальный `smok`. Для Wyrm’s Blessing обоснован `Błogosławieństwo smoka`: в BG3 wyrm передаётся как smok. Это предложенные адаптации, не найденные официальные имена.

Для нового состояния `Short Resting` официальный термин действия — `Krótki odpoczynek`; названия `Short Resting` как состояния в корпусе нет. Выбор идентичного `Krótki odpoczynek` или явно текущего `Trwa krótki odpoczynek` является редакторской адаптацией.

Значения новых механик, ограничения и версии должны проверяться по текущему English мода. Официальный корпус используется только как терминологический приоритет.

## Дополнительный первичный источник D&D: издатель Rebel

[Страница издателя с официальной errata](https://www.wydawnictworebel.pl/pages/errata-do-pierwszego-druku-d-d-podrecznika-gracza-1390.html) непосредственно ссылается на [PHB_PL_errata_v1-2019.pdf](https://files.rebel.pl/images/wydawnictwo/zapowiedzi/DnD/PHB_PL_errata_v1-2019.pdf). Физическая страница PDF 2 воспроизводит фрагмент книжной страницы 93. Прямо подтверждено название **Wytrzymały przywołaniec** для способности Conjuration Wizard, дающей временные пункты выносливости призванным существам (Durable Summons). В том же фрагменте присутствуют `Bezpieczne przeniesienie`, `Skupienie`, `Instynktowny urok`, `Podwójne zauroczenie`.

Название Durable Summons отсутствует в BG3-корпусе; поэтому применимо подтверждённое польское D&D-название издателя. Механика нового мода отличается от PHB 2014, переводится с нового English и не заимствуется из errata.

## Отдельная терминологическая проверка 51 строки root-translations.json

Прочитаны все 51 перевода, сопоставлены найденные названия заклинаний и состояний. Найдено одно повторяющееся расхождение: `Lightning` как тип урона должно быть `Elektryczność`, а не `Błyskawice` (BG3 UID `h647de1eege687g4fe6g83dbg732e1c6e117b`, `h95295c6ag8609g4964g80b8g6caa0b15678a`). Основной агент исправил два пункта выбора типа и два описания. Повторная проверка root-translations.json подтвердила отсутствие Błyskawice/błyskawice; все 51 строки прошли терминологическую проверку. Остальные подтверждённые названия заклинаний, состояний, hit dice и короткого отдыха согласованы.

Дополнительные точные BG3-термины: `Bonus Action` → `Akcja dodatkowa` (`h1920d538g5572g4cf1g9473g213c48de26a6`), `Fear` → `Strach` (`h6f38a9b4gc4deg4318g9f6cg4d073b48bde2`), `Thunder` → `Dźwięk` (`h24650d5cgd8afg46e7ga817g87a20ae8da3d`).
