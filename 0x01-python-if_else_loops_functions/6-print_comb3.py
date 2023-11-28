#!/usr/bin/python3
for i in range(10):
    for x in range(i, 10):
        if i < x :
            print("{:d}{:d}".format(i, x),end="\n" if i == 8 and x == 9 else ", ")

