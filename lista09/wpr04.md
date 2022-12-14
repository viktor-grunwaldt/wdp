We wprawce są różne 'podzadania', za których punkty dodają się.

Będziemy pisać symulator rozgrywek grupowych w mistrzostwach piłki nożnej. Zakładamy, że:

    każda drużyna ma potencjał obronny (D) i potencjał ofensywny (O), siłę bramkarza (B, od 0 do 1) i bramkostrzelność (G, od 0 do 1)
    w danym meczu dla drużyny obliczamy siłę obrony FD dodając do potencjału defensywnego rzut kostką
    w danym meczu dla drużyny obliczamy siłę ataku FA dodając do potencjału defensywnego rzut kostką
    jeżeli FA > FD drużyna ma FA-FD okazji strzeleckich
    okazja strzelecka rozwiązywana jest następująco: losujemy liczbę rzeczywistą b należącą do [0,B], oraz g, należącą do [0,G]. Jeżeli g > b to jest gol

Uwaga: liczbę rzeczywistą od 0 do 1 można losować wywołując funkcję random.random()


Drużynę w Pythonie będziemy reprezentować jako krotkę. Napisz funkcję: mecz(A, B), która symuluje mecz pomiędzy drużyną A i B i zwraca parę liczb: (gole-strzelone-przez-A) oraz (gole-strzelone-przez-B). (0.5) Wykorzystaj tę funkcję do obliczenia prawdopodobieństwa zwycięstwa Polski nad Argentyną. (0.2)

Możesz wykorzystać poniższy kod:

arabia = ('Arabia_Saudyjska', 2, 3, 0.3, 0.3)
argentyna = ('Argentyna', 4, 6, 0.5, 0.8)
meksyk = ('Meksyk', 3, 4, 0.6, 0.5) 
polska = ('Polska', 2, 3, 0.9, 0.8)

grupa = [arabia, argentyna, meksyk, polska]


Przeprowadź rozgrywki grupowe (każdy z każdym), za pomocą funkcji rozgrywki_grupowe(lista_drużyn, czy_wypisywać_wyniki). Funkcja powinna wypisywać wyniki wszystkich meczów (jeżeli drugi parametr jest równy True) [0.3p], oraz zwracać listę drużyn w kolejności od najlepszej, do najgorszej (zasady można uprościć: uwzględniamy tylko punkty oraz bilans bramek . Jeżeli nie dają one rozstrzygnięcia przeprowadzamy losowanie (0.7p) [UWAGA: jest prosty trick, który bardzo upraszcza kod związany z losowaniem -- zastanów się, jaki]

Wykorzystaj kod do oszacowania prawdopodobieństwa tego, że Polska będzie na pierwszym bądź drugim miejscu. [0.25p]
0.03 p jest dla osoby, która jedno z wymienionych prawdopodobieństw poda jako pierwsza