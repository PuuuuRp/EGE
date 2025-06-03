from itertools import *
print(*range(1, 8))
gr = 'АБ БГ ГЕ ЕЗ ЗД ДВ ВА БВ ГД'.split()
mat = '67 567 456 35 234 123 12'.split()

for i in permutations('АБВГДЗЕ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#9 + 12 = 21