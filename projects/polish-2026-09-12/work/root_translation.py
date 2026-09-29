import json, pathlib
W=pathlib.Path(__file__).resolve().parent
rows=json.loads((W/'entries-to-translate.json').read_text(encoding='utf-8'))
T={}
def add(index, text):
    e=next(r['en'] for r in rows if r['index']==index)
    T[e]=text
recovery='W ramach akcji dodatkowej możesz wydać jedną ze swoich kości wytrzymałości, rzucić nią i odzyskać punkty wytrzymałości w liczbie równej wynikowi rzutu.'
add(861,'Oporny na śmierć. Masz ułatwienie w rzutach obronnych przeciwko śmierci.\n\nSzybka regeneracja. '+recovery)
add(5355,'Szybka regeneracja')
add(5356,recovery)
for i,n in enumerate([6,8,10,12],5357): add(i,f'Szybka regeneracja: k{n}')
add(5361,'Krótki odpoczynek')
add(5362,'Zauroczenie potwora')
add(5363,'Jedna istota, którą widzisz w zasięgu czaru, wykonuje rzut obronny na Mądrość. Wykonuje go z ułatwieniem, jeśli ty lub twoi sojusznicy z nią walczycie. Przy niepowodzeniu cel zostaje zauroczony do końca działania czaru albo do chwili, gdy ty lub twoi sojusznicy zadacie mu obrażenia. Zauroczona istota jest do ciebie przyjaźnie nastawiona. Gdy czar się kończy, cel wie, że został przez ciebie zauroczony.')
add(5364,'Zwój zauroczenia potwora')
add(5365,'Dostępne klasy: Bard, Druid, Zaklinacz, Czarownik, Mag')
add(5366,'Domena smoka')
add(5367,'Smok')
add(5368,'Choć głównymi wyznawcami Domeny smoka są smoki, smocze bóstwa przyjmują cześć od każdego, kto pragnie bogactwa lub potęgi. Klerycy Domeny smoka, często uznawani za kultystów, potrafią czerpać ze smoczej mocy i przybierać smocze cechy, by władać przerażającą magią żywiołów i roztaczać budzący grozę majestat pradawnego smoka.\n\nDo głównych bóstw Domeny smoka należą Tiamat, pięciogłowa matka smoków chromatycznych, oraz Bahamut, sprawiedliwy i mądry bóg smoków metalicznych.')
add(5369,'Poziom 3: Chromatyczne powinowactwo')
choice='Po każdym ukończeniu długiego odpoczynku wybierz kwas, zimno, ogień, elektryczność lub truciznę.'
damage='Raz na turę, gdy zadajesz obrażenia istocie, możesz zadać jej dodatkowe obrażenia wybranego typu w liczbie równej twojemu poziomowi kleryka.'
uses='Możesz zadawać te dodatkowe obrażenia tyle razy, ile wynosi twój modyfikator Mądrości (co najmniej raz). Wszystkie zużyte użycia odzyskujesz po ukończeniu długiego odpoczynku.'
add(5370,choice+' '+damage+' '+uses)
add(5371,'Poziom 3: Czary Domeny smoka')
add(5372,'Więź z tą boską domeną sprawia, że zawsze masz przygotowane określone czary. Po osiągnięciu poziomu kleryka wskazanego w tabeli Czarów Domeny smoka zawsze masz przygotowane wymienione w niej czary: na 3. poziomie — Barwna kula, Rozkaz, Widzenie w ciemności i Smocze zionięcie; na 5. poziomie — Lot i Ochrona przed energią; na 7. poziomie — Wypędzenie i Zauroczenie potwora; a na 9. poziomie — Dominacja nad osobą i Szum synaptyczny.')
add(5373,'Poziom 3: Smoczy majestat')
add(5374,'W ramach akcji Magii możesz unieść święty symbol i zużyć jedno użycie Aktu wiary, aby roztoczyć wokół siebie aurę smoczej władzy w emanacji o promieniu 30 stóp. Wybierz stan zauroczenia lub przerażenia. Każda wybrana przez ciebie istota w emanacji musi wykonać udany rzut obronny na Mądrość albo otrzyma wybrany stan na 1 minutę. Istota zauroczona lub przerażona przez tę cechę ponawia rzut obronny na Mądrość na koniec każdej swojej tury. Przy powodzeniu stan się kończy.')
add(5375,'Poziom 6: Błogosławieństwo smoka')
add(5376,'Możesz zużyć jedno użycie Aktu wiary, aby rzucić na siebie Smocze zionięcie lub Ochronę przed energią bez zużywania komórki czaru. Czar rzucony w ten sposób nie wymaga koncentracji. Kończy się wcześniej, jeśli rzucisz ponownie ten sam czar, zostaniesz obezwładniony albo umrzesz.')
add(5377,'Chromatyczne powinowactwo')
add(5379,choice+' '+damage)
add(5380,uses)
for i,n in enumerate(['Kwas','Zimno','Ogień','Elektryczność','Trucizna'],5381): add(i,'Chromatyczne powinowactwo: '+n)
add(5387,damage+' '+uses)
add(5389,'Możesz zadać tej istocie dodatkowe obrażenia wybranego typu w liczbie równej twojemu poziomowi kleryka.')
add(5394,'Smoczy majestat')
add(5396,'Smoczy majestat: Zauroczenie')
add(5397,'Smoczy majestat: Strach')
add(5400,'Smocze zionięcie (Błogosławieństwo smoka)')
add(5401,'Ochrona przed energią (Błogosławieństwo smoka)')
add(5402,'Zwój magicznego oka')
add(5403,'Dostępne klasy: Wynalazca, Mag')
out={r['uid']:T[r['en']] for r in rows if r['index']<=5403}
assert len(out)==51
(W/'root-translations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Wrote {len(out)} translations')
