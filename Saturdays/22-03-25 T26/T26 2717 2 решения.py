from itertools import *
with open('26_2717.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]
arr = sorted(arr, key=lambda x: (x[0], x[1]))

cnt = 1
last = arr[0]
for r, m in arr[1:]:
    if last[0] == r and m-last[1]<=3:
        cnt +=1
        last = [r, m]
    else:
        cnt = 1
        last = [r, m]
    if cnt==5:
        print(r, m)
        break
#1234 38468

cnt = 0
for r, pl in groupby(arr, lambda x: x[0]):
    pl = [i[1] for i in list(pl)]
    if len(pl)>=5:
        for i in range(len(pl)-4):
            cur = pl[i: i+5]
            if cur[-1]-cur[0]<=12:
                if all(cur[x+1]-cur[x]<=3 for x in range(4)):
                    print(r, pl[i+4])
                    cnt += 1
    if cnt==1:
        break
#1234 38468