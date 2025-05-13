with open('24_9753.txt') as f:
    st = f.readline()

m, y, l = [0]*3

for r in range(len(st)):
    if st[r]=='Y': y += 1
    while y > 150:
        if st[l] == 'Y': y -= 1
        l += 1
    if y<=150:
        m = max(m, r-l+1)
print(m)
#244