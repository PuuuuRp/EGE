from itertools import *

gr = 'AF FC CH HB BE EA AB CG GD DH'.split()
mat = '248 157 456 136 23 34 28 17'.split()
print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)]\
           for x, y in gr):
        print(*i)
#23