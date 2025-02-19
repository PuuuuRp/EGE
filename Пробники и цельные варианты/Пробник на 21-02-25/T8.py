from itertools import *
al = sorted('КАЛЕЙДОСП')[::-1]

for p, v in enumerate(product(al, repeat=6)):
    v = ''.join(v)
    if v[0]=="К" and v.count('Й')>=2 and\
            all(i not in v for i in 'СЕ') and p%2==0:
        print(p)
        break
#243698