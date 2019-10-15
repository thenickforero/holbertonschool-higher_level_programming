#!/usr/bin/python3
"""Simple module to check if an object is an instance of a subclass of a
specific class.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    that inherited directly or indirectly from that specific class.

    Arguments:
        obj {unknown}   --      the object that will be checked.
        a_class {type}  --      the class to which the object to be reviewed
                                should be subclass.

    Returns:
        bool -- True if obj is an instance of a subclass of a_class,
        False otherwise.
    """
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
