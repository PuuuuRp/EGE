from itertools import *
def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = a1 <= x <= a2
    return (A and not Q) <= (P or Q)

res = []
OX = [i/5 for i in range(100, 600)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(max(res))
#48