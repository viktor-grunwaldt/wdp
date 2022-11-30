from itertools import cycle, islice
import turtle as t
from string import digits

colors = [
    "red",  # 0
    "orange",  # 1
    "yellow",  # 2
    "green",  # 3
    "blue",  # 4
    "purple",  # 5
    "brown",  # 6
    "black",  # 7
    "white",  # 8
]


def kwadrat(bok):
    t.begin_fill()
    for i in range(4):
        t.fd(bok)
        t.rt(90)
    t.end_fill()


def murek(s, bok):
    for a in s:
        match a:
            case "f":
                kwadrat(bok)
                t.fd(bok)
            case "b":
                kwadrat(bok)
                t.fd(bok)
            case "l":
                t.bk(bok)
                t.lt(90)
            case "r":
                t.rt(90)
                t.fd(bok)
            case c:
                if c in digits:
                    t.color("black", colors[int(c)])
                else:
                    raise Exception("illegal argument: ", c)


t.ht()

t.tracer(0, 0)  # szybkie rysowanie
# examples
# murek("💛fffffffffrffffff🧡fffflfffffffffrfffffl", 10)
# murek("2fffffffffrffffff3fffflfffffffffrfffffl", 10)
# murek(4 * "fffffr", 14)


def compile_square(edge_len: int, sq_colors: tuple[int, int, int, int]) -> str:
    # fffffrfrfffflfl
    turns = enumerate(islice(cycle(("rfr", "lfl")), edge_len))
    row = lambda i, t : f'{sq_colors[i % 4]}{(edge_len - 1) * "f"}{t}'

    return str(sq_colors[-1]) + "f" + "".join(row(i, t) for i, t in turns)[:-2]


def compile_spiral(rotations: int, sq_colors: tuple[str]) -> str:
    assert all(c in range(9) for c in sq_colors)

    iterator = enumerate(islice(cycle(sq_colors), rotations))
    return "r".join(str(c) + "f" * (i + 1) for i, c in iterator)


sq = compile_square(10, (2, 4) * 2)
print(sq)
murek(sq, 20)

t.goto(-300, 300)
spiral = compile_spiral(10, (0, 1, 2, 3, 4, 5))
print(spiral)
murek(spiral, 15)

t.update()
t.mainloop()
