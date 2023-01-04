# Wprawka nr 7 (PLG)

Pobierz plik umieszczony w SKOS obok tego modułu. Składa się on z wierszy takiej postaci:

3.1958;15937;Rozejście szlaków;15943;Kotuszów;jacobs_trail_None
0.0768;5804;Slavný, rozc.;5799;Slavný;hiking_trail_yellow;hiking_trail_blue

tj. zawierających (oddzielone średnikami) kolejno długość, numer i nazwę punktu początkowego, numer i nazwę punktu końcowego, oraz nazwy szlaków turystycznych (co najmniej jednego), którymi oznakowany jest dany odcinek. Nazwy są niepuste i nie zawierają średników, numery punktów są liczbami całkowitymi, długości i nazwy punktów nie mają znaczenia w tym zadaniu.

Każdy ze szlaków turystycznych (np. hiking_trail_blue) będziemy traktować jako osobny graf i dla każdego z nich należy policzyć liczbę spójnych składowych. (Spójna składowa grafu to każdy z jego maksymalnych spójnych podgrafów. Graf spójny to taki, w którym istnieje połączenie, niekoniecznie bezpośrednie, pomiędzy dowolną parą jego wierzchołków.) Grafy te mają wspólny zbiór wierzchołków (numerów punktów), ale np. jeśli wierzchołki leżące na dwóch "osobnych kawałkach" szlaku zielonego połączone są odcinkiem oznakowanym szlakiem czarnym, to w grafie dla szlaku zielonego pozostają w różnych spójnych składowych.

Do liczby spójnych składowych nie należy wliczać wierzchołków izolowanych, tj. jeśli do jakiegoś punktu nie dochodzi szlak żółty, to nie liczy się on (w tym zadaniu) jako spójna składowa grafu tego szlaku. Program powinien wczytać ww. plik i wypisać w kolejnych wierszach nazwy szlaków oraz liczby spójnych składowych ich grafów. Dzięki dostępnym w Pythonie strukturom danych (i nie tak dużego rozmiaru danych wejściowych) nietrudno napisać rozwiązanie nie wykorzystujące algorytmów grafowych, które zwróci wynik w nieco ponad 10 sekund.

- Za rozwiązanie tylko dla szlaku czerwonego (hiking_trail_red) można dostać 1 p.
- Za rozwiązanie dla wszystkich rodzajów szlaków, które ma zapisane w kodzie ich nazwy (albo czyta plik dwa razy, w tym pierwszy raz po to, żeby te nazwy pobrać), można dostać 1½ p.
- Za rozwiązanie dla wszystkich rodzajów szlaków, które czyta plik tylko raz linia po linii i w ten sposób "dowiaduje się" również o istniejących rodzajach, można dostać komplet punktów.

Rodzajów szlaków w ww. pliku jest 18, liczba spójnych składowych dla szlaku czerwonego to 208, a dla szlaku św. Jakuba – 48.

Wskazówka: wstępne wersje rozwiązania może być warto testować na pliku przyciętym do kilkuset linii na wypadek, gdyby jego złożoność miała okazać się kiepska. Nie jest konieczne korzystanie z bibliotek do odczytu plików CSV (ani żadnych innych), zwłaszcza że liczba pól w wierszu pliku jest zmienna. Jak zawsze, w razie wątpliwości nie wahaj się pytać prowadzącego.
