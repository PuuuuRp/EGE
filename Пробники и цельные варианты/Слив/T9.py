with open('9.txt') as f:
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(3)==6 and cnt.count(1)==1

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    once = [i for i in arr if cnt[arr.index(i)]==1]
    pov = set(arr)-set(once)
    return max(pov) > once[0]

c = 0
for i in arr:
    if u1(i):
        if u2(i):
            c += 1
print(c)
#1