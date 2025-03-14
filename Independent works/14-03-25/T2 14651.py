from itertools import *
def f(w, x, y, z): return (z <= x) == (w <= y) or (x and w)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(a1, a2, a3, 1), (a4, a5, 1, 1), (a6, 1, 1, 1)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [0, 0, 0]
            if u: print(*p)
#xwyz