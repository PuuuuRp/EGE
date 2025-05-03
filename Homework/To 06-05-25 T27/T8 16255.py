from itertools import *

cnt = 0
for val in product('012345678', repeat=7):
    val = ''.join(val)
    if val[0] not in '01357' and int(val[-1])%3!=0 and '6' in val:
        cnt += 1
print(cnt)
#827352