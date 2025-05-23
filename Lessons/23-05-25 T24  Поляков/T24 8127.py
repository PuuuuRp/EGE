from re import *
def func(i):
    for l in range(len(i)-1):
        for r in range(len(i)-1, l, -1):
            if int(i[l: r+1], 8)%13==0:
                return [len(i[l: r+1]), int(i[l: r+1]), i[l: r+1]]
    return [0, 0, '']

with open('24-347.txt') as f:
    st = f.readline()

pat = r'[1-7][0-7]+'
m = [i.group() for i in finditer(pat, st)]

res = []
for i in m:
    if int(i, 8)%13==0:
        res.append([len(i), int(i, 8), i])
    else:
        res.append(func(i))
res = sorted(res, key=lambda x: -x[0])

ans = []
for i in res:
    if i[0]==16:
        ans.append(i)
print(st.index(min(ans, key=lambda x: x[1])[2]))
#605381