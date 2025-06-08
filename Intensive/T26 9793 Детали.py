with open('26_9793.txt') as f:
    N = int(f.readline())
    d = [list(map(int, i.split())) for i in f if i]

arr = []
for i in range(1, N + 1):
    arr.append([i, d[i - 1][0], d[i - 1][1]])

arr = sorted(arr, key=lambda x: (x[1] + x[2]))
res_sh = []
res_p = []
last = []
for num, sh, p in arr:
    if sh < p:
        res_sh.append([num, sh, 1])
        last = [num, sh, 1]
    else:
        res_p.append([num, p, 2])
        last = [num, p, 2]
res = res_sh + res_p[::-1]

cnt = 0
for num, d, id_d in res[:res.index(last)]:
    if id_d == 1:
        cnt += 1
print(last[0], cnt)
# 895 488

# =========================================================================

with open('26_9793.txt') as f:
    N = int(f.readline())
    det = [list(map(int, i.split())) for i in f if i]

con = []
for num in range(1, N + 1):
    sh, p = det[num - 1]
    if sh < p:
        con.append([num, sh, p, 1])
    else:
        con.append([num, sh, p, 2])

con = sorted(con, key=lambda x: (x[1] + x[2]))
cnt = 0
for num, sh, p, type in con[:-1]:
    if type == 1:
        cnt += 1
print(arr[-1][0], cnt)
# 895 488
