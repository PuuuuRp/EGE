from re import *
with open('24-303.txt') as f:
    st = f.readline()

z = r'(\+*|\**|\-*)?'
sr = '{'
sl = '}'
pat1 = fr'\((\(\d+{z}\d+\)|{sr}\d+{z}\d+{sl}|\[\d+{z}\d+\])\)'
pat2 = fr'{sr}(\(\d+{z}\d+\)|{sr}\d+{z}\d+{sl}|\[\d+{z}\d+\]){sl}'
pat3 = fr'\[(\(\d+{z}\d+\)|{sr}\d+{z}\d+{sl}|\[\d+{z}\d+\])\]'
pat = fr''