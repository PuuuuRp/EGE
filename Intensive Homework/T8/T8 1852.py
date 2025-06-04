from itertools import *
al = 'гепард'

cnt = 0
for val in product(al, repeat=5):
    val = ''.join(val)
    if val[0] != 'а' and val[-1] != 'е' and val.count('г')==1:
        cnt += 1
print(cnt)
#2200