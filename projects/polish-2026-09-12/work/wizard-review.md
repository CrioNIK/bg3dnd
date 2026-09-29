# Niezależna wyczytka 45 wpisów maga

Porównano wszystkie wpisy `work/wizard-translations.json` z odpowiadającymi im wpisami `work/entries-to-translate.json` (indeksy 5404–5448). Pliku tłumaczeń nie zmieniano. JSON ma komplet 45 oczekiwanych identyfikatorów, brak pustych wartości, a identyczne opisy źródłowe mają identyczne tłumaczenia.

## Zalecane ujednolicenie terminologii

**Poziom czaru / komórki:** stosować `poziom` w całym nowym materiale, w zgodzie z tekstem mnicha i dominującą terminologią oficjalnej lokalizacji BG3. `Krąg` nie jest nazwą zmyśloną ani całkowicie nieobecną w grze, lecz jest wariantem mniejszościowym. Wśród par z angielskim `spell slot` znaleziono 120 polskich wpisów z `poziom` i 3 z `krąg`/`kręg`; jedna z tych trzech ma oba warianty. Nie jest to statystyka całego korpusu wszystkich użyć słowa level, tylko jawnie wskazanej próbki.

Bezpośrednie przykłady z oficjalnego korpusu:

- h0e9835fdg9120g4ecfgb160g4314ea69018e: `Expend a Level 2 ... spell slot ...` → `Zużyj ... komórkę czaru ... poziomu 2 ...`;
- h10ae97cfg8debg4b69g8acagcca48ad52580: `per spell slot level` → `za każdy poziom komórki czaru`;
- h0711db73g48d0g4eb4g932dg762a4e375171: `Level [4] ... Spell Slot Unlocked` → `Odblokowano ... komórkę czaru ... poziomu [4]`.

Mniejszościowy wariant: h7a92f97dg555cg430fgb88ag2322db4c7d3c ma `komórkę czaru kręgu 3`. Oba odczyty pochodzą z oficjalnych korpusów `english.loca.xml` i `polish.loca.xml` w podkatalogach `official_bg3_english_20260828` / `official_bg3_polish_20260828` katalogu `C:/Users/coldb/Documents/Codex/2026-08-24/new-chat/work`.

Wpisy do ujednolicenia:

| Indeks | UID | Zalecana zamiana |
| --- | --- | --- |
| 5411 | h548afd77gc2b3g89dfgd738gf776357e3e79 | `komórkę czaru 3. kręgu lub wyższego` → `komórkę czaru 3. poziomu lub wyższego` |
| 5413 | h7e99425cg912fg30f6gef4ag9591cab2c074 | ta sama zamiana |
| 5438 | h1b565bd8g75aagd7d4g1b3bg1fcb7e03fd42 | `wyższego kręgu` → `wyższego poziomu`; `efektywny krąg czaru` → `efektywny poziom czaru` |
| 5441 | ha516d403gf15cgb9d8ga87dgc79c55b2ab57 | te same dwie zamiany |

## Drobne zalecenia językowe

To poprawki płynności, nie stwierdzone błędy mechaniki:

- **Instynktowny urok, indeksy 5443/5445/5447:** `trafi cię testem ataku` jest zrozumiałe, lecz niezręczne. Naturalniejszy precyzyjny wariant: `trafi cię w wyniku testu ataku`. Zachować warunek trafienia; samo `zaatakuje cię` osłabiłoby wymóg źródła.
- **Czarujący rozmówca, indeksy 5424/5426:** `w jednej z następujących wybranych umiejętności` sugeruje niepotrzebnie, że lista jest już wybrana. Czytelniej: `w jednej z następujących umiejętności do wyboru: Oszustwo, Zastraszanie lub Perswazja`.
- **Podwójne zauroczenie, indeksy 5438/5441:** `aby objąć dodatkową istotę` warto dopełnić jako `aby objąć działaniem dodatkową istotę`.
- **Wytrzymały przywołaniec, indeksy 5415/5417/5420:** ujednolicić `poziomu Maga` na `poziomu maga`, jak `poziomu mnicha` i `poziomu kleryka` w pozostałych nowych opisach. Nazwy klas w polskim tekście ciągłym są rzeczownikami pospolitymi.

## Kontrola mechanik

- **Bezpieczne przeniesienie:** akcja dodatkowa, do 30 stóp, widoczne niezajęte miejsce; alternatywnie miejsce zajęte przez istotę średnią lub mniejszą w zasięgu, zgoda tej istoty, teleportacja obojga i zamiana miejsc. Zgoda nie została rozszerzona na wymóg sojuszu. Limit modyfikatora Inteligencji z minimum jednego i odnowienie wszystkich użyć po długim odpoczynku zachowano.
- **Dalekie przeniesienie:** zasięg 60 stóp, odzyskanie jednego użycia kosztem komórki poziomu co najmniej 3, bez akcji. Brak dodatkowego limitu odpoczynku albo obowiązku rzucenia czaru.
- **Wytrzymały przywołaniec:** wymagany czar przywoływania oraz użycie komórki; obejmuje zarówno przywołanie, jak i stworzenie istoty. Tymczasowe PW przy pierwszym pojawieniu się to dwukrotność poziomu maga. Odporność obowiązuje tylko podczas posiadania tych konkretnych tymczasowych PW; zachowano wszystkie cztery wyjątki: moc, nekrotyczne, psychiczne, światłość. `Jest odporna` odpowiada Resistance, nie Immunity. Oficjalne pary potwierdzają `Resistance` → `Odporność` (h1afac00ag5f88g47d9gb095g54fd18427730), `Force` → `Moc` (h1e927ef5g95e7g4c38g8534g39dcb3d42691), `Necrotic` → `Nekrotyczne` (h09c7f407gd08fg4e4fgb21ag0863096d70eb), `Psychic` → `Psychiczne` (hc72a5653g5557g4bc0g9cddgb800298afaad), `Radiant` → `Światłość` (h97e5a269gf0ecg4481g9ccbge4a60aadfcaa).
- **Czarujący rozmówca:** biegłość w jednej wybranej z trzech umiejętności; premia Inteligencji do testów tej umiejętności, minimum +1. Nie dodano premii do pozostałych umiejętności ani nie pomylono minimum premii z limitem użyć.
- **Hipnotyzująca obecność:** akcja Magii, jeden widoczny cel do 10 stóp; cel musi widzieć **lub** słyszeć rzucającego. Rzut na Mądrość przeciw ST czarów; przy niepowodzeniu zauroczenie do 1 minuty. Przedwczesny koniec następuje po oddaleniu na **więcej niż** 10 stóp, jednoczesnym braku widzenia **i** słyszenia rzucającego, albo otrzymaniu obrażeń. Przekład `ani widzieć, ani słyszeć` jest poprawny i nie kończy efektu po utracie tylko jednego ze zmysłów. Obezwładnienie i szybkość 0 obowiązują podczas tego zauroczenia. Nie dopisano powtarzanego rzutu obronnego ani koncentracji. Limit Inteligencji z minimum jednego dotyczy wpisów 5427/5430/5433, zgodnie ze źródłem.
- **Podwójne zauroczenie:** komórka jest użyta do rzucenia czaru szkoły uroków; kwalifikuje się tylko czar, którego rzucenie z wyższej komórki pozwala objąć dodatkową istotę. Efektywny poziom rośnie o 1. Limit równy modyfikatorowi Inteligencji **bez dopisanego minimum** pozostawiono w 5439/5441; wszystkie użycia odnawiają się po długim odpoczynku.
- **Instynktowny urok:** wyzwalaczem jest trafienie przez widoczną istotę do 30 stóp; nie samo zadeklarowanie ataku. Reakcja wymusza Mądrość przeciw ST czarów. Przy niepowodzeniu atak chybia, a ten sam atak zostaje skierowany przeciw innej istocie w swoim zasięgu, z wyłączeniem atakującego. Nie dodano wymogu osobnego testu ataku, ponownego ataku, zgody nowego celu, odporności po udanym rzucie, rozmiaru celu ani dodatkowego zasięgu. Użycie odnawia się po długim odpoczynku **albo** rzuceniu czaru uroków z komórki; nie dopisano minimalnego poziomu tego czaru.

Nie znaleziono błędów zmieniających mechaniki. Po ujednoliceniu `poziom` oraz zastosowaniu wybranych poprawek płynności materiał jest gotowy do scalenia.
