with open('17_9840.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = max(i for i in arr if abs(i) in range(10**3, 10**4) and abs(i)%100==39)**2

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u1 = sum(abs(i) in range(10**3, 10**4) for i in p) == 1
    u2 = sum(p)**2 <= m
    if u1 and u2:
        res.append(sum(p))
print(len(res), max(res))
#1591 9233