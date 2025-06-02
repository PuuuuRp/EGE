from itertools import *
def f(w, x, y, z):
    return x > y or z == w or z

for a1, a2, a3, a4, a5, a6, a7 in product([1, 0], repeat=7):
    tab = [(0, 0, a1, a2),
           (a3, a4, 1, a5),
           (a6, 1, 0, a7)]
    if len(tab) == len(set(tab)):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [0, 0, 0]
            if u: print(*p)
#zyxw