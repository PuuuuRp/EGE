from itertools import *

gr = 'AF FE EC CG GD DB FB ED BA'.split()
mat = '256 134 267 27 16 135 34'.split()
print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] \
           for x,y in gr):
        print(*i)
#55