for x in range(1, 10_001):
    a = 6**900 + 6**10 - x
    c3 = 0
    c5  = 0
    while a:
        if a%6==3: c3 += 1
        if a%6==5: c5 += 1
        a //= 6
    if c3==c5: print(x)
#9591