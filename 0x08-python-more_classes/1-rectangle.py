#!/usr/bin/python3
"""Simple module that contains a Rectangle class with dimmensions.

It contains the basic geometry logic of a rectangle and his properties are
managed by the getters and setters-
"""


class Rectangle:
    """Simple Rectangle class with height and width.
    """
    def __init__(self, width=0, height=0):
        """Instantiate a Rectangle with certain dimmensions:

        Arguments:
            width {int}     --  The width of the new Rectangle (default: {0})
            height {int}    --  The height of the new Rectangle (default: {0})
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """The width of the Rectangle which is an integer value bigger than 0

            Raises:
            TypeError:  When the value passed to the setter isn't an integer.
            ValueError: When the value passed to the setter is less than or
                        equal to zero.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """The height of the Rectangle which is an integer value bigger than 0

            Raises:
            TypeError:  When the value passed to the setter isn't an integer.
            ValueError: When the value passed to the setter is less than or
                        equal to zero.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
