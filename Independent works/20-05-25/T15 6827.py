from itertools import *
def f(x):
    P = 257 <= x <= 1000
    Q = 5 <= x <= 100
    R = 99 <= x <= 258
    A = a1 <= x <= a2
    return A <= R and ((not A) <= P) <= Q
res = []
OA = [i for i in [5, 99, 100, 257, 258, 1000]]
OX = [i+1 for i in OA] + [i-1 for i in OA]
for a1, a2 in combinations(OA, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#0