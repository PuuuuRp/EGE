from itertools import *

def f(x):
    P = 254 <= x <= 800
    Q= 410 <= x <= 823
    A = a1 <= x <= a2
    return (P and not A) <= Q

res = []
OA = [254, 410, 800, 823]
OX = [i+1 for i in OA] + [i-1 for i in OA]
for a1, a2 in combinations(OA, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#156