from itertools import *
print(*range(1, 8))
gr = 'АБ БВ ВГ ГД ДЕ ЕБ БЖ ЖА БД ВД'.split()
mat = '346 45 16 12567 24 1347 46'.split()

for i in permutations('АБВГДЕЖ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#47