def set_of_sum_of_subsets_iter(numbers):
    n = len(numbers)
    possibilities = 2**n
    sums = set()
    for mask in range(possibilities):
        mask_str = "{0:0{1}b}".format(mask, n)
        acc = 0
        for m, num in zip(mask_str, numbers, strict=True):
            if m == "1":
                acc += num
        print(mask_str, numbers, acc)
        sums.add(acc)

    return sums
    # return set(sum(num for m, num in zip(mask.zfill(n), numbers) if m=='1') for mask in map(str, range(possibilities)))


def set_of_sum_of_subsets_comp(numbers):
    make_mask = lambda x: "{0:{1}b}".format(x, len(numbers))
    return set(
        sum(num for m, num in zip(mask, numbers) if m == "1") for mask in map(make_mask, range(2 ** len(numbers)))
    )


print(set_of_sum_of_subsets_comp([1, 2, 3, 100]))


def set_of_sum_of_subsets_rec(numbers):
    if not numbers:
        return {0}
    n = numbers.pop()
    s = set_of_sum_of_subsets_rec(numbers)
    return set(x + n for x in s) | s
    # add_n = lambda x: x + n
    # return set(map(add_n, s)) | s


print(set_of_sum_of_subsets_rec([1, 2, 3, 100]))


def ciagi_niemalejace(a, b, n):
    if n <= 0:
        return [[]]
    l = ciagi_niemalejace(a, b, n - 1)
    return [subseq + [k] for subseq in l for k in range(a, b + 1)]


print(ciagi_niemalejace(0, 3, 3))
# 4**3 opcji
