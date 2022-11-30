def is_divisible(n: int) -> bool:
    return lambda x: n % x == 0


def is_prime(n: int):
    return not any(map(is_divisible(n), range(2, int(n**0.5) + 1)))


def fac_shortest(n: int):
    return set(filter(is_prime, filter(is_divisible(n), range(2, n + 1))))


def factorisation_functional(n: int) -> set[int]:
    if n == 1:
        return set()
    factor = next(filter(is_divisible(n), range(2, n + 1)), None)
    while is_divisible(n)(factor):
        n //= factor
    return {factor} | factorisation_functional(n)


print(factorisation_functional(2 * 3 * 5 * 7 * 11 * 13))
print(fac_shortest(4 * 3 * 5 * 7 * 11 * 13 * 13))
