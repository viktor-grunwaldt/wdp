def koperta(n:int)-> str:
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
        img+='\n'
    
    return img

print(koperta(5), end='')