def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0: div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(550001, 551000):
    div = d(n)
    if div and int(sum(div)/len(div))%31==13 and c<5:
        print(n, int(sum(div)/len(div)))
        c += 1
# 550032 28285
# 550040 49117
# 550046 28905
# 550050 19419
# 550066 35725