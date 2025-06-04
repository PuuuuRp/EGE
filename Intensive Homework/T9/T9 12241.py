with open('9_12241.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2)==6 and cnt.count(1)==1

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    pov = [i for i in arr if cnt[arr.index(i)]==2]
    npov = [i for i in arr if cnt[arr.index(i)]==1]
    return (max(pov) + min(pov))/2 < npov[0]

cnt = 0
for i in arr:
    if u1(i):
        if u2(i):
            cnt += 1
print(cnt)
#3382