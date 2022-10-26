import random


def shuffle(x: list) -> list:
    """Shuffle list x in place, and return shuffled list."""

    for i in reversed(range(1, len(x))):
        # pick an element in x[:i+1] with which to exchange x[i]
        j = random.randrange(0, i)
        x[i], x[j] = x[j], x[i]

    return x


def randperm(max: int) -> list[int]:
    return shuffle(list(range(max)))


print(randperm(10**6)[:20])
