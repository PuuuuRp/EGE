from itertools import *
print(*range(1, 9))
gr = 'АБ БД ДГ ГЖ ЖЗ ЗЕ ЕВ ВА БВ ДЕ ДЖ ЖЕ'.split()
mat = '3578 346 1258 26 13 248 18 1367'.split()

for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x)+1) in mat[i.index(y)] for x, y in gr):
        print(*i)
#15