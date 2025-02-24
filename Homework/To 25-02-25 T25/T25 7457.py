from itertools import *
ch = '2468'
nch = '13579'
res = []
for r in range(6):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for z1 in nch:
            for v in ch:
                zv = int(f'{v}136{z}{z1}')
                if zv%53191 == 0:
                    res.append([zv, zv//53191])

for i in sorted(res): print(*i)

# 8136574079 152969
# 8136680461 152971
# 8136786843 152973
# 8136893225 152975
# 8136999607 152977