with open('26_3088.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]
arr = sorted(arr, key=lambda x: x[0])

day = [0]*1441
z = []
for i in range(1000):
    z.append([1])
for i in range(len(arr)):
    if 'r' in arr[i]: continue
    for x in range(i+1, len(arr)):
        if arr[x][1]==arr[i][1]:
            day[arr[x][0]] += 1
            z[arr[i][1]].append(arr[x][0]-arr[i][0])
            arr[x].append('r')
            break

res_hour = 0
for i in range(len(day)-60):
    res_hour = max(res_hour, sum(day[i:i+60]))

res_time = []
for i in z:
    if len(i)>1:
        res_time.append(sum(i[1:])/(len(i)-1))
    else:
        res_time.append(sum(i) / len(i))

print(res_hour, res_time.index(max(res_time)))
#190 129