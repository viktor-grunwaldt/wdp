from itertools import groupby
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


def zad3():
    # casefold to remove capitalization problems
    # https://www.w3.org/TR/charmod-norm/#definitionCaseFolding
    data = get_lalka("data/lalka.txt").casefold()

    # import list of polish words
    with open("data/popularne_slowa.txt", "r") as f:
        polish_words = set(f.read().casefold().split())

    has_no_funky_letters = lambda s: re.search(r"[ąćęłńóśźż]", s) is None
    requirements =  lambda s: has_no_funky_letters(s) and s in polish_words
    word_len =      lambda s: len(re.sub(r"[^\w+]", "", s))
    sentence_len =  lambda l: sum(map(word_len, l))

    grps = groupby(data.split(), key=requirements)
    top10 = sorted((list(grp) for i, grp in grps if i), key=sentence_len, reverse=True)[:10]
    # print(*p[:10], sep='\n')

    # print table
    for sentence in top10:
        print(" ".join(sentence), end="\n\n\n")


if __name__ == "__main__":
    zad3()
