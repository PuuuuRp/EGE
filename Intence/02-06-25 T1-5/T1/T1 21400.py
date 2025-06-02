from itertools import *
print(*range(1, 8))
gr = 'EF FA AB BG GE EC CD DF DA CB'.split()
mat = '457 567 45 136 123 247 126'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#18 + 4 = 22