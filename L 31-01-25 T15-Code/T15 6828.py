from binascii import a2b_qp
from itertools import *
def f(x):
    P = 257 <= x <= 356
    Q = 5 <= x <= 600
    R = 59 <= x <= 228
    A = a1 <= x <= a2
    return not R or A or x%3==0 and not P or not Q
OX = [i for i in range(0, 610)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#168