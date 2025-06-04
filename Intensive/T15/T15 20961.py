from itertools import *
def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = a1 <= x <= a2
    return (Q <= (((not A) and P) <= (not Q)))

OA = [15, 38, 142, 167]
OX = [i+0.5 for i in OA] + [i-0.5 for i in OA]
res = []
for a1, a2 in combinations(OA, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#104