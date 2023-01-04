from itertools import groupby
import sys
from zipfile import ZipFile
from collections import defaultdict as defdict

alpha = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
alpha_dict = dict(zip(alpha, range(99)))


def cesar(word, shift, decode=False):
    if decode:
        shift *= -1
    shifter = str.maketrans(alpha, alpha[shift:] + alpha[:shift])

    return word.translate(shifter)


def read_file():
    with ZipFile("data/sjp-20221023.zip", "r") as zipf:
        print("files in zip: ", zipf.namelist())
        filename = zipf.namelist()[0]
        with zipf.open(filename, "r") as f:
            corpus = f.read().decode("utf-8")

    print("corpus size: ", sys.getsizeof(corpus) // 1024, "KiB")
    # print("word count: ", corpus.count("\n"))
    # word count: 3185486
    print("file opened")
    return corpus


def main():
    corpus = read_file().splitlines()
    corpus.sort(key=len, reverse=True)
    print("words have been sorted")
    found = False
    for l, grp in groupby(corpus, key=len):
        words_normalized = defdict(list)
        for word in grp:
            # we assume our dataset is nice and doesn't contain duplicates
            norm = alpha_dict[word[0]]
            word_norm = cesar(word, norm, decode=True)
            words_normalized[word_norm].append(norm)

        matches = [(k, v) for k, v in words_normalized.items() if len(v) > 1]
        if matches:
            found = True
            break
        else:
            print(f"{len(words_normalized)} words checked, no cesar pairs in {l} length words found.")

    if found:
        for word_norm, shifts in matches:
            decrypted_words = [cesar(word_norm, shift) for shift in shifts]
            print("ceasar group found:", decrypted_words)


if __name__ == "__main__":
    main()
    # words_normalized = defdict(list)
    # grp = ["bąb", "cdc", "cbc", "abc"]
    # for word in grp:
    #     # we assume our dataset is nice and doesn't contain duplicates
    #     norm = alpha_dict[word[0]]

    # print(*words_normalized.items(), sep='\n')
