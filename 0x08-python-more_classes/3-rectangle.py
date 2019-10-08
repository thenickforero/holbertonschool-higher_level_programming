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

    def area(self):
        """Computes the Area of a Rectangle.
        Based on the formula AreaRectangle = Height * Width

        Returns:
            {int} -- The integer value of the Rectangle's Area.
        """
        return self.height * self.width

    def perimeter(self):
        """Computes the Perimeter of a Rectangle.
        Based on the formula PerimeterRectangle = 2 * (Height + Width)

        Returns:
            {int} -- The integer value of the Rectangle's Perimeter or
                     0 if the width or height of the Rectangle is 0
                     because that will be a line.
        """
        base = self.height + self.width
        return 2 * base if self.width != 0 and self.height != 0 else 0

    def __str__(self):
        """Generates a human readable string that represents the Rectangle

        Returns:
            {str} -- The string representation of the Rectangel using the #
                     character, it represents a 2d rectangle.
        """
        rectangle = ''
        for row in range(self.height):
            rectangle += '#' * self.width
            rectangle += '\n' if row != self.height - 1 else ''
        return rectangle
