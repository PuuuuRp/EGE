from re import *
with open('24_17641.txt') as f:
    st = f.readline()
pat = r'([1-9]\d*|0)([+*]([1-9]\d*|0))+'
m = [i.group() for i in finditer(pat, st)]

def f(i):
    for l in range(len(i)):
        for r in range(len(i)-1, l, -1):
            if i[l] in '*+' or i[r] in '+*':
                continue
            if i[l]=='0' and i[l+1] in '0123456789':
                continue
            if eval(i[l: r + 1]) == 0:
                return len(i[l: r+1])
    return 0

x = 0
for i in m:
    if eval(i)==0:
        x = max(x, len(i))
    else:
        x = max(x, f(i))
print(x)
#142