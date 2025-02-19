from itertools import *
print(*range(1, 9))
gr = 'АБ БГ ГЕ ЕЗ ЗЖ ЖД ДГ ГВ ВА АГ ГЗ ГЖ'.split()
mat = '235 13 1245678 36 13 347 368 37'.split()

for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#44