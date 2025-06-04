with open('9_4589.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

cnt = 0
for i in arr:
    if max(i) < sum(i) - max(i):
        if max(i) + min(i) == sum(i) - max(i) - min(i):
            cnt += 1
print(cnt)
#104