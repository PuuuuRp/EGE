from itertools import *
def f(w, x, y, z):
    return (x <= z) <= y or not w

for a1, a2, a3, a4, a5, a6, a7 in product([1, 0], repeat=7):
    tab = [(1, 0, a1, a2),
           (a3, 1, 0, a4),
           (0, a5, a6, a7)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [0, 0, 0]
            if u: print(*p)
#zxyw