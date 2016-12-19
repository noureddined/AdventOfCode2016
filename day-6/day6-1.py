#!/usr/bin/python3
import re
import string
import pprint
from collections import Counter

file = open("input.txt", 'r')
lines = file.readlines()
file.close()

totaal = ''
for line in lines:
    s = line
    s = " ".join(s)
    s= s.replace('\n','')
    totaal = totaal +'\n'+ s

totaal = "\n".join(totaal.split("\n")[1:])

file = open("test.txt", "w")
file.write(totaal)
file.close()

file = open("test.txt", 'r')

lines = file.readlines()
file.close()


column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []
column7 = []
column8 = []

for line in lines:
    parts = line.split() # split line into parts
    column1.append(parts[0])
    column2.append(parts[1])
    column3.append(parts[2])
    column4.append(parts[3])
    column5.append(parts[4])
    column6.append(parts[5])
    column7.append(parts[6])
    column8.append(parts[7])

c1 = Counter(elem[0] for elem in column1).most_common(1)[0][0]
c2 = Counter(elem[0] for elem in column2).most_common(1)[0][0]
c3 = Counter(elem[0] for elem in column3).most_common(1)[0][0]
c4 = Counter(elem[0] for elem in column4).most_common(1)[0][0]
c5 = Counter(elem[0] for elem in column5).most_common(1)[0][0]
c6 = Counter(elem[0] for elem in column6).most_common(1)[0][0]
c7 = Counter(elem[0] for elem in column7).most_common(1)[0][0]
c8 = Counter(elem[0] for elem in column8).most_common(1)[0][0]

print (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8)


