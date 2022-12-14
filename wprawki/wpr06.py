import sys
from collections import defaultdict as defdict


try:
    with open(sys.argv[1], "r") as f:
        d = defdict(set)
        letters = set()
        for line in f.readlines():
            lang_id, text = line.strip().replace(' ', '').split(":")
            letters |= set(text)
            d[lang_id] |= set(text)

        d_letters = defdict(list)
        for letter in letters:
            for lang_id in d.keys():
                if letter in d[lang_id]:
                    d_letters[letter].append(lang_id)

        letters_by_langs = defdict(str)

        for letter, langs in d_letters.items():
            langs_str = " ".join(sorted(langs))
            letters_by_langs[langs_str] += letter

        letters_by_langs_ordered = sorted(
            letters_by_langs.items(),
            key=lambda x: len(x[0]),
            reverse=True,
        )
        for a, b in letters_by_langs_ordered:
            print(a, ":", b, sep='')

except IOError as ioe:
    print("error with file handling")
    # raise ioe
except IndexError as ioe:
    print("please enter input file as param!")
    # raise ioe
