from itertools import *
def f(val):
    for i in '02468a':
        val = val.replace(i, '0')
    for i in '13579b':
        val = val.replace(i, '1')
    if val == '1010101' or val == '0101010':
        return True
    return False

c = 0
for val in product('0123456789ab', repeat=7):
    val = ''.join(val)
    if val.count('b') == 2 and f(val) and val[0]!='0': c += 1
print(c)
#48600