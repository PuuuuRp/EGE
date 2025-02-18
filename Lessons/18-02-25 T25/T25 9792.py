from fnmatch import *
res = []
for i in range(1923, 10**8, 1923):
    if fnmatch(str(i), '1*2??76'):
        res.append([i, i//1923])
for i in sorted(res): print(*i)
# 10022676 5212
# 12522576 6512
# 15022476 7812
# 17522376 9112
# 19829976 10312