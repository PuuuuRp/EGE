with open('26_3230.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr[:-1], key=lambda x: (-x[0], x[1]))
for i in range(len(arr)-1):
    p1, p2 = arr[i: i+2]
    if p1[0] == p2[0]:
        if p2[1] - p1[1] == 12:
            print(p1[0], p1[1]+1)
            break
#2261 5087