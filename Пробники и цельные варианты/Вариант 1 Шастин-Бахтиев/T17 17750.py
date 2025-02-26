with open('17_17750.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = min(arr)

res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u1 = (p[0]%77 + p[1]%77) == m
    if u1: res.append(sum(p))
print(len(res), max(res))
#35 186613