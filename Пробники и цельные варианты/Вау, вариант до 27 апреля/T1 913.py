from itertools import *
print(*range(1, 8))
gr = 'AE EG GF FB BA AC CE CD DB DF'.split()
mat = '235 146 145 236 137 247 56'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#34