from more_itertools import flatten
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
def generate_nums_with_sevens(numbers: int, seven_len: int) -> list[str]:
    lucky = "7" * seven_len
    upper_bound = 10 ** (numbers - seven_len)

    def seq_dash_w(x, y):
        return [str(i).zfill(numbers - seven_len) for i in range(x, y)]

    nums_to_insert = seq_dash_w(0, upper_bound)
    res = []
    for position in range(numbers - seven_len + 1):
        res.extend([n[:position] + lucky + n[position:] for n in nums_to_insert])

    # filter out invalid numbers
    return [num for num in set(res) if num[0] != '0']


def zad1() -> list[int]:
    # wygeneruj 3 - 6cio cyfrowe liczby
    all_sevens = [generate_nums_with_sevens(i, 3) for i in range(3, 7)]
    lucky_nums = map(int, flatten(all_sevens))
    primes = set(primes_upto2(LIMIT))
    return list(filter(primes.__contains__, lucky_nums))


lucky_primes = zad1()
print(f"liczba wystąpień szczęśliwych liczb pierwszych między 1 a {LIMIT} : {len(lucky_primes)}")
print(f"oto one:\n{lucky_primes}")

# PS: is_prime works, but it's O(sqrt(n)) for each prime,
# which means (k * sqrt(n)) where k is the range size
# prime sieve is has O(n * log (log n)) and after transfomring it into a set
# it has O(1) lookup time
# PPS: yes, it's overkill, but I like to challenge myself
