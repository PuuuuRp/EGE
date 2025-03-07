from itertools import *

def f(x):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= ((not C and not A) <= (not D))

OX = [i/5 for i in range(2*5, 110*5)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#21.8 = 22