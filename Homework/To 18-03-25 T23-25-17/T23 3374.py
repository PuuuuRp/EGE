res = set()
c = 0
def f(a, n):
    global res, c
    if a==n:
        c += 1
        return
    if a<-50 or a>50: return
    if a in res: return
    res.add(a)
    f(a+2, n)
    f(a-3, n)
    res -= {a}
f(1, 30)
print(c)
#851