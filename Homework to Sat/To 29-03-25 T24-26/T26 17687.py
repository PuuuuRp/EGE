with open('26_17687.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f.readlines() if i]

arr = sorted(arr)[::-1]
print(sum(arr[1103:]))
s = 0
cnt = 0
for i in arr:
    cnt += 1
    if cnt<9:
        s += i
    if cnt==9:
        cnt = 0
print(s)
#39450073 44329073