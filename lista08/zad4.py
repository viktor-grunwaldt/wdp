import numpy as np
import turtle as t
from itertools import product
from scipy import signal


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


def create_map(n, size):
    kolory = np.array([(0, 1, 0), (0, 1, 1), (1, 0, 1), (1, 0, 0), (0.5, 0, 0)])
    arr = np.zeros((size, size))
    # hills = np.empty((2, n), dtype=np.uint32)
    # print(hills)
    hills_pos = np.random.randint(0, size, (n, 2))
    for pos in hills_pos:
        arr[pos[0], pos[1]] = np.random.uniform()
        # print(arr[pos[0], pos[1]])
    print(arr.shape)
    window = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32) / 16
      # np.ones((3,3))/5

    for _ in range(20):
        arr = signal.fftconvolve(arr, window)[1:-1, 1:-1]

    arr *= kolory.shape[0] - 1
    # for row in arr:
    #     for elem in row:
    #         if elem>4:
    # print(elem)

    arr = arr - arr.min()
    arr = arr / arr.max()
    arr = np.clip(arr * len(kolory), 0, len(kolory) - 1)

    arr = kolory[arr.astype(np.int32)]
    # print(arr)
    print(arr.shape)
    return arr


def draw_screen(array):
    edge_len = 5
    canvas = t.Screen()
    canvas.setup(700, 600)
    x_begin = -300
    y_begin = 300
    t.penup()
    # t.colormode(255)
    t.tracer(0, 0)
    # array = np.transpose(array, axes=(1, 0, 2))
    x, y, _ = array.shape

    iterator = product(range(x), range(y))
    for i, j in iterator:
        x_abs = x_begin + i * edge_len
        y_abs = y_begin - j * edge_len
        kwadrat(x_abs, y_abs, edge_len, array[i][j])


arr = create_map(500, 100)
draw_screen(arr)
t.update()
t.mainloop()
