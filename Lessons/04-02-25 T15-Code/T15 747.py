from itertools import *
def f(x):
    P = 43 <= x <= 49
    Q = 43 <= x <= 53
    A = a1 <= x <= a2
    return A <= P or Q

res = []
OX = [40, 43, 44, 49, 53, 55]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in range(a1, a2+1)):
        res.append(a2-a1)
print(max(res))
#10