with open('17_18582.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

m = min(arr)
res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    s = abs(sum(p))
    u1 = len([x for x in p if x<0]) > 1
    u2 = abs(sum(p))%10 == abs(m)%10
    if u1 and u2:
        res.append(s)
print(len(res), max(res))

#440 210834