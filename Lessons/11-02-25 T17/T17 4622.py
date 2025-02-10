with open('17_4622.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = min(i for i in arr if i>0 and i%19==0)
res = []
for i in range(len(arr)-1):
    p1, p2 = arr[i], arr[i+1]
    u1 = p1+p2 < m
    if u1:
        res.append(abs(p1+p2))
print(len(res), max(res))
#4984 696