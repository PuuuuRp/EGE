from itertools import *
gr = 'АБ БГ ГЕ ЕЗ ЗД ДВ ГД БВ ВА'.split()
mat = '67 567 456 35 234 123 12'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕЗ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)