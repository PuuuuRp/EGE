from itertools import *
def f(w, x, y, z, u):
    return (z <= w and y == (not x)) <= (u == (y or z))

for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    tab= [(0, a1, 0, 0, 0), (0,a2, a3, 0, 0), (a4, 0, 0, 0, a5), (0, 0, a6, a7, a8)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyzu'):
            u = [f(**dict(zip(p, t))) for t in tab] == [0, 0, 0, 0]
            if u: print(*p)
#uywzx