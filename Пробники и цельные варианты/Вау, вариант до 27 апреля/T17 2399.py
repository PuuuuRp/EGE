with open('17_2399.txt') as f:
    arr = [int(i) for i in f if i]

def toq(a,q):
    al = '0123456789abcdef'
    res = ''
    while a:
        res += al[a%q]
        a //= q
    return res[::-1]

def u1(x, s):
    return x>s
s = sum(sum(int(i) for i in str(x)) for x in arr if x % 35 == 0)

def u2(x):
    return toq(x, 16)[-2:] == 'ef'

res = []
for i in range(len(arr)-1):
    x, y = arr[i: i+2]
    if (u1(x, s) and u2(y)) and not (u1(y, s) and u2(x)): res.append(x+y)
    if (u1(y, s) and u2(x)) and not (u1(x, s) and u2(y)): res.append(x+y)
print(len(res), min(res))
#51 6410