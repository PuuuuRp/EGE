from re import *
with open('24_21908.txt') as f:
    st = f.readline()

pat = r'[1-9A-D][0-9A-D]+'
m = [i.group() for i in finditer(pat, st)]

res = []
for i in m:
    if i[-1] in '13579BD':
        for r in range(len(i)-1, 0, -1):
            if i[r] in '02468AC':
                res.append([int(i[:r+1], 14), len(i[:r+1])])
    else:
        res.append([int(i, 14), len(i)])
print(max(res)[1])
#2598