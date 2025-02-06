with open('24_13715.txt') as f:
    st = f.readline()

m = l = 0
kAB = 0

for i in range(1, len(st)):
    if st[i-1]+st[i] == 'AB': kAB += 1
    while kAB > 50:
        if st[l]+st[l+1] == 'AB': kAB -= 1
        l += 1
    if kAB == 50: m = max(m, i-l+1)
print(m)
#10128