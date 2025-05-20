with open('24_19254.txt') as f:
    st = f.readline()

m, l, f = [0]*3
for r in range(3, len(st)):
    if st[r-3: r+1]=='FSRQ': f+=1
    while f>80:
        if st[l: l+4] == 'FSRQ': f -= 1
        l += 1
    if f==80:
        m = max(m, r-l+1)
print(m)
#2379