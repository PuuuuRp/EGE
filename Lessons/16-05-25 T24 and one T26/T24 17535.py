with open('24_17535.txt') as f:
    st = f.readline()

c, m= [0]*2
l = 0
for r in range(1, len(st)):
    if st[r-1:r+1]=='CD': c += 1
    while c>160:
        if st[l:l + 2] == 'CD': c -= 1
        l += 1
    if c==160:
        m = max(m, r-l+1)
print(m)
#9712