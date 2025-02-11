with open('17_17558.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = len([i for i in arr if abs(i)%32==0])

res= []
for x in range(len(arr)-1):
    p = arr[x: x+2]
    u1 = any(i<0 for i in p)
    u2 = sum(p) < m
    if u1 and u2:
        res.append(sum(p))
print(len(res), max(res))
#4969 299