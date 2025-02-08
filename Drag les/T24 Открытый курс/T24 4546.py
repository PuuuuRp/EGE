st = open('24_4546.txt').readline()

m = [0]*len(st)
for i in range(2, len(st)):
    if st[i-2]+st[i] == 'AA' or st[i-2]+st[i] == 'CC':
        m[i] = m[i-3]+1
print(max(m))
#21