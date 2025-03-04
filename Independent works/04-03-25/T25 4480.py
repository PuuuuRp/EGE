def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(800001, 10**12):
    div = d(n)
    u1 = sum(div)%2!=0
    # kal = '*'.join([str(i) for i in div])
    # u2 = eval(kal)
    u2 = 1
    for i in div: u2 *= i
    if u1 and u2%2!=0 and len(div)>10 and c<6:
        print(n, len(div)+2)
        c += 1
    if c==6: break

# 804609 27
# 815409 27
# 826281 15
# 837225 27
# 855625 15
# 859329 15