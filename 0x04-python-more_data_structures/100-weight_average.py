#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    dend = 0
    numo = 0
    

    for tup in my_list:
        dend += tup[1]
        numo += tup[0] * tup[1]

    return (num / den)
