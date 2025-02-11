with open('17_9748.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = max(i for i in arr if i%100==15)
res = []

for i in range(len(arr)-2):
    p1, p2, p3 = arr[i], arr[i+1], arr[i+2]
    u1 = p1 in range(10**3, 10**4) and p2 not in range(10**3, 10**4) and p3  not in range(10**3, 10**4)
    u2 = p2 in range(10**3, 10**4) and p1 not in range(10**3, 10**4) and p3 not in range(10**3, 10**4)
    u3 = (p3 in range(10**3, 10**4) and p2 not in range(10**3, 10**4) and p1 not in range(10**3, 10**4))
    if (u1 or u2 or u3) and p1+p2+p3 >= m:
        res.append(p1+p2+p3)
print(len(res), max(res))
#299 196183