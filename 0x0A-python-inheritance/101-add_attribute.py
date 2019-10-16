#!/usr/bin/python3
"""Simple module to add a new attribute to an object.
"""


def add_attribute(obj, key, value):
    """Simple function that add a new attribute to an object
    in a safety mode

    Arguments:
        key     {str}   --  the name of the new attribute.
        value   {any}   --  the value of the new attribute.
    Raises:
        TypeError:  if can't add the attribute to the object
                    for example by__slots__
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, key, value)
