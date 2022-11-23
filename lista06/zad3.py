from itertools import count, takewhile
from operator import itemgetter
import numpy


# https://rosettacode.org/wiki/Sieve_of_Eratosthenes#Using_numpy
# implementing sieve with numpy array allows python to use the
# c implementation of numpy to set all multiplicatives of a prime to false
# which is substancially faster
def primes_upto(limit):
    primes = numpy.ones(limit + 1, dtype=bool)
    for n in range(2, int(limit**0.5 + 1.5)):
        if primes[n]:
            primes[n * n :: n] = 0
    return numpy.nonzero(primes)[0][2:]


def is_divisible(n: int) -> bool:
    return lambda x: n % x == 0


def power_of_factor_func(n: int, k: int) -> int:
    return sum(1 for _ in takewhile(is_divisible(n), map(lambda x: k**x, count(1))))


def factorisation_functional(n: int, primes) -> list[tuple[int, int]]:
    if n == 1:
        return []
    factor = next(filter(is_divisible(n), primes), None)
    if not factor:
        # shouldn't happen, but who knows. theoretically possible if limit(primes)<n
        return []
    power = power_of_factor_func(n, factor)
    return [(factor, power)] + factorisation_functional(n // (factor**power), primes)


def fac_set(n: int, primes) -> set[int]:
    return set(map(itemgetter(0), factorisation_functional(n, primes)))


ps = primes_upto(10000)
print(fac_set(36, ps))
