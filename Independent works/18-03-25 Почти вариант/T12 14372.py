def prime(a):
    for i in range(2, round(a**.5)+1):
        if a%i==0: return 0
    return 1

for n in range(4, 1000):
    a = n*4 + 75
    if prime(a):
        print(n)
        break
#7