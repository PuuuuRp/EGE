def d(n):
    div = set()
    for i in range(1, round(n**0.5)+1):
        if n%i == 0:
            div |= {i, n//i}
    return sorted(div)

def prime(n):
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

c = 0
for n in range(10**8+1, 10**12):
    div = d(n)
    p = [i for i in div[1:] if prime(i)]
    e = [i for i in div if i%2==0]
    m = abs(sum(p)-sum(e))
    if len(p)==len(e) and c<5:
        c += 1
        print(n, m)
    if c==5: break

