res = []
for x in range(1, 2031):
    a = 2**2025 + 2**2024 - 2**2021 - x
    c = 0
    while a:
        if a%4==0: c += 1
        a//=4
    res.append([c, x])
res = sorted(res, key=lambda x: (-x[0], -x[1]))
print(res[0])
#1024