from functools import lru_cache
import math
import random

from more_itertools import flatten
from losowanie_fragmentow import losuj_fragment
from itertools import combinations_with_replacement

# print(*(losuj_fragment() for _ in range(5)), sep='\n')


def losuj_fragment_o_dl(n: int) -> str:
    frag = ""
    while len(frag) != n:
        frag = losuj_fragment()

    return frag


def losuj_haslo(n: int) -> str:
    assert n > 1
    haslo = ""
    # losujemy dopóki l < n-4 aby uniknąć sytuacji, gdzie l= n-1
    # (wtedy trzeba by bylo coś usuwać)
    while len(haslo) < n - 5:
        frag = losuj_fragment()
        haslo += frag

    # pominięcie przypadku len(haslo) = n-1
    if len(haslo) == n - 5:
        while True:
            frag = losuj_fragment()
            if len(frag) < 4:
                haslo += frag
                break

    # szukamy ostatnich fragmentów
    # dla n-4 mamy dwie opcje:
    # albo dobieramy blok o dł 4 albo 2 * 2
    if len(haslo) == n - 4:
        haslo += (
            losuj_fragment_o_dl(2) + losuj_fragment_o_dl(2)
            if random.randint(0, 1)
            else losuj_fragment_o_dl(4)
        )
    else:
        haslo += losuj_fragment_o_dl(n - len(haslo))

    return haslo


POSSIBLE_LENGTHS = (2, 3, 4)


# brute force dla wszystki możliwych kombinacji z powtórzeniem
def losuj2(n: int) -> str:
    # longest number of blocks it could take to create the password
    max_blockcount = math.ceil(n / min(POSSIBLE_LENGTHS))
    # same, but shortest
    min_blockcount = math.ceil(n / max(POSSIBLE_LENGTHS))
    # all possible combinations from min to max number of blocks
    comb_generator = flatten(
        combinations_with_replacement(POSSIBLE_LENGTHS, n)
        for n in range(min_blockcount, max_blockcount + 1)
    )

    # sifting out invalid combinations
    viable_combinations = list(filter(lambda x: sum(x) == n, comb_generator))
    # print(viable_combinations)

    # if I had the list of blocks, I could generate the probability
    # of occurence of each block len combination
    # but for now I'll just take with equal chance
    pass_blocks = list(random.choice(viable_combinations))
    # shuffle blocks around
    random.shuffle(pass_blocks)
    # fetch blocks from module
    haslo_generator = map(losuj_fragment_o_dl, pass_blocks)

    return "".join(haslo_generator)


# brute force oparty na DFS-ie wyszukującym ścieżki o dł 12
def losuj3(n: int) -> str:

    # path musi być tuple, bo lista nie jest hashowalna
    @lru_cache(maxsize=None)
    def find_valid_paths(pass_len: int, path: tuple[int] = tuple()
                         ) -> list[tuple[int]]:
        if pass_len < 0 or pass_len == 1:
            return []
        elif pass_len == 0:
            return [path]
        else:
            return (
                find_valid_paths(pass_len - 2, path + (2,))
                + find_valid_paths(pass_len - 3, path + (3,))
                + find_valid_paths(pass_len - 4, path + (4,))
            )

    viable_combinations = find_valid_paths(n)

    pass_blocks = list(random.choice(viable_combinations))
    # wymieszaj bloki
    random.shuffle(pass_blocks)
    # znajdź bloki o wskazanej długości
    haslo_generator = map(losuj_fragment_o_dl, pass_blocks)

    return "".join(haslo_generator)


# print(*(losuj_haslo(8) for _ in range(10)), sep='\n')
# print(*(losuj2(8) for _ in range(10)), sep='\n')
print(*(losuj3(8) for _ in range(10)), sep="\n")
print(*(losuj3(12) for _ in range(10)), sep="\n")
# print(*(losuj_haslo(12) for _ in range(10)), sep='\n')
