with open('9_9778.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2)==2 and cnt.count(1)==4

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    pov = [i for i in arr if cnt[arr.index(i)]>1]
    sr = sum(i for i in arr if cnt[arr.index(i)]==1)//4
    return pov[0] >= sr

for pos, i in enumerate(arr, 1):
    if u1(i):
        if u2(i):
            print(pos)
            break
#34