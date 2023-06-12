#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specified index without modifying\n
    the list.
    """
    if idx > (len(my_list) - 1) or idx < 0:
        return (my_list)
    my_copy = [i for i in my_list]
    my_copy[idx] = element
    return (my_copy)
