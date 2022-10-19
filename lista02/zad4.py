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


print(dlc(123), end="")
print(dlc(2137), end="")
