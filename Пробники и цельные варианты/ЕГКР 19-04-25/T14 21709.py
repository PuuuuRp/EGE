res = []
for x in range(1, 3001):
    cnt = 0
    a = 4**210 + 4**110 - x
    while a:
        if a%4==0: cnt += 1
        a//=4
    res.append([cnt, x])
print(sorted(res, key=lambda x: (-x[0], x[1]))[0])
#1024