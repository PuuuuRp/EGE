from itertools import *
gr = 'BC CD DF FG GE EF ED EC BA AC AD'.split()
mat = '347 3456 1245 1237 236 25 14'.split()
print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr): print(*i)
#42