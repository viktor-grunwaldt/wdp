
# Wprawka nr 4 (PLG)

Napisz następujące funkcje, które przyjmą dodatni całkowity argument n:

* isprime, która zwróci wartość logiczną zdania "n jest pierwsza";
* isperfect, która zwróci wartość logiczną zdania "n jest doskonała" (liczby doskonałe są równe sumie     * swoich dzielników z wyjątkiem samych siebie, np. 6 = 1 + 2 + 3);
* totient, która zwróci wartość funkcji φ Eulera, zdefiniowanej jako moc zbioru { m ∈ {1, 2, …, n} | m i n są względnie pierwsze };
* catheti, która zwróci listę długości krótszych przyprostokątnych trójkątów pitagorejskich (tj. trójkątów prostokątnych o bokach całkowitych) o przeciwprostokątnej n.

Funkcje powinny być (a isprime – musi być) zaimplementowane jako "jednolinijkowce", tj. zawierać tylko jedną instrukcję `return <wyrażenie>`, choć możesz zaimplementować (albo zaimportować z modułu math) inne funkcje pomocnicze, jeśli ich potrzebujesz. Prawdopodobnie będzie to wymagać list comprehension (także w "filtrującym" wariancie `[ … for … in … if … ]`) bądź podobnej konstrukcji. Przydatne mogą być też takie funkcje wbudowane jak `sum, any, all` bądź wyrażenia warunkowe `<wyr1> if <warunek> else <wyr2>`. Nie wahaj się pytać prowadzącego o wskazówki!
