with open('17_17558.txt') as f:
    arr = [int(i) for i in f if i]

m = sum(abs(i)%32==0 for i in arr)

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u1 = any(x<0 for x in p)
    u2 = sum(p) < m
    if u1 and u2:
        res.append(sum(p))
print(len(res), max(res))
#4969 299