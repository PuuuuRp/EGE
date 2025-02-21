from itertools import *
al = '0123456789'
res = []
for z in product(al, repeat=3):
    for v in al:
        zov = int('21'+''.join(z)+'68'+v+'79')
        if zov%1777==0: res.append([zov, zov//1777])
for i in sorted(res): print(*i)

# 2110768579 1187827
# 2135468879 1201727
# 2137068179 1202627
# 2161768479 1216527
# 2186468779 1230427
# 2188068079 1231327