st = open('24_11954.txt').readline()

m = 10**6
k = l = 0
for i in range(len(st)):
    if st[i] == 'Y':
        k = 0
        l = i+1
    if st[i]=='X': k+=1
    while k>=500:
        m = min(m, i-l+1)
        if st[l]=='X': k-=1
        l+=1
print(m)
#68500