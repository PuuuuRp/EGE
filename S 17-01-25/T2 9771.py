from itertools import *
def f(x, y, w, z): return (y <= x) and not z and w

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(1, 0, a1, a2), (1, 1, a3, a4), (a5, 1, 1, a6)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 1, 1]
            if u: print(*p)
#