with open('26_1232.txt') as f:
    S, N = list(map(int, f.readline().split()))
    arr = [int(i) for i in f if i]

arr.sort()
res = []
for i in arr:
    if S - i >= 0:
        S -= i
        res.append(i)
    else: break

arr = sorted(arr)[::-1]
S += res[-1]
for i in arr:
    if S - i >= 0:
        print(len(res), i)
        break
#1614 79