from fnmatch import *
def d(n):
    div = set()
    for i in range(1, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

for n in range(10**6):
    div = d(n)
    poop = [i for i in div if fnmatch(str(i), '4*')]
    if len(poop)==24:
        print(n, max(poop))

#997920 498960