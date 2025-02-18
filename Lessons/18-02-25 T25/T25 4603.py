from itertools import *
res= []
for i in range(4):
    for x in product('0123456789', repeat=i):
        num = int('1234' + ''.join(x) + '7')
        if num%141==0:
            res.append([num, num//141])
for i in res:
    print(*i)
# 1234737 8757
# 12341307 87527
# 12342717 87537
# 12344127 87547
# 12345537 87557
# 12346947 87567
# 12348357 87577
# 12349767 87587