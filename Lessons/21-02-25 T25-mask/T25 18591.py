from fnmatch import *

for i in range(1984, 10**10, 1984):
    i = str(i)
    if fnmatch(i[1:-2], '9?23?*23') and int(i[0])%2==0\
        and int(i[-2])%2!=0 and int(i[-1])%2==0:
        i = int(i)
        print(i, i//1984)

# 2902302336 1462854
# 4912342336 2475979
# 6922382336 3489104
# 6932302336 3494104
# 8912332352 4492103
# 8942342336 4507229