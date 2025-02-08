st = open('24_10105.txt').readline()

m = l = k = 0

for i in range(len(st)):
    if st[i] == 'T': k+=1
    while k > 100:
        if st[l] == 'T': k-=1
        l += 1
    if k == 100: m = max(m, i-l+1)
print(m)
#133