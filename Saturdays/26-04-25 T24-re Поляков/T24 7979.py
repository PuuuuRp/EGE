from re import *
with open('24_314.txt') as f:
    st = f.readline()

pat = r'(?<=F)(0[+*])*[1-7][0-7]*([+*](0[+*])*[1-7][0-7]*([+*]0)*)+'
m = [i.group() for i in finditer(pat, st)]
res = []
for i in m:
    l = 0
    s = ''
    for r in range(len(i)):
        if i[r] in '+*':
            num = int(i[l:r], 8)
            s += str(num) + i[r]
            l = r+1
    s += f'{int(i[l:], 8)}'
    s.strip('+*')
    res.append([eval(s), len(i), i])
print(max(res, key=lambda x: (x[1], x[0])))
#142844