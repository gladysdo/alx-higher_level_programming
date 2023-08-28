#!/usr/bin/python3
def raise_exception():
    a = "This is a string"
    b = 10
    try:
        result = a + b  # This will raise a TypeError since you can't concatenate a string and an integer
    except:
        raise TypeError("This is a custom type exception")
