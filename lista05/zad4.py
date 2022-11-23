from itertools import groupby
from operator import itemgetter
from string import ascii_lowercase as alc


def wsk():
    w = "zbman mnzvravp yvfgr an yvfgr cne mnjvrenwnplpu jnegbfp j\
beltvanyarw yvfpvr v cbmlpwr, anfgrcavr gr yvfgr cbfbegbjnp, hfhanp qhcyvxngl jnegbfpv v cbfbeg-\
bjnp wrfmpmr enm mr jmtyrqh an cbmlpwr."
    translator = dict(
        zip(
            alc[13:] + alc[:13],
            alc,
        )
    )
    decoded = "".join(translator.get(c, c) for c in w)
    print(decoded)


def dedup(lst: list[any]) -> list[any]:
    # generate pairs and sort them
    sorted_pairs = sorted(enumerate(lst), key=itemgetter(1))
    # groupby item in array and return only the first ones
    grps = (next(group) for _, group in groupby(sorted_pairs, key=itemgetter(1)))
    # sort by index (to preserve order) and return items
    return list(map(itemgetter(1), sorted(grps, key=itemgetter(0))))


wsk()
l = dedup([1, 2, 3, 1, 2, 3, 8, 2, 9, 9, 4])
print(l)
