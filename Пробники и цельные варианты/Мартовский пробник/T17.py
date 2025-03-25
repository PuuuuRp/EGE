with open('1706.txt') as f:
    arr = [int(i) for i in f.readlines()]
m = min(i for i in arr if abs(i)%100==19 and 100<=abs(i)<=999)**2

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = any(10**4<=abs(i)<10**5 and abs(i)%100==19 for i in p)
    u2 = sum(p)>m
    if u1 and u2:
        res.append(sum(p))
print(len(res), min(res))
#169 101954