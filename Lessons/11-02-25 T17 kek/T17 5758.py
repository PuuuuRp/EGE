with open('17_5758.txt') as f:
    arr = [int(i) for i in f.readlines() if i]

s = [arr.count(i) for i in range(-1000, 1001)]
moda = s.index(max(s)) - 1000

res = []
for x in range(len(arr)):
    for y in range(x+2, len(arr), 2):
        p = sorted([arr[x], arr[y]])
        u1 = p[0] < moda < p[1]
        if u1:
            res.append(max(moda - p[0], p[1] - moda))
print(len(res), max(res))
#254546 1343