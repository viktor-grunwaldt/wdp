import random
from collections import Counter, defaultdict as dd
import re

pol_ang = dd(list)

for x in open('data/pol_ang.txt'):
    L = x.strip().split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)

with open("data/brown_corpus.txt", 'r') as f:
    words = f.read()
    words = re.sub(r" [^\w+] ", ' ', words).split()
    
    occurences = Counter(words)


def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            eng_words = pol_ang[s]
            counts = [occurences[w] for w in eng_words]
            most_common = max(counts)
            most_common_words = [w for ct, w in zip(counts,eng_words) if ct == most_common]
            wynik.append(random.choice(most_common_words))
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()

for i in range(15):
    print (tlumacz(zdanie))            
            
