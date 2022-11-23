# Wprawka nr 3 (PLG)

Dowiedz się, jak wyglądają znaki alfabetu Braille'a dla liter alfabetu łacińskiego, cyfr i spacji (inne znaki będziemy pomijać). Napisz funkcję, która przyjmie jako argument napis i przy użyciu modułu turtle narysuje na ekranie (w pozycji związanej albo z bieżącą pozycją żółwia, albo z podaną w kolejnych argumentach – do Twojego wyboru) jego odpowiednik w alfabecie Braille'a.

Postaraj się, aby Twój kod był maksymalnie przejrzysty i w miarę zwięzły; w tym celu np. odpowiednio podziel go na funkcje pomocnicze. Oczywiście możesz używać kodu napisanego w rozwiązaniach zadań z list, w których pojawiały się podobne elementy.

Wskazówka: zamiast instrukcji if o 37 rozgałęzieniach lepiej użyć słownika o 37 kluczach; zamiast wpisywać słownik o 37 kluczach w całości ręcznie do kodu programu, lepiej wpisać ręcznie słownik / listę długości 10, a resztę wygenerować proceduralnie. Przydatna może się okazać także funkcja ord lub słownik(i) konstruowane np. tak:

```py
import string
alph_pos = { c: i for i, c in enumerate(string.ascii_lowercase) }
```
