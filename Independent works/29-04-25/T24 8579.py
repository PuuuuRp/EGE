from re import *
with open('24_8579.txt') as f:
    st = f.readline()

pat = r'(?<=1|3|5|7|9)[^\d]+(?=0|2|4|6|8)|(?<=0|2|4|6|8)[^\d]+(?=1|3|5|7|9)'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len))+2)
#49