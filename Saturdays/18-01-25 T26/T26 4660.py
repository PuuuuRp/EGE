with open('26_4660.txt') as f:
    N = int(f.readline())
    arr =  [int(i) for i in f if i]

arr = sorted(arr)
ans_1 = sum(arr[:len(arr)//4+1])+sum(arr[len(arr)//4+1:])

arr = sorted(arr)[::-1]
ans_2 = 0
for i in range(0, len(arr), 4):
    ans_2 += sum(arr[i:i+3]) + arr[i+3]//2
print(ans_1, ans_2)
#44101521 50399596