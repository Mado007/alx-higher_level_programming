#!/usr/bin/python3
# Author - Mado007

d = 0
    """removing the character at the position n."""
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - d)), end="")
    d = 32 if d == 0 else 0
