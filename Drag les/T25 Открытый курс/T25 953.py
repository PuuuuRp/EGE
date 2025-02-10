def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

def IsPrime(n): return not d(n)

c = 0
for n in range(500_000-1, 400_000, -1):
    div = [i for i in d(n) if IsPrime(i)]
    s = sum(div)
    if s!=0 and s%10==0 and c<7:
        c += 1
        print(n, s)
# 499996 2560
# 499995 320
# 499994 22740
# 499989 860
# 499981 13550
# 499971 166660
# 499959 18520