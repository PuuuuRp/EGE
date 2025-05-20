with open('24_19489.txt') as f:
    st = f.readline()
m = 0
w = 0
l = 0
nw = 0
for r in range(2, len(st)):
    if st[r-2: r+1]=='WWF': w += 1
    if st[r - 4: r + 1] == 'WSFWW': nw += 1
    while w > 120 or nw:
        if st[l: l+3]=='WWF': w-=1
        if st[l: l+5] == 'WSFWW': nw -= 1
        l += 1
    if w<=120:
        m = max(m, r-l+1)
print(m)
#3072