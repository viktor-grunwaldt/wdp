# rozm DLC = 5x5 + 2 spacji
from duze_cyfry import daj_cyfre


def dlc(n: int) -> str:
    num = str(n)
    count_of_digits = len(num)
    img = ""
    for i in range(5):
        # 7 kratek na miejsce: 5 dla wiersza liczby i 2 spacji
        # ostatnie 2 kolumny spacji są pomijane przez - 2
        for j in range(7 * count_of_digits - 2):
            if j % 7 < 5:
                pole_cyfry = int(num[j // 7])
                img += daj_cyfre(pole_cyfry)[i][j % 7]
            else:
                img += " "
        img += "\n"

    return img


def dlc_simple(n: int) -> str:
    num = str(n)
    count_of_digits = len(num)
    img = ""
    for i in range(5):
        # 7 kratek na miejsce: 5 dla wiersza liczby i 2 spacji
        # ostatnie 2 kolumny spacji są pomijane przez - 2
        for j in range(count_of_digits):
            img += daj_cyfre(j)[i] + "  "
        img += "\n"

    return img

##################################


def dlc_oneliner(n: int) -> str:
    return "\n".join(
        "  ".join(
            daj_cyfre(int(digit))[i]
            for digit in str(n))
        for i in range(5))


# lista
#     .chars()
#     .map(int)
#     .map(daj_cyfre)
#     .map(itemgetter(i))
#     .collect()


# [[[    ]  [[     ]
#   [    ]   [     ]
#   [    ]], [     ]], ...]
# chcemy zamienić na:
# [[                 ],
#  [                 ],
#  [                 ]]
# ta operacja nazywa się transpozycją
# zip(*zagnieżdżona_lista)
def dlc_but_with_transpositions(number: int) -> str:
    # wczytujemy cyfry potrzebne do narysowania
    digits = map(daj_cyfre, map(int, str(number)))
    # łączymy wiersze każdej cyfry jako do jednego
    return "\n".join(map("  ".join, zip(*digits)))


print(dlc(123))
print(dlc_oneliner(2137))
print(dlc_but_with_transpositions(4242))
