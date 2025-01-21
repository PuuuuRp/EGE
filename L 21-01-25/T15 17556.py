def f(A):
    for x in range(1, 1000):
        B = 70 <= x <= 90
        f = x%A==0 or B <= (x%22!=0)
        if not f: return False
    return True

res = []
for A in range(1, 100000):
    if f(A):
        res.append(A)
print(res[-1])
#88