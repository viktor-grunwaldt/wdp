# pattern szachownicy osiągniemy sprawdzjąc mod 2 sumy i + j
# gdzie i, j są współrzędnymi
def szachownica_gen(n: int, k: int) -> str:
    return '\n'.join(
        ''.join(('#'
                 if (i//k + j//k) % 2 == 1
                 else ' ')
                for j in range(k * n * 2))
        for i in range(k * n * 2)
    )


szachownica = lambda n, k: print(szachownica_gen(n, k))


szachownica(4, 3)
print("*"*40)
szachownica(8, 1)
