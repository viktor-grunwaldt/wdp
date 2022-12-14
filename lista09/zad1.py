import turtle as t


def trojkat(edge):
    # h = t.heading()
    # t.setheading(0)
    t.begin_fill()
    # t.circle(edge, steps=3)
    for _ in range(3):
        t.forward(edge)
        t.left(120)
    t.end_fill()
    # t.setheading(h)


def sierp(size, depth):
    if depth <= 0:
        trojkat(size)
        t.update()
        return

    size //=2
    sierp(size, depth - 1)
    t.forward(size)
    sierp(size, depth - 1)
    t.back(size)
    t.lt(60)
    t.forward(size)
    t.rt(60)
    sierp(size, depth-1)
    t.lt(60)
    t.bk(size)
    t.rt(60)
    # t.forward(size)

t.penup()
t.tracer(0, 0)
# t.speed("fastest")
t.color("green")
t.goto(-200,0)
sierp(512, 4)
t.update()
t.mainloop()
