from fnmatch import *
def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

for i in range(1, 10**7):
    if fnmatch(str(i), '12?*45') and len(d(i))==18:
        print(i, d(i)[-1])

# 1202445 400815
# 1234845 411615
# 1251045 417015
# 1259145 419715
# 1283445 427815
# 1299645 433215