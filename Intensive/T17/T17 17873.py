with open('17_17873.txt') as f:
    arr = [int(i) for i in f if i]

m = min(arr)

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u = any(x%16==m for x in p)
    if u:
        res.append(sum(p))
print(len(res), max(res))
#1214 176024