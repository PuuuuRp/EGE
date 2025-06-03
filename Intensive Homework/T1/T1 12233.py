from itertools import *
print(*range(1, 9))
gr = 'EH HG GC CF FA AE ED DF DB BH BG'.split()
mat = '367 568 18 58 247 127 156 234'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#19 + 27 = 46