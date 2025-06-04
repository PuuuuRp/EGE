for x in range(2031):
    a = 6**260 + 6**160 + 6**60 - x
    cnt = 0
    while a:
        if a%6==0: cnt += 1
        a //= 6
    if cnt == 202:
        print(x)
        break
#216