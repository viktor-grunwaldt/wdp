from dataclasses import dataclass
import time
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
window_size = 1000
canvas.setup(window_size, window_size)
canvas.title("Polnareff")
radius = int(window_size * 0.4)
π = math.pi
t.hideturtle()
# european style refresh rate
refresh_rate = 50

# define hand properites
# class HandType(Enum):
#     HOUR = 0
#     MINUTE = 1
#     SECOND = 2


@dataclass
class Hand:
    # h_type: HandType
    width: int
    length: int
    color: str


hour_hand = Hand(5, radius * 0.5, "black")
minute_hand = Hand(3, radius * 0.7, "black")
second_hand = Hand(2, radius * 0.8, "red")
# hour_hand = Hand(HandType.HOUR, 5, radius // 4, "black")
# minute_hand = Hand(HandType.MINUTE, 3, radius // 3, "black")
# second_hand = Hand(HandType.SECOND, 1, radius // 2, "red")
# no delay drawing
t.tracer(0, 0)


def home():
    t.penup()
    t.home()
    t.pendown()


# https://en.wikipedia.org/wiki/Sine_and_cosine#/media/File:Sinus_und_Kosinus_am_Einheitskreis_1.svg
def draw_clock_face():
    for i in range(5 * 12):
        angle = π * 2 * i / 60
        # moving to a point on a circle
        move(radius * math.sin(angle), radius * math.cos(angle))
        # + π to rotate by 180 degrees (going backwards)
        t.setheading(angle + π)
        # draw a mark
        # size of mark depends if it's an hour mark or a minute mark
        width, length = (3, radius // 10) if i % 5 == 0 else (2, radius // 20)
        t.width(width)
        t.fd(length)

        # reset width
        t.width(None)
        # reset pos
        # home()


def draw_hand(hand: Hand, value: int):
    angle = π * 2 * value / 60
    home()
    t.setheading(angle)
    t.width(hand.width)
    t.color(hand.color)
    t.fd(hand.length)
    t.width(None)
    t.color("black")
    home()


def draw_hands(h: int, m: int, s=None):
    assert 0 <= h <= 24  # we assume 24:00 is allowed and == 00:00
    assert 0 <= m < 60

    # we're splitting watch face into 60 parts, so 12 hours fit into 60 mins when *5
    # hour hand offset is equal to m/12, cuz 1h = 1/12th of the clock
    draw_hand(hour_hand, (h % 12) * 5 + m / 12)
    draw_hand(minute_hand, m)
    if s is not None:
        assert 0 <= s < 60
        draw_hand(second_hand, s)


def clock():
    curtime = time.localtime()
    t.clear()
    draw_clock_face()
    draw_hands(curtime.tm_hour, curtime.tm_min, curtime.tm_sec)
    t.update()
    # magic function to call f after a delay
    # it's not recursion so it's doesn't nuke the stack
    t.ontimer(clock, 1000 // refresh_rate)


# draw_clock_face()
# # draw_hands(10, 10)
# draw_hands(11, 59, 30)
# update screen to show drawings
# t.update()
# while True:
#     t.ontimer(clock, 1000)
# for i in range(10):
#     #
#     clock()
#     time.sleep(1)

clock()
t.mainloop()
