res = []
for x in range(1, 2031):
    a = 7**170 + 7**100 - x
    cnt = 0
    while a:
        if a%7==0: cnt += 1
        a //= 7
    res.append([cnt, x])
print(max(res))
#1715