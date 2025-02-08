from itertools import  *
def f(x):
    p = 69 <= x <= 91
    q = 77 <= x <= 114
    a = a1 <= x <= a2
    return q <= (p == q or (not p) <= a)
res = []
OX = [i/5 for i in range(325, 575)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append((a2-a1))
print(min(res))
#23