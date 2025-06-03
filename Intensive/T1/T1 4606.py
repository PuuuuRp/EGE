from itertools import *
print(*range(1, 9))
gr = 'CE EG GF FA AC CD DH HE AB BF'.split()
mat = '68 47 45 237 368 15 248 157'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#13 + 5 = 18