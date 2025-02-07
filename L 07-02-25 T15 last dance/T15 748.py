from itertools import *
def f(x):
    p = 44 <= x <= 49
    q = 28 <= x <= 53
    a = a1 <= x <= a2
    return a <= p or q
res = []
OX = [i/5 for i in range(100, 300)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(max(res))
#25