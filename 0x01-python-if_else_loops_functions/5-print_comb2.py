#!/usr/bin/python3
# Author - Mado007

"""Print numero 0 to 99."""
for numero in range(0, 100):
    if numero == 99:
        print("{}".format(numero))
    else:
        print("{:02}".format(numero), end=", ")
