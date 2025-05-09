with open('17_6089.txt') as f:
    arr = [int(i) for i in f if i]

m = max(i for i in arr if str(i)[-1]=='2')

res = []
for i in arr:
    u1 = abs(i)%3==0 and abs(i)%7!=0 and abs(i)%17!=0
    u2 = m%abs(i)==0
    if u1 and u2:
        res.append(i)
print(len(res), max(res))
#11 1416