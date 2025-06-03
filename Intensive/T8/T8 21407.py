from itertools import *
al = 'дгиашэ'

cnt = 0
for val in product(al, repeat=5):
    val = ''.join(val)
    if val[0] not in 'иаэ' and val[-1] not in 'дгш':
        cnt += 1
print(cnt)
#1944