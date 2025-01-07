from itertools import *
al = sorted('ПРИВЫЧКА')
sl = 'ПРВЧК'
res = []
for pos, val in enumerate(product(al, repeat=5), 1):
    val = ''.join(val)
    if all(i in sl and val.count(i)==1 for i in val) and pos%5 != 0:
        res.append(pos-pos//5)
print(res[0])
#4754