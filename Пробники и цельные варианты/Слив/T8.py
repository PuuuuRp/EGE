from itertools import *
al = 'дгиашэ'
c = 0
for val in product(al, repeat=5):
    val = ''.join(val)
    if val[0] in 'иаэ' or val[-1] in 'дгш': continue
    else: c += 1
print(c)
#1944