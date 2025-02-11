with open('17_17530.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = min(arr)

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u1 = any(i%55==m for i in p)
    if u1:
        res.append(sum(p))
print(len(res), min(res))
#201 2942
