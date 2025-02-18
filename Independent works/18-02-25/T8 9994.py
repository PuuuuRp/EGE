from itertools import *
al = sorted('ШКОЛА')
for pos, val in enumerate(product(al, repeat=5), 1):
    val = ''.join(val)
    if val == "ШАЛАШ":
        print(pos)
        break
#2555