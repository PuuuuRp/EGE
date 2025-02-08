from itertools import *
gr = 'AB BC CF FG GE EA DA DB DC DF DE'.split()
mat = '23567 145 146 23 127 137 156'.split()
print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#65