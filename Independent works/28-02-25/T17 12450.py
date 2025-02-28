with open('17_12450.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = min(i for i in arr if i%52==0)

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    s = sum(x%113 for x in p)
    if s==m: res.append(sum(p))
print(len(res), max(res))
#