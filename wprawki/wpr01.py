from itertools import chain, repeat, tee
import itertools as i
from more_itertools import flatten


# takes an iterator, copies it and appends it to the end with each item reversed
def copy_and_flip_iter(it):
    # https://stackoverflow.com/questions/42132731/how-to-create-a-copy-of-python-iterator
    it_fst_copy, it_snd_copy = i.tee(it)
    return i.chain(it_fst_copy, map(lambda x: x[::-1], it_snd_copy))


# generates 2 borders, and then adds their flipped counterpart
def sq_gen(n: int) -> list[tuple[int, int]]:
    top = zip(i.repeat(0), range(n))
    bottom = zip(i.repeat(n - 1), range(n))

    return list(i.chain(copy_and_flip_iter(top), copy_and_flip_iter(bottom)))


# shifts a list of points by a point
def move_points_by_vec(
    vec: tuple[int],
    pts: list[tuple[int]],
) -> list[tuple[int]]:
    return [(x + vec[0], y + vec[1]) for x, y in pts]


def kwadkonc2(n: int, s: str) -> str:
    border_char = s[0]
    inner_char = s[1]
    # create borders which are 4 smaller (save thier size for shift)
    borders = [(n - i, sq_gen(i)) for i in range(n, 0, -4)]
    # shifts by half of the distance of the border differ from size
    shift_border = lambda i, b: move_points_by_vec((i // 2, i // 2), b)
    # make a set with all borders
    borders_with_offset = set(flatten(shift_border(i, border) for i, border in borders))
    img = "\n".join(
        "".join(border_char if (i, j) in borders_with_offset else inner_char
                for i in range(n))
        for j in range(n)
    )
    return img


kwadkonc = lambda n, s: print(kwadkonc2(n, s))
# it = copy_and_flip_iter(iter(["ab", "cd", "ef"]))
# print(list(it))
kwadkonc(8, "#_")

kwadkonc(3, "*.")
kwadkonc(11, "`%")
kwadkonc(0, "`%")
kwadkonc(1, "`%")
