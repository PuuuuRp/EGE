from itertools import *
def f(w, x, y, z): return x and (z <= y) == w

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(1, a1, 1, a2), (0, a3, 1, 1), (1, 1, 1, a4), (1, 1, 1, a5)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 1, 1, 1]
            if u: print(*p)
#wyxz