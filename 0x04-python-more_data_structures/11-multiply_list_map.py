#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all number multiplied by a \n
    number without using any loop.
    """
    return (list(map((lambda i: i * number), my_list)))
