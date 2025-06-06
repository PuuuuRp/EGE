with open('26_16390.txt') as f:
    S, N = map(int, f.readline().split())
    arr = [int(i) for i in f if i]

arr = sorted(arr)
res = []
for i in arr:
    if S-i>=0:
        res.append(i)
        S -= i

arr = sorted(arr)[::-1]
for i in arr:
    if S+res[-1] - i >= 0:
        print(len(res), i)
        break
#2216 56