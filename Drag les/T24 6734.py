st = open('24_6734.txt').readline()

m = 100000
l = k = 0
for i in range(len(st)):
    if st[i]=='.': k+=1
    while k==7:
        m = min(m, i - l + 1)
        if st[l] == '.': k -= 1
        l+=1
print(m)
#16