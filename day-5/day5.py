#!/usr/bin/python3
import hashlib

count = 0
hashlist = [ ]
password = ''

while True:
    input = 'wtnhxymk'
    input = input + str(count)
    hash_object = hashlib.md5(input.encode())


    hash = hash_object.hexdigest()
    count = count + 1


    if len(hashlist) != 8:
        if '00000' in hash[:5]:
            hashlist.append(str(hash))

    else:
        print("Het werkt!")
        for x in range(len(hashlist)):
            abc = hashlist[x][5]

            password = password + abc
        print(password)
        break




