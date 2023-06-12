#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a given index.
    """
    if idx < 0 or idx >= (len(my_list)):
        return (my_list)

    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
