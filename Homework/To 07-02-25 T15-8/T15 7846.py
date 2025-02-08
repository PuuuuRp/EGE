from itertools import *
def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not((not P) <= Q)) <= (A <= ((not Q) <= P))

res = []
OX = [i/5 for i in range(50, 125)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(max(res))
#10