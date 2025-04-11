with open('26_8512.txt') as f:
    K, N = int(f.readline()), int(f.readline())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]
arr = [[i[0], i[1], i[1]-i[0]] for i in arr]
arr = sorted(arr, key=lambda x: (x[0], x[1], x[2]))

res = []
cam = [0] * K
for i in arr:
    for x in range(len(cam)):
        if cam[x]==0:
            cam[x] = i
            res.append(x+1)
            break
        if i[0]-cam[x][1] >= 1:
            cam[x] = i
            res.append(x+1)
            break
print(len(res), res[-1])
#389 133

#с сортировкой arr = sorted(arr, key=lambda x: (x[2], x[0], x[1]))
#ответ 448 207, т.е. их больше
#и вот интересно: это недоработка автора или куда?