#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers: list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = list_of_integers
    if size == []:
        return None
    list = len(size)

    list_of, mid = 0, list - 1
    while list_of < mid:
        mid_idx = list_of + (mid - list_of) // 2
        if size[mid_idx] > size[mid_idx - 1] and size[mid_idx] > size[mid_idx + 1]:
            return size[mid_idx]
        if size[mid_idx - 1] > size[mid_idx + 1]:
            mod = mid_idx
        else:
            list_of = mid_idx + 1
    return size[list_of]
