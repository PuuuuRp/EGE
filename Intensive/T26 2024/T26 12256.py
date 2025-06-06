with open('26_12256.txt') as f:
    s, N= map(int, f.readline().split())
    arr = [int(i) for i in f if i]

arr = sorted(arr)
res = []
for i in arr:
    if s-i>=0:
        res.append(i)
        s -= i

arr = sorted(arr)[::-1]
for i in arr:
    if s+res[-1]-i>=0:
        print(len(res), i)
        break
#629 50