#!/usr/bin/python3
# Author - Mado007

def remove_char_at(str, n):
    """removing the character at the position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
