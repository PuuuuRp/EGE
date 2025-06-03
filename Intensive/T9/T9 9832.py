with open('9_9832.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2)==4 and cnt.count(1)==3

def u2(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt[arr.index(max(arr))]==1

for i in arr:
    if u1(i) and u2(i):
        print(sum(x for x in i))
        break
#261