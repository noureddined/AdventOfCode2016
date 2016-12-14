#!/usr/bin/python3

f  = open('input.txt','r')


inputlist = f.read().replace("    ", "  ")
inputlist = inputlist.replace("  ",",")

dict = inputlist.split("\n")

counter = 0
for i in range(len(dict)):

    a = dict[i].split(",")[0].replace(" ","")
    b = dict[i].split(",")[1].replace(" ","")
    c = dict[i].split(",")[2].replace(" ","")

    a = int(a)
    b = int(b)
    c = int(c)
    
    if a+b > c and b+c > a and a+c > b:
        counter = counter + 1
        print (counter)
