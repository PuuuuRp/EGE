with open('26_9756.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: (x[1], x[0]))
cnt = 0
last_fn = 0
res = []
for st, fn in arr:
    if st - last_fn >= 0:
        cnt += 1
        last_fn = fn
        res.append(st)

arr = sorted(arr, key=lambda x: (-x[1], x[0]))
for st, fn in arr:
    if st>=res[-2] and fn>=last_fn:
        print(cnt, fn)
        break
#16 1345