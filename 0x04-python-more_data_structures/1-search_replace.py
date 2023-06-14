#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    element by another in a new list
    which is funct that replac eoccurrences

    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
