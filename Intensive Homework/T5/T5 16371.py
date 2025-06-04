m = 10**9
for n in range(1, 10000):
    r = bin(n)[2:]
    if n%3==0: r += r[-2:]
    else: r += bin(n%3*3)[2:]
    if int(r, 2) >= 195:
        m = min(int(r, 2), m)
print(m)
#199