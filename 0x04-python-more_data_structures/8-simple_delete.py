#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Function that deletes Key in a Dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
