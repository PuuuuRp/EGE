from itertools import *

def f(w, x, y, z): return not(w <= (x == (y or y))) and z <= x

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(a1, 1, 1, a2), (0, a3, a4, 0), (a5, 0, 1, 0)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 1, 1]
            if u: print(*p)
#yxwz