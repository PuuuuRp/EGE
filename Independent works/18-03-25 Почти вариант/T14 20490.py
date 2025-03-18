for x in range(1, 2006):
    a = 5*4**163 + 12**62 - x
    c1 = 0
    c4 = 0
    while a:
        if a%5==1: c1 += 1
        if a%5==4: c4 += 1
        a//=5
    if c1<c4: print(x)
#2000