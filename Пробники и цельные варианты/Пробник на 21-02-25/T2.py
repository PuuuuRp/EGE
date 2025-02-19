from itertools import *
def f(x, y, z, w):
    return not(x == (w and not z)) and (y == (x and not w))

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(a1, a2, 0, a3), (a4, 0, a5, 0), (0, a6, 1, 0)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 1, 1]
            if u: print(*p)
#wxyz