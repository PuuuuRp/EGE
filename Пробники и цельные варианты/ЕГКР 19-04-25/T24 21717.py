with open('24_21717.txt') as f:
    st = f.readline()

st = st[::-1]
RSQ, l = [0]*2
res = []
for r in range(2, len(st)):
    if st[r-2:r+1]=='QSR': RSQ += 1
    while RSQ>130:
        if st[l:l+3]=='QSR': RSQ -= 1
        l += 1
    if RSQ == 130: res.append([len(st[l:r+1]), st[l:r+1]])
print(min(res))
#498 - 1 = 497