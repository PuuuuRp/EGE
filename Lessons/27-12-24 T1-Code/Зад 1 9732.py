from itertools import *

gr = 'AD DB BF FC CG GA CE GE FE BE'.split()
mat = '47 357 2567 16 236 345 123'.split()
print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] \
           for x,y in gr):
        print(*i)
#25
