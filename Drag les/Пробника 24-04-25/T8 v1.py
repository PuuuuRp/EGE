from itertools import *
al = '0123456789abcd'
c = 0
for val in product(al, repeat=8):
    val = ''.join(val)
    if val[0]!='0':
        if val.count('0')==2:
            if sum(val.count(i) for i in 'abcd')<=4:
                c += 1
print(c)
#100115757