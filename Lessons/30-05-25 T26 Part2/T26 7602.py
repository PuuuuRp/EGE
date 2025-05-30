with open('26_7602.txt') as f:
    K = int(f.readline())
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr)
timeline = [0]*(K+1)
m = 0
cnt = 0
for st, fn in arr:
    for i in range(len(timeline)-1):
        if st - timeline[i] >= 1:
            timeline[i] = fn
            m = i+1
            cnt += 1
            break
print(cnt, m)
#586 3