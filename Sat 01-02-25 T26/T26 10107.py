with open('26_10107.txt') as f:
    N = f.readline()
    arr = [[int(i.split()[0]), int(i.split()[1])] for i in f.readlines() if i]

arr = sorted(arr, key=lambda x: (x[1], -x[0]))

res = [arr[0]]
for i in range(1, len(arr)):
    if arr[i][0] >= res[-1][1]:
        res.append(arr[i])
print(len(res))
#32
print(res[-1][0] - res[-2][1])
#15