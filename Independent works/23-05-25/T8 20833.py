from itertools import *
al = '0123456789'

for pos, val in enumerate(range(10**4, 10**5), 1):
    val = ''.join(str(int(i)%2) for i in str(val))
    if '00' not in val and '11' not in val and pos%15==0:
        print(pos)
#88950