with open('24_19254.txt') as f:
    st = f.readline()

m = 0
for start in range(len(st)-1):
    for end in range(start+1, len(st)):
        if st[start:end+1].count('FSRQ') == 80:
            m = max(m, len(st[start:end+1]))
            break
print(m)
# не робит