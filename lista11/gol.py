################################################################################
# conway.py
#
# Author: electronut.in, edited by vik
#
# Description:
#
# A simple Python/matplotlib implementation of Conway's Game of Life.
################################################################################

# The rules:
#    cell        neighbor    cell's next state
#    ---------   --------    -----------------
# 1. live        < 2         dead
# 2. live        2 or 3      live
# 3. live        > 3         dead
# 4. dead        3           live

# Simplified rules:
#    cell        neighbor    cell's next state
#    ---------   --------    -----------------
# 1. live        2           live
# 2. live/dead   3           live
# 3. Otherwise, dead.

from itertools import filterfalse, groupby, pairwise
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import signal

N = 100
ON = 1
OFF = 0
vals = np.array([ON, OFF], dtype=np.int8)


# Bill Gosper discovered the first glider gun in 1970, earning $50 from Conway.
# The discovery of the glider gun eventually led to the proof that Conway's Game of Life
# could function as a Turing machine. For many years this glider gun was the smallest one
# known in Life,[4] although other rules had smaller guns.
# this function tries to read .rle files, more info here: https://conwaylife.com/wiki/Run_Length_Encoded
def read_text_to_grid(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    is_comment = lambda x: x[0] == "#"
    data = [line.strip() for line in filterfalse(is_comment, data)]
    metadata = data[0]
    board_rle = "".join(data[1:])
    # use a bit of regex magic to insert 1 before each tag without a length count
    board_rle = re.sub(r"(?<!\d)([^\d])", r"1\1", board_rle)
    parsed_metadata = [elem.split(" = ")[1] for elem in metadata.split(", ")]
    x, y = map(int, parsed_metadata[:2])

    print(x, y)
    assert N >= x and N >= y
    grid = np.zeros((N, N), dtype=np.int8)
    chunks = ["".join(grps) for _, grps in groupby(board_rle, key=str.isdigit)]
    x, y = (0, 0)
    for pair in pairwise(chunks):
        match pair:
            # fmt: off
            case _, "$":
                x, y = (0, y + 1)
            case _, "!":
                break
            case count, "b":
                x += int(count)
            case count, "o":
                ct = int(count)
                grid[y, x:(x + ct)] = 1
                x += ct
            # fmt: on

    return grid


def update_convolve(data):
    global grid
    # use convolve and kernel to calculate sum of neighbors and only take
    # scipy.signal.convolve uses some interal magic to figure out which
    # convolve method is the fastest, then applies it
    neighbors = signal.convolve(grid, kernel, mode="same")

    grid &= neighbors == 2  # alive if it was alive and has 2 neighbors else dead
    grid |= neighbors == 3  # alive if it has 3 neighbors

    # update data
    mat.set_data(grid)
    return [mat]


# populate grid with random on/off - more off than on

grid = read_text_to_grid("data/glider_gun.rle")
# grid = np.random.choice(vals, N * N, p=[0.1, 0.9]).reshape(N, N)
kernel = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1], dtype=np.int8).reshape(3, 3)

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap="Greys")

# If I were to build game of life for massive boards, https://en.wikipedia.org/wiki/Hashlife
# could be a potential algorithm which would increase performance. It uses hashed quadtrees
# to store data of given grid and skip computations for repeating patterns
ani = animation.FuncAnimation(fig, update_convolve, interval=50, save_count=50)
plt.show()
