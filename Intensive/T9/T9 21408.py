with open('9_21408.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(3) == 6

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    pov = max(i for i in arr if cnt[arr.index(i)] != 1)
    npov = [i for i in arr if cnt[arr.index(i)] == 1]
    return pov > npov[0]

cnt = 0
for i in arr:
    if u1(i):
        if u2(i):
            cnt += 1
print(cnt)
#1