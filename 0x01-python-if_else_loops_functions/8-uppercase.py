#!/usr/bin/python3
def uppercase(str):
    change_case = 0
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            change_case = 32
        else:
            change_case = 0
        print('{:c}'.format(ord(i) - change_case), end="")
    print()
