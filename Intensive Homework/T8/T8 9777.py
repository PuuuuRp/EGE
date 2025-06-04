from itertools import *
al = 'екмопртью'

for pos, v in enumerate(product(al, repeat=5), 1):
    v = ''.join(v)
    if pos%2!=0 and v.count('к')==2 and v[0]!='ь':
        print(pos)
#58979