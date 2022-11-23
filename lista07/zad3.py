from collections import Counter
from operator import itemgetter
import os
import re
import requests


def get_lalka():
    if not os.path.isfile("lalka.txt"):
        try:
            result = requests.get("https://wolnelektury.pl/media/book/txt/lalka-tom-pierwszy.txt")
            data = result.text
        except Exception as e:
            raise e("fetching the book failed")

        with open("lalka.txt", "w") as f:
            f.write(data)
    else:
        with open("lalka.txt", "r") as f:
            data = f.read()

    return data


# https://docs.python.org/3/howto/unicode.html#unicode-regular-expressions
# " Similarly, \w matches a wide variety of Unicode characters but only [a-zA-Z0-9_]in bytes
# or if re.ASCII is supplied, and \s will match either
# Unicode whitespace characters or [ \t\n\r\f\v]."
def calc_weight(word, count, alpha: int) -> int:
    return (len(word) * count) ** alpha


def zad3(alpha):
    data = get_lalka()
    # https://www.w3.org/TR/charmod-norm/#definitionCaseFolding
    data = re.sub(r"[^\w+]", " ", data).casefold()
    # c_words = Counter(data).most_common()
    ordered_words = [(w, calc_weight(w, c, alpha)) for w, c in Counter(data.split()).items()]
    top = sorted(ordered_words, key=itemgetter(1))[-10:]
    # calc str len for text justing
    max_col1, max_col2 = (max(len(str(i)) for i in col) for col in zip(*top))
    print_tabulated = lambda x, y: print(x.rjust(max_col1) + " | " + y.rjust(max_col2))
    # print table
    print_tabulated("word", "weight")
    print("-" * (max_col1 + max_col2 + 5))
    for word, weight in reversed(top):
        print_tabulated(word, str(weight))


if __name__ == "__main__":
    zad3(1)
