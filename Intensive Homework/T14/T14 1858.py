a = 4*625**9 - 25**15 + 2*5**11 - 7
cnt = 0
while a:
    if a%5==4: cnt += 1
    a //= 5
print(cnt)
#15