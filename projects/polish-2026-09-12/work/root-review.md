# Niezależna wyczytka 51 wpisów root-translations.json

Przeczytano i porównano z angielskim źródłem 51 wpisów: 2 aktualizacje Durable oraz nowe wpisy 5355–5403. JSON ma komplet oczekiwanych identyfikatorów; nie ma pustych tłumaczeń; identyczne opisy angielskie mają identyczny polski przekład. Pliku tłumaczeń nie zmieniano.

## Wymagana poprawka terminologii

**Lightning jako typ obrażeń powinno mieć oficjalną nazwę `Elektryczność`, a nie `Błyskawice`.** W sprawdzonych korpusach BG3 EN/PL odpowiadają sobie:

- h647de1eege687g4fe6g83dbg732e1c6e117b: `Lightning` → `Elektryczność`;
- h95295c6ag8609g4964g80b8g6caa0b15678a: `Lightning` → `Elektryczność`;
- hc3cd9b4eg4ea4g4438gbfbbg493c0abb6dd7_8: `Lightning` → `Elektryczność`.

Wpisy do poprawienia:

| Indeks | UID | Zmiana |
| --- | --- | --- |
| 5370 | hc78a280cge0f8gaed4gabceg8275d4b016b4 | `błyskawice` → `elektryczność` |
| 5379 | hf814f210g333ag4aeag5f87g929a9260c5cb | `błyskawice` → `elektryczność` |
| 5384 | he8275a17g6f90ge548g0527g7eb734361d44 | `Błyskawice` → `Elektryczność` |
| 5392 | hf56293bcgbef0g670dgdc2cgaafbafce938b | `Błyskawice` → `Elektryczność` |

Korpusy: `C:/Users/coldb/Documents/Codex/2026-08-24/new-chat/work/official_bg3_english_20260828/english.loca.xml` i `C:/Users/coldb/Documents/Codex/2026-08-24/new-chat/work/official_bg3_polish_20260828/polish.loca.xml`. Zalecenie wynika z odczytu rzeczywistych par contentuid, zgodnie z pierwszeństwem oficjalnej lokalizacji BG3.

## Kontrola mechanik i języka

- **Durable / Szybka regeneracja:** zachowano ułatwienie w rzutach przeciwko śmierci. Leczenie wymaga akcji dodatkowej i wydania jednej kości wytrzymałości; przywraca liczbę PW równą wynikowi rzutu, bez starego maksymalnego leczenia. Rozmiary kości k6/k8/k10/k12 są prawidłowe.
- **Charm Monster:** jedna widoczna istota w zasięgu; rzut na Mądrość; ułatwienie, gdy rzucający lub sojusznicy walczą z celem. Zauroczenie kończy się z końcem czaru albo po obrażeniach od rzucającego/sojuszników. `Przyjaźnie nastawiona` dokładnie oddaje relację Friendly i nie obiecuje posłuszeństwa ani przejścia pod kontrolę gracza. Zachowano wiedzę celu o zauroczeniu po zakończeniu czaru.
- **Chromatyczne powinowactwo:** wybór po każdym długim odpoczynku; dodatkowe obrażenia raz na turę; wartość równa poziomowi kleryka; limit użyć równy modyfikatorowi Mądrości, minimum jedno; pełne odnowienie po długim odpoczynku. Po wskazanej poprawce nazwy typu obrażeń brak zastrzeżeń.
- **Czary domeny:** zachowano poziomy 3/5/7/9, wszystkie pary/czwórkę czarów i stałe przygotowanie po osiągnięciu odpowiedniego poziomu.
- **Smoczy majestat:** akcja Magii, święty symbol, jedno użycie Aktu wiary, emanacja wokół rzucającego o promieniu 30 stóp, wybór zauroczenia lub przerażenia, wybrane istoty, Mądrość, 1 minuta, ponowny rzut na koniec każdej własnej tury. Sukces kończy stan u istoty wykonującej rzut. Nie dodano wymogu koncentracji.
- **Błogosławieństwo smoka:** oba czary są rzucane na siebie, zużywają użycie Aktu wiary zamiast komórki, nie wymagają koncentracji. Zachowano wszystkie trzy przesłanki wcześniejszego zakończenia: ponowne rzucenie tego samego czaru, obezwładnienie, śmierć. Zapis `ten sam czar` trafnie zachowuje odniesienie angielskiego `that spell`, bez rozszerzenia na dowolny czar.
- **Nazwy i zwoje:** spójne z przekazanymi ustaleniami terminologicznymi; `Strach` potwierdza oficjalny korpus (h6f38a9b4gc4deg4318g9f6cg4d073b48bde2 i hf774105fgf2cbg4efdgb3c7gf1b924357c86).

Poza czterema wystąpieniami nazwy Lightning nie znaleziono wymagających poprawki błędów znaczenia, warunków działania lub polszczyzny. Jednostkę `30 stóp` zachowano dosłownie zgodnie z bieżącym angielskim źródłem; w tym przeglądzie nie zmieniano przyjętej polityki jednostek.
