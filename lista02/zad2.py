def koperta(n:int) -> str:
    img = ""
    for i in range(2*n+1):
        for j in range(2*n+1):
            img += '*' if (
                       i*j  == 0       # góra + lewo
                    or i    == j       # skos z góry
                    or j+i  == 2*n     # skos z dołu
                    or i    == 2*n     # dół
                    or j    == 2*n     # prawo
                    ) else ' '
        img += '\n'
    return img


show_koperta = lambda n: print(koperta(n))
show_koperta(5)
show_koperta(10)
show_koperta(1)
show_koperta(0)
# print(koperta(5))
# print(koperta(10))
