for n in range(1, 13):
    r = bin(n)[2:]
    if n%2==0: r = '10' + r
    else: r = '1' + r + '01'
    print(int(r, 2))
#109