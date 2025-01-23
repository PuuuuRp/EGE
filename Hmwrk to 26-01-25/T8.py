from itertools import *
def f(val):
    old = int(val[0], 12)
    for i in val[1:]:
        i = int(i, 12)
        if old%2!=0 and i%2!=0 or old%2==0 and i%2==0:
            return False
        old = i
    return True

c = 0
for val in product('0123456789ab', repeat=7):
    val = ''.join(val)
    if val.count('b') == 2 and f(val): c += 1
print(c)
#51840