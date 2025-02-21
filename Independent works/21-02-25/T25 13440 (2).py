from itertools import *

res = []
for r in range(4):
    for z in product('0123456789', repeat=r):
        for v in '0123456789':
            zov = int('85' + v + '16' + ''.join(z) + '4')
            if zov%2658 == 0:
                res.append([zov, zov//2658])
for i in sorted(res): print(*i)

# 85316484 32098
# 850169274 319853
# 851166024 320228
# 852162774 320603
# 854169564 321358
# 855166314 321733
# 856163064 322108
# 858169854 322863
# 859166604 323238