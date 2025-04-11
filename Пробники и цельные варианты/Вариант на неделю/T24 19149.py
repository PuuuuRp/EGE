with open('24_19149.txt') as f:
    st = f.readline()
st = st.replace('++', ' ').replace(')(', ') (').replace('(+', ' ').replace('+)', ' ')
st = st.replace(')+', ') ').replace('+(', ' (')
st = st.replace(')(', ') (').replace('))', ') ').replace('((', ' (')
st = st.replace(')(', ') (').replace('))', ') ').replace('((', ' (')
for i in '1234':
    st = st.replace(')'+i, ') ').replace(i+'(', ' (')

st = st.split()

res = []
for i in st:
    if i[0]=='(' and i[-1]==')' and i[1] in '1234' and eval(i[1:-1])%2==0:
        res.append(len(i))
print(max(res))
#78