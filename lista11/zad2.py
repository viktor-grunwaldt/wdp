def pnn(word: str) -> str:
    alfa = dict()
    sol = []
    for letter in word:
        pos = alfa.get(letter)
        if pos is None:
            pos = len(alfa) + 1
            alfa[letter] = pos

        sol.append(pos)

    return "-".join(map(str, sol))


print(pnn("indianin"))
