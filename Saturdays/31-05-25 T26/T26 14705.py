with open('26_14705.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

time = [0]*(5*10**6)
for st, fn in arr:
    time[st] += 1
    time[fn] -= 1

res = [0]*(5*10**6)
res[0] = time[0]
for i in range(len(res)):
    res[i] += time[i] + time[i-1]

m = max(res)
ans = []
for i in range(len(res)):
    if res[i] == m:
        ans.append(i)
print(m)
#