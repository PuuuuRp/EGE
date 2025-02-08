with open('17_8562.txt') as f:
    arr = [int(i) for i in f if i]

min_1 = min(i for i in arr if str(i)[-1]=='1' and len(str(abs(i)))==2)**2
res = []
for i in range(len(arr)-1):
    n1, n2 = arr[i], arr[i+1]
    if n1**2<min_1 and n2**2>min_1 or n1**2>min_1 and n2**2<min_1:
        if n1+n2>=0:
            res.append(n1+n2)
print(len(res), min(res))
#157 113