#!/usr/bin/python3
"""
This modules finds the peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Args:
        list_of_integer(int): Int whose peak is to be found
    Returns: peak of list_of_int or None
    """

    size_list = len(list_of_integers)
    mid_pt = size_list
    mid = size_list // 2

    if size_list == 0:
        return (None)

    while True:
        mid_pt = mid_pt // 2
        if (mid < size_list - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_pt // 2 == 0:
                mid_pt = 2
            mid = mid + mid_pt // 2
        elif mid_pt > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_pt // 2 == 0:
                mid_pt = 2
            mid = mid - mid_pt // 2
        else:
            return (list_of_integers[mid])
