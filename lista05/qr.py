import turtle as t
import qrcode


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


def qr_matrix_from_data(data) -> list[list[bool]]:
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    pattern = qr.get_matrix()
    return pattern


if __name__ == "__main__":
    edge_len = 20
    x_begin = -500
    y_begin = 400
    # t.tracer(0,0)
    t.speed("fastest")

    t.penup()
    pattern = qr_matrix_from_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    for j, row in enumerate(pattern):
        for i, elem in enumerate(row):
            x_abs = x_begin + i * edge_len
            y_abs = y_begin - j * edge_len
            kwadrat(x_abs, y_abs, edge_len, ["white", "black"][int(elem)])

    # t.update()
    t.mainloop()
