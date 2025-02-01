from itertools import *
def f(x):
    P = 15 <= x <= 33
    Q = 35 <= x <= 48
    A = a1 <= x <= a2
    return (A and not Q) <= (P or Q)

res = []
OX = [i/5 for i in range(50, 250)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(max(res))
#18