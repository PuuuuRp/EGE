from itertools import *
gr = 'FE ED DC CB BG GF GA AD BA'.split()
mat = '234 156 17 15 246 257 36'.split()
print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)]\
           for x,y in gr):
        print(*i)
#46