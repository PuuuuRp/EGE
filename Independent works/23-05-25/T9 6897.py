with open('9_6897.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    return max(arr) < sum(arr) - max(arr)

def u2(arr):
    return max(arr)+min(arr) != sum(arr) - max(arr) - min(arr)

cnt = 0
for i in arr:
    if u1(i) and u2(i):
        cnt += 1
print(cnt)
#2396