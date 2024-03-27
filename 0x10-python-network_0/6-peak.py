#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers : list of integers to find peak of
    Returns: peak of list_of_integers or None
    """

    size = list_of_integers
    list = len(size)
    if list == 0:
        return (None)
