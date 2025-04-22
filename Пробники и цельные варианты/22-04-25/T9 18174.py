with open('9_18174.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(2)==2

def u2(arr):
    ot = sum(abs(i) for i in arr if i<0)
    pol = sum(abs(i) for i in arr if i>0)
    return ot > pol

cnt = 0
for i in arr:
    if u1(i) and u2(i):
        cnt += 1
print(cnt)
#44