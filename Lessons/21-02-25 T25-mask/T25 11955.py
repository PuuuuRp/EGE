from itertools import *
res= []
for r in range(4):
    for z in product('13579', repeat=r):
        for v in '02468':
            zov = int('1'+v+'2157'+''.join(z)+'4')
            if zov%133==0:
                res.append([zov, zov//133])
for i in sorted(res): print(*i)

# 122157574 918478
# 1021575394 7681018
# 1421575554 10688538
# 1821575714 13696058