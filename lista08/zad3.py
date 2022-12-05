import numpy as np

alpha = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
alpha_dict = dict(zip(alpha, range(99)))


def frequency_count(s) -> np.array:
    return np.fromiter((s.count(c) for c in alpha), dtype=np.int8)


def main():
    print(frequency_count("ddddaąbbccc"))
    with open("data/popularne_slowa.txt", "r") as f:
        slowa = f.readlines()


if __name__ == "__main__":
    main()
