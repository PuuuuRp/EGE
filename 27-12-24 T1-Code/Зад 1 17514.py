from itertools import *

gr = 'AB BH HF FD DC CE EA AH EG GF GC'.split()
mat = '247 148 578 126 38 47 136 235'.split()
print(*range(1,9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] \
           for x,y in gr):
        print(*i)
#38