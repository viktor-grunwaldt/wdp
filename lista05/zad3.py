from duze_cyfry import daj_cyfre
import turtle as t
import random
import numpy as np

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def kwadrat(x, y, bok, kolor):
    move(x, y)
    t.begin_fill()
    t.fillcolor(*kolor)
    for i in range(4):
        t.fd(bok)
        t.rt(90)
    t.end_fill()


def rect(x, y, bok1, bok2, kolor):
    move(x, y)
    t.begin_fill()
    t.fillcolor(kolor)
    for bok in [bok1, bok2] * 2:
        t.fd(bok)
        t.rt(90)
    t.end_fill()


# t.speed("fastest")
t.tracer(0, 0)

# t.colormode(255)
# kwadrat(-200, -200, 50, (128, 0, 0))

edge_len = 50
length = -(edge_len * 10)
height = -(edge_len * 5)
x_begin = -300
y_begin = 200
proportion = 8 / 16

# def dlc_oneliner(n: int) -> str:
#     return "\n".join(
#         "  ".join(
#             daj_cyfre(int(digit))[i]
#             for digit in str(n))
#         for i in range(5))
# lista
#     .chars()
#     .map(int)
#     .map(daj_cyfre)
#     .map(itemgetter(i))
#     .collect()


# [[[    ]  [[     ]
#   [    ]   [     ]
#   [    ]], [     ]], ...]
# chcemy zamienić na:
# [[                 ],
#  [                 ],
#  [                 ]]
# ta operacja nazywa się transpozycją
# zip(*zagnieżdżona_lista)
def dlc_but_with_transpositions(number: int) -> str:
    # wczytujemy cyfry potrzebne do narysowania
    digits = map(daj_cyfre, map(int, str(number)))
    # łączymy wiersze każdej cyfry jako do jednego
    return "\n".join(map("  ".join, zip(*digits)))


def draw_number(num: int):
    grid = dlc_but_with_transpositions(num)
    # CoLoRs
    w = 5 + 2  # dlc w + space w
    np.random.random(3)
    colors = [[random.uniform(0, 1) for _ in range(3)] for _ in range(w)]

    for y, line in enumerate(grid.splitlines()):
        for x, c in enumerate(line):
            y_abs = y_begin - y * edge_len
            x_abs = x_begin + x * edge_len * proportion
            if c == "#":
                rect(x_abs, y_abs, edge_len * proportion, edge_len, colors[x//w])


draw_number(1337)
t.update()
t.mainloop()
