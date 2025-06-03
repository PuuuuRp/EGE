with open('9_21704.txt') as f:
    arr = [list(map(int, i.split())) for i in f if i]



def u1(arr):
    return sorted(arr)[::-1] == arr and len(set(arr)) == 7
    #return sorted(arr)[::-1] == arr

def u2(arr):
    sr1 = (max(arr) + min(arr))/2
    sr2 = (sum(arr) - max(arr) - min(arr))/5
    return sr1 > sr2

for i in arr:
    if u1(i) and u2(i):
        print(sum(i))
        break
#652