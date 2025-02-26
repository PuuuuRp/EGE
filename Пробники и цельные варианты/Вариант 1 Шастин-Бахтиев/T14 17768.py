a = 4**644 + 4**322 + 16**35 - 64**3
cnt = 0
while a:
    if a%4==3: cnt += 1
    a //= 4
print(cnt)
#61