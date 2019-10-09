#!/usr/bin/python3
"""This module contains a class called LockedClass with no class or object
attribute and prevents the user from dynamically creating new instance
attributes
"""


class LockedClass:
    """Simple class that only allows to create a new instance attribute if
    it's called first_name.
    """
    __slots__ = 'first_name'
