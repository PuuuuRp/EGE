from itertools import *
def f(x):
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    A = a1 <= x <= a2
    return (P <= (not Q)) <= (not A)

res = []
OX = [i/5 for i in range(5, 300)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(max(res))
#16