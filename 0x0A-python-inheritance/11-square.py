#!/usr/bin/python3
"""Simple module with a Square class that inherits Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Simple class Square with a size as width and height,
    also it has input validation.
    """

    def __init__(self, size):
        """Initialize the square after checking if the value of size passed is
        a valid integer using it's superclass method.

        Arguments:
            size   {int}   --  a positive non zero integer.

        Raises:
            TypeError:  if the size value is not an integer.
            ValueError: if the size value is an integer less or equal to zero.
        """
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__width = size
        self.__height = size
        self.__size = size

    def area(self):
        """ Compute the area of a square
            with the formula:
                                area = @size ^ 2 = @size * @size
            Return:
                    Power of the Square size to 2 or
                    size multiplicated by size."""
        return self.__size**2

    def __str__(self):
        """Generates a human readable string that represents the Rectangle

        Returns:
            {str} -- The string representation of the Rectangel using the #
                        character, it represents a 2d rectangle.
        """
        return '[Square] {:d}/{:d}'.format(self.__width, self.__height)
