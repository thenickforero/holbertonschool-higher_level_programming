#!/usr/bin/python3
"""Module to find a peak (number greather than its neighbours)
in a list of integers.
"""


def find_peak(list_of_integers):
    """Function that searches a peak in a list of integer,
    only if the list isn't empty.

    Arguments:
        list_of_integers {list[int]} -- The list with integer numbers
                                        that will be checked.

    Returns:
        int -- Returns the biggest integer number in the list,
               if the list is empty it returns None.
    """

    return max(list_of_integers) if list_of_integers else None
