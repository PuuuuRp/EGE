from itertools import *
al = '012345678'
cnt = 0
for val in product(al, repeat=7):
    val = ''.join(val)
    if val[-1] not in '347' and all(i*3 not in val for i in al) and val[0]!='0':
        cnt += 1
print(cnt)
#2676053