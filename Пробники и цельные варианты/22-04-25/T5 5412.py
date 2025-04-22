cnt = 0
for n in range(1, 10000):
    r = hex(n)[2:]
    if r.count('b')%2==0: r = '1' + r
    else: r += '1'
    r = int(r, 16)
    if 10 <= r <= 99:
        cnt += 1
print(cnt)
#14