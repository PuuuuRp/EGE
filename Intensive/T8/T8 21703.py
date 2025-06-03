from itertools import *
al = 'абдеоп'

for pos, val in enumerate(product(al, repeat=6), 1):
    val = ''.join(val)
    if val[0] == 'о' and all(val.count(i)==1 for i in al) and pos%2==0:
        print(pos)
#38306