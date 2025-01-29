from itertools import *

def f(x):
    P = 257 <= x <= 1000
    Q = 5 <= x <= 100
    R = 99 <= x <= 258
    A = a1 <= x <= a2
    return A <= R and (not (A <= P)) <= Q

OX = [i/3 for i in range(1*3, 1010*3)]
res = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) for x in OX):
        res.append(a2-a1)
print(min(res))
#0.3333333333333144 = 0
#дикий рофл решать это заздание кодом, но я хотел полмучить свой комп