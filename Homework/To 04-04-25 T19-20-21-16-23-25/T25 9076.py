from fnmatch import *
for i in range(2023, 10**9, 2023):
    if fnmatch(str(i), '20*23'):
        s = sum(int(x) for x in str(i))
        if s%7==0 and s<20:
            print(i)

# 2023
# 204323
# 2025023
# 20232023
# 202302023