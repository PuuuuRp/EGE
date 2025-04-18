with open('24.5_19717.txt') as f:
    st = f.readline()

m, l = 0, 0
c = 0
for r in range(len(st)):
    if st[r]=='M': m += 1
    while m > 278:
        if st[l]=='M': m -= 1
        l += 1
    if m <= 278:
        c = max(c, r-l+1)
print(c)
#2471