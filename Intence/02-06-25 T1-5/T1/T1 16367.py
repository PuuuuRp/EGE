from itertools import *
print(*range(1, 8))
gr = 'EF FD DC CA AG GB BE BA FC'.split()
mat = '246 16 57 15 347 127 356'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#23