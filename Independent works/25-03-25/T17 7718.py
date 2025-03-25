with open('17 (2)_7718.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

res = []
for x in range(len(arr)-1):
    for i in range(x+1, len(arr)):
        p = [arr[x], arr[i]]
        u1 = sum(p)%18==0
        u2 = p[0]*p[1]%18==0
        if u1 ^ u2:
            res.append(sum(p))
print(len(res), max(res))
#120400 19971