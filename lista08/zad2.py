from collections import Counter


def _letters(s: str) -> dict[str, int]:
    return Counter(s)


def letters(s: str) -> dict[str, int]:
    letters = {}
    for c in s:
        letters[c] = letters.get(c, 0) + 1

    return letters


def is_subset(smaller: str, bigger: str) -> str:
    s_letters = letters(smaller)
    b_letters = letters(bigger)
    return all(val <= b_letters.get(c, -1) for c, val in s_letters.items())


print(is_subset("abc", "abcd"))  # true
print(is_subset("abce", "abcd"))  # false
print(is_subset("aabb", "aaaabcd"))  # false
print(is_subset("", "a"))  # true?
print(is_subset("aaa", "aaa"))  # true
print(is_subset("aabc", "aabbbbccccccc"))  # true
