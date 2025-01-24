from itertools import *
al = 'ИМНСУ'
res = []
for pos, val in enumerate(product(al, repeat=4), 1):
    val = ''.join(val)
    if sum(val.count(i) for i in 'МНС') >= \
            sum(val.count(i) for i in 'ИУ'):
        res.append(pos)
print(res[-1])
#625