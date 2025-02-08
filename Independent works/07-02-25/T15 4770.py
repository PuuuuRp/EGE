from itertools import *
def f(x):
    p = 35 <= x <= 55
    q = 45 <= x <= 65
    a = a1 <= x <= a2
    return p<=a and (not a) <= (not q)

res = []
OX = [i/5 for i in range(150, 350)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#30