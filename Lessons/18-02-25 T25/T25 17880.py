from itertools import *
res = []
for r in range(3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            for o in '0123456789':
                zov= int('3'+v+'12'+o+'14'+z+'5')
                if zov%1917==0:
                    res.append([zov, zov//1917])
for i in sorted(res): print(*i)
# 351261495 183235
# 3212614035 1675855
# 3412614645 1780185
# 3712414275 1936575
# 3912414885 2040905