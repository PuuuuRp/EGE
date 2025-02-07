from itertools import *
print(*range(1, 9))
gr = 'FC CH HB BE EA AF AB CG GD DH'.split()
mat = '248 157 456 136 23 34 28 17'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#23