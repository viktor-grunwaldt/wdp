from itertools import groupby
import sys
from zipfile import ZipFile

alpha = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
alpha_dict = dict(zip(alpha, range(99)))

def ceasar(word, shift, decode=False):
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


corpus = read_file().splitlines()
corpus.sort(key=len)
for _, grp in groupby(corpus, key=len):
    
    for word in grp:
        # we assume our dataset is nice and doesn't contain duplicates
        norm = alpha_dict[word[0]]
        