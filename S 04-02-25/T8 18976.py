from itertools import *
from string import ascii_lowercase
al = '0123456789' + ascii_lowercase

def f(val):
    for i in range(len(val)-1):
        l, t = int(val[i], 20), int(val[i+1], 20)
        if l%2 == t%2: return False
    return True

c =0
for val in product(al[:20], repeat=5):
    val = ''.join(val)
    if val[0]!='0' and int(val[0], 20)+int(val[-1], 20) ==26\
        and f(val): c+=1
print(c)
#1330