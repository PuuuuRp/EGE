with open('9_9740.txt') as f:
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

def u1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(3) == 3 and cnt.count(1)==4

def u2(arr):
    for i in range(len(arr)-1):
        if arr[i] in arr[i+1:]:
            n_arr = set(arr)-{arr[i]}
            sr = sum(n_arr)/len(n_arr)
            return sr<=arr[i]
    return False
c = 0
for i in arr:
    if u1(i):
        if u2(i):
            c += 1
print(c)
#36