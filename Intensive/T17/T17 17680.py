with open('17_17680.txt') as f:
    arr = [int(i) for i in f if i]

m = min(i for i in arr if i>0 and i%41==0)

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u1 = p[1] != p[0]
    u2 = abs(p[0]-p[1])%m==0
    if u1 and u2:
        res.append(sum(p))
print(len(res), max(res))
#10 92404