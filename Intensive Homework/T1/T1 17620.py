from itertools import *
print(*range(1, 8))
gr = 'AF FE EC CG GD DB BA FB ED'.split()
mat = '256 134 267 27 16 135 34'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#53 + 2 = 55