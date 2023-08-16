#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = sorted(a_dictionary.keys())
    for key in k:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
