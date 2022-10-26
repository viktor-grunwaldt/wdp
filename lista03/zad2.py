from itertools import takewhile
from math import ceil
from timeit import timeit
import numpy


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


# for collections python passes a reference (I think), which means
# not much time is being lost by passing in the prime numbers
def prime(num: int, primes) -> bool:
    if num < 2:
        return False
    # we have to check up to ceil(sqrt(num))
    potential_divisors = takewhile(lambda x: x * x <= num, primes)
    return all((num % k) != 0 for k in potential_divisors)


# we are supposed to check all numbers containing "7"*7
# which are smaller than LIMIT
# so I just generate numbers from 0 to 10**10 // 10**7
# and insert somewhere before, after or inbetween "7777777"
def generate_nums_with_sevens(numbers: int, seven_len: int) -> list[str]:
    lucky = "7" * seven_len
    upper_bound = 10 ** (numbers - seven_len)
    seq_dash_w = lambda x, y: [str(i).zfill(numbers - seven_len)
                                for i in range(x, y)]
    nums_to_insert = seq_dash_w(0, upper_bound)
    res = []
    for position in range(len(lucky) + 1):
        res.extend([n[:position] + lucky + n[position:] for n in nums_to_insert])
    
    # filter out invalid numbers
    return [num for num in set(res) if num[0] != '0']


def digit_sum(numeral: str) -> int:
    return sum(map(int, numeral))


def remove_multiples_of_3(numerals: list[str]) -> list[str]:
    return list(filter(lambda x: digit_sum(x) % 3 != 0, numerals))


def zad2(numbers, sevens) -> list[int]:
    numerals = generate_nums_with_sevens(numbers, sevens)
    # print(f"we have {len(set(numerals))} hyperlucky numbers")

    limit = 10 ** numbers
    newmerals = remove_multiples_of_3(numerals)
    lucky_nums = map(int, newmerals)
    print("multiples of 3 removed,")
    print(f"now we have {len(set(newmerals))} numbers to check")
    print("generating primes...")
    primes = primes_upto2(ceil(limit**0.5) + 1)

    print("checking numbers...")
    return [lucky_num for lucky_num in lucky_nums if prime(lucky_num, primes)]


ps = primes_upto2(20)
lucky_primes = zad2(10, 7)
print(f"liczba wystąpień hiperszczęśliwych liczb pierwszych między \
{10**9} a {10**10}: {len(lucky_primes)}")
# print(f"oto one:\n{lucky_primes}")

# overkilling first task actually paid off
# wait, I can't just generate primes up to 10**10
# filtering out candidates it is

exec_time = timeit(lambda: zad2(10, 7), number=10)
print(f"{exec_time/10=:4.5f} sec")
