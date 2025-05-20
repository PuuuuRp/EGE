with open('17_5882.txt') as f:
    arr = [int(i) for i in f if i]

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    if sum(abs(i)%10==3 for i in p) == 1:
        res.append(p[0])
        res.append(p[1])
m = sum(int(i)**2 for i in str(abs(min(res))))

res = []
for i in arr:
    u1 = '3' in str(i)
    u2 = i >= m
    if u1 and u2:
        res.append(i)
print(len(res), min(res))
#893 237