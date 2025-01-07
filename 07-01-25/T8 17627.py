from string import ascii_lowercase
from itertools import *
al = '0123456789' + ascii_lowercase

c = 0
for val in product(al[:15], repeat=5):
    val = ''.join(val)
    if val.count('8') == 1 and val[0]!='0' and \
            sum(val.count(i) for i in 'abcde' if i in val) >= 2:
        c += 1
print(c)
#83175