#!/usr/bin/python3
"""Simple module with the definition of an empty class with an unimplemented
method.
"""


class BaseGeometry():
    """Simple empty BaseGeometry class"""

    def area(self):
        """Prototype of the area function that actually isn't implemented.

        Raises:
            Exception:  a simple exception that tells that the area function is
                        not implmenet yet.
        """
        raise Exception('area() is not implemented')
