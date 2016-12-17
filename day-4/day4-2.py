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

key = 'abcdefghijklmnopqrstuvwxyz'
def decrypt(sectorid, name):
    result = ''

    for l in name:
        try:
            i = (key.index(l) + sectorid) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

for i in range(len(inputlist)):
    st = inputlist[i]

    split = re.findall('\d*\D+',st)
    name = split[0].replace('-',' ')
    checksecid = split[1].replace(']','')
    checksecid = checksecid.split("["[-1].replace(']',''))

    checksum = checksecid[1]
    sectorid = int(checksecid[0])
    decrypted = decrypt(sectorid, name)

    if "north" in decrypted:
        print("Sectorid:" +str(sectorid))


