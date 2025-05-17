with open('26_3745.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: (x[0], x[1]))
cnt = [0]*79
res = []
for i in range(N-1):
    f, t = arr[i: i+2]
    if f[0]==t[0] and t[1]-f[1]==1:
        u1 = [f[0]-1, f[1]] in arr and [t[0]-1, t[1]] in arr #проверка на свободные снизу
        u2 = [f[0] + 1, f[1]] in arr and [t[0] + 1, t[1]] in arr #проверка на свободные сверху
        if u1:
            #проверки на занятость по бокам
            f1 = [f[0]+1, f[1]] not in arr and [t[0]+1, t[1]] not in arr
            f2 = [f[0], f[1]-1] not in arr and [f[0]-1, f[1]-1] not in arr
            f3 = [t[0], t[1]+1] not in arr and [t[0]-1, t[1]+1] not in arr
            f4 = [f[0]-2, f[1]] not in arr and [t[0]-2, t[1]] not in arr
            if f1 and f2 and f3 and f4:
                res.append([f, t, [f[0] - 1, f[1]], [t[0] - 1, t[1]]])
                cnt[f[0]] += 1
        elif u2:
            # проверки на занятость по бокам
            f1 = [f[0]-1, f[1]] not in arr and [t[0]-1, t[1]] not in arr
            f2 = [f[0], f[1]-1] not in arr and [f[0]+1, f[1]-1] not in arr
            f3 = [t[0], t[1]+1] not in arr and [t[0]+1, t[1]+1] not in arr
            f4 = [f[0]+2, f[1]] not in arr and [t[0]+2, t[1]] not in arr
            if f1 and f2 and f3 and f4:
                cnt[f[0]] += 1
print(len(res), cnt.index(max(cnt)))
#169 55