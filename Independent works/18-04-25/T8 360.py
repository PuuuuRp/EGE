from itertools import *
al = sorted('инставк')
print(al)
c = 0
for val in product(al, repeat=4):
    val = ''.join(val)
    if val[0] in 'нствк' and val[-1] in 'иа':
        c += 1
        if val == 'ника':
            print(c)
            break
#231