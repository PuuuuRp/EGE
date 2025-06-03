m = 0
for n in range(1, 10000):
    r = bin(n)[2:]
    if n%3==0: r += r[-3:]
    else: r += bin(n%3*3)[2:]
    if int(r, 2) <= 170:
        m = max(m, int(r, 2))
print(m)
#166