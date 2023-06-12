#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a given index.
    """
    if idx < len(my_list) or idx >= 0:
        my_list[idx] = element
    return (my_list)
