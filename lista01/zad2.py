from functools import reduce
import operator
import math


def factorial(n: int) -> int:
    return reduce(operator.mul, range(1, n + 1))


def num_len(n: int) -> int:
    return math.ceil(math.log10(n))


def poliszinator(n: int) -> str:
    if n == 1:
        return "cyfrę"
    elif 1 < (n % 10) < 5 and (n // 10) % 10 in (0, 2):
        return "cyfry"
    else:
        return "cyfr"


if __name__ == "__main__":
    # test gramatyki polskiej
    # for i in range(1, 131):
    #     print(f"ma {i} {poliszinator(i)}")
    for i in range(4, 101):
        f = factorial(i)
        dig = num_len(f)
        print(f"{i}! ma {dig} {poliszinator(dig)}")
    for i in range(13):
            print(*[(j, poliszinator(j)) for j in range(i*10, (i+1)*10)], sep='\t')

