with open('17_4329.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

def d(n):
    div = set()
    for i in range(1, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

m_d = []
for n in set(arr):
    m_d.append([d(n), n])
m_d = sorted(m_d, key=lambda x: len(x[0]))
m = m_d[-1][0]

def gen_d(n, m):
    res = []
    for i in m:
        for x in n:
            if x==i: res.append(i)
    return len(res)

ans = []
for i in range(len(arr)-1):
    p1, p2 = arr[i: i+2]
    u1 = gen_d(d(p1), m)>=3
    u2 = gen_d(d(p2), m)>=3
    if u1 and u2:
        ans.append(gen_d(d(p1), d(p2)))
print(len(ans), max(ans))
#643 16