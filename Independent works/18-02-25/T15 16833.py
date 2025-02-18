from itertools import  *
def f(x):
    p = 25 <= x <= 73
    q = 75 <= x <= 118
    a = a1 <= x <= a2
    return (a and not q) <= (p or q)
res= []
OX = [25, 73, 75, 118]
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in range(a1, a2+1)):
        res.append(a2-a1)
print(max(res))
#48