#!/usr/bin/python3
"""Simple module with a Rectangle class that inherits BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Simple class Rectangle with width, height and input validation.
    """

    def __init__(self, width, height):
        """Initialize the rectangle after checking if the values passed are
        valid integers using it's superclass method.

        Arguments:
            width   {int}   --  a positive non zero integer.
            height  {int}   --  a positive non zero integer.

        Raises:
            TypeError:  if any value is not an integer.
            ValueError: if any value is an integer less or equal to zero.
        """
        super().__init__()
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the Area of a Rectangle.
        Based on the formula AreaRectangle = Height * Width

        Returns:
            {int} -- The integer value of the Rectangle's Area.
        """
        return self.__height * self.__width

    def __str__(self):
        """Generates a human readable string that represents the Rectangle

        Returns:
            {str} -- The string representation of the Rectangel using the #
                        character, it represents a 2d rectangle.
        """
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
