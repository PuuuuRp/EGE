from itertools import *
def f(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    A = a1 <= x <= a2
    return A <= P or Q

res = []
OX = [0, 12, 26, 30, 53, 60]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in range(a1, a2+1)):
        res.append(a2-a1)
print(max(res))
#23