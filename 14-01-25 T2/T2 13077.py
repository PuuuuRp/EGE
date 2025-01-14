from itertools import *

def f(w, x, y, z):
    return [w == x and y <= z, (w <= x) <= (y == z)]

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tab = [(1, a1, 1, 1), (a2, 1, 0, 0), (a3, 0, 0, a4)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxzy'):
            u1 = [f(**dict(zip(p, t))) for t in tab] == [[1, 0], [1, 1], [0, 0]]
            u2 = [f(**dict(zip(p, t))) for t in tab] == [[1, 0], [1, 0], [0, 0]]
            if u1 or u2:
                print(*p)
#zywx