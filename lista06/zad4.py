from itertools import groupby
from operator import itemgetter
import string

# import re
# def podziel(text:str) -> list[str]:
#     return re.split(r"\s+", text)


def podziel(text: str) -> list[str]:
    mask = [c not in string.whitespace for c in text]
    grps = groupby(zip(mask, text), key=itemgetter(0))
    # print(list(filter(itemgetter(0), grps)))
    grps_no_spaces = ["".join(map(itemgetter(1), grp)) for _, grp in filter(itemgetter(0), grps)]
    return grps_no_spaces


print("      ala            \nma\tkota\r\nbiałego".split())
print(podziel("      ala            \nma\tkota\r\nbiałego\n\n"))
