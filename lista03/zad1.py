import numpy
from math import ceil

LIMIT = 100_000


# https://rosettacode.org/wiki/Sieve_of_Eratosthenes#Using_numpy
# implementing sieve with numpy array allows python to use the
# c implementation of numpy to set all multiplicatives of a prime to false
# which is substancially faster
def primes_upto2(limit):
    is_prime = numpy.ones(limit + 1, dtype=bool)
    for n in range(2, int(limit**0.5 + 1.5)):
        if is_prime[n]:
            is_prime[n * n :: n] = 0
    return numpy.nonzero(is_prime)[0][2:]


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    # +1 w range dla p^2
    return all((num % k) != 0 for k in range(2, ceil(num**0.5) + 1))


# we are supposed to check all nnumbers containing 777
# which are smaller than 100_000
# so I just generate numbers from 00 to 99
# and insert somewhere before, after or inbetween "777"
def generate_nums_with_sevens(lim: int) -> list[str]:
    lucky = "777"
    nums_to_insert = [f"{i:02}" for i in range(lim // 1000)]
    res = []
    for position in range(len(lucky) + 1):
        res.extend([n[:position] + lucky + n[position:] for n in nums_to_insert])

    return res


def zad1() -> list[int]:
    lucky_nums = map(int, generate_nums_with_sevens(LIMIT))
    primes = set(primes_upto2(LIMIT))
    return [lucky_num for lucky_num in lucky_nums if lucky_num in primes]


lucky_primes = zad1()
print(f"liczba wystąpień szczęśliwych liczb pierwszych między 1 a {LIMIT} : {len(lucky_primes)}")
print(f"oto one:\n{lucky_primes}")

# PS: is_prime works, but it's O(sqrt(n)) for each prime,
# which means (k * sqrt(n)) where k is the range size
# prime sieve is has O(n * log (log n) and after transfomring it into a set
# it has O(1) lookup time
# PPS: yes, it's overkill, but I like to challenge myself
