from fnmatch import *

res = []
for i in range(1234, 10**10, 1234):
    if fnmatch(str(i), '4*5*6') and fnmatch(str(i), '?74*68?'):
        res.append([i, i//1234])
for i in res[::-1]: print(*i)

# 4749516686 3848879
# 4747665686 3847379
# 4745814686 3845879
# 4745197686 3845379
# 4744580686 3844879
# 4741495686 3842379