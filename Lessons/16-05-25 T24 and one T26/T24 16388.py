from re import *
with open('24_16388.txt') as f:
    st = f.readline()
pat = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#182