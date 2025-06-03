from itertools import *
print(*range(1, 9))
gr = 'DE EA AH HC CF FG GB BD EB HG'.split()
mat = '38 58 146 36 27 347 568 127'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#6 + 31 = 37