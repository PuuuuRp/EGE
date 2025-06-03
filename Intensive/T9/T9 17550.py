with open('9_17550.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(3)==3 and cnt.count(1)==3

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    pov = sum(i for i in arr if cnt[arr.index(i)]>1)**2
    npov = sum(i for i in arr if cnt[arr.index(i)]==1)**2
    return pov > npov

cnt = 0
for i in arr:
    if u1(i) and u2(i):
        cnt +=1
print(cnt)
#19