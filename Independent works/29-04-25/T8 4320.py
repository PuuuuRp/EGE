from itertools import *
al = '01234567'
c = 0
for val in product(al, repeat=6):
    val = ''.join(val)
    poo = [i for i in val]
    if val[0]!='0' and len(set(poo)) == len(poo)\
        and all(''.join(i) not in val for i in product('0246', repeat=2))\
        and all(''.join(i) not in val for i in product('1357', repeat=2))\
        and int(val, 8)%5==0:
        c += 1
print(c)
#208