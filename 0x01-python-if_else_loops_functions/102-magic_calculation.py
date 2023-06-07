#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Match the bytecode provided by ALX."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
