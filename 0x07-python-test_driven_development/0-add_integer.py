#!/usr/bin/python3
"""
Module check if a and b are either integers or floats
"""


def add_integer(a, b=98):
    """Cast a and b to integers if they are floats
    Return the addition of a and b as an integer
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return int(a + b)
