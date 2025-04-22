res = []
for x in range(2, 2026):
    a = 5**2025 + 5**200 - x
    c = 0
    while a:
        if a%5==4: c += 1
        a //= 5
    res.append([c, x])
print(max(res))
#1876