with open('26_9847.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

# arr = [[10, 50],
#        [100, 150],
#        [110, 155],
#        [120, 160],
#        [130, 170],
#        [151, 170]]

res = [0]*1441
for st, fn in arr:
    for t in range(st, fn):
        res[t] += 1

for i in range(len(res)):
    if res[i] == max(res):
        print(i)
print(max(res))
#2 643