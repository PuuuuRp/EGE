from itertools import *
def f(w, x, y, z):
    return (z <= (not(y <= x))) or w

for a1, a2, a3, a4, a5, a6, a7 in product([0,1], repeat=7):
    tab = [(a1, 1, a2, a3), (a4, a5, 0, 0), (a6, 0, 1, a7)]
    if len(set(tab)) == len(tab):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in tab] == [0, 0, 0]
            if u:
                print(*p)
#zyxw