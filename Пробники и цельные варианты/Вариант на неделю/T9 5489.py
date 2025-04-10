with open('9_5489.txt') as f:
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

def f1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(1)==5

def f2(arr):
    ch = sum(i%2==0 for i in arr)
    nch = sum(i%2!=0 for i in arr)
    return ch>nch

def f3(arr):
    ch = sum(i for i in arr if i%2==0)
    nch = sum(i for i in arr if i%2!=0)
    return ch<nch

c = 0
for i in arr:
    if f1(i) and f2(i) and f3(i):
        c += 1
print(c)
#241