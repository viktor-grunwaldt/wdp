# def krzyzyk3(n: int) -> str:
#     return '\n'.join(
#         ''.join('*' if ((i//n)*3 + j//n) % 2 == 1 # nieparzyste pola
#                     or ((i//n)*3 + j//n)     == 4 # środek
#                     else ' '
#                 for j in range(3*n))
#         for i in range(3*n)
#     )


# pattern szachownicy osiągniemy sprawdzjąc mod 2 sumy i + j
def szachownica_gen(n: int, k: int) -> str:
    return '\n'.join(
        ''.join(('#'
                 if (i//k + j//k) % 2 == 1
                 else ' ')
                for j in range(k * n * 2))
        for i in range(k * n * 2)
    )


show_szachownica = lambda n, k: print(szachownica_gen(n, k))
szachownica = lambda f, *n: print(f(*n))


szachownica(szachownica_gen, 4, 3)
print("*"*40)
show_szachownica(4, 3)
print("*"*40)
show_szachownica(8, 1)
