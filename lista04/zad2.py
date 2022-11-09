"""
10001st prime

Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
(neatly fits with prime sieve in list 4 lol)
"""
from functools import lru_cache
from itertools import islice
from math import ceil, log
import numpy


# pure pythonic sieve
def primes_with_sieve(limit):
    nums = [True] * (limit + 1)
    for n in range(2, int(limit**0.5 + 1.5)):
        if nums[n]:
            for i in range(n * n, limit + 1, n):
                nums[i] = False

    return [i for i, n in islice(enumerate(nums), 2, None) if n]


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


# https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
# mathematicians write this as π(x)
# we only need the upper bound, which is smaller than n(log n + log log n)
# https://sci-hub.se/10.2307/2371291
def approximate_nth_prime(n: int) -> int:
    return ceil(n * (log(n) + log(log(n))))


def find_nth_prime(n: int) -> int:
    return primes_upto2(approximate_nth_prime(n))[n]


def project_euler7():
    # https://www.wolframalpha.com/input?i=10001th+prime
    # p_10001 = 104743
    print(f"there is {len(primes_with_sieve(1000))} between 1 and 1000")
    print("the 10001th prime is:", find_nth_prime(10_001))


"""
Longest Collatz sequence
[Show HTML problem content]
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# https://xkcd.com/710/


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


def longest_collatz(n: int) -> int:
    # skipping evens, since they are always shorter
    return max(map(collatz_len, range(1, n + 1, 2)))


def project_euler14():
    print(longest_collatz(1_000_000))


if __name__ == "__main__":
    project_euler7()
    project_euler14()
