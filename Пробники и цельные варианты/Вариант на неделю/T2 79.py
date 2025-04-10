from itertools import *

def f(x, w, y, z):
    return not w and (y or z) <= (not x and y)

for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    tab = [(a1, a2, a3, 1), (a4, a5, 1, a6), (a7, 1, 1, a8)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 1, 1]
            if u: print(*p)
#wzyx