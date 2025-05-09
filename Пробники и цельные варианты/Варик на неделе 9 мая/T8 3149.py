from itertools import *
al = '0123456789'
cnt = 0
for val in product(al, repeat=5):
    val = ''.join(val)
    if val[0] !='0' and val[-1] not in '347' and \
        all(i*3 not in val for i in al):
        cnt += 1
print(cnt)
#61236