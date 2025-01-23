from itertools import *
print(*range(1, 8))
gr = 'FB BD DE EA AG GF BC CG CE'.split()
mat = '47 57 45 136 236 457 126'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#41