def pr(n):
    if n<=1: return False
    for i in range(2, round(n**0.5)+1):
        if n%i==0: return False
    return True

c=0
for n in range(600001, 10**12):
    bef = n-1
    aft = n+1
    if n%6==0 and pr(bef) and pr(aft) and c<6:
        print(bef, aft)
        c += 1
    if c==6: break

# 600071 600073
# 600167 600169
# 600239 600241
# 600317 600319
# 600359 600361
# 600401 600403