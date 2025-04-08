from string import ascii_uppercase
with open('24.txt') as f:
    st = f.readline()
for i in ('0123456789'+ascii_uppercase)[12:]:
    st = st.replace(i, ' ')
while ' 0' in st:
    st = st.replace(' 0', ' ')

st = st.split()
res = []
for i in st:
    if int(i, 12)%2==0:
        res.append(len(i))
    else:
        for x in range(len(i)):
            if int(i[:x+1], 12)%2==0:
                res.append(len(i[:x+1]))
print(max(res))
#19