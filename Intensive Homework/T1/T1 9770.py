from itertools import *
print(*range(1, 9))
gr = 'AC CF FD DH HG GA AB BC BE ED'.split()
mat = '56 378 26 68 17 134 258 247'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#18 + 43 = 61