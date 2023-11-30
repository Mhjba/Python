#!/usr/bin/python3
import sys
if __name__ == "__main__":

    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments.".format(i))
    elif i == 1:
        print("1 argument:".format(i))
    else:
        print("{} arguments:".format(i))
        for x in range(i):
            print("{}: {}".format(x + 1, sys.argv[x + 1]))
