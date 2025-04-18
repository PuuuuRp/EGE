res = []
for x in range(2, 2026):
    cnt = 0
    a = 5**2025 + 5**200 - x
    while a:
        if a%5==4: cnt += 1
        a //= 5
    res.append([cnt, x])
print(sorted(res, key=lambda x: (x[0], x[1]))[-1])
#1876