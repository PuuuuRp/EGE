from itertools import *
def f(w, x, y, z):
    return x and not y or x == z or w

for a1, a2, a3, a4 in product([1, 0], repeat=4):
    tab = [(a1, a2, 0, 1),
           (1, 0, a3, 1),
           (1, 1, 0, a4)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [0, 0, 0]
            if u: print(*p)
#yxwz