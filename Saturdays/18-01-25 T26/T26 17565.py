with open('26_17565.txt') as f:
    N, S = map(int, f.readline().split())
    arr = [[sum(map(int, i.split()[1:4])), int(i.split()[4]), int(i.split()[0])] for i in f if i]

arr = sorted(arr, key=lambda x: (-x[0], -x[1], x[2]))
res = arr[:S]
print(res[-1])
pr = sum(i[0] for i in arr)//N+1
lust_s = []
for i in range(S-1):
    if res[i+1][0] < pr:
        print(res[i])
        lust_s.append(res[i])
        break