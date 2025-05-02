def d(n):
    div = set()
    for i in range(1, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return div

st_2 = [2**i for i in range(1, 100)]
cnt = 0
for n in range(10**6+1, 10**12):
    div = d(n)
    if len(div) >= 20:
        u = sum(i in st_2 for i in div) >= 20
        if u:
            cnt += 1
            print(n, sum(i for i in div if i not in st_2 and i!=1 and i!=n))
            if cnt == 5: break

# 1048576 0
# 2097152 0
# 3145728 3145725
# 4194304 0
# 5242880 5242875