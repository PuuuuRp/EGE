with open('24_14502.txt') as f:
    st = f.readline()

l = 0
res = 10**18

for r in range(len(st)):
    while len(set(st[l:r+1])) == 26:
        res = min(res, len(st[l:r + 1]))
        l += 1
print(res)
#440
#P.S. работает ппц как долго