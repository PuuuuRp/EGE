def trian(n, m, k):
    if n+m>k and k+m>n and k+n>m:
        return True
    return False

res = []
for A in range(1, 1000):
    if all(trian(A, 7, x) <= ((max(x+5, 27)<=27) == (not(trian(36, 21, x))))\
           for x in range(1, 1000)):
        res.append(A)
print(res[-1])
#50