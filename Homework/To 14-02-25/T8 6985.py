from itertools import *
al = 'АКЛМРС'
for pos, val in enumerate(product(al, repeat=6), 1):
    val = ''.join(val)
    if val == 'СССРМЛ':
        print(pos)
        break
#46605