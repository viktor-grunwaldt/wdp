
### Wprawka nr 1 (PLG)

Napisz funkcję, która przyjmie dwa argumenty – liczbę naturalną n ≥ 0 oraz napis s składający się z dwóch znaków. Efektem jej działania powinno być wypisanie na standardowe wyjście napisu w formie kwadratu o boku n (tj. składającego się z n wierszy po n znaków każdy) wypełnionego koncentrycznymi brzegami kwadratów złożonych naprzemiennie ze znaków napisu s. Efekty przykładowych wywołań takiej funkcji wyglądają tak:

```txt
>>> kwadkonc(3, "*.")
***
*.*
***
>>> kwadkonc(8, "#_")

########
#______#
#_####_#
#_#__#_#
#_#__#_#
#_####_#
#______#
########
```

Dla argumentów niespełniających specyfikacji (np. n < 0 bądź s niewłaściwej długości) działanie funkcji może oczywiście być dowolne.

Uwaga: ½ punktu z 2 do zdobycia za tę wprawkę będzie przyznawane za użycie "czegoś Pythonowego" w rozwiązaniu, np. wyrażeń "arytmetycznych" z napisami, list comprehension itp.
Last modified: Wednesday, 9 November 2022, 1:04 PM
