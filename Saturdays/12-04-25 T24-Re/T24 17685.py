from re import *
with open('24_17685.txt') as f:
    st = f.readline()

pattern = r'([0-9]+[+*][0-9]*)+'
match = [i.group() for i in finditer(pattern, st)]

res = []
for i in match:
    if i[-1] not in '+*':
        if eval(i)==0:
            res.append([len(i), i])
    else:
        if eval(i[:-1])==0:
            res.append([len(i[:-1]), i])
print(max(res))
#