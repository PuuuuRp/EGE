with open('26_17687.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)[::-1]
res1 = sum(arr) - sum(arr[:N//9])

res2 = sum(arr) - sum(arr[8::9])

print(res1, res2)
#39450073 44329073