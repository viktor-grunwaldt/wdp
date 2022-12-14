alpha = "aąbcćdeęfghijklłmnńoóprsśtuwyzź"


def ceasar(word, shift, decode=False):
    if decode:
        shift *= -1
    shifter = str.maketrans(alpha, alpha[shift:] + alpha[:shift])
    
    return word.translate(shifter)

msg = ceasar("witam, cześć i czołem", 4)
print(msg)
print(ceasar(msg, 4, decode=True))