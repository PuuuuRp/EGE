from fnmatch import *
res = []
for i in range(2023, 10**8, 2023):
    if fnmatch(str(i), '3?1*57'):
        res.append([i, i//2023])
for i in sorted(res): print(*i)
#321657 159
# 34105757 16859
# 35117257 17359
# 36128757 17859
# 37140257 18359
# 38151757 18859
# 39163257 19359