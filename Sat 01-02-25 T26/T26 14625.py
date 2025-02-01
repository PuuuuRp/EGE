with open('26_14625.txt') as f:
    N = int(f.readline())
    K, R, M = map(int, f.readline().split())
    arr =[]
    for i in f.readlines():
        v = i[-3:-1]
        i = list(map(int, i.split()[:-1]))
        i.append(v)
        if i[2] == 'kb':
            i[1] = i[1]*2**10
            arr.append(i[:-1])
        if i[2] == 'mb':
            i[1] = i[1]*2**20
            arr.append(i[:-1])
        if i[2] == ' b': arr.append(i[:-1])
M = M*2**20
arr = sorted(arr, key=lambda x: -x[1])

tipe = [0]*17
c = 0
suma = 0
last = []
for i in arr:
    if tipe[i[0]-1] < 87 and suma+i[1] <= M:
        c += 1
        suma += i[1]
        tipe[i[0] - 1] += 1
        last.append(i)

suma -= last[-1][1]
tipe[last[-1][0] - 1] -= 1
for i in arr[::-1]:
    if tipe[i[0]-1] < 87 and suma+i[1] >= M:
        print(i[1])
        break
print(c)
#1406 356515840