from collections import Counter
from operator import itemgetter
import os
import re
import requests


def get_lalka(filename: str):
    if not os.path.isfile(filename):
        try:
            result = requests.get("https://wolnelektury.pl/media/book/txt/lalka-tom-pierwszy.txt")
            data = result.text
        except Exception as e:
            raise e("fetching the book failed")

        with open(filename, "w") as f:
            f.write(data)
    else:
        with open(filename, "r") as f:
            data = f.read()

    return data


# https://docs.python.org/3/howto/unicode.html#unicode-regular-expressions
# " Similarly, \w matches a wide variety of Unicode characters but only [a-zA-Z0-9_]in bytes
# or if re.ASCII is supplied, and \s will match either
# Unicode whitespace characters or [ \t\n\r\f\v]."
def calc_weight(word, count, alpha: int) -> int:
    return (len(word) * count) ** alpha


def zad3(alpha):
    data = get_lalka("data/lalka.txt")
    # strip unneeded symbols and casefold to remove capitalization problems
    # https://www.w3.org/TR/charmod-norm/#definitionCaseFolding
    data = re.sub(r"[^\w+]", " ", data).casefold()

    # count, calc and order words
    ct = Counter(data.split()).items()
    ordered_words = [(w, calc_weight(w, c, alpha)) for w, c in ct]
    top = sorted(ordered_words, key=itemgetter(1))[-10:]

    # calc str len for text justing
    max_col1, max_col2 = (max(len(str(i)) for i in col) for col in zip(*top))
    print_tabulated = lambda x, y: print(x.rjust(max_col1) + " | " + y.rjust(max_col2))

    # print table
    print_tabulated("word", "weight")
    print("-" * max_col1 + "-+-" + "-" * max_col2)
    for word, weight in reversed(top):
        print_tabulated(word, str(weight))


if __name__ == "__main__":
    zad3(1)
