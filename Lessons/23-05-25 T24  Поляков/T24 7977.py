from re import *
with open('24-314.txt') as f:
    st = f.readline()

pat = r'([1-5][0-5]*|0)([+*]([1-5][0-5]*|0))+'
m = [i.group() for i in finditer(pat, st)]
m = sorted(m, key=len)[::-1]

res = []
for i in m:
    res.append([len(i), i])
res = max(res)[1]

l = 0
ans = ''
for r in range(len(res)):
    if res[r] in '+*':
        ans += str(int(res[l:r], 6)) + res[r]
        l = r+1
ans += str(int(res[l:], 6))
print(eval(ans)%10**6)
#5513