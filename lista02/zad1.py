# def krzyzyk3(n: int) -> str:
#     return '\n'.join(
#         ''.join('*' if ((i//n)*3 + j//n) % 2 == 1 # nieparzyste pola
#                     or ((i//n)*3 + j//n)     == 4 # środek
#                     else ' '
#                 for j in range(3*n))
#         for i in range(3*n)
#     )


# pattern szachownicy osiągniemy sprawdzjąc mod 2 sumy i j
def szachownica(n:int, k:int) -> str:
    return '\n'.join(
        ''.join('#' if (i//k + j//k)%2 == 1
                    else ' '
                for j in range(k*n*2))
        for i in range(k*n*2)
    )
    
print(szachownica(4,3))