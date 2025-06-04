with open('9_16375.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2) == 2 and cnt.count(1) == 5

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    pov = [i for i in arr if cnt[arr.index(i)] == 2]
    npov = sorted([i for i in arr if cnt[arr.index(i)] == 1])
    p = 1
    for i in npov[:3]: p *= i
    return p > pov[0]**2

cnt = 0
for i in arr:
    if u1(i):
        if u2(i):
            cnt += 1
print(cnt)
#293