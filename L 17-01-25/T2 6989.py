from itertools import *
def f(x, y, z): return x <= (y and z)

tab = [(0, 1, 0), (1, 1, 0)]
for p in permutations('xyz'):
    u = [f(**dict(zip(p, t))) for t in tab] == [0, 0]
    if u: print(*p)
#2