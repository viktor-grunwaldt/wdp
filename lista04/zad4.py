from itertools import dropwhile
from zad2 import primes_upto2


def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def palindromy(a: int, b: int) -> list[int]:
    """
    Returns all prime palindromes from range a, b inclusive

    Parameters:
    a: lower bound
    b: upper bound

    Returns:
    list[int]: a list of numbers satisfying the position
    """
    primes = primes_upto2(b + 1)
    return list(filter(is_palindrome, dropwhile(lambda x: x < a, primes)))


print(palindromy(1, 1_000_000))
