from fnmatch import *

def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

for i in range(333, 10**9, 333):
    if fnmatch(toq(i, 7), '?213*5664'):
        print(i, i//333)

# 24888420 74740
# 371885742 1116774
# 654120891 1964327
# 937155573 2814281