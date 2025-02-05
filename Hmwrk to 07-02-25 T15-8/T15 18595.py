from itertools import *
def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = a1 <= x <= a2
    return (not (C or J)) <= (not A)

res = []
OX = [i/5 for i in range(200, 550)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(max(res))
#52