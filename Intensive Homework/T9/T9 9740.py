with open('9_9740.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(3)==3 and cnt.count(1)==4

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    pov = [i for i in arr if cnt[arr.index(i)]==3]
    npov = sum(i for i in arr if cnt[arr.index(i)]==1)/4
    return npov <= pov[0]

cnt = 0
for i in arr:
    if u1(i):
        if u2(i):
            cnt += 1
print(cnt)
#36