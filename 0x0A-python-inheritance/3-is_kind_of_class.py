#!/usr/bin/python3
"""Simple module to check if an object is an instance of a specific class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a specific class
    or a class that inherited from that specific class.

    Arguments:
        obj {unknown}   --      the object that will be checked.
        a_class {type}  --      the class to which the object to be reviewed
                                should inherit.

    Returns:
        bool -- True if obj is an instance of a_class or it's superclasses,
        False otherwise.
    """
    return isinstance(obj, a_class)
