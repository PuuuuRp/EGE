def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

def pr(n):
    return n>1 and not d(n)

cnt = 0
for n in range(32500001, 10**12):
    div = [i for i in d(n) if pr(i)]
    S = sum(div) if div else 0
    if S!=0 and S%145==0:
        print(n, S)
        cnt += 1
        if cnt==7: break

# 32500280 2755
# 32500301 58290
# 32500440 1450
# 32500623 17545
# 32500665 722245
# 32500700 7975
# 32500834 4785