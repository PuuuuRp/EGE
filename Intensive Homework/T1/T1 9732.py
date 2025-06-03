from itertools import *
print(*range(1, 8))
gr = 'FC CG GA AD DB BF CE FE BE GE'.split()
mat = '47 257 2567 16 236 345 123'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#25