#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digitso = abs(number) % 10
if number < 0:
    digitso = -digitso
print(f"Last digit of {number:d} is {digitso:d} and is ", end="")
if digitso > 5:
    print("greater than 5")
elif digitso == 0:
    print("0")
else:
    print("less than 6 and not 0")
