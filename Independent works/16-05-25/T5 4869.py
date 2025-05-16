for n in range(2, 10000):
    r = bin(n)[2:]
    _1 = r[1::2].count('1')
    _0 = r[::2].count('0')
    r = abs(_1-_0)
    if r==5:
        print(n)
        break
#1023