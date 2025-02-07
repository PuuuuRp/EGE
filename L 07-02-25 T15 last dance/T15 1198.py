from itertools import *
def f(x):
    b = 18 <= x <= 52
    c = 16 <= x <= 41
    a = a1 <= x <= a2
    return b <= a and ((not c) or a)
res = []
OX = [i/5 for i in range(75, 275)]
for a1,a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#36