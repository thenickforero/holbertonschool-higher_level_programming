#!/usr/bin/python3
"""Simple module to check if an object is an exactly instance of a specific
class.
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specific class and
    isn't a subclass of another class.

    Arguments:
        obj {unknown}   --      the object that will be checked.
        a_class {type}  --      the class to which the object to be reviewed
                                should inherit.

    Returns:
        bool -- True if obj is an exactly instance of a_class, False otherwise.
    """
    return type(obj) is a_class
