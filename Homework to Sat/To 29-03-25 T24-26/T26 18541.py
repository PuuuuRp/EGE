with open('26_18541.txt') as f:
    N, M = list(map(int, f.readline().split()))
    arr = [int(i) for i in f.readlines() if i]

weight = sorted(arr[:N])[::-1]
w_atl = sorted(arr[N:])[::-1]
w = []
for atl in w_atl:
    for m in weight:
        if m<=atl:
            w.append(m)
            break
sr = sum(w)//len(w)

set_w = set(w)
pop_w = []
for cur in set_w:
    cnt = 0
    for cur_w in w:
        if cur_w==cur: cnt += 1
    pop_w.append([cnt, cur])
pop_w = sorted(pop_w, key=lambda x: (-x[0], -x[1]))

print(sr, pop_w[0][1])
#49989 65113