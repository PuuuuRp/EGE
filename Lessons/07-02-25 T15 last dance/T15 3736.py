from itertools import *
def f(x):
    p = 117 <= x <= 158
    q = 129 <= x <= 180
    a = a1 <= x <= a2
    return p <= ((q and not a) <= (not p))
res= []
OX = [i/5 for i in range(500, 950)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#29