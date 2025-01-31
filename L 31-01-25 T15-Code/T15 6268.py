from itertools import *
def f(x):
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    A = a1 <= x <= a2
    return ((not B) <= C) <= A
OX = [i/5 for i in range(19*5, 77*5)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#