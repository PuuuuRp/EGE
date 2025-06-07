with open('26_21719.txt') as f:
    n = int(f.readline())
    d = [list(map(int, i.split())) for i in f if i]

d = sorted(d, key=lambda x: (x[0], x[1]))
arr = [d[0]]
for i in d[1:]:
    if arr[-1] != i:
        arr.append(i)

res = []
last_cnt = 0
cur_cnt = 1
for i in range(len(arr)-1):
    id = arr[i][0]
    if any(y[0] == id for y in res): continue
    last_t = arr[i][1]
    for x in range(i+1, len(arr)):
        cur_id = arr[x][0]
        if cur_id == id:
            if arr[x][1] - last_t == 2:
                cur_cnt += 1
                last_t = arr[x][1]
            else:
                last_cnt = max(last_cnt, cur_cnt)
                cur_cnt = 1
                last_t = arr[x][1]
        else:
            res.append([id, max(last_cnt, cur_cnt)])
            last_cnt = 0
            cur_cnt = 1
            last_t = arr[x][1]
            break

res = sorted(res, key=lambda x: (-x[1], x[0]))
print(res[0])
#10135 42