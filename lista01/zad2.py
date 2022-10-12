from functools import reduce
import operator
import math
def factorial(n:int) -> int:
    return reduce(operator.mul, range(1, n+1))


def num_len(n:int) -> int:
    # return len(str(n))
    return math.ceil(math.log10(n))

def poliszinator(n:int) -> str:
    if n == 1:
        return "cyfrę"
    elif 1<n<5:
        return "cyfry"
    else:
        return "cyfr"
    
if __name__ == "__main__":
    for i in range(4,101):
        f = factorial(i)
        dig = num_len(f)
        print(f"{i}! ma {dig} {poliszinator(dig)}")