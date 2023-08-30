#!/usr/bin/python3
def raise_exception():
    a = "This is a string"
    b = 10
    try:
        result = a + b
    except Exception:
        raise TypeError("This is a custom type exception")
