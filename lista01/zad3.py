krzyz = [
    [' ', '*', ' '],
    ['*', '*', '*'],
    [' ', '*', ' '],
]


def krzyzyk(n: int) -> str:
    img = ""
    assert n >= 1
    for i in range(3*n):
        for j in range(3*n):
            img += krzyz[i//n][j//n]

        img += '\n'

    return img


def krzyzyk2(n: int) -> str:
    return '\n'.join(
        ''.join(krzyz[i//n][j//n]
                for j in range(3*n))
        for i in range(3*n)
    )


def krzyzyk3(n: int) -> str:
    return '\n'.join(
        ''.join('*' if ((i//n)*3 + j//n) % 2 == 1 # nieparzyste pola
                    or ((i//n)*3 + j//n)     == 4 # środek
                    else ' '
                for j in range(3*n))
        for i in range(3*n)
    )


print(krzyzyk3(4))
