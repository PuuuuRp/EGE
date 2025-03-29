with open('26_5988.txt') as f:
    N = int(f.readline())
    arr = [[int(i.split()[0]), i.split()[1]] for i in f.readlines() if i]
arr = sorted(arr, key=lambda x: x[0])[::-1]

res = []
for x in range(0,1):
    for first in arr[x:]:
        cnt = 1
        color = first[0]
        razm = first[0]
        for m, col in arr[x+1:]:
            if razm-m>=7 and color!=col:
                cnt += 1
                razm = m
                color = col
        res.append([cnt, razm])
print(max(res, key=lambda x: x[0]))
#