with open('26_2480.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

# arr = [[10, 40],
#        [50, 130],
#        [70, 130],
#        [75, 90],
#        [120, 170],
#        [140, 170],
#        [150, 180]]

arr = sorted(arr)
road = '0'*2_000_000
for st, end in arr:
    l = end-st
    road = road[:st] + '1'*l + road[end:]
road = road.replace('0', ' ')
road = road.split()
print(len(road), sum(len(i) for i in road))
#1226 822094