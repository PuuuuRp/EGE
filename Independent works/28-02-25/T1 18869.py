from itertools import *
print(*range(1, 9))
gr = 'EH HA AB BC CD DE EF FC HG GF GA'.split()
mat = '568 36 247 368 178 124 35 145'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#