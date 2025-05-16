with open('24_10105.txt') as f:
    st = f.readline()

m, l, t = [0]*3
for r in range(len(st)):
    if st[r]=='T': t += 1
    while t>100:
        if st[l]=='T': t-=1
        l += 1
    if t == 100:
        m = max(m, r-l+1)
print(m)
#133