with open('26_4712.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)[::-1]
res = [arr[0]]
for i in arr[1:]:
    if res[-1]-i>=3:
        res.append(i)
print(len(res), res[-1])
#2767 51