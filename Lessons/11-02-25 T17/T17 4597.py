with open('17_4597.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = min(arr)
res = []
for i in range(len(arr)-1):
    p1, p2 = arr[i], arr[i+1]
    if p1%117 == m or p2%117 == m:
        res.append(p1+p2)
print(len(res), max(res))
#175 173738