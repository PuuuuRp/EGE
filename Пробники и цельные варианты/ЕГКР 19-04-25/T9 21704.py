with open('9_21704.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]

def u1(arr):
    return sorted(arr)[::-1] == arr

def u2(arr):
    arr.sort()
    sr_m = (arr[0]+arr[-1])/2
    sr = sum(arr[1:-1])/len(arr[1:-1])
    return sr_m > sr

for i in arr:
    if u1(i) and u2(i):
        print(sum(i))
        break
#652