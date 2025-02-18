with open('17_13882.txt') as f:
    arr = [int(i) for i in f.readlines() if i]
m = max(i for i in arr if i%401==0)

res = []
for i in range(len(arr)-2):
    p = arr[i: i+3]
    suma = [sum(int(i) for i in str(x)) for x in p]
    u1 = len(set(suma)) == len(suma)
    s = sum(p)
    u2 = s > m
    if u1 and u2: res.append(s)
print(len(res), min(res))
#6283 9627