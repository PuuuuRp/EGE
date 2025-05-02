from itertools import *
al = 'абдеоп'
for pos, val in enumerate(product(al, repeat=6), 1):
    if val[0]=='о' and len(set(val)) == len(val) and pos%2==0:
        print(pos)
#38306