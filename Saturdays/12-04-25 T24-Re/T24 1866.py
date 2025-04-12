from re import *
with open('24_1866.txt') as f:
    st = f.readline()

pattern = r'(?<=ad|da)\w+?(?=ad|da)'
match = finditer(pattern, st)
m = [i.group() for i in match]
print(len(max(m, key=len))+2)
#2252