#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ Check if first_name and last_name are strings """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    """Print the message"""
    print(f"My name is {first_name} {last_name}")
