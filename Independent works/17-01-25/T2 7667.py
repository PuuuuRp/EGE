from itertools import *
def f(a, b, c, d): return (a <= b) == c or not d and d <= (not a)

for a1, a2, a3,a4, a5, a6, a7, a8, a9 in product([0, 1], repeat=9):
    tab = [(0, a1, a2, a3), (a4, a5, 0, a6), (0, a7, a8, 0), (0, a9, 0, 0)]
    if len(set(tab)) == len(tab):
        for p in permutations('abcd'):
            u = [f(**dict(zip(p, t))) for t in tab] == [0, 0, 0, 0]
            if u: print(*p)
