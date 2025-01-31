from itertools import *
def f(x):
    P = 35 <= x <= 55
    Q = 45 <= x <= 65
    A = a1 <= x <= a2
    return P <= A and (not A) <= (not Q)
OX = [i/5 for i in range(30*5, 70*5)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#30