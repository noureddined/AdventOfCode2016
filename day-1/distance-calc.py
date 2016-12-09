#!/usr/bin/python3

f  = open('input.txt','r')
inputlist = f.read().split(", ")

x = 0
y = 0
orientatie = 'n'
draai = ''
stap = ''

def newrichting(draai, orientatie):
    if draai == "L":
        if orientatie == 'n':
            orientatie = 'w'
            return orientatie

        elif orientatie == 'o':
            orientatie = 'n'
            return orientatie

        elif orientatie == 's':
            orientatie = 'o'
            return orientatie

        elif orientatie == 'w':
            orientatie = 's'
            return orientatie

    elif draai == "R":
        if orientatie == 'n':
            orientatie = 'o'
            return orientatie

        elif orientatie == 'o':
            orientatie = 's'
            return orientatie

        elif orientatie == 's':
            orientatie = 'w'
            return orientatie

        elif orientatie == 'w':
            orientatie = 'n'
            return orientatie

def stappen(orientatie, stap, x, y):
    if orientatie == "n":
        y = y + stap
        return x,y
    elif orientatie == "s":
        y = y - stap
        return x,y
    elif orientatie == "o":
        x = x + stap
        return x,y
    elif orientatie == "w":
        x = x - stap
        return x,y

for i in inputlist:
    draai = i[0]
    stap = i[1:]
    orientatie = newrichting(draai, orientatie)
    print ('Draai:' + draai + ' stap:'+stap + ' Orientatie:'+ str(orientatie))

    xy = stappen(orientatie, int(stap), x, y)
    xy = xy
    x = xy[0]
    y = xy[1]

print (xy)
antwoord = abs(x) + abs(y)
print ('response: '+ str(antwoord))



