from itertools import *
al = '0123456789'

res = []
for r in range(5):
    for z in product(al, repeat=r):
        for v in al:
            zov = int('12'+''.join(z)+'34'+v+'5')
            if zov%21025==0 and \
                    sum(1 for p in str(zov) if int(p) % 2 == 0) == \
                    sum(1 for p in str(zov) if int(p) % 2 != 0):
                res.append([zov, zov//21025])
for i in sorted(res): print(*i)

