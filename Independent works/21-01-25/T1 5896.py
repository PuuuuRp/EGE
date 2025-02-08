from itertools import *
gr = 'АВ ВГ ГД ДБ БЖ ЖА АЗ ЗВ ЗГ ЗД ДЖ'.split()
mat = '256 135 2457 37 1236 157 346'.split()
print(*range(1, 8))

for i in permutations('АБВГДЖЗ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#ВГДБЗАЖ