#!/usr/bin/python3
def uniq_add(my_list=[]):
    # create empty set to keep unique integers
    unique_set = set()
    for i in my_list:
        unique_set.add(i)
    result = sum(unique_set)
    return result
