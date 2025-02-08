for x in range(1, 5556):
    a = 5**150 + 5**135 - x
    c = 0
    while a:
        if a%5 == 4:
            c += 1
        a //= 5
    if c == 134:
        print(x)
#3126