from itertools import *
res = []
for i in range(3):
    for x in product('0123456789', repeat=i):
        arr = [int('12' + ''.join(x) + '4' + str(j) + '65') for j in '0123456789']
        for j in arr:
            if j%161==0:
                res.append([j, j // 161])
for i in res: print(*i)
# 1234065 7665
# 12004965 74565
# 12214265 75865
# 12294765 76365
# 12504065 77665
# 12584565 78165
# 12874365 79965
# 12954865 80465