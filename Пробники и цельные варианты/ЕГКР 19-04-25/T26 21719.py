with open('26_21719.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: (x[0], x[1]))

res = []
last = arr[0]
for num, c in arr[1:]:
    if last[0]==num:
        if c-last[1]==2:
            res[num][1].append(last[1])
            res[num][1].append(c)
    last = [num, c]

res = [[num, list(set(kek))] for num, kek in res]
for i in res: print(*i)
