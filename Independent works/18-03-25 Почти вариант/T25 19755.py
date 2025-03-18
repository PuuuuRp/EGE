def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

def prime(n): return n>1 and not d(n)

c = 0
for n in range(1200001, 10**12):
    div = [i for i in d(n) if prime(i)]
    M = min(div) + max(div) if div else 0
    if M>2000 and M%10==8 and c<5:
        print(n, M)
        c += 1
    if c == 5: break

# 1200005 2248
# 1200011 2388
# 1200037 17978
# 1200067 109108
# 1200197 2598