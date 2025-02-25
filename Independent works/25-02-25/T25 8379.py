from itertools import *
al = '0123456789'

res = []
for r in range(7):
    for z in product(al, repeat=r):
        z = ''.join(z)
        s = sum(int(i) for i in z)**3
        v = int(f'1234{z}')
        if v%137==0 and int(z)%s==0:
            res.append(v)
for i in sorted(res): print(i)