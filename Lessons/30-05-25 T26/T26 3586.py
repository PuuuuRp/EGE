with open('26_3586.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: (-x[0], x[1]))
m = []
for i in range(len(arr)-1):
    p1, p2 = arr[i: i+2]
    if p1[0] == p2[0]:
        m.append([p2[1]-p1[1]-1, p1[0]])
print(max(m, key=lambda x: (x[0], x[1])))
#4802 7468