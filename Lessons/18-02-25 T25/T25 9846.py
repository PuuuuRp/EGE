from itertools import *
al = '0123456789'
res = []
for r in range(3):
    for z in [''.join(i) for i in product(al, repeat=r)]:
        for v in al:
            zov = int('12'+z+'34'+v+'5')
            if zov%2025==0:
                res.append([zov, zov//2025])
for i in sorted(res): print(*i)
# 1253475 619
# 12103425 5977
# 12593475 6219
# 12913425 6377