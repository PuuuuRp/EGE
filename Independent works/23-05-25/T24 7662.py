with open('24_7662.txt') as f:
    st = f.readline()

solo, m, l = [0]*3
for r in range(3, len(st)):
    if st[r-3: r+1] == 'SOLO': solo += 1
    while solo > 4:
        if st[l: l+4] == 'SOLO': solo -= 1
        l += 1
    if solo<=4 and sum(i in st[l: r+1] for i in '0123456789')>=5:
        m = max(m, len(st[l: r+1]))
print(m)
#431