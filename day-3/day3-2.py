#!/usr/bin/python3
import itertools

file = open("input.txt", 'r')

lines = file.readlines()
file.close()


column1 = []
column2 = []
column3 = []

for line in lines:
    parts = line.split() # split line into parts
    column1.append(parts[0])
    column2.append(parts[1])
    column3.append(parts[2])

print(column1)
print(column2)
print(column3)

counter = 0
for a, b, c in zip(*[iter(column1)]*3):
    #print(a, b, c)
    a = int(a)
    b = int(b)
    c = int(c)

    if a+b > c and b+c > a and a+c > b:
        counter = counter + 1
#print ("Counter: " + str(counter))


counter2 = 0
for a, b, c in zip(*[iter(column2)]*3):
    #print(a, b, c)
    a = int(a)
    b = int(b)
    c = int(c)
    if a+b > c and b+c > a and a+c > b:
        counter2 = counter2 + 1
#print ("Counter2: " + str(counter2))

counter3 = 0
for a, b, c in zip(*[iter(column3)]*3):
    #print(a, b, c)
    a = int(a)
    b = int(b)
    c = int(c)
    if a+b > c and b+c > a and a+c > b:
        counter3 = counter3 + 1
#print ("Counter3: " + str(counter3))

totaal = counter + counter2 + counter3

print ("Totaal:" + str(totaal))










