#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for dic in list_keys:
        if value == a_dictionary.get(dic):
            del a_dictionary[dic]

    return (a_dictionary)
