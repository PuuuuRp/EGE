with open('9_18134.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2)==4 and cnt.count(1)==2

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    pov = [i for i in arr if cnt[arr.index(i)]==2]
    npov = [i for i in arr if cnt[arr.index(i)]==1]
    pr = 1
    for i in npov:
        pr *= i
    return max(pov)**2>pr

cnt = 0
for i in arr:
    if u1(i) and u2(i):
        cnt += 1
print(cnt)
#4278