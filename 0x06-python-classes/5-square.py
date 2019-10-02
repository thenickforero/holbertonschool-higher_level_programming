#!/usr/bin/python3
class Square:
    """Simple square class with his size as a field"""

    def __init__(self, size=0):
        """ Instance the class Square
            Arguments:
                @size: the size of every side of the Square,
                        it must be a positive integer value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ Getter for the field size as a property
            Return:
                    Value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter for the field size as a property.
            Arguments:
                @value: the value of size
                        that must be a positive integer value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Compute the area of a square
            with the formula:
                                area = @size ^ 2 = @size * @size
            Return:
                    Power of the Square size to 2
                    or size multiplicated by size."""
        return (self.__size ** 2)

    def my_print(self):
        """ Prints a square using the character # in the standard output
            or a blank line if @size is 0"""
        if not self.size:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
