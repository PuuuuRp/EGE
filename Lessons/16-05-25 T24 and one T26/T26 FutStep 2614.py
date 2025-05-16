with open('2614.txt') as f:
    N, M = list(map(int, f.readline().split()))
    arr = [list(map(int, i.split())) for i in f if i]

r = []
b = []
for i in arr:
    if len(i)==2:
        r.append([i[0], 'r'])
        b.append([i[1], 'b'])
    else:
        r.append([i[0], 'r'])
arr = r + b
arr = sorted(arr)[::-1]

ans = []
for i in range(3400):
    res = [arr[i]]
    for d, col in arr[i+1:]:
        if res[-1][1] != col and res[-1][0]-d>=5:
                res.append([d, col])
    ans.append([len(res), res[-1][0]])
print(max(ans))
#536 306