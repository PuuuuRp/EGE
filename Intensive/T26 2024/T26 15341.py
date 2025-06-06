with open('26_15341.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)[::-1]
res = [arr[0]]
for i in arr[1:]:
    if res[-1]-i>=8:
        res.append(i)
print(len(res), res[-1])
#1198 54