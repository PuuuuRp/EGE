with open('9_6262.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return sum(cnt)>6

def u2(arr):
    return sum(i%2!=0 for i in arr)==3

cnt = 0
for i in arr:
    if u1(i) and not u2(i): cnt += 1
    if u2(i) and not u1(i): cnt += 1
print(cnt)
#1852