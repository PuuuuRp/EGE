with open('26_4684.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)[::-1]
res1 = sum(arr) - sum(arr[5::6])/2

arr = sorted(arr)
res2 = sum(arr) - sum(arr[:N//6])/2
print(res1, res2)
#46201709 49699604