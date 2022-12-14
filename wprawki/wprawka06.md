# Wprawka nr 6 (PLG)

Skopiuj poniższą treść, wklej do edytora tekstu, i zapisz ją w swoim systemie plików:

uk:абвгґд еєжз иіїйкл мн опрст у фхцч шщь   юя
ru:абвг д еёжз и  йкл мн опрст у фхцч шщъыьэюя
be:абвг д еёжз  і йкл мн опрст уўфхцч ш  ыьэюя
bg:абвг д е жз и  йкл мн опрст у фхцч шщъ ь юя
sh:абвг дђе жз и  јклљмнњопрстћу фхцчџш
mk:абвг дѓе жзѕи  јклљмнњопрстќу фхцчџш

Upewnij się, że plik został zapisany poprawnie – użyty przez Ciebie edytor powinien korzystać (czy przynajmniej mieć taką możliwość) z odpowiedniego kodowania, np. UTF-8 (dobry jest np. "Edytor tekstu" dostępny na pracownianych Linuxach).

Napisz program, który:

    otworzy i przeczyta plik o zawartości takiej, jak powyższa, tj. którego każdy wiersz (możesz założyć, że jakieś są) będzie składać się z:
        sekwencji znaków innych niż dwukropek (stanowiącej identyfikator, np. kod ISO 639-1, jakiegoś języka), możesz założyć, że identyfikatory nie będą się powtarzać w obrębie pliku;
        dwukropka,
        sekwencji znaków systemu pisma (alfabetu, abdżadu, pisma logograficznego itp.) wykorzystywanego w danym języku (mogą się tu też pojawiać spacje, które należy pomijać), możesz założyć, że znaki (poza spacjami) nie powtarzają się w obrębie linii, i że nie ma wśród nich dwukropka;
    na podstawie wczytanych danych wypisze na standardowe wyjście wiersze, z których każdy będzie składać się z:
        identyfikatorów języków porozdzielanych spacjami,
        dwukropka,
        niepustego napisu składającego się z wszystkich znaków systemów pisma wykorzystywanych w dokładnie tych językach, które pojawiły się w tym wierszu przed dwukropkiem.

W szczególności: w pliku z danymi oraz na standardowym wyjściu na prawo od dwukropka będą pojawiać się te same znaki, ale na standardowym wyjściu nie mogą się one powtarzać. Wiersze wyjścia powinny zostać wypisane w kolejności od najliczniejszego zbioru języków ("przed dwukropkiem") do najmniej licznego. Nazwa pliku z danymi nie powinna być umieszczona na stałe w kodzie programu, tylko odczytywana z argumentu wywołania (odróżnij od standardowego wejścia; jeśli nie było tego na wykładzie, to dowiedz się o liście argv z modułu sys). Brak argumentów wywołania bądź błąd odczytu pliku powinny być sygnalizowane czytelnym komunikatem (a nie np. niezłapanym wyjątkiem).

Przykładowe wyjście dla powyższych danych wygląda tak:

be bg mk ru sh uk:абвгдежзклмнопрстуфхцчш
bg mk ru sh uk:и
be bg ru uk:йьюя
bg ru uk:щ
be ru:ёыэ
be uk:і
bg ru:ъ
mk sh:јљњџ
be:ў
mk:ѓѕќ
sh:ђћ
uk:ґєї

Komentarze do treści niewpływające na rozwiązanie zadania:

    Pojęcie "systemu pisma wykorzystywanego w danym języku" nie jest jednoznaczne – choćby uwzględniony w przykładowych danych serbsko-chorwacki może być zapisywany przy użyciu cyrylicy (jw.) bądź łacinki.
    Przykładowe dane w intencji uwzględniają wszystkie języki słowiańskie zapisywane przy użyciu cyrylicy, ale pomijają język rusiński ze względu na jego liczniejsze warianty, także różniące się nieco alfabetami (przy czym nie pojawiają się w nich żadne znaki nie wykorzystywane w innych językach wschodniosłowiańskich).
    Odrębność i nazewnictwo języków bywa kwestią debaty naukowej, a nawet politycznej. Być może w tym zadaniu powinien zamiast języka serbsko-chorwackiego pojawić się serbski, bo to w nim dominującym systemem pisma jest cyrylica – w przeciwieństwie do chorwackiego (w którym właściwie nie jest stosowana), bośniackiego i czarnogórskiego…
    … w którym w 2009 wprowadzono dwa znaki niewystępujące w innych wariantach cyrylicy, ale nie doczekały się one (jeszcze?) uwzględnienia w Unicode, muszą być reprezentowane przy użyciu dodatkowego znaku (akcent ostry dostawny) i dla uproszczenia zadania zostały w nim pominięte. W łacince są to znajomo wyglądające "Ś" i "Ź".
