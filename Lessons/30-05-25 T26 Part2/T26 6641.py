with open('26_6641.txt') as f:
    N, M = map(int, f.readline().split())
    arr = [list([int(i.split()[0]), i.split()[1]]) for i in f if i]

arr = sorted(arr)
res_s = []
res_w = []
for price, type in arr.copy():
    if M - price >= 0:
        if type == 'S':
            res_s.append(price)
            arr.remove([price, type])
        else:
            res_w.append(price)
            arr.remove([price, type])
        M -= price

for pr, t in arr:
    if t == 'S' and res_w:
        if M + res_w[-1] - pr >= 0:
            res_s.append(pr)
            M = M + res_w[-1] - pr
            res_w.remove(res_w[-1])
print(len(res_s), M)
#393 4