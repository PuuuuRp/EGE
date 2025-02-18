with open('17_7716.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = max(i for i in arr if all(int(j)%2!=0 for j in str(abs(i))))

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    s = sum(p)
    u1 = any(all(int(j)%2==0 for j in str(abs(x))) for x in p)
    u2 = s > m
    if u1 and u2:
        res.append(s)
print(len(res), max(res))
#