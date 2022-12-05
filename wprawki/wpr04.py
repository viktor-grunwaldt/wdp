from itertools import product
import sympy


def is_divisible(n: int) -> bool:
    return lambda x: n % x == 0


def dumb_is_prime(n: int):
    return all(n%i != 0 for i in range(2, int(n**0.5) + 1))
    # return not any(map(is_divisible(n), range(2, int(n**0.5) + 1)))


# functional
def is_perfect_functional(n: int) -> bool:
    return n == (1 + sum(map(lambda k: k + n // k, filter(is_divisible(n), range(2, int(n**0.5) + 1)))))


# using list comprehensions
def is_perfect_comp(n: int) -> bool:
    return n == 1 + sum(k + n // k for k in range(2, int(n**0.5) + 1) if n % k == 0)


def dumb_gcd(n, m):
    mult = 1
    while m > 0:
        if m > n:
            n, m = m, n
        if (n % 2 + m % 2) == 2:
            n -= m
        elif n % 2 == 0:
            if m % 2 == 0:
                mult *= 2
                m //= 2
            else:
                n //= 2
    return n * mult


def dumb_totient2(n):
    return sum(1 for i in range(1, n) if dumb_gcd(i, n) == 1)


def dumb_catheti(n):
    return list(set(min(a,b) for a,b in product(range(1,n), range(1,n)) if a**2 + b**2 == n**2))


# the REAL solution
isprime = lambda x: sympy.simplify(x).is_prime
isperfect = sympy.is_perfect
totient = sympy.ntheory.factor_.totient
gcd = sympy.gcd


print([i for i in range(2, 50) if dumb_is_prime(i)])
print([i for i in range(2, 50) if is_perfect_comp(i)])
print(dumb_catheti(25))
