#!/usr/bin/python3
def remove_char_at(str, n):
    """Make a copy of the string without the cahracter at position n."""
    if n < 0:
        return str
    return (str[:n] + str[(n+1):])
