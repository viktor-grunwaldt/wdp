import numpy as np
import turtle as t
import qrcode
import re


# eval demonstration
def what_is_love(expr):
    eval(expr)


# https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html seems interesting
def manly_man_parsing(data: str) -> np.array:
    data = re.sub(r"[\(\)]", "", data)
    h = data.count("\n")
    w = data.split("\n", maxsplit=1)[0].count(" ") + 1
    img = np.zeros(shape=(h, w, 3), dtype=np.uint8)  # dtype = u8
    for i, row in enumerate(data.splitlines()):
        for j, pixel in enumerate(row.split()):
            # rgb = map(int, pixel.replace("(", "").replace(")", "").strip().split(","))
            # for k, u8 in enumerate(rgb):
            #     img[i, j, k] = u8
            img[i, j] = np.fromstring(pixel, sep=",", dtype=np.uint8)

    return img


def move(x, y):
    # t.penup()
    t.goto(x, y)
    # t.pendown()


def kwadrat(x, y, bok, kolor):
    move(x, y)
    t.begin_fill()
    t.fillcolor(kolor)
    for i in range(4):
        t.fd(bok)
        t.rt(90)
    t.end_fill()


def test():
    def qr_matrix_from_data(data) -> list[list[bool]]:
        qr = qrcode.QRCode()
        qr.add_data(data)
        qr.make(fit=True)
        pattern = qr.get_matrix()
        return pattern

    bool_to_rgb = lambda x: ((0 if x else 255),) * 3
    ricky = qr_matrix_from_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    out = "\n".join(" ".join("({},{},{})".format(*bool_to_rgb(b)) for b in row) for row in ricky)
    # write to file
    with open("data/test.textimageformat", "w") as f:
        f.write(out)


def random_image(img: np.array) -> np.array:
    old_shape = np.shape(img)
    new_img = np.reshape(img, newshape=(old_shape[0] * old_shape[1], old_shape[2]))
    np.random.shuffle(new_img)

    return np.reshape(new_img, newshape=old_shape)


if __name__ == "__main__":
    what_is_love("""print("baby don't hurt me")""")
    # test()
    with open("data/obrazek.txt") as f:
        array = manly_man_parsing(f.read())

    # array = random_image(array)
    edge_len = 10
    canvas = t.Screen()
    canvas.setup(700, 600)
    x_begin = -300
    y_begin = 300
    t.tracer(0, 0)
    t.colormode(255)
    # t.speed("fastest")
    t.penup()
    for j, row in enumerate(np.transpose(array, axes=(1, 0, 2))):
        for i, elem in enumerate(row):
            x_abs = x_begin + i * edge_len
            y_abs = y_begin - j * edge_len
            kwadrat(x_abs, y_abs, edge_len, elem)

    t.update()
    t.mainloop()
