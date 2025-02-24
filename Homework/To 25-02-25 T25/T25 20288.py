from itertools import *
ch = '24680'
nch = '13579'
res = []
for r in range(6):
    for z in product(ch, repeat=r):
        z = ''.join(z)
        for v1 in nch:
            for v2 in nch:
                zv = int(f'{z}12{v1}4{v2}')
                if zv%9231==0:
                    res.append([zv, zv//9231])

for i in sorted(res): print(*i)

# 608812143 65953
# 2086012149 225979
# 4440212541 481011
# 6286412541 681011
# 8486012145 919295