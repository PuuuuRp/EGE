from itertools import *
al= '0123456'
c = 0
for val in product(al, repeat=5):
    val = ''.join(val)
    if val[0]!='0' and val.count('6')==1 and\
        sum(int(i) for i in val if int(i)%2==0) < sum(int(i) for i in val if int(i)%2!=0):
        c += 1
print(c)
#1390