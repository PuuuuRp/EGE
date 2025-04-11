from itertools import *
print(*range(1, 9))
gr = 'АБ БД ДЕ ЕЗ ЗЖ ЖВ ВГ ГА АД ГД ВЗ'.split()
mat = '245 15 478 135 1246 58 38 367'.split()

for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#11