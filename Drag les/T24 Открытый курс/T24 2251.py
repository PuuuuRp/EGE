st = open('24_2251.txt').readline()

m = l = 0
k = 0

for i in range(len(st)):
    if st[i] == 'D': k += 1
    while k > 2:
        if st[l] == 'D': k -= 1
        l += 1
    if k <= 2: m = max(m, i-l+1)
print(m)
#373