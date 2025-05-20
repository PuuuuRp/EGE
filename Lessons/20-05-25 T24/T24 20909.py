with open('24_20909.txt') as f:
    st = f.readline()

m, l, ab = [0]*3
for r in range(1, len(st)):
    if st[r-1: r+1]=='AB': ab+=1
    while ab>100:
        if st[l: l + 2] == 'AB': ab -= 1
        l += 1
    if ab==100:
        m = max(m, r-l+1)
print(m)
#750