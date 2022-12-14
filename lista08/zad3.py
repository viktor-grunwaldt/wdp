from collections import defaultdict
import numpy as np
import numpy.typing as npt

# len = 35
alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
dict_alpha = dict(zip(alphabet, range(99)))

np_alph = np.array(list(alphabet))
np_alph_as_num = np_alph.view(np.int32)
lookup = np.empty((np_alph_as_num.max() + 1), dtype=np.uint8)
lookup[np_alph_as_num] = np.arange(np_alph.size + 1)


def frequency_count(s: str) -> npt.NDArray[np.int8]:
    counter = np.zeros(len(alphabet), dtype=np.int8)
    for i in s:
        #     pos = dict_alpha.get(i)
        #     if pos is None:
        #         return None
        counter[dict_alpha[i]] += 1


def np_counter(s: str):
    return np.histogram(lookup[np.array(list(s)).view(np.int32)], bins=np.arange(np_alph.size + 1))[0]
    # num = 0
    # for i in counter:
    #     print(num)
    #     num = (num * 8) + i
    #     # for np.ulonglong
    #     # TypeError: ufunc 'left_shift' not supported for the input types, and the inputs
    #     # could not be safely coerced to any supported types according to the casting rule ''safe''
    #     # num <<= 8

    # return counter


def freq_count_to_str(fr_ct: npt.NDArray[np.int_]) -> str:
    # A common use for nonzero is to find the indices of an array, where a condition is True. Given an array a, the condition a > 3 is a boolean array and since False is interpreted as 0, np.nonzero(a > 3) yields the indices of the a where the condition is true.
    letters_occuring = np.nonzero(fr_ct)
    letter_count = fr_ct[letters_occuring]
    # a lot to unpack here:
    # vstack stacks vectors as rows of matrix
    # .T transposes so that we have shape (2, n)
    # flatten reshapes matrix into a vec of a list (index, count)
    pairs = np.vstack((letters_occuring, letter_count)).T
    return "".join(f"{alphabet[i]}{j}" for i, j in pairs)


def main():
    # x = frequency_count("ddddaąbbccc")
    # print(x)

    # print(freq_count_to_str(x))

    # print(x[np.nonzero(x)])
    # input()

    print("warning: long data, this may take a while...")
    with open("data/slowa.txt", "r") as file:
        slowa = file.read().splitlines()
    # slowa = np.genfromtxt("data/slowa.txt", dtype=np.str_)

    # slowa = f.readlines()
    # rozklady = np.fromiter(map(frequency_count, f.readlines()), dtype=int)
    # https://stackoverflow.com/questions/49566474/converting-numpy-of-string-to-numpy-characters-python
    # see example in numpy_lookups.py

    # np_alph = np.array(list(alphabet))
    # np_alph_as_num = np_alph.view(np.int32)
    # lookup = np.zeros((np_alph_as_num.max()+1), dtype=np.uint8)
    # lookup[np_alph_as_num] = np.arange(len(np_alph))

    print("creating freq counts")
    # create freq arrays
    frequency_arrays = np.array(list(map(frequency_count, slowa)))

    # frequency_arrays = np.histogram(slowa.view(np.))
    print(f"{frequency_arrays.shape=}")
    # i ran highest letter count and it turns out that you don't need 8bit array for freq count
    # since highest letter count is 7, I can just write them as an octal
    # also, there's always 35 letters so size = 35*3= 105 bits
    # EDIT: there's no 128 bit data type in numpy, I'm screwed
    # print("highest letter count: ", np.max(rozklady))

    puzzle = "Bolesław Prus".lower().replace(" ", "")
    freq_puzzle = frequency_count(puzzle)
    # https://numpy.org/doc/stable/user/basics.broadcasting.html
    print("calculating symmetrical pairs")
    missing_letters_arrays = freq_puzzle - frequency_arrays
    # m = sol - w
    # we're looking for such m, that for current w m exists in previous w
    scrambled_words = defaultdict(list)
    pairs = []
    print("finding pairs")
    for w, m, s in zip(frequency_arrays, missing_letters_arrays, slowa):
        w = freq_count_to_str(w)
        m = freq_count_to_str(m)

        if m in scrambled_words and w not in scrambled_words:
            pairs.append((m, w))
        scrambled_words[w].append(s)

    del slowa

    sol = [(scrambled_words[w], scrambled_words[m]) for w, m in pairs]
    print(sol)


if __name__ == "__main__":
    main()
