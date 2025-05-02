for x in range(1, 2006):
    a = 43**56 + 113**841 - x
    ch = 0
    nch = 0
    cnt = 0
    while a:
        if a%4%2==0: ch += 1
        elif a%4%2!=0: nch += 1
        if a%4 == 2: cnt += 1
        a//=4
    if ch%2==0 and nch%2==0 and cnt <= 712:
        print(x)
#2001