with open('24_21717.txt') as f:
    st = f.readline()

m = 10**18
l = 0
rsq= 0
for r in range(2, len(st)):
    if st[r-2: r+1]=='RSQ': rsq += 1
    while rsq>130:
        if st[l: l+3] == 'RSQ': rsq -= 1
        l += 1
    if rsq == 130:
        m = min(m, len(st[l: r]))
print(m)
#497