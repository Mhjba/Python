#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        Aver = 0
        num = 0
        for tup in my_list:
            Aver += (tup[0] * tup[1])
            num += tup[1]
        return (Aver / num)
    return 0
