import random
import time
import turtle as t
import numpy as np
from collections import deque


def draw_square(xy, bok: int, color: np.ndarray):
    y, x = xy
    t.goto(x, y)
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(4):
        t.fd(bok)
        t.rt(90)
    t.end_fill()


black = np.array([0.0] * 3)


def draw_rfs(image: np.ndarray, start: np.ndarray):
    x = random.randrange(0, image.shape[0])
    y = random.randrange(0, image.shape[1])
    starting_pixel = np.array((y, x), dtype=np.uint32)

    neigh = np.array([1, 0, 0, 1, -1, 0, 0, -1], dtype=int).reshape((4, 2))

    visited = np.zeros(image.shape[:-1], dtype=np.bool_)
    to_visit = []
    to_visit.append(starting_pixel)

    is_inside = lambda x: 0 <= x[0] < visited.shape[0] and 0 <= x[1] < visited.shape[1]
    while to_visit:
        # drawing square
        current = to_visit.pop(random.randrange(0, len(to_visit)))
        draw_square(start + current * 10, 10, black)
        t.update()
        visited[tuple(current)] = 1

        for p in current + neigh:
            # print("a:", p, "b:", is_inside(p))
            if is_inside(p):
                if not visited[p[0], p[1]]:
                    to_visit.append(p)
                    visited[p[0], p[1]] = 1


t.tracer(0, 0)
t.penup()
img = np.empty((40, 40, 3))
img[:, :] = black

draw_bfs(img, np.array((100, -100), dtype=int))
t.mainloop()
