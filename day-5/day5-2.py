#!/usr/bin/python3
import hashlib

count = 0
hashlist = [ ]
password = ''

while len(hashlist) != 8:
    input = 'wtnhxymk'
    input = input + str(count)
    hash_object = hashlib.md5(input.encode())
    hash = hash_object.hexdigest()

    listrange = {'0','1','2','3','4','5','6','7'}
    abc = False
    if hash[:5] == '00000' and hash[5] in listrange:
        for every in range(len(hashlist)):
            if hash[5] in hashlist[every][0]:
                abc = True
                break
            else:
                abc = False
        if abc == False:
            hashlist.append(str(hash[5:7]))
            count = count + 1

        else:
            count = count + 1

    else:
        count = count + 1


else:
    print("Het werkt!")

    hashlist.sort()
    print (hashlist)
    for x in range(len(hashlist)):
        position = hashlist[x][0]
        key = hashlist[x][1]
        print(position + key)

        password = password + key
    print(password)





