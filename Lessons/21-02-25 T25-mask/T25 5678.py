from itertools import *
al = '0123456789'

res = []
for r in range(3):
    for y in range(3-r):
        for z in product(al, repeat=r):
            for v in product(al, repeat=y):
                zov = int('124'+''.join(z)+'5'+''.join(v)+'79')
                s = sum(int(i) for i in str(zov) if int(i)%2!=0)
                if zov%s==0:
                    res.append([zov, sum(int(i) for i in str(zov))])
for i in sorted(res): print(*i)

