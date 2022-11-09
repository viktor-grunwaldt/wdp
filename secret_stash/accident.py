from time import time
import turtle as t
import math


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# usable speed
t.speed("fastest")
# usable angle system
t.radians()
# usable coordinate mode
t.mode("logo")

# setup
canvas = t.Screen()
canvas.setup(500, 500)
canvas.title("Polnareff")
radius = 200

# https://en.wikipedia.org/wiki/Sine_and_cosine#/media/File:Sinus_und_Kosinus_am_Einheitskreis_1.svg
t.tracer(0, 0)
for i in range(5 * 12):
    angle = math.pi * 2 * i / 60
    move(radius*math.cos(angle), radius*math.sin(angle))
    t.setheading(angle)
    t.fd(100)
    # t.penup()
    # t.fd(radius*(0.9 if i % 5 == 0 else 0.95))
    # t.pendown()
    t.home()

t.update()
t.mainloop()
