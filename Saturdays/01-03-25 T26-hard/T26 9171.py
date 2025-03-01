with open('26_9171.txt') as f:
    M, K, N = map(int, f.readline().split())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]
arr = sorted(arr, key=lambda x: (x[0], -x[1]))

cur = []
res = 0
st = 0
for i in arr:
    for x in range(st, i[0]+1):
        while x in cur:
            cur.remove(x)
            K += 1
    st = i[0]
    if K>0:
        cur.append(i[1])
        K -= 1
        res += 1

print(res)