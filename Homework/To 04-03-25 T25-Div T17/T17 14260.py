with open('17_14260.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = min(i for i in arr if i>0 and 1000<=i<=9999 and str(i)[-1]==str(i)[-2])

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = all(100<=abs(x)<=999 for x in p)
    u2 = sum(p)>m
    if u1 and u2:
        res.append(sum(p))
print(len(res), max(res))
#8 1958