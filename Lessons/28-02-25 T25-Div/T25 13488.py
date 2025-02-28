def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

for n in range(18782, 18823):
    div = d(n)
    nch = [i for i in div if i%2!=0]
    if len(nch) == 3:
        print(*nch)