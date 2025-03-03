with open('17_18617.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m_3 = max(arr)%3
m_7 = min(arr)%7

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u1 = any(x%3==m_3 for x in p)
    u2 = any(x%7==m_7 for x in p)
    if u1 and u2:
        res.append(sum(p))
print(len(res), max(res))

#1467 197700