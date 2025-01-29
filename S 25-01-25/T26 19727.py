with open('26_19727.txt') as f:
    M, N = [int(i) for i in f.readline().split()]
    arr = [int(i) for i in f if i]

arr = sorted(arr)
s = 0
c = 0
for i in arr:
        if s+i <= M:
            s += i
            c += 1
        else: break
a = 0
for i in arr[::-1]:
    if sum(arr[:c-1])+i > M: a += 1

print(c, a)
#162 788