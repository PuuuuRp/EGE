from itertools import *
al = '01234'

c = 0
for val in product(al, repeat=6):
    val = ''.join(val)
    if val[0]=='3' and int(val, 5)%2==0:
        c += 1
print(c)
#1562