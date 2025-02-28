from itertools import *
al = sorted('котбус')
c = 0
for v in product(al, repeat=8):
    v = ''.join(v)
    if v[0] not in 'оу' and 'кот' in v:
        c += 1
print(c)
#33516