from itertools import *
print(*range(1, 9))
gr = 'АГ ГЖ ЖЗ ЗД ДВ ВА АБ БВ БГ ГД ЕЖ ЕЗ ЕД'.split()
mat = '256 1458 478 237 126 158 348 2367'.split()

for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#1357