from re import *
with open('24_333.txt') as f:
    st = f.readline()

pat = r'\w+(\.\w+)+@(gmail.com|yandex.ru)'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#118