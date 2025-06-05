from fnmatch import *
for i in range(2025, 10**8+2, 2025):
    if fnmatch(str(i), '12*34?5'):
        print(i, i//2025)

#1253475 619
# 12103425 5977
# 12593475 6219
# 12913425 6377