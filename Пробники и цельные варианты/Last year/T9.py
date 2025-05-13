with open('9_ok_11946.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(3)==3 and cnt.count(1)==4

def u2(arr):
    return sorted(arr)[::-1] == arr

cnt = 0
for i in arr:
    if u1(i) + u2(i) <=1:
        cnt += 1
print(cnt)
#14982