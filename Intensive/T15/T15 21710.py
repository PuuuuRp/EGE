from itertools import *
def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2
    return (not A) <= (B == C)

res = []
OX = [i/5 for i in range(150, 550)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#74