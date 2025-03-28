from itertools import *
def f(x):
    P = 1 <= x <= 98
    Q = 25 <= x <= 42
    A = a1 <= x <= a2
    return Q <= ((not P and Q) <= A)
OX = [i/5 for i in range(5, 500)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#0