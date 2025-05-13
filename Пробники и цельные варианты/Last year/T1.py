from itertools import *
print(*range(1, 9))
gr = 'АБ БД ДЕ ЕЗ ЗГ ГА ЕГ ГЖ ЖД ДВ ВЖ ВА ВГ'.split()
mat = '457 37 267 1678 16 3458 12348 467'.split()

for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#23