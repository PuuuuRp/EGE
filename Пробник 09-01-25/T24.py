with open('24.txt') as f:
    st = f.readline()

pos_a = []
for i in range(len(st)):
    if st[i] == 'A':
        pos_a.append(i)
print(len(pos_a))
cnt_a = len(pos_a) - 1
c = 0
for i in range(len(pos_a)-1):
    pos1, pos2 = pos_a[i], pos_a[i+1]
    if pos2 - pos1 > 1:
        c += cnt_a
    else:
        c += cnt_a - 1
    cnt_a -= 1
print(c)
#42587173055