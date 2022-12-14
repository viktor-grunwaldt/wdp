from collections import Counter
import numpy as np
import numpy.typing as npt
# len = 35
alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż\n"

np_alph = np.array(list(alphabet))
np_alph_as_num = np_alph.view(np.int32)
lookup = np.empty((np_alph_as_num.max() + 1), dtype=np.uint8)

lookup[np_alph_as_num] = np.arange(np_alph.size)
# print(lookup)
a = np.array(list("ź"))
# print(lookup[a.view(np.int32)])

data = np.array(list("kot\nsamolot\nchrząszcz"))
np_slowa = np.array(["kot", "samolot", "chrząszcz"], dtype=np.str_)
# slowa = np.fromstring('kot\nsamolot\nchrząszcz\n', sep='\n', dtype=np.str_)
slowa = ["kot", "samolot", "chrząszcźż"]

# str_to_ints = lambda x: np.array(list(x)).view(np.int32)
str_to_ints = lambda x: np.fromiter(map(ord, x), dtype=np.int32)

k = lookup[data.view(np.int32)]
# https://stackoverflow.com/questions/5274243/split-array-at-value-in-numpy
print(k)
# x = np.where(data == '\n')[0]
# split = np.split(data, x+1)
# print(split)

# keys = lookup[str_to_ints(slowa[1])]
# print(keys)
# # counter = np.zeros(np_alph.size, dtype=np.int8)
# # counter[keys] += 1
# counter = np.histogram(keys, bins=np.arange(np_alph.size))

def np_counter(s:str):
    return np.histogram(lookup[str_to_ints(s)], bins=np.arange(np_alph.size+1))[0]

# v = np.vectorize(np_counter)
ct = np.array(Counter(lookup[str_to_ints(slowa[2])]).most_common()) 
freq = np.zeros(np_alph.size, dtype=np.int32)
freq[ct[:,0]] = ct[:,1]
print(freq)
# print(v(slowa))
print(np_counter(slowa[2]))
# TypeError: only size-1 arrays can be converted to Python scalars

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "/home/vi/Documents/uwr/wdp-listy/lista08/numpy_lookups.py", line 33, in <module>
#     print(v(slowa))
#   File "/home/vi/Documents/code/venv/lib/python3.10/site-packages/numpy/lib/function_base.py", line 2328, in __call__
#     return self._vectorize_call(func=func, args=vargs)
#   File "/home/vi/Documents/code/venv/lib/python3.10/site-packages/numpy/lib/function_base.py", line 2414, in _vectorize_call
#     res = asanyarray(outputs, dtype=otypes[0])
# ValueError: setting an array element with a sequence.
# (ve

# def hist_fn(x):
#     return np.histogram(lookup[x.view(np.int32)], np.arange(len(np_alph)))

# s2 = slowa.view('S1').reshape((slowa.size, -1))
# print(s2[0])
# print(hist_fn(s2[0]))

# hist_vectorized = np.vectorize(hist_fn)
# print(hist_vectorized(s2))
