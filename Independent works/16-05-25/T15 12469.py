from itertools import *
def f(x):
    D = 7 <= x<= 68
    C = 29 <= x<= 100
    A = a1 <= x<= a2
    return D <= ((not C and not A) <= (not D))

res= []
OA = [i for i in [7, 29, 68, 100]]
OX = [i+1 for i in OA] + [i-1 for i in OA]
for a1, a2 in combinations(OA, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#22