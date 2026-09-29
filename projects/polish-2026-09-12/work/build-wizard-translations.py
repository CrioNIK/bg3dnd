import json
from pathlib import Path

source = json.loads(Path('work/entries-to-translate.json').read_text(encoding='utf-8'))
entries = {x['index']: x for x in source if 5404 <= x['index'] <= 5448}
uses = 'Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator Inteligencji (co najmniej raz), a wszystkie zużyte użycia odzyskujesz po ukończeniu długiego odpoczynku.'
benign = 'W ramach akcji dodatkowej teleportujesz się na odległość do 30 stóp w niezajęte miejsce, które widzisz. Zamiast tego możesz wybrać miejsce w zasięgu zajęte przez istotę o rozmiarze średnim lub mniejszym. Jeśli ta istota wyraża zgodę, oboje teleportujecie się, zamieniając się miejscami.'
restore = 'Możesz odzyskać jedno użycie tej zdolności, zużywając komórkę czaru 3. poziomu lub wyższego (bez użycia akcji).'
summon = 'Gdy rzucasz czar ze szkoły przywoływania z użyciem komórki czaru, aby przywołać lub stworzyć istotę, przy pierwszym pojawieniu się zyskuje ona tymczasowe punkty wytrzymałości w liczbie równej dwukrotności twojego poziomu Maga. Dopóki ma te tymczasowe punkty wytrzymałości, jest odporna na wszystkie typy obrażeń z wyjątkiem obrażeń od mocy, nekrotycznych, psychicznych i od światłości.'
summon_short = 'Przy pierwszym pojawieniu się istota zyskuje tymczasowe punkty wytrzymałości w liczbie równej dwukrotności twojego poziomu Maga. Dopóki ma te tymczasowe punkty wytrzymałości, jest odporna na wszystkie typy obrażeń z wyjątkiem obrażeń od mocy, nekrotycznych, psychicznych i od światłości.'
proficiency = 'Zyskujesz biegłość w jednej z następujących wybranych umiejętności: Oszustwo, Zastraszanie lub Perswazja.'
hypnotic = 'W ramach akcji Magii wybierz jedną istotę, którą widzisz w odległości do 10 stóp od siebie. Jeśli cel cię widzi lub słyszy, musi wykonać rzut obronny na Mądrość przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu otrzymuje stan zauroczenia na 1 minutę lub do chwili, gdy znajdzie się dalej niż 10 stóp od ciebie, nie będzie cię ani widzieć, ani słyszeć lub otrzyma obrażenia. Dopóki cel jest zauroczony, ma stan obezwładnienia, a jego szybkość ruchu wynosi 0.'
split = 'Gdy używasz komórki czaru, aby rzucić czar ze szkoły uroków, taki jak Zauroczenie osoby, który można rzucić przy użyciu komórki czaru wyższego poziomu, aby objąć dodatkową istotę, możesz zwiększyć efektywny poziom czaru o 1.'
split_uses = 'Możesz użyć tej zdolności tyle razy, ile wynosi twój modyfikator Inteligencji, a wszystkie zużyte użycia odzyskujesz po ukończeniu długiego odpoczynku.'
instinctive = 'Gdy istota, którą widzisz w odległości do 30 stóp od siebie, trafi cię testem ataku, możesz użyć reakcji, aby zmusić atakującego do wykonania rzutu obronnego na Mądrość przeciwko twojemu ST obrony przed czarami. Przy niepowodzeniu atak zamiast tego chybia, a jeśli w jego zasięgu znajduje się inna istota (poza atakującym), atakujący kieruje atak, który wywołał tę reakcję, przeciwko niej.'
instinctive_uses = 'Gdy użyjesz tej reakcji, nie możesz zrobić tego ponownie do ukończenia długiego odpoczynku. Możesz również odzyskać jej użycie, rzucając czar ze szkoły uroków z użyciem komórki czaru.'
translations = {
5404: 'Mag przywoływania',
5405: 'Mag przywoływania uważa odległość i materię za elastyczne wytyczne, a nie niezmienne prawa fizyki. Magowie przywoływania opanowują magię, która błyskawicznie przenosi istoty w przestrzeni i przywołuje je do walki w ich imieniu.',
5406: 'Bezpieczne przeniesienie',
5407: benign + '\n\n' + uses,
5408: 'Poziom 3: Bezpieczne przeniesienie',
5409: benign,
5410: 'Poziom 6: Dalekie przeniesienie',
5411: 'Zasięg twojej zdolności Bezpieczne przeniesienie zwiększa się do 60 stóp. Ponadto możesz odzyskać jedno jej użycie, zużywając komórkę czaru 3. poziomu lub wyższego (bez użycia akcji).',
5412: 'Dalekie przeniesienie',
5413: restore,
5414: 'Poziom 6: Wytrzymały przywołaniec',
5415: summon,
5416: 'Wytrzymały przywołaniec',
5417: summon_short,
5418: 'Poziom 10: Skupienie',
5419: 'Wytrzymały przywołaniec',
5420: summon,
5421: 'Mag uroków',
5422: 'Magia maga uroków mami lub zniewala umysły. Niektórzy magowie uroków wykorzystują swoje zdolności, by szerzyć pokój i łagodzić okrucieństwo, inni zaś posługują się magią wpływającą na umysł dla własnych korzyści.',
5423: 'Poziom 3: Czarujący rozmówca',
5424: proficiency + '\n\nPonadto, gdy wykonujesz test cechy z użyciem wybranej umiejętności, zyskujesz premię do testu równą twojemu modyfikatorowi Inteligencji (co najmniej +1).',
5425: 'Czarujący rozmówca',
5426: proficiency,
5427: uses,
5428: 'Poziom 3: Hipnotyzująca obecność',
5429: 'Twoje czarujące słowa i zniewalające spojrzenie mogą omamić inną istotę. ' + hypnotic,
5430: uses,
5431: 'Hipnotyzująca obecność',
5432: 'Hipnotyzująca obecność',
5433: hypnotic + '\n\n' + uses,
5434: 'Hipnotyzująca obecność',
5435: 'Hipnotyzująca obecność',
5436: 'Twoje zniewalające spojrzenie utrzymuje istotę w transie. Cel ma stany zauroczenia i obezwładnienia, a jego szybkość ruchu wynosi 0. Efekt kończy się, jeśli cel oddali się od ciebie na więcej niż 10 stóp, nie będzie cię ani widzieć, ani słyszeć lub otrzyma obrażenia.',
5437: 'Poziom 6: Podwójne zauroczenie',
5438: split,
5439: split_uses,
5440: 'Podwójne zauroczenie',
5441: split + '\n\n' + split_uses,
5442: 'Instynktowny urok',
5443: instinctive + '\n\n' + instinctive_uses,
5444: 'Poziom 10: Instynktowny urok',
5445: instinctive,
5446: instinctive_uses,
5447: instinctive,
5448: instinctive_uses,
}
assert set(entries) == set(translations)
result = {entries[index]['uid']: text for index, text in translations.items()}
Path('work/wizard-translations.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(result)} translations written.')
