from fnmatch import *
a = 210314505
for i in range(a-a%2025, 10**10, 2025):
    if fnmatch(str(i), '21?3*145?5'):
        print(i, i//2025)

# 2123214525 1048501
# 2163714525 1068501
# 2173114575 1073143