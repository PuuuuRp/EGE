from string import ascii_lowercase
from itertools import *
al = '0123456789' + ascii_lowercase
c = 0
for val in product(al[:12], repeat=5):
    val = ''.join(val)
    if val[0]!='0' and val.count('7')==1 and\
        sum(val.count(i) for i in al[9:12])<=3:
        c += 1
print(c)
#67476