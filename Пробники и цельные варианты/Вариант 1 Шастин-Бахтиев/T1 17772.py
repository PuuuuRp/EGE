from itertools import *
print(*range(1, 8))
gr = 'АБ АВ ВД ВЕ ВГ ДЕ ЕГ ЕК ГК'.split()
mat = '24 146 56 1267 36 23457 46'.split()

for i in permutations('АБВГДЕК'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#35