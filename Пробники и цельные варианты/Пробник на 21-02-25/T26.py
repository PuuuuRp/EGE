with open('26.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

for i in range(len(arr)):
    arr[i].append(arr[i][0] + arr[i][1])
arr = sorted(arr, key=lambda x: (x[2], x[0]))

res = [arr[0]]
for i in arr[1:]:
    if i[0] >= res[-1][2]:
        res.append(i)
print(len(res))
ans = []
for i in arr[arr.index(res[-1]):][::-1]:
    ans.append([i[0]-res[-2][2], i])
print(max(ans))
#29 22