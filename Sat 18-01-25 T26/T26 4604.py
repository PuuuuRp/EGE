with open('26_4604.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)[::-1]

res = [arr[0]]
for i in range(1, N):
    if res[-1] - arr[i] >= 3: res.append(arr[i])
print(len(res), res[-1])
#2767 51