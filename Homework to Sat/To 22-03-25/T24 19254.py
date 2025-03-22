with open('24_19254.txt') as f:
    st = f.readline()

#st = 'FSRQ FSRSRQ FSRQ FSRSRQ FSRQ RQ FSRQ FSQ FSRQ FQFSR'
#проверка FSRQ встречается ровно 2 раза

cnt = 0
l = 0
res = []
for r in range(len(st)-3):
    if st[r:r+4]=='FSRQ': cnt+=1
    while cnt>80:
        if st[l: l+4]=='FSRQ': cnt-=1
        l += 1
    if cnt==80: res.append([r-l+1+3, st[l: r+1]])
print(max(res))
#2379