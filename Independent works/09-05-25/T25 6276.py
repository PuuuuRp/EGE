from fnmatch import *
for i in range(2023, 10**10+1, 2023):
    if fnmatch(str(i),'1?1?1?1*1') and sum(int(x) for x in str(i))==22:
        print(i)

# 19131511
# 1012141291
# 1319111311
# 1516111051