from itertools import *
def f(w, x, y, z):
    return (w <= (y == z)) and (y == (z <= x))

for a1, a2 in product([0, 1], repeat=2):
    tab = [(a1, 0, 0, 0), (0, a2, 1, 1), (0, 0, 0, 1)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 1, 0]
            if u: print(*p)
#zwyx