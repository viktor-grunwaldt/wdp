def kolo(n: int, padding: int = 0) -> list[str]:
    img = []
    d = 2 * n + 1
    for i in range(1, d - 2):
        row = ""
        for j in range(1, d - 2):
            # nierówność koła : (x-a)^2 + (y-b)^2 <= r^2
            row += "#" if (i - n) ** 2 + (j - n) ** 2 < (n - 1) ** 2 else " "
        img.append(" " * padding + row)

    return img


def bauwan(a: int, b: int):
    for i in range(a, b):
        k = kolo(i, (b - i))

        for line in k:
            if '#' in line:
                print(line)


bauwan(5, 8)
bauwan(15, 17)
