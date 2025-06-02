from itertools import *
print(*range(1, 8))
gr = 'BD DE EA AC CG GB GF FE FC'.split()
mat = '26 147 456 237 37 13 245'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#39 + 21 = 60