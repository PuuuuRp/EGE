from itertools import *
al = 'бенрстья'

res = []
for p, v in enumerate(product(al, repeat=5), 1):
    v = ''.join(v)
    if p%2==0 and v[0] == 'р' and 'ь' not in v:
        res.append(p)
print(res[-1])
#16384