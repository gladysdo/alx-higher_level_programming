#!/usr/bin/python3
""" Define function to returns True if the object is an instance of a class """


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) != a_class
