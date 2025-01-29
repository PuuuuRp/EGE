from itertools import *
def f(x):
    P = 5 <= x <= 40
    Q = 41 <= x <= 54
    R = 6 <= x <= 53
    A = a1 <= x <= a2
    return not((not P) <= Q and R and not A)
OX = [i/5 for i in range(5, 60*5)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#47