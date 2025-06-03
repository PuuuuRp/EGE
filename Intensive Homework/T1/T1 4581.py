from itertools import *
print(*range(1, 8))
gr = 'AD DE EG GC CF FA AB BE BF'.split()
mat = '37 367 125 56 34 247 126'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#13 + 53 = 66