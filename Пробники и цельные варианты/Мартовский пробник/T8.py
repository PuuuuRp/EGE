from itertools import product, repeat
from string import ascii_lowercase
al = 'АИКЛНТУ'

res = []
for pos, val in enumerate(product(al, repeat=6), 1):
    val = ''.join(val)
    if sum(val.count(i) for i in 'АИУ')==1 and val[0]=='Н':
        res.append(pos)
print(res[-1])
#83635
print(int('465555', 7)+1)
#83635