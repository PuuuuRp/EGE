with open('9_4614.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

cnt = 0
for i in arr:
    if max(i) < sum(i) - max(i):
        if sum(i.count(x)==2 for x in i) == 2:
            cnt += 1
print(cnt)
#133