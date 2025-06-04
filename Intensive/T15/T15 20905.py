from itertools import *
def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return P <= ((Q and not A) <= (not P))

OX = [i/5 for i in range(17*5, 85*5)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#29