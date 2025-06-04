from itertools import *
al = '012345678'
cnt = 0
for v in product(al, repeat=5):
    v = ''.join(v)
    if v[0] not in '01357' and v[-1] not in '18'\
        and v.count('3') <= 1:
        cnt += 1
print(cnt)
#18944