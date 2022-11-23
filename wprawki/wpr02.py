import turtle as t
import math


def signum(n):
    return n if n == 0 else (1 if n > 0 else -1)


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_circle(rad, x, y, color=None):
    move(x, y - rad)
    if color is not None:
        t.begin_fill()
        t.fillcolor(color)
        t.circle(rad)
        t.end_fill()


def face(color_type: int, iris: int, smile_factor: int):
    # configs
    assert color_type in range(3)
    assert iris in range(1, 11)
    assert smile_factor >= 1.0 or smile_factor <= -1.0
    # normalizes smile factor
    smile_factor = signum(smile_factor) + signum(smile_factor) / math.log(abs(smile_factor))
    color = ["white", "yellow", "brown"][color_type]
    eye_color = ["blue", "brown", "white"][color_type]
    smile_factor = 1 / smile_factor

    # shape
    move(0, -400)
    t.width(5)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(400)
    t.end_fill()

    # eyes
    for i in (-1, 1):
        draw_circle(50, i * 150, 150, "black")
        draw_circle(50 / iris, i * 150, 150, eye_color)

    # nose
    move(0, 0)
    t.fd(30)
    t.lt(110)
    t.fd(50)

    # mouth
    x = 200
    sgn = -1 if smile_factor < 0 else 1
    alpha = 180 * abs(smile_factor)
    rad_a = math.radians(alpha)
    r = math.sqrt(x**2 / (1 - math.cos(rad_a)))
    # drawing
    move(sgn * 2 * x / 3, -200)

    # beta = 90-gamma
    # gamma = 90- alfa/2
    # beta = alfa/2
    t.setheading((90 + 90 * sgn) - alpha / 2)
    t.circle(r, alpha)


canvas = t.Screen()
window_size = 1000
canvas.setup(window_size, window_size)
canvas.title("Polnareff")
t.tracer(0, 0)
t.hideturtle()

face(color_type=1, smile_factor=-2, iris=1)
t.update()
t.mainloop()
