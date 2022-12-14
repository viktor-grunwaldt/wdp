def by_sort(s):
    s.sort()

alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
dict_alpha = dict(zip(alphabet, range(99)))

def by_dict(s):
    dd = dict()
    for c in s:
        v = dd.get(c, 0)
        dd[c] = v+1

    for k,v in 