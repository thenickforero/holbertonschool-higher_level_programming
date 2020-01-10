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

    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if len(list_of_integers) == 2:
        return max(list_of_integers)

    middle = int(len(list_of_integers) / 2)

    if (list_of_integers[middle] > list_of_integers[middle - 1] and
            list_of_integers[middle] > list_of_integers[middle + 1]):
        return list_of_integers[middle]

    if list_of_integers[middle + 1] > list_of_integers[middle]:
        return find_peak(list_of_integers[middle + 1:])

    return find_peak(list_of_integers[0:middle])
