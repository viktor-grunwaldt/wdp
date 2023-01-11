import itertools as it
from typing import Iterable


def _combinations(iterable: Iterable, r: int):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def rel_rown(s: set) -> list[list[set]]:
    return [list(map(set, it.combinations(s, i))) for i in range(1, len(s) + 1)]


print(list(_combinations(range(4), 2)))
print(rel_rown({1, 2, 3, 4}))
