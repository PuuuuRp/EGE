def d(n):
    div = set()
    for i in range(1, round(n**0.5)+1):
        if n%i==0: div |= {i, n//i}
    return sorted(div)

for n in range(190201, 190261):
    div = d(n)
    ch = [i for i in div if i%2==0]
    if len(ch)==4:
        print(ch[-1], ch[-2])
# 190226 838
# 190234 17294
# 190238 2606
# 190252 95126
# 190258 758