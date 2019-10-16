#!/usr/bin/python3
"""Simple module with a Rectangle class that inherits BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Simple class Rectangle with width an height with input validation.
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
