from itertools import *
print(*range(1, 9))
gr = 'FB BE EG GH HC CD DF BA AG AC AD'.split()
mat = '36 478 178 258 46 158 23 2346'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#