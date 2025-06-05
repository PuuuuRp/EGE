for x in range(1, 2031):
    a = 3**100 - x
    cnt = 0
    while a:
        if a%3==0: cnt += 1
        a //= 3
    if cnt==5: print(x)
#2024