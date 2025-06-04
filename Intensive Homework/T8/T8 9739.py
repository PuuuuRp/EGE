from itertools import *
al = 'агмнсту'

for pos, v in enumerate(product(al, repeat=6), 1):
    v = ''.join(v)
    if v[0] != "у" and v.count('м')==2 and v.count('г')<=1:
        print(pos)
#100810