with open('26_4205.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: (-x[0], x[1]))

for i in range(len(arr)-1):
    pot = arr[i: i+2]
    if pot[1][0] == pot[0][0]:
        if pot[1][1] - pot[0][1]==14:
            print(pot[0][0], pot[0][1]+1)
            break
#59966 50449