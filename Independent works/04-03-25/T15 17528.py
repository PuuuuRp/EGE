from itertools import *
def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    return p <= ((q and not a) <= (not p))

res = []
OA = [0, 15, 21, 40, 63]
OX = [i+1 for i in OA]
for a1, a2 in combinations(OA, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#19