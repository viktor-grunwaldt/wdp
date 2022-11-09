from colorsys import hls_to_rgb
import turtle as t
import random


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def kwadrat(x, y, bok, kolor):
    move(x, y)
    t.begin_fill()
    t.fillcolor(kolor)
    for i in range(4):
        t.fd(bok)
        t.rt(90)
    t.end_fill()


# t.speed("fastest")
t.tracer(0, 0)

# t.colormode(255)
# kwadrat(-200, -200, 50, (128, 0, 0))

chunk_size = 5
grid_size = 4
edge_len = 20
x = -(edge_len * 10)
y = -(edge_len * 5)


def szachownica_gen(n: int, k: int) -> list[list[bool]]:
    return [[(i // k + j // k) % 2 == 1 for j in range(k * n)] for i in range(k * n)]


pattern = szachownica_gen(grid_size, chunk_size)


def color_maker(brightness: bool):
    """generates bright/dark hls and then converts to rgb"""
    h = random.uniform(0.0, 1.0)
    l = random.uniform(0.1, 0.4) + (0.5 if brightness else 0.0)
    s = random.uniform(0.5, 1.0)
    return hls_to_rgb(h, l, s)


for i, row in enumerate(pattern):
    for j, elem in enumerate(row):
        kwadrat(x + j * edge_len, y + i * edge_len, edge_len, color_maker(elem))
        # t.update()


t.update()
t.mainloop()
