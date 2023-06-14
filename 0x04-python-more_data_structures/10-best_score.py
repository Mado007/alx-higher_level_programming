#!/usr/bin/python3

def best_score(a_dictionary):
    """

    A func that return a key with the biggest int value

    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())

        leader = ""
        score = 0
        
        for i in my_list:
            if a_dictionary[i] > score:

                leader = i
                score = a_dictionary[i]
                
        return leader
