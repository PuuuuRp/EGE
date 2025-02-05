from itertools import *
def f(a, b, c): return a and not b or c

tab = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0,), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
for p in permutations('abc'):
    u = [f(**dict(zip(p, t))) for t in tab] == [0, 1, 1, 1, 0, 0, 1, 1]
    if u: print(*p)
#bca