from itertools import accumulate
import re


def usun_w_nawiasach(s: str) -> str:
    return re.sub(r"\([^\)]*\)", "", s)


# nawiasy występują w parach, więc można sie pozbyć zamykającego
# za pomocą replace
def usun_ale_nwm_coto_regex(s: str) -> str:
    bracket_value = lambda c: 1 if c == "(" else -1 if c == ")" else 0
    # with list comprehension and the walrus operator
    bracket_mask = list(accumulate(map(bracket_value, s)))

    return "".join(c for c, m in zip(s, bracket_mask) if m == 0).replace(")", "")


test1 = "Ala ma kota (perskiego)!"
print(usun_w_nawiasach(test1))
print(usun_ale_nwm_coto_regex(test1))

test2 = "aaaa(bbbbb)c(ddd)e"
print(usun_w_nawiasach(test2))
print(usun_ale_nwm_coto_regex(test1))
