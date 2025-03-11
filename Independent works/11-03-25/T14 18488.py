for x in range(1, 1000):
    c = 0
    a = 7**666 + 7**333 + 49**x - 343
    while a:
        if a%7==6: c += 1
        a//=7
    if c==49:
        print(x)
        break
#26