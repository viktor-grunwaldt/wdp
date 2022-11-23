def find_reverses(data: list[str]) -> list[tuple[str]]:
    sol = []
    visited = set()
    for word in data:
        if word[::-1] in visited and word not in visited:
            sol.append((word, word[::-1]))
        visited.add(word)

    return sol


with open("popularne_slowa.txt", 'r') as f:
    sol = find_reverses(map(str.strip, f.readlines()))
    print(len(sol))
