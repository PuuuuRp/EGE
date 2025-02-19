with open('17.txt') as f:
    arr = [int(i) for i in f.readlines()]
m = max(i for i in arr if abs(i)%100==50)
res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = len(set(p)) == len(p)
    u2 = all(abs(x) in range(10**4, 10**5) for x in p)
    s = sum(p)
    u3 = s <= m
    if u1 and u2 and u3: res.append(s)
print(len(res), max(res))
#72 58037