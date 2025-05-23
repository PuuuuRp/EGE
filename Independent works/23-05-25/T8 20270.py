from itertools import *
al = '0123456'

cnt = 0
for val in product(al, repeat=5):
    val = ''.join(val)
    if val[0]!='0' and \
        sum(val.count(''.join(i)) for i in product('0246', repeat=2))>=2 \
        and sum(val.count(''.join(i)) for i in product('0246', repeat=3))==0:
        cnt += 1
print(cnt)
#576