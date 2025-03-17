from fnmatch import *
def d(n):
    div = set()
    for i in range(1, round(n**.5)+1):
        if n%i == 0:
            div |= {i, n//i}
    return div

c = 0
for n in range(65001, 10**12):
    div = [i for i in d(n) if i%2==0]
    if fnmatch(str(n), '6*97*5?') and len(div)>=4 and c<7:
        print(n, sum(div))
        c += 1
    if c==7: break

# 69750 129792
# 69752 122080
# 69756 139536
# 69758 75152
# 609750 1103232
# 609752 1291248
# 609754 630840