from itertools import *

def f(w, x, y, z): return y <= x and not w and z

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tab = [(1, 0, 1, 1), (1, 0, a1, 1), (a2, a3, a4, 1)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 1, 1]
            if u: print(*p)
#xwyz