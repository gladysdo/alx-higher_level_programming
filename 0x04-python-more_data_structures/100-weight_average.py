#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_num = 0
    sum_wigh = 0

    for tup in my_list:
        sum_num += tup[0] * tup[1]
        sum_wigh += tup[1]

    return (sum_num / sum_wigh)
