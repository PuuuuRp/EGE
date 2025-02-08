from itertools import *
def f(x):
    p = 25 <= x <= 240
    q = 175 <= x <= 300
    r = 270 <= x <= 340
    a = a1 <= x <= a2
    return q <= p or (not a) <= r
res = []
OX = [25, 175, 240, 270, 300, 340]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in range(a1, a2+1)):
        res.append(a2-a1)
print(min(res))
#30