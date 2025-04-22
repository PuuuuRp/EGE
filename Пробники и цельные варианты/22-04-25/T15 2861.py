from itertools import *
def f(x):
    P = 69<=x<=91
    Q = 77<=x<=114
    A = a1 <= x <= a2
    return Q <= (P == Q or (not P) <= A)
OX = [i/5 for i in range(65*5, 115*5)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#23