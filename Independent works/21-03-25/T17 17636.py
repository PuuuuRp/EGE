with open('17_17636.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = max(i for i in arr if abs(i)%10==3 and 100<=abs(i)<=999)
res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    u1 = any(abs(i)%10==3 and 100<=abs(i)<=999 for i in p)
    u2 = sum(p) < m
    if u1 and u2: res.append(sum(p))
print(len(res), max(res))
#147 944