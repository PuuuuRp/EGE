from itertools import *
def f(w, x, y, z):
    return (z == (not x)) <= (w <= (not y) and y<=x)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(1, 1, 1, 0), (a1, a2, 0, 0), (a3, 0, a4, a5)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [1, 0, 0]
            if u: print(*p)
#yzxw