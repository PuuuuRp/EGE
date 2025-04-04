with open('9_17522.txt') as f:
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

def u1(arr):
    return max(arr) < sum(arr) - max(arr)

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2)==2

c = 0
for i in arr:
    if u1(i) and u2(i):
        c += 1
print(c)
#147