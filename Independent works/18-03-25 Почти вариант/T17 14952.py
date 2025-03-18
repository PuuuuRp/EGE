with open('17_14952.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = max(i for i in arr if abs(i)%1000==121)

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = sum(abs(x) in range(1000, 10000, 2) for x in p)<=1
    u2 = sum(p) <= m
    if u1 and u2:
        res.append(sum(p))
print(len(res), max(res))
#5211 20116