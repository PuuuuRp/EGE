with open('17_12735.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = max(i for i in arr if str(i)[-2:] == '09')

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = sum(x%7==0 for x in p)==2
    u2  = sum(p)<m
    pr = 1
    for x in p:
        pr *= x
    if u1 and u2:
        res.append(pr)
print(len(res), min(res))
#300 8820