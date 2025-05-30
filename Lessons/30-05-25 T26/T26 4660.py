with open('26_4660.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)[::-1]
res1 = sum(arr) - sum(arr[3::4])/2

arr = sorted(arr)
res2 = sum(arr) - sum(arr[:N//4])/2
print(res1, res2)
#44101521 48825239
