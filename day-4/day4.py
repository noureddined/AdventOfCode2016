#!/usr/bin/python3
import re
import string
import pprint
from collections import OrderedDict

file = open("input.txt", 'r')

inputlist = file.read()
inputlist = inputlist.split()

counter = 0
sectoridcount = 0
for i in range(len(inputlist)):
    st = inputlist[i]

    split = re.findall('\d*\D+',st)
    name = split[0].replace('-','')
    checksecid = split[1].replace(']','')
    checksecid = checksecid.split("["[-1].replace(']',''))

    checksum = checksecid[1]
    sectorid = checksecid[0]

    letter = {}
    for s in string.ascii_lowercase:
        if s in name:
            letter[s] = name.count(s)


    sorta = OrderedDict(sorted(letter.items(), key=lambda t: t[0]))
    sort = sorted(sorta.items(), key=lambda x: x[1], reverse=True)
    sort = sort[:5]


    #print(sort)
    for a, b, c, d, e in zip(*[iter(sort)]*5):
        a = a[0]
        b = b[0]
        c = c[0]
        d = d[0]
        e = e[0]
        checksumnew = (a+b+c+d+e)
        print (checksumnew)

        if checksumnew == checksum:
            sectoridcount = sectoridcount + int(sectorid)

print(sectoridcount)
