with open('2600.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

for i in range(len(arr)):
    a = arr[i][1]//10 if arr[i][1]%10==0 else arr[i][1]//10+1
    arr[i].append(arr[i][0]+a)
arr = sorted(arr, key=lambda x: (x[2], x[0]))

res = []
for x in range(N):
    p = [arr[x]]
    topl = arr[x][1]
    for i in arr[x+1:]:
        if i[0]>=p[-1][2]:
            p.append(i)
            topl += i[1]
    res.append([len(p), topl])
res = sorted(res, key=lambda x: (-x[0], -x[1]))
print(res[0])
#84 11468