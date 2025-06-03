from itertools import *
from string import *
al = '0123456789' + ascii_lowercase

cnt = 0
for val in product(al[:15], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1\
        and sum(val.count(i) for i in al[10:15])>=2:
        cnt += 1
print(cnt)
#83175