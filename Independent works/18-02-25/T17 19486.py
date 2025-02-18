with open('17_19486.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

cnt = len([i for i in arr if abs(i)%10==7])
res = []
for i in range(len(arr)-1):
    p = arr[i: i+2]
    u1 = not any(x==0 for x in p) and p[0]*p[1] < 0
    s = sum(p)
    u2 = s<cnt
    if u1 and u2: res.append(s)
print(len(res), max(res))
#2452 962