from fnmatch import *

def prime(n):
    for i in range(2, round(n**.5)+1):
        if n%i==0: return 0
    return 1

for i in range(301111, 10**7+1):
    if prime(i):
        if fnmatch(str(i), '3?1111*'):
            print(i)

# 311111
# 361111
# 3011117
# 3011119
# 3311117
# 3611119
# 3811117
# 3911111