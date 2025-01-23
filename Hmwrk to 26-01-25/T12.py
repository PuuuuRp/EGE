def simp(n):
    for i in range(2, int(n**0.5)):
        if n%i == 0: return False
    return True

for n in range(1, 100):
    if simp(n) and (43+n*4)%n == 0:
        print(n)
        break
#1