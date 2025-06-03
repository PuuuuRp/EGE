from itertools import *
al = 'косуф'
for pos, val in enumerate(product(al, repeat=5), 1):
    val = ''.join(val)
    if 'ф' not in val and val.count('у')==2:
        print(pos)
#2313