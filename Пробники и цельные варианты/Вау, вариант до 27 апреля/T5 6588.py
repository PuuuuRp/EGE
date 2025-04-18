for n in range(1, 1000):
    r = bin(n)[2:]
    r = ''.join([str(int(not int(i))) for i in r])
    r = '1' + r
    r += '1' if r.count('1')%2!=0 else '0'
    r = int(r, 2)
    if r > 180:
        print(n)
        break
#32