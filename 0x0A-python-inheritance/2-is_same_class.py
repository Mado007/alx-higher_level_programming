#!/usr/bin/python3

"""Check the object as an instance in a class or not"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the
    class, otherwise return false
    """
    return (type(obj) == a_class)
