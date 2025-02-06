st = open('24_12476.txt').readline()

st = st.replace('ORO', 'OR RO')
st = st.replace('ROR', 'RO OR')
st = st.split()

m = l = k = 0
for i in st:
    for j in range(1, len(i)):
        if i[j-1]+i[j] == 'RO': k+=1
        while k > 21:
            if i[l - 1] + i[l] == 'RO': k -= 1
            l+=1
        if k==21: m = max(m, j-l+1)
    l = k = 0
print(m)
#814