from fnmatch import *
def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return div

for n in range(400_000, 500_001):
    div = [i for i in d(n) if fnmatch(str(i), '*7?')]
    if len(div)>=18:
        print(n, sum(div))

# 404250 160335
# 415800 74834
# 433125 320927
# 450450 162782
# 477750 339235
# 481950 345774