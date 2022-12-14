import random
import time
import numpy as np
import numpy.typing as npt
from itertools import count, product


def d4_roll(rolls: int = 0):
    """custom number generator for a d4 roll. If no parameters passed, it's infinite"""
    state = 0
    it = count() if rolls == 0 else range(rolls)
    for i in it:
        if i & 15 == 0:
            state = random.randrange(2 << 32)
        d, m = divmod(state, 4)
        state = d
        yield m


def create_board(n, m):
    return np.zeros((n, m), dtype=np.int8) - 1


def load_board(file, default_power=0):
    with open(file, "r") as f:
        data = f.readlines()
    matcher = {
        " ": -2,
        ".": -1,
        "k": 0+default_power,
        "p": 5+default_power,
        "n": 10+default_power,
    }
    shape = (len(data) + 2, len(data[0]) + 2)
    array = np.zeros(shape, dtype=np.int8) - 2
    for i, line in enumerate(data):
        for j, elem in enumerate(line.strip()):
            array[i + 1, j + 1] = matcher[elem]

    return array


def print_board(board):
    mapper = "kkkkkpppppnnnnn ."
    print("\n".join("".join(map(mapper.__getitem__, row)) for row in board[1:-1, 1:-1]))


NEIGH = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def array_type(n: int):
    return n if n < 0 else n // 5


def life_cycle(board: npt.ArrayLike):
    sh = board.shape
    d4 = d4_roll()
    new_board = np.copy(board)
    for i, j in product(range(sh[0]), range(sh[1])):
        # only change stuff for filled cells
        if board[i, j] < 0:
            continue

        dx, dy = NEIGH[next(d4)]
        # avoid checking out of bound
        while board[i + dx, j + dy] < -1:
            dx, dy = NEIGH[next(d4)]

        neig_type = array_type(board[i + dx, j + dy])
        neig_pow = board[i + dx, j + dy] % 5
        self_type = array_type(board[i, j])
        self_pow = board[i, j] % 5
        
        if board[i + dx, j + dy] == -1:
            if self_pow == 0:
                continue
            base_power = (board[i, j] // 5) * 5
            new_board[i + dx, j + dy] = max(base_power, board[i, j] - 1)
            continue


        if neig_type == self_type:
            continue

        match (neig_type - self_type + 3) % 3:
            case 0:
                continue  # draw, doesn't happen
            case 1:  # neigh won
                new_neig_power = min(4, neig_pow + 1)
                new_self_power = max(0, self_pow - 1)
                # change neig value
                new_value = neig_type * 5 + new_neig_power
                new_board[i + dx, j + dy] = new_value

                # change self value
                if self_pow == 0:
                    new_value = 0 if new_self_power == 0 else neig_type * 5 + new_self_power
                new_board[i, j] = new_value

            case 2:  # self won
                new_self_power = min(4, neig_pow + 1)
                new_neig_power = max(0, self_pow - 1)
                # change self value
                new_value = self_type * 5 + new_self_power
                new_board[i, j] = new_value

                # change neig value
                if neig_pow == 0:
                    new_value = 0 if new_neig_power == 0 else neig_type * 5 + new_neig_power
                new_board[i+dx, j+dy] = new_value
    
    return new_board


if __name__ == "__main__":
    b = load_board("test.txt",default_power=4)
    print_board(b)
    for i in range(20):
        b = life_cycle(b)
        print('-'*25)
        print_board(b)
        time.sleep(0.5)