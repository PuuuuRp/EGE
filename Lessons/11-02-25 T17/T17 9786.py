with open('17_9786.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = max(i for i in arr if abs(i)%100==25)

res = []

for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = sum(abs(i) in range(10**3, 10**4) for i in p) <= 2
    u2 = sum(p) <= m
    if u1 and u2:
        res.append(sum(p))
print(len(res), max(res))
#8295 98773