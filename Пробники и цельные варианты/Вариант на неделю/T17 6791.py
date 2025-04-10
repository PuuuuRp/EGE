with open('17_6791.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = min(i for i in arr if abs(i)%100==68)**2

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u1 = sum(abs(x)%100==68 for x in p)==1
    u2 = sum(x**2 for x in p) >= m
    if u1 and u2:
        res.append(sum(x**2 for x in p))
print(len(res), max(res))
#26 188357305