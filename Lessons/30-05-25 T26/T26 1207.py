with open('26_1207.txt') as f:
    S, N = map(int, f.readline().split())
    arr = [int(i) for i in f if i]

arr.sort()
res = []
for i in arr:
    if S - i >= 0:
        res.append(i)
        S -= i
    else: break

S += res[-1]
arr = sorted(arr)[::-1]
for i in arr:
    if S - i >= 0:
        print(len(res), i)
        break
#1611 90