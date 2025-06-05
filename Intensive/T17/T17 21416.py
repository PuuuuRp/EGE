with open('17_21416.txt') as f:
    arr = [int(i) for i in f if i]

m = sum(i for i in arr if i<0)

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u = min(p)*max(p)>m
    if u:
        res.append(sum(p))
print(len(res), max(res))
#10007 7953