from itertools import product
import re
import turtle as t

# https://stackoverflow.com/questions/41922629/convert-text-to-braille-unicode-in-python
code_table = {
    "a": "100000",
    "b": "110000",
    "c": "100100",
    "d": "100110",
    "e": "100010",
    "f": "110100",
    "g": "110110",
    "h": "110010",
    "i": "010100",
    "j": "010110",
    "k": "101000",
    "l": "111000",
    "m": "101100",
    "n": "101110",
    "o": "101010",
    "p": "111100",
    "q": "111110",
    "r": "111010",
    "s": "011100",
    "t": "011110",
    "u": "101001",
    "v": "111001",
    "w": "010111",
    "x": "101101",
    "y": "101111",
    "z": "101011",
    "#": "001111",
    "1": "100000",
    "2": "110000",
    "3": "100100",
    "4": "100110",
    "5": "100010",
    "6": "110100",
    "7": "110110",
    "8": "110010",
    "9": "010100",
    "0": "010110",
    " ": "000000",
}


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


def draw_circle(x, y, rad, color=None):
    move(x, y - rad)
    if color is not None:
        t.begin_fill()
        t.fillcolor(color)
        t.circle(rad)
        t.end_fill()


color = {
    "1": (0,) * 3,
    "0": (0.95,) * 3,
}


def draw_braille_char(x, y, edge_len, char):
    braille_char = code_table[char]
    for i, j in product(range(2), range(3)):
        x_abs = x + edge_len / 2 + i * edge_len
        y_abs = y - edge_len - j * edge_len
        draw_circle(x_abs, y_abs, edge_len / 2, color[braille_char[i * 3 + j]])


def draw_braille_word(x, y, edge_len, word: str):
    word = word.lower()
    if re.match(r"[^\d\w ]", word):
        raise Exception("invalid input")

    for i, c in enumerate(word):
        draw_braille_char(x + 2.5 * edge_len * i, y, edge_len, c)


def main():
    canvas = t.Screen()
    window_size = 1000
    canvas.setup(window_size, window_size)
    canvas.title("Polnareff")
    t.tracer(0, 0)
    t.hideturtle()
    draw_braille_word(-400, 0, 20, "braille 123 42")
    t.update()
    t.mainloop()


if __name__ == "__main__":
    main()
