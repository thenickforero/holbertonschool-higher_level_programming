#!/usr/bin/python3
"""Simple module to seek the attributes and functions of a certain object.
"""


def lookup(obj):
    """Computes the attributes and methods of an object.

    Arguments:
        obj {object} -- The object that will be processed.

    Returns:
        {list} -- a the list of the available attributes and methods of @obj
                  otherwise None.
    """
    response = None
    if obj is not None:
        response = dir(obj)
    return response
