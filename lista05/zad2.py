from copy import deepcopy
import turtle as t


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


def kwadrat_srodek(x, y, bok, kolor):
    move(x - bok // 2, y + bok // 2)
    kwadrat(x - bok // 2, y + bok // 2, bok, kolor)
    move(x, y)


def kw_rek(x, y, bok, kolory):
    k = next(kolory, None)
    if not k:
        return

    kwadrat_srodek(x, y, bok, k)
    bok //= 2
    for a, b in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        l = x + a * bok * 3 // 2
        r = y + b * bok * 3 // 2
        kw_rek(l, r, bok, deepcopy(kolory))


kolory = iter((
    "black",
    "blue",
    "yellow",
    "lime",
    "red",
))
t.speed("fastest")
kw_rek(0, 0, 200, kolory)
t.mainloop()
