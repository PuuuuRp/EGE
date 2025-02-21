from itertools import *
al = '0123456789'
res = []
for z in al:
    for o in al:
        for v in al:
            zov = int('12'+z+'345'+o+'67089'+v)
            if zov%206 == 0:
                res.append([zov, zov//206])
for i in sorted(res): print(*i)

# 1203458670898 5842032383
# 1223459670896 5939124616
# 1233450670896 5987624616
# 1253451670894 6084716849
# 1273452670892 6181809082
# 1293453670890 6278901315