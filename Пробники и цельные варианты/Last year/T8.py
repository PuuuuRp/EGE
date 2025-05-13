from itertools import *

cnt = 0
for val in product('012345678', repeat=9):
    val = ''.join(val)
    if '0' not in val and all(val.count(i)<=3 for i in '012345678'):
        _ = [int(i)%2 for i in val]
        if '11' not in _ and '00' not in _:
            cnt += 1
print(cnt)
#114723840