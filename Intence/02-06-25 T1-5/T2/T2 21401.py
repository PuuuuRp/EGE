from itertools import *
def f(w, x, y, z):
    return x and z <= w and not y

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    tab  = [(a1, a2, 1, a3),
            (a4, 1, 0, a5),
            (1, 0, a6, a7)]
    if len(tab) == len(set(tab)):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 1, 1]
            if u: print(*p)
#xwzy