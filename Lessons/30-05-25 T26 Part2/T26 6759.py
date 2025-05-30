with open('26_6759.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)[::-1]
res1 = sum(arr) - sum(arr[:N//3])

res2 = sum(arr) - sum(arr[2::3])
print(res1, res2)
#22262050 33246829