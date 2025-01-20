from itertools import *
def f(x, y, z): return not(x == (y <= z))

tab = [(0, 0, 1), (0, 1, 1)]
for p in permutations('xyz'):
    u = [f(**dict(zip(p, t))) for t in tab] == [1, 0]
    if u: print(*p)
#yxz