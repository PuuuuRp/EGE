with open('26_9847.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr)
day = [0]*1441
for st, fn in arr:
    for i in range(st, fn):
        day[i] += 1

m = max(day)
res = []
for i in range(len(day)):
    if day[i] == m:
       res.append(i)

print(res)
cnt = 1
for i in range(len(res)-1):
    p1, p2 = res[i: i+2]
    if p2 - p1 > 1:
        cnt += 1
print(cnt, m)
#2 643