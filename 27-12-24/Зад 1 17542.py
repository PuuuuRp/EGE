from itertools import *

gr = 'AH HC CF FG GB BD DE EA EB GH'.split()
mat = '38 58 146 36 27 347 568 127'.split()
print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] \
           for x,y in gr):
        print(*i)
#37