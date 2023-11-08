#!/usr/bin/python3

def weight_average(my_list=[]):
    avg, res, d = 0, 0, 0
    if my_list:
        for i in my_list:
            res = res + i[0] * i[1]
        for j in my_list:
            d = d + j[1]
        return res / d
    else:
        return 0
