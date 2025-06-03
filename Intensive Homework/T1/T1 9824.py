from itertools import *
print(*range(1, 8))
gr = 'GD DF FA AB BC CE EG ED CA'.split()
mat = '346 45 16 125 247 137 56'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#14