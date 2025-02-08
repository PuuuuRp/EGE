from itertools import *
def f(x):
    P = 23 <= x < 45
    Q = 34 <= x <= 56
    A = a1 <= x <= a2
    return not A or not P and Q

res = []
OX = [i/5 for i in range(20*5, 60*5)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(max(res))
#11