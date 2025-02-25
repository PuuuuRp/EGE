m = max(abs(i) for i in data)%10
m_1 = max(data)%10

ans = []
for i in range(len(data)-2):
    p = data[i: i+3]
    u1 = sum(abs(i) in range(10**3, 10**4) for i in p) > 1
    u2 = sum(abs(i)%10 == m for i in p) <= 1
    u3 = sum(abs(i)%10 == m_1 for i in p) >= 1
    if u1 and u2 and u3:
        ans.append(sum(p))

print(len(ans), sum(ans)//len(ans))