with open('17_13088.txt') as f:
    arr = [int(i) for i in f if i]

m = max(i for i in arr if i%100==17)

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = sum(10**3 <= x < 10**4 for x in p) == 2
    u2 = any(x%5==0 for x in p)
    u3 = sum(p) > m
    if u1 and u2 and u3:
        res.append(sum(p))
print(len(res), max(res))
#21 114132