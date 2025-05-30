with open('26_2944.txt') as f:
    S, N = list(map(int, f.readline().split()))
    arr = [int(i) for i in f if i]

arr = sorted(arr)
res = []
for i in arr:
    if S - i >= 0:
        res.append(i)
        S -= i
    else: break

arr = sorted(arr)[::-1]
S += res[-1]
for i in arr:
    if S - i >= 0:
        print(len(res), i)
        break
#263 86