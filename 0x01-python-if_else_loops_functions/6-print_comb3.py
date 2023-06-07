#!/usr/bin/python3
# Author - Mado007

for digits1 in range(0, 10):
    for digits2 in range(digits1 + 1, 10):
        if digits1 == 8 and digits2 == 9:
            print("{}{}".format(digits1, digits2))
        else:
            print("{}{}".format(digits1, digits2), end=", ")
