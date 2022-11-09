from functools import lru_cache
from statistics import mean, median


def collatz_generator(n: int):
    while n > 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1

    yield 1


@lru_cache(maxsize=None)
def collatz_len(n: int) -> int:
    if n <= 1:
        return 1
    arg = n // 2 if n % 2 == 0 else 3 * n + 1
    return 1 + collatz_len(arg)


def solve(lower_bound: int, upper_bound: int) -> tuple[float, int | float, int, int]:
    energies = list(map(collatz_len, range(lower_bound, upper_bound + 1)))

    sol = (func(energies) for func in (mean, median, max, min))
    return sol


def show_sol(sol: tuple[float, int | float, int, int]):
    labels = [
        "średnia: ",
        "mediana: ",
        "maksimum: ",
        "minimum: ",
    ]
    for l, val in zip(labels, sol):
        print(l, val)


sol = solve(1, 10_000)
show_sol(sol)
