from itertools import repeat
from operator import itemgetter
from random import randrange
import turtle as t

from more_itertools import flatten
from duze_cyfry import daj_cyfre


def move(x, y):
    t.penup()
    t.goto(x, y)


def square(x, y, bok, kolor):
    move(x, y)
    if kolor != "white":
        t.pendown()
    t.begin_fill()
    t.fillcolor(kolor)
    for i in range(4):
        t.fd(bok)
        t.rt(90)
    t.end_fill()


canvas = t.Screen()
window_size = 1000
canvas.setup(window_size, window_size)
canvas.title("Polnareff")
t.tracer(0, 1)

edge_len = 20
dlc_len = 5
x_begin = -500
y_begin = 500
size = window_size // edge_len
# proportion = 8 / 16
NEIGH = ((1, 0), (0, 1), (-1, 0), (0, -1))


def move_points_by_vec(vec: tuple[int], pts):
    return map(lambda x: (x[0] + vec[0], x[1] + vec[1]), pts)


def dlc_to_points(num: int):
    return ((j, i) for j, row in enumerate(daj_cyfre(num)) for i, c in enumerate(row) if c == "#")


def create_mosaic(num: int, size: int, colors: list[str]) -> list[list[None | str]]:
    grid = [[None] * size for _ in range(size)]
    for c in flatten(repeat(colors, num)):
        collision = True
        digit_points = []
        while collision:
            x = randrange(0, size - dlc_len)
            y = randrange(0, size - dlc_len)
            digit = randrange(0, 10)
            digit_points = list(move_points_by_vec((x, y), dlc_to_points(digit)))
            if not any(
                grid[i][j] is not None or any(grid[i + dx][j + dy] == c for dx, dy in NEIGH)
                for i, j in digit_points
            ):
                collision = False

        for i, j in digit_points:
            grid[i][j] = c

    return grid


def draw_mosaic(grid: list[list[None | str]]):
    for y, row in enumerate(grid):
        for x, c in filter(itemgetter(1), enumerate(row)):
            y_abs = y_begin - y * edge_len
            x_abs = x_begin + x * edge_len
            square(x_abs, y_abs, edge_len, c)
            t.update()


grid = create_mosaic(7, size, ["red", "green", "blue", "yellow", "magenta"])

draw_mosaic(grid)

t.mainloop()
