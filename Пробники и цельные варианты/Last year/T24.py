with open('24_11954.txt') as f:
    st = f.readline()

st = st.replace('Y', ' ')
st = st.split()

m = 10**18
for i in st:
    if i.count('X') >=500:
        l = 0
        x = 0
        for r in range(len(i)):
            if i[r]=='X': x += 1
            while x >= 500:
                m = min(m, len(i[l:r+1]))
                if i[l] == 'X': x -= 1
                l += 1
print(m)
#68500