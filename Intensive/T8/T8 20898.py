from itertools import *
al = '012345678'

cnt = 0
for val in product(al, repeat=5):
    val = ''.join(val)
    if val[0]!='0' and val.count('0') == 1\
        and all(i+'0' not in val and '0'+i not in val for i in '1357'):
        cnt += 1
print(cnt)
#5120