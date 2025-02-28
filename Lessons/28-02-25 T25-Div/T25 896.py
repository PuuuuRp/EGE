def pr(n):
    for i in range(2, round(n**0.5)+1):
        if n%i==0: return False
    return True

c = 1
for pos, n in enumerate(range(194441, 196501), 1):
    if pr(n) and n%100==93:
        print(c, n)
        c += 1

# 1 195193
# 2 195493
# 3 195593
# 4 195893
# 5 196193