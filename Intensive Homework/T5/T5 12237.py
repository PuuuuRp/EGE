for n in range(1, 10000):
    r = bin(n)[2:]
    if n%2==0: r += r[-2:]
    else: r = '1' + r + '0'
    if int(r, 2) < 100: print(n)
#24