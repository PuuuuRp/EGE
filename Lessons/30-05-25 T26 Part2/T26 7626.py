with open('26_7626.txt') as f:
    K = int(f.readline()) + 1
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr)
cnt = 0
last = 0
box = [0]*K
for st, fn in arr:
    for i in range(len(box)-1):
        if st-box[i]>=1:
            box[i] = fn
            cnt += 1
            last = i
            break
print(cnt, last+1)
#581 59