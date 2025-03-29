with open('24_10131.txt') as f:
    st = f.readline()

a, b = [0]*2
m = []
for r in range(len(st)):
    if st[r]=='A': a += 1
    if st[r]=='B': b += 1
    if a==b:
        m.append(r+1)
    if abs(a-b)==1:
        m.append(r)
m = sorted(m)[::-1]
for i in m: print(i)
print(max(m))
#484336