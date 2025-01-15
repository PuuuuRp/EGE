from itertools import *
from string import ascii_lowercase
al = '0123456789' + ascii_lowercase

cnt = 0
for val in product(al[:16], repeat=5):
    val = ''.join(val)
    if val.count('6') == 2 and \
            all(i+'6' not in val for i in '02468ace') and \
            all('6'+i not in val for i in '02468ace') and\
            val[0]!='0':
        cnt += 1
print(cnt)
#4352