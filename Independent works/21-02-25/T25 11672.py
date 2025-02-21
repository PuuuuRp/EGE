from fnmatch import *
for i in range(21025, 10**10, 21025):
    if fnmatch(str(i), '12*34?5') and\
            sum(1 for p in str(i) if int(p)%2==0) ==\
            sum(1 for p in str(i) if int(p)%2!=0):
        print(i, i//21025)

