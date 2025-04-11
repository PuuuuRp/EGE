with open('17.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = sum(i for i in arr if i<0)

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = max(p)*min(p) > m
    if u1:
        res.append(sum(p))
print(len(res), max(res))
#10007 7953