from itertools import *

gr = 'AC CF FD DH HG GA AB CB BE ED'.split()
mat = '56 378 26 68 17 134 258 247'.split()
print(*range(1,9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] \
           for x,y in gr):
        print(*i)
#61