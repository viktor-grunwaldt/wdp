import random
from timeit import timeit


def shuffle(x: list) -> list:
    """Shuffle list x in place, and return shuffled list."""

    for i in reversed(range(1, len(x))):
        # pick an element in x[:i+1] with which to exchange x[i]
        j = random.randint(0, i-1)
        x[i], x[j] = x[j], x[i]

    return x


def randperm(lim: int) -> list[int]:
    return shuffle(list(range(lim)))


for _ in range(6):
    print(sorted(a+1 for a in randperm(49)[:6]))


print("randperm(10**6) runtime: "timeit(lambda : randperm(10**6), number=1), "seconds")
