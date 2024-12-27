from itertools import *
gr = 'AB BE AD DE AF FC CG EG BF'.split()
mat =  '37 367 125 56 34 247 126'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)