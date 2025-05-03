with open('17_21712.txt') as f:
    arr = [int(i) for i in f if i]

m = min(i for i in arr if i>0 and 1000<=i<=9999 and i%10==6)

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = sum(1000<=abs(x)<=9999 and abs(x)%10==6 for x in p)==1
    u2 = sum(p)<=m
    if u1 and u2: res.append(sum(p))
print(len(res), max(res))
#507 1042