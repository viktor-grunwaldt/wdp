from functools import reduce
import operator
import sys
from zipfile import ZipFile
import itertools as i
from collections import defaultdict as defdict

alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźżvqx"
# freq from: https://www.sttmedia.com/characterfrequency-polish#letters
alphabet_by_freq = "IEAONZRSWYCTDKPMŁJLUBGHĘŻĄÓŚĆFŃŹ".lower()
dict_alpha = dict(zip(alphabet, range(99)))


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


def gen_wordmaps(simplified_query: str, word_count: int):
    # let's assume query has been simplified

    masks = i.product(range(word_count), repeat=len(simplified_query))

    masks = filter(lambda x: len(set(x)) == word_count, masks)
    # use set to remove duplicated pairs
    words = set()
    for mask in masks:
        frags = tuple("".join(c for c, fr in zip(simplified_query, mask) if i == fr) for i in range(word_count))
        # sort to remove duplicate pairs with different order
        words.add(tuple(sorted(frags)))

    print(f"{len(words)} possible anagram permutations found")
    return words


# bolesław prus takes 2 seconds to generate for 3 subwords
# possible_letters = gen_wordmaps("Bolesław Prus", 2)
# print(len(possible_letters))
# possible_words = list(gen_wordmaps("PawełLaskośGrabowski", 2))

# ? name could be incorrect
def word_tokenizer(word: str, size=32) -> int:
    token = 0
    for c in word:
        token |= 1 << dict_alpha[c]

    return token & ((1 << size) - 1)


def find_candidates(corpus, query):

    query_token = word_tokenizer(query)
    # remove words which don't contain queried letters
    is_query_subset = lambda s: (query_token | word_tokenizer(s)) == query_token
    corpus = corpus.split()
    print(len(corpus))
    corpus = list(filter(is_query_subset, corpus))
    return corpus


def simplify_word(s: str) -> str:
    simplified_word = [c for c in s.lower() if c in alphabet]
    simplified_word.sort()
    return "".join(simplified_word)


def unpack_tuples(t: list[tuple[list[str]]]) -> list[tuple[str]]:
    sol = []
    for a, b, c in t:
        chunk = i.product(a, b, c)
        sol.extend(chunk)

    return sol


def find_n_anagrams(query, subword_count):
    corpus = read_file()
    simplified_query = simplify_word(query)

    corpus = find_candidates(corpus, simplified_query)
    print(f"corpus reduced to {len(corpus)} words")

    sorted_words = defdict(list)
    for word in corpus:
        sorted_words["".join(sorted(word))].append(word)

    subqueries = gen_wordmaps(simplified_query, subword_count)

    filtered_subqueries = []
    # remove all words which are not in data
    is_valid = lambda s: s and s in sorted_words
    filtered_subqueries = [slices for slices in subqueries if all(map(is_valid, slices))]

    print("query slice anagrams reduced to:", len(filtered_subqueries))
    # print(filtered_subqueries)
    # find back words
    sol = []
    for slices in filtered_subqueries:
        pairs = tuple(sorted_words[subslice] for subslice in slices)
        sol.append(pairs)

    sol_count = 0
    arithmetic_product = lambda x: reduce(operator.mul, x)
    sol_count = sum(arithmetic_product(map(len, pair_groups)) for pair_groups in sol)

    print(*sol, sep="\n")
    # trojki = unpack_tuples(sol)
    #with open("trojki.txt", "w") as f:
    #    f.write('\n'.join(' '.join(t) for t in trojki))

    print(len(sol))
    print("number of possible tuples found:", sol_count)


def main():
    find_n_anagrams("Bolesław Prus", 3)
    # find_n_anagrams("Wiktor Gruenwaldt", 2)


if __name__ == "__main__":
    main()
