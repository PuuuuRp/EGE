from itertools import *
print(*range(1, 9))
gr = 'AE EH HG GC CF FA ED DF DB BH BG'.split()
mat = '23 168 158 578 347 27 456 234'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#31