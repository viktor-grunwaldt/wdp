from collections import Counter, defaultdict
import hashlib
import numpy as np
# len = 35
alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

np_alph = np.array(list(alphabet))
np_alph_as_num = np_alph.view(np.int32)
lookup = np.empty((np_alph_as_num.max() + 1), dtype=np.uint8)

lookup[np_alph_as_num] = np.arange(np_alph.size)

# data = np.array(open("data/slowa.txt", 'r').read())
parent = "bolesław prus".replace(' ', '')
letters = np.array(list(parent))
ords = lookup[letters.view(np.int16)]
parent_freqs = np.histogram(ords, bins=np.arange(np_alph.size+1))[0]
# ct = np.array(Counter(ords).most_common(),dtype=np.int32)
# daddy_freqs = np.zeros(np_alph.size, dtype=np.int16)
# print(ct[:,0])
# print(lookup[ct[:,0]])
# daddy_freqs[lookup[ct[:,0]]] = ct[:,1]

seen_words = defaultdict(list)
pairs = []

with open('data/slowa.txt', 'r') as f:
    for word in f.readlines():
        word = word.strip()
        letters = np.array(list(word))
        ords = lookup[letters.view(np.int16)]

        # ct = np.array(Counter(ords).most_common())
        # freqs = np.zeros(np_alph.size+1, dtype=np.int32)
        # freqs[ct[:,0]] = ct[:,1]
        
        freqs = np.histogram(ords, bins=np.arange(np_alph.size+1))[0]
        # print( freqs != ct)
        inverse_freq = parent_freqs - freqs
        if np.any(inverse_freq<0):
            continue
        
        hashed_freq = hashlib.sha1(freqs.view(np.uint8)).hexdigest()
        hashed_inv = hashlib.sha1(inverse_freq.view(np.uint8)).hexdigest()
        
        if hashed_inv in seen_words and hashed_freq not in seen_words:
            pairs.append((hashed_freq, hashed_inv))
        
        seen_words[hashed_freq].append(word)
        
sol = [((seen_words[h_word]),seen_words[h_inv]) for h_word, h_inv in pairs]
print(sol)
