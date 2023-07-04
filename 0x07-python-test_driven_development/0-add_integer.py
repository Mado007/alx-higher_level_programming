!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(d, c).
"""


def add_integer(d, c):
    """Return the addition of two numbers."""
    if type(d) is not int and type(d) is not float:
        raise TypeError("d must be an integer")
    if type(c) is not int and type(c) is not float:
        raise TypeError("c must be an integer")
    if type(d) is float:
        d = int(d)
    if type(c) is float:
        c = int(c)
    return d + c
