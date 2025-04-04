# print(int('4567', 8)+1)
#2424
####################################

from itertools import *
al = ''.join(sorted('АРГУМЕНТ'))
#al = '01234567'
for pos, val in enumerate(product(al, repeat=4), 1):
    val = ''.join(val)
    if val in al:
        print(pos)
#2424