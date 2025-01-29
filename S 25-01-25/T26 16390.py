with open('26_16390.txt') as f:
    S, N = [int(i) for i in f.readline().split()]
    arr = [int(i) for i in f if i]

arr = sorted(arr)

s = 0
c = 0
for i in arr:
    if s+i<=S:
        s += i
        c += 1
a = 0
for i in arr[::-1]:
    if sum(arr[:c-1])+i <= S:
        print(c, i)
        break
#2216 56