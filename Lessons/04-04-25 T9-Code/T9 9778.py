with open('09_9778.txt') as f:
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2)==2 and cnt.count(1)==4

def u2(arr):
    enemy = [i for i in arr if arr.count(i)!=1]
    once = [i for i in arr if arr.count(i)==1]
    return enemy[0] >= sum(once)//len(once)

for pos, i in enumerate(arr, 1):
    if u1(i) and u2(i):
        print(pos)
        break
#34