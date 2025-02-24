from itertools import *
from string import ascii_lowercase
al = '0123456789' + ascii_lowercase

c = 0
for val in product(al[:25], repeat=4):
    val = ''.join(val)
    if val[0]!='0' and\
        sum(i in al[::2] for i in val)==1 and \
            sum(i in al[16:] for i in val)<=2:
        c += 1
print(c)
#77184