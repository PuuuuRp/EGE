def umn(num):
    n = [int(i) for i in str(num) if not int(i)%2]
    u = 1
    for i in n:
        u *= i
    return u

for n in range(10**4, 10**5):
    num = [n%10, n//10%10, n//100%10, n//1000%10, n//10000]
    num1 = (min(num) + max(num))**2
    num2 = umn(n)
    res = str(max(num1, num2)) + str(min(num1, num2))
    if res == '12116':
        print(n)
        break
#22229