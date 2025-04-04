for x in range(1, 2031):
    a = 3**100 - x
    c = 0
    while a:
        if a%3==0: c += 1
        a //= 3
    if c==1: print(x)
#1823