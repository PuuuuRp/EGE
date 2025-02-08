from itertools import *
from string import ascii_lowercase
al = '0123456789' + ascii_lowercase

c = 0
for val in product(al[:9], repeat=7):
    val = ''.join(val)
    if all(val[0] != i for i in '0246') and \
        all(val[-3:] != i*3 for i in al[:9]):
        c += 1
print(c)
#2624400