from re import *
with open('24_19149.txt') as f:
    st = f.readline()

pattern = r'[(]([1234]+[+][1234]*)+[)]'
match = [i.group() for i in finditer(pattern, st)]
res = []
for i in match:
    if i[-2]!='+':
        if eval(i[1:-1])%2==0:
            res.append([len(i), i])
print(max(res))
#78