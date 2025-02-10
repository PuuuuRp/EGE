with open('26_9711.txt') as f:
    M, N = map(int, f.readline().split())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

arr = sorted(arr, key=lambda x: (x[0], x[1]))

#Сто проц рабочее решение, но жопа для понимания
park = []
for i in range(M+1):
    park.append([])
scuter = [0]*21

for i in arr:
    if len(park[i[2]]) != 0\
            and min(park[i[2]]) <= i[0]:
            park[i[2]].remove(min(park[i[2]]))
    else: scuter[i[2]] += 1
    park[i[3]].append(i[1] + i[0] + 1)
print(scuter.index(max(scuter)))

#Просто, но ХЗшное решение
# scuter = [0]*21
# for i in arr:
#     scuter[i[2]] -= 1
#     scuter[i[3]] += 1
# print(scuter)

time = [0]*2000
for ar in arr:
    for i in range(ar[0], ar[0]+ar[1]+1):
        time[i] += 1
print(time.index(max(time)))