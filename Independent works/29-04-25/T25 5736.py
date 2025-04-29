def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

cnt = 0
for n in range(10**9+1, 10**18):
    if str(n)==str(n)[::-1]:
        div = d(n)
        m = max(div) if div else 1
        if m%7==0:
            cnt += 1
            print(n, m)
    if cnt == 5: break

# 1001771001 333923667
# 1002002001 334000667
# 1003003001 143286143
# 1004774001 334924667
# 1005005001 335001667