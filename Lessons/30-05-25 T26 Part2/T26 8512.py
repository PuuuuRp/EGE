with open('26_8512.txt') as f:
    K = int(f.readline()) + 1
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr)
last = 0
cnt = 0
box = [0]*K
for st, fn in arr:
    for i in range(1, len(box)):
        if st - box[i] >= 1:
            last = i
            cnt += 1
            box[i] = fn
            break
print(cnt, last)
#389 133