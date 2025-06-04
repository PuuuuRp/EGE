from itertools import *
al = '01234567'
cnt = 0
for v in product(al, repeat=5):
    v = ''.join(v)
    if v[0] != '0' and v.count('6')==1 \
            and all(i+'6' not in v and '6'+i not in v for i in '1357'):
        cnt += 1
print(cnt)
#2961