with open('26_17786.txt') as f:
    N, V = [int(i) for i in f.readline().split()]
    arr = [int(i) for i in f if i]

arr = sorted(i for i in arr if 7000<=i<=12000)[::-1]

res = []
for i in arr:
    if sum(res)+i<=V*1000:
        res.append(i)
print(len(res), res[-1])
#75 9196