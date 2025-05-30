with open('26_4629.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)[::-1]
res_1 = sum(arr) - sum(arr[:N//4])/2

arr = sorted(arr)
res_2 = sum(arr) - sum(arr[:N//4])/2
print(res_1, res_2)
#39434611 48825239